#!/usr/bin/env python3
"""
Setup script for Linux Networking Fundamentals exercises
Based on: Podstawy sieci Linux, które MUSISZ znać!
Generated: 2026-02-14
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

EXERCISE_DIR = Path("exercises")

def create_directory_structure():
    """Create the main directory structure for exercises."""
    print(f"Creating exercise directory: {EXERCISE_DIR}")
    
    if EXERCISE_DIR.exists():
        shutil.rmtree(EXERCISE_DIR)
    
    EXERCISE_DIR.mkdir()

def setup_exercise_01():
    """Setup files for exercise 01: Interface and Connectivity Audit."""
    ex_dir = EXERCISE_DIR / "01_interface_audit"
    ex_dir.mkdir()
    
    (ex_dir / "README.md").write_text("""# Exercise 1: Interface and Connectivity Audit

## Objective
Verify local network stack and interface configuration.

## Tasks
1. Identify all network interfaces and their IP addresses.
2. Verify the loopback interface is responding.
3. Find the default gateway IP address.
4. Test connectivity to the default gateway.

## Commands to use
- `ip addr show`
- `ping -c 3 127.0.0.1`
- `ip route show`
""")

def setup_exercise_02():
    """Setup files for exercise 02: Service and Port Discovery."""
    ex_dir = EXERCISE_DIR / "02_port_discovery"
    ex_dir.mkdir()
    
    # We can't easily start a real service without root/complex setup, 
    # but we can simulate a "listening" port by starting a simple nc listener in background if available,
    # or just instruct the user to find existing ones like SSH.
    # For this environment, we'll assume SSH (22) is running.
    
    (ex_dir / "README.md").write_text("""# Exercise 2: Service and Port Discovery

## Objective
Identify listening services and verify port accessibility.

## Context
A developer reports that their web application is running but they can't connect to it. You need to check if the service is actually listening and on which port.

## Tasks
1. List all listening TCP and UDP ports using numeric output.
2. Identify which port the SSH service is listening on.
3. Use `telnet` or `nc` to verify if port 22 is reachable locally.

## Commands to use
- `ss -tuln`
- `telnet localhost 22` or `nc -zv localhost 22`
""")

def setup_exercise_03():
    """Setup files for exercise 03: DNS and Path Troubleshooting."""
    ex_dir = EXERCISE_DIR / "03_dns_troubleshooting"
    ex_dir.mkdir()
    
    (ex_dir / "README.md").write_text("""# Exercise 3: DNS and Path Troubleshooting

## Objective
Diagnose external connectivity and DNS resolution issues.

## Tasks
1. Check if `google.com` resolves to an IP address.
2. Use `dig` or `nslookup` to find the mail servers (MX records) for `google.com`.
3. Trace the path to `8.8.8.8` to see the network hops.
4. (Optional) Capture 5 packets of ICMP traffic while pinging a host.

## Commands to use
- `nslookup google.com`
- `dig google.com MX`
- `traceroute 8.8.8.8`
- `sudo tcpdump -c 5 icmp` (requires sudo)
""")

def setup_exercise_04():
    """Setup files for exercise 04: The Rescue Sequence."""
    ex_dir = EXERCISE_DIR / "04_rescue_sequence"
    ex_dir.mkdir()
    
    (ex_dir / "README.md").write_text("""# Exercise 4: The Rescue Sequence

## Objective
Create a diagnostic script for rapid troubleshooting.

## Tasks
1. Create a bash script named `diagnose.sh`.
2. The script should:
   - Print "--- INTERFACES ---" and run `ip addr show`.
   - Print "--- ROUTING ---" and run `ip route show`.
   - Print "--- GATEWAY PING ---" and ping the default gateway once.
   - Print "--- DNS TEST ---" and resolve `google.com`.
3. Make the script executable: `chmod +x diagnose.sh`.
4. Run it: `./diagnose.sh`.
""")

def main():
    """Main setup function."""
    print("=" * 60)
    print("Setting up exercises for: Linux Networking Fundamentals")
    print("=" * 60)
    
    try:
        create_directory_structure()
        setup_exercise_01()
        setup_exercise_02()
        setup_exercise_03()
        setup_exercise_04()
        
        print("\n✅ Setup complete!")
        print(f"Exercises created in: {EXERCISE_DIR.absolute()}")
        print("\nNext steps:")
        print(f"1. cd {EXERCISE_DIR}")
        print("2. Start with 01_interface_audit/README.md")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
