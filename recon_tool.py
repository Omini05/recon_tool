#!/usr/bin/env python3
import argparse
from modules.subdomain_enum import enumerate_subdomains
from modules.port_scan import scan_ports
from modules.report import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Automated Reconnaissance Tool"
    )

    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target domain or IP address"
    )

    args = parser.parse_args()
    target = args.target

    print(f"[+] Starting reconnaissance on: {target}")

    subdomains = enumerate_subdomains(target)

    if not subdomains:
        print("[-] No subdomains found. Exiting.")
        return

    scan_results = scan_ports(subdomains)

    generate_report(target, subdomains, scan_results)

    print("[+] Reconnaissance workflow completed successfully")


if __name__ == "__main__":
    main()
