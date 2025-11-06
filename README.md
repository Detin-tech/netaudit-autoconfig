# NetAudit AutoConfig

A Python + Ansible-based utility that scans local or remote networks, inventories devices and services, identifies misconfigurations, and optionally pushes auto-remediation playbooks.

## Features

- **Network Discovery**: Scans subnets via Nmap or native socket probing to identify hosts, open ports, and running services.
- **Configuration Fetch**: Uses Ansible modules (SSH/WinRM/SNMP) to pull config data from servers, switches, routers, or VMs.
- **Audit Engine**: Compares collected configs against YAML-defined baselines (e.g., open SSH to world, missing TLS, weak passwords, outdated packages).
- **Reporting**: Generates Markdown/HTML reports highlighting misconfigurations, severity, and remediation steps.
- **Auto-Config Mode**: Optionally applies fixes via predefined Ansible roles or configuration templates.
- **Extensible**: Supports custom rule packs — e.g., "CIS Ubuntu 22.04" or "Kubernetes Hardening Guide."

## Installation

```bash
git clone https://github.com/yourusername/netaudit-autoconfig.git
cd netaudit-autoconfig
pip install -r requirements.txt
```

## Usage

### Basic Network Scan

```bash
python netaudit.py --subnet 192.168.1.0/24 --output report.md
```

### Detailed Audit with Configuration Check

```bash
python netaudit.py --subnet 192.168.1.0/24 --audit --config-path /etc/ansible/conf_baselines/ --output report.md
```

### Auto-Remediation Mode

```bash
python netaudit.py --subnet 192.168.1.0/24 --audit --auto-fix --config-path /etc/ansible/conf_baselines/ --playbook-path /etc/ansible/playbooks/
```

## Requirements

- Python 3.7+
- Nmap
- Ansible 2.9+
- Additional Python dependencies listed in `requirements.txt`

## Project Structure

```
netaudit-autoconfig/
├── README.md
├── requirements.txt
├── netaudit.py              # Main application entry point
├── config/
│   ├── baseline_configs/    # Default security baselines
│   └── rules/               # Custom audit rules
├── playbooks/               # Ansible playbooks for auto-remediation
├── reports/                 # Generated audit reports
└── utils/
    ├── scanner.py           # Network discovery functionality
    ├── auditor.py           # Configuration audit engine
    ├── reporter.py          # Reporting module
    └── configurator.py      # Auto-configuration module
```

## License

MIT