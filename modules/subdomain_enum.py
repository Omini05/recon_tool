import subprocess
import os


def enumerate_subdomains(domain):
    print("[+] Enumerating subdomains...")

    os.makedirs("output/scans", exist_ok=True)
    output_file = "output/scans/subdomains.txt"

    try:
        subprocess.run(
            ["sublist3r", "-d", domain, "-o", output_file],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if not os.path.exists(output_file):
            print("[-] No subdomains found")
            return []

        with open(output_file, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]

        print(f"[+] {len(subdomains)} subdomains discovered")
        return subdomains

    except Exception as e:
        print(f"[-] Error during subdomain enumeration: {e}")
        return []
