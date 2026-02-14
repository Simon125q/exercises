# Linux Networking Fundamentals: Practice Exercises

**Material**: [Podstawy sieci Linux, które MUSISZ znać!](https://www.youtube.com/watch?v=yqzeEVl2TnM)  
**Date**: 2026-02-14  
**Total Estimated Time**: ~55 minutes

## Overview
These exercises are designed to reinforce the systematic approach to Linux networking troubleshooting presented in the video. You will move from local interface verification to service discovery and external connectivity diagnosis.

---

## Exercise 1: Interface and Connectivity Audit (Apply)
- **Estimated Time**: 8 minutes
- **Objective**: Verify local network stack and interface configuration.
- **Context**: You've just logged into a new server and need to verify its network identity and basic connectivity.
- **Tasks**:
    1. Identify all network interfaces and their IP addresses.
    2. Verify the loopback interface is responding.
    3. Find the default gateway IP address.
    4. Test connectivity to the default gateway.
- **Reference**: `ip addr show`, `ping`, `ip route show`.
- **Validation**: You should have the IP of the main interface and the gateway, and pings to both 127.0.0.1 and the gateway should succeed.

## Exercise 2: Service and Port Discovery (Adapt)
- **Estimated Time**: 12 minutes
- **Objective**: Identify listening services and verify port accessibility.
- **Context**: A developer reports that their web application is running but they can't connect to it. You need to check if the service is actually listening and on which port.
- **Tasks**:
    1. List all listening TCP and UDP ports using numeric output.
    2. Identify which port the SSH service is listening on.
    3. Use `telnet` or `nc` to verify if port 22 is reachable locally.
- **Reference**: `ss -tuln`, `telnet`.
- **Validation**: Identify the port (e.g., 22) and successfully "connect" to it using telnet or a similar tool.

## Exercise 3: DNS and Path Troubleshooting (Extend)
- **Estimated Time**: 20 minutes
- **Objective**: Diagnose external connectivity and DNS resolution issues.
- **Context**: Users are reporting they cannot reach external services. You need to determine if it's a DNS issue or a routing issue.
- **Tasks**:
    1. Check if `google.com` resolves to an IP address.
    2. Use `dig` or `nslookup` to find the mail servers (MX records) for `google.com`.
    3. Trace the path to `8.8.8.8` to see the network hops.
    4. Capture 5 packets of ICMP traffic while pinging a host.
- **Reference**: `dig`, `nslookup`, `traceroute`, `tcpdump`.
- **Validation**: Successfully resolve the hostname and identify the path taken by packets.

## Exercise 4: The Rescue Sequence (Synthesis)
- **Estimated Time**: 15 minutes
- **Objective**: Create a diagnostic script for rapid troubleshooting.
- **Context**: You want to automate the "Rescue Sequence" shown in the video to quickly audit any server you log into.
- **Tasks**:
    1. Create a bash script `diagnose.sh` that combines interface check, routing check, gateway ping, and DNS test.
    2. The script should output clear headers for each section.
    3. Make the script executable and run it to verify the current environment.
- **Reference**: Rescue Sequence one-liner from the video.
- **Validation**: Running `./diagnose.sh` provides a complete overview of the network status without manual command entry.

---

## Getting Started
1. Run the setup script: `python3 setup_exercises.py`
2. Navigate to the `exercises/` directory.
3. Follow the instructions in each exercise's `README.md`.

## Cleanup
When finished, run the cleanup script: `bash cleanup_exercises.sh`
