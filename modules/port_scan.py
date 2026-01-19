import subprocess
import os


def scan_ports(subdomains):
    print("[+] Starting fast port scanning (common ports only)...")

    os.makedirs("output/scans", exist_ok=True)
    scan_results = {}

    for host in subdomains:
        print(f"    Scanning {host}")
        output_file = f"output/scans/{host.replace('.', '_')}.xml"

        try:
            subprocess.run(
                [
                    "nmap",
                    "-p", "80,443,8080,8443",
                    "-T4",
                    "--open",
                    "-oX", output_file,
                    host
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            scan_results[host] = output_file

        except Exception as e:
            print(f"[-] Scan failed for {host}: {e}")

    return scan_results
