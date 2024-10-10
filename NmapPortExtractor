import csv
import os
import sys
import socket
import re

def resolve_dns(ip):
    """
    Attempt to resolve DNS name for the given IP address.
    If it fails, return 'N/A'.
    """
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "N/A"

def parse_nmap_file(nmap_file):
    """
    Parse the Nmap file and extract each host's IP, open ports, and DNS names.
    """
    hosts_info = []
    with open(nmap_file, 'r') as file:
        current_ip = None
        for line in file:
            # Match IP address
            ip_match = re.search(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                current_ip = ip_match.group(1)
                dns_name = resolve_dns(current_ip)
                continue

            # Match open ports
            port_match = re.search(r'(\d+)/tcp\s+open', line)
            if port_match and current_ip:
                port = port_match.group(1)
                hosts_info.append([current_ip, port, dns_name])

    return hosts_info

def save_to_csv(hosts_info, output_file):
    """
    Save the parsed data to a CSV file.
    """
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['IP Address', 'Port', 'DNS Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for host_info in hosts_info:
            writer.writerow({'IP Address': host_info[0], 'Port': host_info[1], 'DNS Name': host_info[2]})

def main(nmap_file, output_file):
    """
    Main function to parse the Nmap file and save the results to a CSV.
    """
    if not os.path.isfile(nmap_file):
        print(f"Error: The file '{nmap_file}' does not exist.")
        sys.exit(1)

    hosts_info = parse_nmap_file(nmap_file)
    save_to_csv(hosts_info, output_file)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <nmap_file> <output_csv_file>")
        sys.exit(1)

    nmap_file = sys.argv[1]
    output_file = sys.argv[2]
    main(nmap_file, output_file)
