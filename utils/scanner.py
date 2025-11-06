"""
Network Scanner Module

This module handles network discovery using nmap and socket probing.
"""

import nmap
import socket
from netaddr import IPNetwork


class NetworkScanner:
    def __init__(self, subnet):
        self.subnet = subnet
        self.nm = nmap.PortScanner()
    
    def discover_hosts(self):
        """Scan subnet and return list of active hosts with open ports"""
        try:
            # Perform SYN scan on common ports
            print(f"[*] Scanning {self.subnet} for active hosts...")
            self.nm.scan(hosts=self.subnet, arguments='-sn')
            
            hosts = []
            for ip in self.nm.all_hosts():
                if self.nm[ip].state() == 'up':
                    host_info = {
                        'ip': ip,
                        'hostname': self.nm[ip].hostname() or 'Unknown',
                        'ports': self._scan_ports(ip)
                    }
                    hosts.append(host_info)
            
            return hosts
        except Exception as e:
            print(f"Error during network scan: {e}")
            return []
    
    def _scan_ports(self, ip):
        """Scan common ports for a specific host"""
        try:
            # Scan common ports
            self.nm.scan(hosts=ip, arguments='-p 22,80,443,3389 -sV')
            
            ports = []
            if 'tcp' in self.nm[ip]:
                for port in self.nm[ip]['tcp']:
                    port_info = {
                        'port': port,
                        'state': self.nm[ip]['tcp'][port]['state'],
                        'service': self.nm[ip]['tcp'][port]['name'],
                        'version': self.nm[ip]['tcp'][port].get('product', '')
                    }
                    ports.append(port_info)
            
            return ports
        except Exception as e:
            print(f"Error scanning ports for {ip}: {e}")
            return []