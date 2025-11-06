"""
Configuration Auditor Module

This module compares host configurations against security baselines.
"""

import os
import yaml


class ConfigAuditor:
    def __init__(self, config_path):
        self.config_path = config_path
        self.baselines = self._load_baselines()
    
    def _load_baselines(self):
        """Load baseline configurations from YAML files"""
        baselines = {}
        
        if not os.path.exists(self.config_path):
            print(f"Warning: Config path {self.config_path} does not exist")
            return baselines
        
        for filename in os.listdir(self.config_path):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                with open(os.path.join(self.config_path, filename), 'r') as f:
                    try:
                        baseline = yaml.safe_load(f)
                        baselines[filename] = baseline
                    except yaml.YAMLError as e:
                        print(f"Error loading baseline {filename}: {e}")
        
        return baselines
    
    def audit_hosts(self, hosts):
        """Audit hosts against loaded baselines"""
        findings = []
        
        for host in hosts:
            host_findings = self._audit_host(host)
            findings.extend(host_findings)
        
        return findings
    
    def _audit_host(self, host):
        """Audit a single host against applicable baselines"""
        findings = []
        
        # Check for common security issues
        for port in host.get('ports', []):
            # Check for SSH open to world
            if port['port'] == 22 and port['state'] == 'open':
                finding = {
                    'host': host['ip'],
                    'type': 'Security Issue',
                    'risk': 'High',
                    'description': 'SSH service accessible from network',
                    'recommendation': 'Restrict SSH access with firewall rules'
                }
                findings.append(finding)
            
            # Check for insecure HTTP
            if port['port'] == 80 and port['state'] == 'open':
                finding = {
                    'host': host['ip'],
                    'type': 'Security Issue',
                    'risk': 'Medium',
                    'description': 'HTTP service running without encryption',
                    'recommendation': 'Enable HTTPS with valid certificate'
                }
                findings.append(finding)
            
            # Check for RDP open to world
            if port['port'] == 3389 and port['state'] == 'open':
                finding = {
                    'host': host['ip'],
                    'type': 'Security Issue',
                    'risk': 'Critical',
                    'description': 'RDP service accessible from network',
                    'recommendation': 'Restrict RDP access with firewall rules and enable NLA'
                }
                findings.append(finding)
        
        return findings