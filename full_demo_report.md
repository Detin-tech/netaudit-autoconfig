# NetAudit AutoConfig Report
_Generated on: 2025-11-06 15:47:00_

## Discovered Hosts
Found 3 active hosts in the network:

### 192.168.1.10 (webserver01.example.com)
Open Ports:
- 22/TCP (ssh) - open
  Version: OpenSSH 8.0
- 80/TCP (http) - open
  Version: Apache 2.4.6
- 443/TCP (https) - open
  Version: Apache 2.4.6

### 192.168.1.20 (dbserver01.example.com)
Open Ports:
- 22/TCP (ssh) - open
  Version: OpenSSH 8.0
- 3306/TCP (mysql) - open
  Version: MySQL 8.0.28

### 192.168.1.30 (workstation01.example.com)
Open Ports:
- 3389/TCP (ms-wbt-server) - open
  Version: Microsoft Terminal Services

## Security Findings
### High/Critical Risk Issues
- **Host:** 192.168.1.10 | **Risk:** High

  **Issue:** SSH service accessible from network

  **Recommendation:** Restrict SSH access with firewall rules and use key-based authentication

- **Host:** 192.168.1.20 | **Risk:** High

  **Issue:** MySQL database listening on all interfaces

  **Recommendation:** Bind MySQL to localhost only and use SSH tunneling for remote access

- **Host:** 192.168.1.30 | **Risk:** Critical

  **Issue:** RDP service accessible from network without Network Level Authentication

  **Recommendation:** Enable Network Level Authentication (NLA) and restrict RDP access with firewall rules

### Medium Risk Issues
- **Host:** 192.168.1.10 | **Risk:** Medium

  **Issue:** HTTP service running without encryption

  **Recommendation:** Redirect all HTTP traffic to HTTPS and obtain a valid SSL certificate

## Summary
- **Total Hosts Scanned:** 3
- **Total Findings:** 4
- **High/Critical Issues:** 3