"""
Auto Configurator Module

This module applies automatic remediation using Ansible playbooks.
"""

import os
import subprocess


class AutoConfigurator:
    def __init__(self, playbook_path):
        self.playbook_path = playbook_path
    
    def apply_fixes(self, findings):
        """Apply fixes using relevant Ansible playbooks"""
        if not os.path.exists(self.playbook_path):
            print(f"Error: Playbook path {self.playbook_path} does not exist")
            return
        
        # Group findings by host
        host_findings = {}
        for finding in findings:
            host = finding['host']
            if host not in host_findings:
                host_findings[host] = []
            host_findings[host].append(finding)
        
        # Apply fixes for each host
        for host, issues in host_findings.items():
            print(f"[*] Applying fixes to {host}")
            self._apply_host_fixes(host, issues)
    
    def _apply_host_fixes(self, host, issues):
        """Apply fixes for issues on a specific host"""
        # Determine which playbooks to run based on findings
        playbooks_to_run = set()
        
        for issue in issues:
            # Map issue types to playbook names
            if 'SSH' in issue['description']:
                playbooks_to_run.add('harden_ssh.yml')
            elif 'RDP' in issue['description']:
                playbooks_to_run.add('harden_rdp.yml')
            elif 'HTTP' in issue['description']:
                playbooks_to_run.add('enable_https.yml')
        
        # Run each playbook
        for playbook in playbooks_to_run:
            playbook_full_path = os.path.join(self.playbook_path, playbook)
            if os.path.exists(playbook_full_path):
                print(f"  Running playbook: {playbook}")
                self._run_playbook(playbook_full_path, host)
            else:
                print(f"  Warning: Playbook {playbook} not found")
    
    def _run_playbook(self, playbook_path, host):
        """Run an Ansible playbook on a specific host"""
        try:
            cmd = ["ansible-playbook", playbook_path, "-i", f"{host},"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print(f"    Success: Playbook completed successfully")
            else:
                print(f"    Error: Playbook failed with return code {result.returncode}")
                print(f"    stderr: {result.stderr}")
        except subprocess.TimeoutExpired:
            print(f"    Error: Playbook timed out")
        except FileNotFoundError:
            print(f"    Error: ansible-playbook command not found. Is Ansible installed?")
        except Exception as e:
            print(f"    Error running playbook: {e}")