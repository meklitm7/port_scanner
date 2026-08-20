# Network Scanning Tools

This project contains Python and Bash tools developed.

## Tools

- **Python Port Scanner** – Scans TCP and UDP ports without using the Nmap Python module.
- **Nmap Python Scanner** – Uses the `python-nmap` module to perform different Nmap scans.
- **Host Discovery Tool** – Accepts an IP address and IP class, determines the network range, and checks which hosts are up or down.
- **Bash NSE Scanner** – Accepts an IP address and an Nmap NSE script name, then runs the selected NSE script against the target.

## Technologies

- Python
- Bash
- Nmap
- Python `socket`, `ipaddress`, `subprocess`, `threading`, and `queue` modules
- Nmap NSE