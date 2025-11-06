"""
Report Generator Module

This module generates markdown/html reports from audit findings.
"""

from datetime import datetime

class ReportGenerator:
    def __init__(self):
        pass
    
    def generate_report(self, hosts, findings):
        """Generate a markdown report from hosts and findings"""
        report = []
        
        # Header
        report.append("# NetAudit AutoConfig Report")
        report.append(f"_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
        
        # Host inventory
        report.append("## Discovered Hosts")
        report.append(f"Found {len(hosts)} active hosts in the network:\n")
        
        for host in hosts:
            report.append(f"### {host['ip']} ({host['hostname']})")
            if host['ports']:
                report.append("Open Ports:")
                for port in host['ports']:
                    report.append(f"- {port['port']}/TCP ({port['service']}) - {port['state']}")
                    if port['version']:
                        report.append(f"  Version: {port['version']}")
            else:
                report.append("No open ports detected")
            report.append("")  # Empty line
        
        # Findings
        if findings:
            report.append("## Security Findings")
            high_risk = [f for f in findings if f['risk'] == 'High' or f['risk'] == 'Critical']
            medium_risk = [f for f in findings if f['risk'] == 'Medium']
            low_risk = [f for f in findings if f['risk'] == 'Low']
            
            if high_risk:
                report.append("### High/Critical Risk Issues")
                for finding in high_risk:
                    report.append(f"- **Host:** {finding['host']} | **Risk:** {finding['risk']}\n")
                    report.append(f"  **Issue:** {finding['description']}\n")
                    report.append(f"  **Recommendation:** {finding['recommendation']}\n")
            
            if medium_risk:
                report.append("### Medium Risk Issues")
                for finding in medium_risk:
                    report.append(f"- **Host:** {finding['host']} | **Risk:** {finding['risk']}\n")
                    report.append(f"  **Issue:** {finding['description']}\n")
                    report.append(f"  **Recommendation:** {finding['recommendation']}\n")
            
            if low_risk:
                report.append("### Low Risk Issues")
                for finding in low_risk:
                    report.append(f"- **Host:** {finding['host']} | **Risk:** {finding['risk']}\n")
                    report.append(f"  **Issue:** {finding['description']}\n")
                    report.append(f"  **Recommendation:** {finding['recommendation']}\n")
        else:
            report.append("## Security Findings")
            report.append("No security issues found during the audit.")
        
        # Summary
        report.append("## Summary")
        report.append(f"- **Total Hosts Scanned:** {len(hosts)}")
        report.append(f"- **Total Findings:** {len(findings)}")
        high_count = len([f for f in findings if f['risk'] in ['High', 'Critical']])
        report.append(f"- **High/Critical Issues:** {high_count}")
        
        return "\n".join(report)