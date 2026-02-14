#!/bin/bash

# Setup script for tcpdump Network Analysis exercises
# Generated: February 10, 2026

set -e  # Exit on error

EXERCISE_DIR="exercises"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Setting up exercises for: tcpdump Network Analysis"
echo "================================================"

# Create main exercise directory
if [ -d "$EXERCISE_DIR" ]; then
    echo "Warning: $EXERCISE_DIR already exists. Files may be overwritten."
    read -p "Continue? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 1
    fi
fi

mkdir -p "$EXERCISE_DIR"
cd "$EXERCISE_DIR"

# ============================================================
# Exercise 1: Verify Network Connectivity with ICMP Capture
# ============================================================
echo "Creating Exercise 1: ICMP Capture..."
mkdir -p 01_icmp_connectivity

cat > 01_icmp_connectivity/README.md << 'EOF'
# Exercise 1: Verify Network Connectivity with ICMP Capture

## Quick Start

1. Open two terminal windows
2. In terminal 1, start pinging: `ping 8.8.8.8`
3. In terminal 2, capture ICMP traffic: `sudo tcpdump -i any -n -c 20 icmp`
4. Observe the captured packets
5. Stop the ping with Ctrl+C

## What to Look For

- ICMP echo request packets (your ping going out)
- ICMP echo reply packets (responses coming back)
- Packet pairs indicating successful connectivity

## Reference Commands

- List interfaces: `tcpdump -D`
- Basic ICMP capture: `sudo tcpdump -i any -n icmp`
- Limited capture: `sudo tcpdump -i any -n -c 20 icmp`
EOF

# ============================================================
# Exercise 2: Analyze HTTP Traffic
# ============================================================
echo "Creating Exercise 2: HTTP Traffic Analysis..."
mkdir -p 02_http_analysis

cat > 02_http_analysis/README.md << 'EOF'
# Exercise 2: Analyze HTTP Traffic to Diagnose Slow Website

## Quick Start

1. Open two terminal windows
2. In terminal 1, start capturing HTTP traffic: `sudo tcpdump -i any -A port 80`
3. In terminal 2, make an HTTP request: `curl http://example.com`
4. Observe the HTTP headers in the capture output
5. Stop the capture with Ctrl+C

## What to Look For

- HTTP GET request with headers (Host, User-Agent, etc.)
- HTTP response status code (200 OK, 404 Not Found, etc.)
- Request/response pattern

## Reference Commands

- Capture with ASCII output: `sudo tcpdump -A port 80`
- Make HTTP request: `curl http://example.com`
- Limit packets: `sudo tcpdump -A -c 50 port 80`
EOF

# ============================================================
# Exercise 3: Investigate Suspicious Network Activity
# ============================================================
echo "Creating Exercise 3: Suspicious Activity Investigation..."
mkdir -p 03_suspicious_activity

cat > 03_suspicious_activity/README.md << 'EOF'
# Exercise 3: Investigate Suspicious Network Activity

## Quick Start

