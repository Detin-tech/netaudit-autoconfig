# NetAudit AutoConfig Report
_Generated on: 2025-11-06 15:44:44_

## Discovered Hosts
Found 2 active hosts in the network:

### 192.168.1.10 (test-server-01)
Open Ports:
- 22/TCP (ssh) - open
  Version: OpenSSH 7.9
- 80/TCP (http) - open
  Version: Apache 2.4.38

### 192.168.1.20 (test-workstation-01)
Open Ports:
- 3389/TCP (ms-wbt-server) - open
  Version: Microsoft Terminal Services
- 443/TCP (https) - open
  Version: nginx 1.18.0

## Security Findings
### High/Critical Risk Issues
- **Host:** 192.168.1.10 | **Risk:** High

  **Issue:** SSH service accessible from network

  **Recommendation:** Restrict SSH access with firewall rules

- **Host:** 192.168.1.20 | **Risk:** Critical

  **Issue:** RDP service accessible from network

  **Recommendation:** Restrict RDP access with firewall rules and enable NLA

### Medium Risk Issues
- **Host:** 192.168.1.10 | **Risk:** Medium

  **Issue:** HTTP service running without encryption

  **Recommendation:** Enable HTTPS with valid certificate

## Summary
- **Total Hosts Scanned:** 2
- **Total Findings:** 3
- **High/Critical Issues:** 2