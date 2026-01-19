import json
import os
from modules.xml_parser import parse_nmap_xml


def generate_report(target, subdomains, scan_results):
    print("[+] Generating final report...")

    os.makedirs("output/reports", exist_ok=True)

    parsed_results = {}

    for host, xml_file in scan_results.items():
        parsed_results[host] = parse_nmap_xml(xml_file)

    report_data = {
        "target": target,
        "total_subdomains": len(subdomains),
        "results": parsed_results
    }

    report_file = f"output/reports/{target}_report.json"

    with open(report_file, "w") as f:
        json.dump(report_data, f, indent=4)

    print(f"[+] Report generated: {report_file}")
