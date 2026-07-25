#!/usr/bin/env python3

import json
import sys
from collections import Counter
from datetime import datetime

def parse_cowrie_log(log_file):
    events = []
    
    with open(log_file, 'r') as f:
        for line in f:
            try:
                event = json.loads(line.strip())
                events.append(event)
            except json.JSONDecodeError:
                continue
    
    print("=" * 50)
    print("Cowrie Honeypot Analysis Report")
    print("Generated: " + str(datetime.now()))
    print("=" * 50)
    
    # Count event types
    event_types = Counter(e.get('eventid', 'unknown') for e in events)
    print("\n--- EVENT SUMMARY ---")
    for event_type, count in event_types.most_common():
        print(str(count) + " " + event_type)
    
    # Login attempts
    login_attempts = [e for e in events if e.get('eventid') == 'cowrie.login.failed']
    print("\n--- FAILED LOGIN ATTEMPTS: " + str(len(login_attempts)) + " ---")
    
    usernames = Counter(e.get('username', '') for e in login_attempts)
    print("Top usernames tried:")
    for username, count in usernames.most_common(5):
        print("  " + str(count) + "x " + username)
    
    passwords = Counter(e.get('password', '') for e in login_attempts)
    print("Top passwords tried:")
    for password, count in passwords.most_common(5):
        print("  " + str(count) + "x " + password)
    
    # Successful logins
    success = [e for e in events if e.get('eventid') == 'cowrie.login.success']
    print("\n--- SUCCESSFUL LOGINS: " + str(len(success)) + " ---")
    for e in success:
        print("  " + e.get('src_ip', '') + " logged in with " + e.get('username', '') + "/" + e.get('password', ''))
    
    # Commands run
    commands = [e for e in events if e.get('eventid') == 'cowrie.command.input']
    print("\n--- COMMANDS EXECUTED: " + str(len(commands)) + " ---")
    for e in commands[:10]:
        print("  " + e.get('src_ip', '') + ": " + e.get('input', ''))
    
    # Source IPs
    src_ips = Counter(e.get('src_ip', '') for e in events if e.get('src_ip'))
    print("\n--- SOURCE IPs ---")
    for ip, count in src_ips.most_common(5):
        print("  " + str(count) + " events from " + ip)
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cowrie_parser.py <cowrie.json>")
        sys.exit(1)
    parse_cowrie_log(sys.argv[1])
