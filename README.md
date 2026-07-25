# Cowrie SSH Honeypot Lab

A SSH honeypot deployed on Raspberry Pi 5 for 
capturing attacker behavior and post-exploitation commands.

## Project Overview

This project deploys Cowrie, a medium-interaction SSH honeypot used 
by real threat intelligence researchers, on a Raspberry Pi 5 running 
Kali Linux. All attacker interactions are captured in JSON format and 
analyzed with a custom Python parser that produces actionable reports.

## Lab Architecture

Internet/LAN
↓
Raspberry Pi 5 (Kali Linux)
├── Port 22 → Real SSH 
├── Port 2222 → Cowrie Honeypot
│ ├── Fake Linux filesystem
│ ├── Credential logging
│ └── Command execution logging
└── Logs → cowrie_parser.py → Analysis Report

## What It Captures

- Every SSH connection attempt with source IP and timestamp
- All usernames and passwords attempted
- Every command executed in the fake shell environment
- File download attempts
- Session duration and attacker behavior patterns

## Skills Demonstrated

- Network security monitoring and honeypot deployment
- Python scripting for log parsing and threat analysis
- Threat intelligence collection methodology

## Sample Parser Output
==================================================
Cowrie Honeypot Analysis Report
Generated: 2026-07-25 16:02:02.005949
==================================================

--- EVENT SUMMARY ---
4 cowrie.command.input
2 cowrie.login.failed
2 cowrie.client.var
1 cowrie.session.connect
1 cowrie.client.version
1 cowrie.client.kex
1 cowrie.client.fingerprint
1 cowrie.login.success
1 cowrie.client.size
1 cowrie.session.params
1 cowrie.log.closed
1 cowrie.session.closed

--- FAILED LOGIN ATTEMPTS: 2 ---
Top usernames tried:
  2x root
Top passwords tried:
  1x 
  1x root

--- SUCCESSFUL LOGINS: 1 ---
  10.0.0.31 logged in with root/root123

--- COMMANDS EXECUTED: 4 ---
  10.0.0.31: whoami
  10.0.0.31: cat /etc/shadow
  10.0.0.31: cat /etc/passwd
  10.0.0.31: exit

--- SOURCE IPs ---
  17 events from 10.0.0.31

==================================================

## Setup Guide

See [docs/setup_guide.md](docs/setup_guide.md) for full installation instructions.

## Usage

```bash
# Copy logs from Pi
scp pi:~/Projects/captures/cowrie.json ./captures/

# Run the parser
python3 scripts/cowrie_parser.py captures/cowrie.json

# Test with sample data
python3 scripts/cowrie_parser.py sample_data/cowrie_sample.json
```
## Author

Alan Kriger — NJIT Information Techonology Student
Forensics Minor
