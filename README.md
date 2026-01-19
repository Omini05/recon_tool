# Recon Tool

Recon Tool is a Python-based automated reconnaissance and attack surface mapping CLI tool.
It automates subdomain enumeration, fast port scanning, and service discovery, and generates
structured reports for analysis.

This project is intended for educational use, security labs, and authorized reconnaissance only.

---

## Features

- Automated subdomain enumeration
- Fast common-port scanning (web-focused)
- Nmap XML parsing
- Extraction of open ports and services
- Structured JSON report generation
- Command-line interface (CLI)
- Safe and reproducible installation using pipx

---

## Installation
```bash
git clone https://github.com/Omini05/recon-tool.git
cd recon-tool
pip install -r requirements.txt
export PATH=$PATH:$(pwd)/bin
=======
- Automated subdomain enumeration
- Fast common-port scanning (web-focused)
- Nmap XML parsing
- Extraction of open ports and services
- Structured JSON report generation
- Command-line interface (CLI)
- Safe and reproducible installation using pipx

---

## Requirements

- Linux (Kali Linux recommended)
- Python 3.9+
- Nmap
- Sublist3r
- pipx

---

## Installation (Recommended: pipx)

Important (Kali Linux Users)
Kali uses an externally managed Python environment.
Do NOT use pip install . directly.
Use pipx, which is designed for CLI tools.

---

### Step 1: Install pipx (one-time)

sudo apt update
sudo apt install pipx -y
pipx ensurepath

Restart the terminal once after this step.

---

### Step 2: Clone the repository

git clone https://github.com/Omini05/recon_tool.git
cd recon_tool

---

### Step 3: Install the tool

pipx install .

This will:
- Create an isolated virtual environment
- Install dependencies
- Register the recon command permanently

---

### Step 4: Verify installation

recon --help

---

## Usage

recon -t example.com

Example:

recon -t sakec.ac.in

---

## Output

output/reports/<target>_report.json

Each report includes:
- Discovered subdomains
- Open ports
- Detected services

---

## Project Structure

recon_tool/
├── modules/
│   ├── subdomain_enum.py
│   ├── port_scan.py
│   ├── xml_parser.py
│   └── report.py
├── recon_tool.py
├── setup.py
├── requirements.txt
└── README.md

---

## Disclaimer

This tool is intended only for educational purposes and authorized security testing.
Do NOT scan systems or networks without explicit permission.
The author is not responsible for misuse of this tool.

---

## Author

Omini Vishwakarma
Cyber Security Engineering Student

