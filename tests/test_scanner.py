"""
Test script for NetAudit AutoConfig

This script demonstrates how to use the NetAudit AutoConfig tool.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.scanner import NetworkScanner
from utils.auditor import ConfigAuditor
from utils.reporter import ReportGenerator

def test_scanner():
    """Test the network scanner functionality"""
    print("Testing Network Scanner...")
    
    # Create mock hosts data for testing
    mock_hosts = [
        {
            'ip': '192.168.1.10',
            'hostname': 'test-server-01',
            'ports': [
                {'port': 22, 'state': 'open', 'service': 'ssh', 'version': 'OpenSSH 7.9'},
                {'port': 80, 'state': 'open', 'service': 'http', 'version': 'Apache 2.4.38'}
            ]
        },
        {
            'ip': '192.168.1.20',
            'hostname': 'test-workstation-01',
            'ports': [
                {'port': 3389, 'state': 'open', 'service': 'ms-wbt-server', 'version': 'Microsoft Terminal Services'},
                {'port': 443, 'state': 'open', 'service': 'https', 'version': 'nginx 1.18.0'}
            ]
        }
    ]
    
    return mock_hosts

def test_auditor(hosts):
    """Test the configuration auditor functionality"""
    print("Testing Configuration Auditor...")
    
    # Create mock findings data for testing
    mock_findings = [
        {
            'host': '192.168.1.10',
            'type': 'Security Issue',
            'risk': 'High',
            'description': 'SSH service accessible from network',
            'recommendation': 'Restrict SSH access with firewall rules'
        },
        {
            'host': '192.168.1.10',
            'type': 'Security Issue',
            'risk': 'Medium',
            'description': 'HTTP service running without encryption',
            'recommendation': 'Enable HTTPS with valid certificate'
        },
        {
            'host': '192.168.1.20',
            'type': 'Security Issue',
            'risk': 'Critical',
            'description': 'RDP service accessible from network',
            'recommendation': 'Restrict RDP access with firewall rules and enable NLA'
        }
    ]
    
    return mock_findings

def test_reporter(hosts, findings):
    """Test the report generator functionality"""
    print("Testing Report Generator...")
    
    reporter = ReportGenerator()
    report_content = reporter.generate_report(hosts, findings)
    
    # Save to test report
    with open('test_report.md', 'w') as f:
        f.write(report_content)
    
    print("Test report saved to test_report.md")
    return report_content

def main():
    print("NetAudit AutoConfig Test Suite")
    print("=" * 40)
    
    # Test scanner
    hosts = test_scanner()
    print(f"Discovered {len(hosts)} hosts\n")
    
    # Test auditor
    findings = test_auditor(hosts)
    print(f"Identified {len(findings)} security issues\n")
    
    # Test reporter
    report = test_reporter(hosts, findings)
    print("\nSample Report Output:")
    print("-" * 20)
    print("\n".join(report.split("\n")[:20]))  # Print first 20 lines
    print("...\n")
    
    print("Test suite completed successfully!")

if __name__ == "__main__":
    main()