1. Navigate to this directory: `cd exercises/03_suspicious_activity`
2. Start capturing traffic to 1.1.1.1: `sudo tcpdump -i any -w suspicious_traffic.pcap host 1.1.1.1`
3. In another terminal, generate test traffic:
   - `ping -c 5 1.1.1.1`
   - `curl http://1.1.1.1` (may timeout, that's OK)
4. Wait 30 seconds, then stop the capture with Ctrl+C
5. Read the saved file: `sudo tcpdump -r suspicious_traffic.pcap`

## What to Look For

- Both ICMP and TCP packets in the capture
- Packet count summary when capture stops
- Different protocol types in the saved file

## Reference Commands

- Save capture: `sudo tcpdump -w filename.pcap host 1.1.1.1`
- Read capture: `sudo tcpdump -r filename.pcap`
- Count packets: Check the summary when tcpdump exits
EOF

# ============================================================
# Exercise 4: Debug Application Communication Issues
# ============================================================
echo "Creating Exercise 4: Application Debugging..."
mkdir -p 04_app_debugging

cat > 04_app_debugging/README.md << 'EOF'
# Exercise 4: Debug Application Communication Issues

## Quick Start

1. Navigate to this directory: `cd exercises/04_app_debugging`
2. Start capturing database traffic: `sudo tcpdump -i any -w db_traffic.pcap port 3306`
3. In another terminal, run the test script: `bash simulate_db_connection.sh`
4. Let it run for 20 seconds
5. Stop the capture with Ctrl+C
6. Read the saved file: `sudo tcpdump -r db_traffic.pcap`

## What to Look For

- TCP SYN packets (Flags [S]) - connection attempts
- TCP RST packets (Flags [R]) - connection refused
- Whether the server responds to connection attempts

## Reference Commands

- Capture on specific port: `sudo tcpdump -w file.pcap port 3306`
- Read and analyze: `sudo tcpdump -r file.pcap`
- Verbose output: `sudo tcpdump -v -r file.pcap`
EOF

# Create the database connection simulation script
cat > 04_app_debugging/simulate_db_connection.sh << 'EOF'
#!/bin/bash

echo "Simulating database connection attempts..."
echo "This will attempt to connect to localhost:3306 every 2 seconds"
echo "Press Ctrl+C to stop"
echo ""

for i in {1..10}; do
    echo "Attempt $i: Connecting to localhost:3306..."
    timeout 1 bash -c 'cat < /dev/null > /dev/tcp/localhost/3306' 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "  ✓ Connection successful"
    else
        echo "  ✗ Connection failed (expected if MySQL is not running)"
    fi
    sleep 2
done

echo ""
echo "Simulation complete. Check your tcpdump capture for the connection attempts."
EOF

chmod +x 04_app_debugging/simulate_db_connection.sh

# ============================================================
# Exercise 5: Create Network Traffic Report
# ============================================================
echo "Creating Exercise 5: Security Audit Report..."
mkdir -p 05_security_audit

cat > 05_security_audit/README.md << 'EOF'
# Exercise 5: Create Network Traffic Report for Security Audit

## Quick Start

1. Navigate to this directory: `cd exercises/05_security_audit`
2. Start the traffic generator: `bash generate_traffic.sh &`
3. Open multiple terminals and start these captures:
   - Terminal 1: `sudo tcpdump -i any -w http_traffic.pcap port 80`
   - Terminal 2: `sudo tcpdump -i any -w https_traffic.pcap port 443`
   - Terminal 3: `sudo tcpdump -i any -w dns_traffic.pcap port 53`
   - Terminal 4: `sudo tcpdump -i any -w icmp_traffic.pcap icmp`
4. Let them run for 60 seconds
5. Stop all captures with Ctrl+C
6. Read each file and count packets
7. Create your report in `traffic_report.txt`

## What to Look For

- Packet counts for each protocol
- Which protocol has the most activity
- Any unusual patterns

## Report Template

Create a file called `traffic_report.txt` with:
- HTTP packets captured: [count]
- HTTPS packets captured: [count]
- DNS packets captured: [count]
- ICMP packets captured: [count]
- Most active protocol: [name]
- Observations: [your notes]

## Reference Commands

- Run in background: `sudo tcpdump -w file.pcap port 80 &`
- Stop background tcpdump: `sudo pkill tcpdump`
- Count packets: Check summary when tcpdump exits
EOF

# Create the traffic generation script
cat > 05_security_audit/generate_traffic.sh << 'EOF'
#!/bin/bash

echo "Generating network traffic for 60 seconds..."
echo "This script will create HTTP, HTTPS, DNS, and ICMP traffic"
echo ""

# Function to generate traffic
generate_traffic() {
    while true; do
        # HTTP traffic
        curl -s http://example.com > /dev/null 2>&1
        sleep 3
        
        # HTTPS traffic
        curl -s https://www.google.com > /dev/null 2>&1
        sleep 3
        
        # DNS queries (curl does this automatically, but we'll be explicit)
        nslookup example.com > /dev/null 2>&1
        sleep 2
        
        # ICMP traffic
        ping -c 2 8.8.8.8 > /dev/null 2>&1
        sleep 3
    done
}

# Run traffic generation in background
generate_traffic &
TRAFFIC_PID=$!

echo "Traffic generation started (PID: $TRAFFIC_PID)"
echo "This will run for 60 seconds..."
echo ""

# Wait for 60 seconds
sleep 60

# Stop traffic generation
kill $TRAFFIC_PID 2>/dev/null
echo ""
echo "Traffic generation stopped."
echo "You can now analyze your captured packets."
EOF

chmod +x 05_security_audit/generate_traffic.sh

# ============================================================
# Create main README
# ============================================================
cat > README.md << 'EOF'
# tcpdump Network Analysis - Exercises

This directory contains 5 hands-on exercises to practice tcpdump network analysis.

## Exercises

1. **ICMP Connectivity** (8 min) - Basic packet capture and ICMP filtering
2. **HTTP Analysis** (12 min) - Port filtering and viewing packet content
3. **Suspicious Activity** (15 min) - Host filtering and saving captures
4. **App Debugging** (15 min) - Debugging application connectivity issues
5. **Security Audit** (20 min) - Comprehensive traffic analysis and reporting

## Getting Started

Each exercise has its own directory with:
- README.md - Instructions and reference commands
- Supporting scripts (where applicable)

Navigate to each exercise directory and follow the README instructions.

## Important Notes

- All tcpdump commands require sudo/root privileges
- Use Ctrl+C to stop packet captures
- Saved .pcap files can be read with `tcpdump -r filename.pcap`
- Exercises are independent - complete them in any order

## Common Commands Reference

- List interfaces: `tcpdump -D`
- Basic capture: `sudo tcpdump -i any -c 10`
- Filter by protocol: `sudo tcpdump icmp`
- Filter by port: `sudo tcpdump port 80`
- Filter by host: `sudo tcpdump host 8.8.8.8`
- View ASCII content: `sudo tcpdump -A`
- Save to file: `sudo tcpdump -w file.pcap`
- Read from file: `sudo tcpdump -r file.pcap`
- No hostname resolution: `sudo tcpdump -n`

## Troubleshooting

- **Permission denied**: Use `sudo`
- **No packets captured**: Check interface with `-i` flag
- **Too much output**: Use `-c` to limit packet count
- **Filter not working**: Check syntax and use quotes for complex filters
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "Exercise directory structure:"
tree -L 2 "$EXERCISE_DIR" 2>/dev/null || find "$EXERCISE_DIR" -type d | head -20

echo ""
echo "Next steps:"
echo "1. Navigate to the exercises directory: cd $EXERCISE_DIR"
echo "2. Read the main README: cat README.md"
echo "3. Start with exercise 01: cd 01_icmp_connectivity"
echo "4. Follow the exercise guide in tcpdump_exercises.md"
echo ""
echo "When finished, run cleanup_tcpdump_exercises.sh to remove all created files"
