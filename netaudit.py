#!/usr/bin/env python3
"""
NetAudit AutoConfig - Network Security Auditing Tool

This tool performs network scanning, configuration auditing, 
and automated remediation using Python and Ansible.
"""

import argparse
import sys
import os
from utils.scanner import NetworkScanner
from utils.auditor import ConfigAuditor
from utils.reporter import ReportGenerator
from utils.configurator import AutoConfigurator

def main():
    parser = argparse.ArgumentParser(description='NetAudit AutoConfig - Automated Network Security Auditing')
    parser.add_argument('--subnet', required=True, help='Subnet to scan in CIDR notation (e.g., 192.168.1.0/24)')
    parser.add_argument('--audit', action='store_true', help='Perform configuration audit')
    parser.add_argument('--auto-fix', action='store_true', help='Apply automatic remediation')
    parser.add_argument('--config-path', help='Path to baseline configuration files')
    parser.add_argument('--playbook-path', help='Path to Ansible playbooks for remediation')
    parser.add_argument('--output', default='report.md', help='Output report file path')
    
    args = parser.parse_args()
    
    # Step 1: Network Discovery
    print(f"[+] Scanning subnet: {args.subnet}")
    scanner = NetworkScanner(args.subnet)
    hosts = scanner.discover_hosts()
    
    if not hosts:
        print("[-] No hosts found in the subnet")
        return
    
    print(f"[+] Found {len(hosts)} hosts")
    
    # Step 2: Configuration Audit (if requested)
    findings = []
    if args.audit:
        print("[+] Performing configuration audit")
        auditor = ConfigAuditor(args.config_path or './config/baseline_configs/')
        findings = auditor.audit_hosts(hosts)
    
    # Step 3: Generate Report
    print("[+] Generating report")
    reporter = ReportGenerator()
    report_content = reporter.generate_report(hosts, findings)
    
    with open(args.output, 'w') as f:
        f.write(report_content)
    
    print(f"[+] Report saved to {args.output}")
    
    # Step 4: Auto Remediation (if requested)
    if args.auto_fix and args.playbook_path:
        print("[+] Applying automatic remediation")
        configurator = AutoConfigurator(args.playbook_path)
        configurator.apply_fixes(findings)

if __name__ == "__main__":
    main()