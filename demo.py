#!/usr/bin/env python3
"""
Demo script for NetAudit AutoConfig

This script demonstrates how to use the NetAudit AutoConfig tool with command-line arguments.
"""

import argparse
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import our modules
from utils.reporter import ReportGenerator

def demo_scan(subnet="192.168.1.0/24"):
    """Demonstrate network scanning functionality"""
    print(f"[DEMO] Scanning subnet: {subnet}")
    
    # In a real scenario, this would use nmap to scan the network
    # For demo purposes, we'll return mock data
    mock_hosts = [
        {
            'ip': '192.168.1.10',
            'hostname': 'webserver01.example.com',
            'ports': [
                {'port': 22, 'state': 'open', 'service': 'ssh', 'version': 'OpenSSH 8.0'},
                {'port': 80, 'state': 'open', 'service': 'http', 'version': 'Apache 2.4.6'},
                {'port': 443, 'state': 'open', 'service': 'https', 'version': 'Apache 2.4.6'}
            ]
        },
        {
            'ip': '192.168.1.20',
            'hostname': 'dbserver01.example.com',
            'ports': [
                {'port': 22, 'state': 'open', 'service': 'ssh', 'version': 'OpenSSH 8.0'},
                {'port': 3306, 'state': 'open', 'service': 'mysql', 'version': 'MySQL 8.0.28'}
            ]
        },
        {
            'ip': '192.168.1.30',
            'hostname': 'workstation01.example.com',
            'ports': [
                {'port': 3389, 'state': 'open', 'service': 'ms-wbt-server', 'version': 'Microsoft Terminal Services'}
            ]
        }
    ]
    
    print(f"[DEMO] Found {len(mock_hosts)} hosts:")
    for host in mock_hosts:
        print(f"  - {host['ip']} ({host['hostname']})")
        for port in host['ports']:
            print(f"    Port {port['port']}: {port['service']} ({port['state']})")
    
    return mock_hosts

def demo_audit(hosts):
    """Demonstrate configuration audit functionality"""
    print("\n[DEMO] Performing configuration audit")
    
    # In a real scenario, this would connect to hosts and check configurations
    # For demo purposes, we'll return mock findings
    mock_findings = [
        {
            'host': '192.168.1.10',
            'type': 'Security Issue',
            'risk': 'High',
            'description': 'SSH service accessible from network',
            'recommendation': 'Restrict SSH access with firewall rules and use key-based authentication'
        },
        {
            'host': '192.168.1.10',
            'type': 'Security Issue',
            'risk': 'Medium',
            'description': 'HTTP service running without encryption',
            'recommendation': 'Redirect all HTTP traffic to HTTPS and obtain a valid SSL certificate'
        },
        {
            'host': '192.168.1.20',
            'type': 'Security Issue',
            'risk': 'High',
            'description': 'MySQL database listening on all interfaces',
            'recommendation': 'Bind MySQL to localhost only and use SSH tunneling for remote access'
        },
        {
            'host': '192.168.1.30',
            'type': 'Security Issue',
            'risk': 'Critical',
            'description': 'RDP service accessible from network without Network Level Authentication',
            'recommendation': 'Enable Network Level Authentication (NLA) and restrict RDP access with firewall rules'
        }
    ]
    
    print(f"[DEMO] Found {len(mock_findings)} security issues:")
    risk_levels = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low': 0}
    for finding in mock_findings:
        risk_levels[finding['risk']] += 1
        print(f"  - {finding['risk']} risk on {finding['host']}: {finding['description']}")
    
    print(f"\nRisk Summary:")
    for risk, count in risk_levels.items():
        if count > 0:
            print(f"  {risk}: {count}")
    
    return mock_findings

def demo_report(hosts, findings, output_file="demo_report.md"):
    """Demonstrate report generation functionality"""
    print(f"\n[DEMO] Generating report to {output_file}")
    
    reporter = ReportGenerator()
    report_content = reporter.generate_report(hosts, findings)
    
    with open(output_file, 'w') as f:
        f.write(report_content)
    
    print(f"[DEMO] Report saved to {output_file}")
    return report_content

def demo_auto_fix(findings):
    """Demonstrate auto-remediation functionality"""
    print("\n[DEMO] Applying automatic remediation")
    
    # In a real scenario, this would execute Ansible playbooks
    # For demo purposes, we'll just print what would happen
    playbook_mapping = {
        'SSH': 'harden_ssh.yml',
        'HTTP': 'enable_https.yml',
        'RDP': 'harden_rdp.yml',
        'MySQL': 'harden_mysql.yml'
    }
    
    # Group findings by host
    host_findings = {}
    for finding in findings:
        host = finding['host']
        if host not in host_findings:
            host_findings[host] = []
        host_findings[host].append(finding)
    
    for host, issues in host_findings.items():
        print(f"  Applying fixes to {host}:")
        playbooks_to_run = set()
        
        for issue in issues:
            # Determine which playbook to run based on the issue
            for keyword, playbook in playbook_mapping.items():
                if keyword in issue['description']:
                    playbooks_to_run.add(playbook)
        
        for playbook in playbooks_to_run:
            print(f"    - Would run playbook: {playbook}")
    
    print("[DEMO] Automatic remediation completed")

def main():
    parser = argparse.ArgumentParser(description='Demo of NetAudit AutoConfig functionality')
    parser.add_argument('--subnet', default='192.168.1.0/24', help='Subnet to scan (demo only)')
    parser.add_argument('--audit', action='store_true', help='Perform configuration audit')
    parser.add_argument('--auto-fix', action='store_true', help='Apply automatic remediation')
    parser.add_argument('--output', default='demo_report.md', help='Output report file')
    
    args = parser.parse_args()
    
    print("NetAudit AutoConfig Demo")
    print("=" * 30)
    
    # Step 1: Network Discovery
    hosts = demo_scan(args.subnet)
    
    # Step 2: Configuration Audit (if requested)
    findings = []
    if args.audit:
        findings = demo_audit(hosts)
    
    # Step 3: Generate Report
    report_content = demo_report(hosts, findings, args.output)
    
    # Step 4: Auto Remediation (if requested)
    if args.auto_fix:
        demo_auto_fix(findings)
    
    print("\nDemo completed successfully!")
    print(f"View the full report at: {args.output}")

if __name__ == "__main__":
    main()