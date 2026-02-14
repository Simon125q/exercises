#!/bin/bash

# Setup script for "Logi systemowe Linux, które MUSISZ znać!" exercises
# Generated: 2026-02-15

set -e  # Exit on error

EXERCISE_DIR="exercises"
DATE_NOW=$(date +"%Y-%m-%d %H:%M:%S")
DATE_1H_AGO=$(date -d "45 minutes ago" +"%Y-%m-%d %H:%M:%S")
DATE_24H_AGO=$(date -d "12 hours ago" +"%Y-%m-%d %H:%M:%S")

echo "Setting up exercises for: Logi systemowe Linux, które MUSISZ znać!"
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

# --- Exercise 1: Basic Journal Inspection ---
# We will simulate journal output by creating a text file that users can "grep" or "cat" 
# since we can't easily inject into the real system journal without root/complex setup.
mkdir -p "$EXERCISE_DIR/01_journal_basics"
cat > "$EXERCISE_DIR/01_journal_basics/mock_journal.txt" << EOF
$DATE_24H_AGO systemd[1]: Starting Session 1 of user ubuntu.
$DATE_24H_AGO kernel: Linux version 5.15.0-101-generic
$DATE_1H_AGO mock-auth[1234]: Checking credentials for user 'admin'
$DATE_1H_AGO mock-auth[1234]: [ERROR] Invalid configuration: missing secret key
$DATE_1H_AGO systemd[1]: Started Session 1 of user ubuntu.
EOF

cat > "$EXERCISE_DIR/01_journal_basics/README.md" << 'EOF'
# Exercise 1: Basic Journal Inspection
Use the `mock_journal.txt` file as if it were the output of `journalctl`.
Task: Find the error from the 'mock-auth' service that occurred in the last hour.
EOF

# --- Exercise 2: Troubleshooting a Failing Service ---
mkdir -p "$EXERCISE_DIR/02_service_debug/etc"
cat > "$EXERCISE_DIR/02_service_debug/etc/config.conf" << EOF
# Web Portal Configuration
port=8080a
host=0.0.0.0
timeout=30
EOF

cat > "$EXERCISE_DIR/02_service_debug/README.md" << 'EOF'
# Exercise 2: Troubleshooting a Failing Service
The 'web-portal' service is failing. 
1. Check the config in `etc/config.conf`.
2. The log (simulated) would say: "Invalid port: 8080a".
3. Fix the port to 8080.
EOF

# --- Exercise 3: Kernel and Hardware Diagnostics ---
mkdir -p "$EXERCISE_DIR/03_hardware_logs/var/log"
cat > "$EXERCISE_DIR/03_hardware_logs/mock_dmesg.txt" << EOF
[    0.000000] Linux version 5.15.0
[    1.234567] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    2.345678] usb 1-1: device descriptor read/64, error -110
[    3.456789] sd 2:0:0:0: [sda] Attached SCSI disk
EOF

cat > "$EXERCISE_DIR/03_hardware_logs/var/log/syslog" << EOF
$DATE_NOW kernel: [    2.345678] usb 1-1: device descriptor read/64, error -110
$DATE_NOW systemd[1]: Reached target Multi-User System.
EOF

cat > "$EXERCISE_DIR/03_hardware_logs/README.md" << 'EOF'
# Exercise 3: Kernel and Hardware Diagnostics
Use `mock_dmesg.txt` to find USB errors.
Check `var/log/syslog` to see if the same error is recorded there.
EOF

# --- Exercise 4: The 24-Hour Error Challenge ---
mkdir -p "$EXERCISE_DIR/04_error_challenge"
cat > "$EXERCISE_DIR/04_error_challenge/daily_logs.txt" << EOF
$DATE_24H_AGO service-a[100]: [ERROR] Connection refused
$DATE_24H_AGO service-b[200]: [ERROR] Database timeout
$DATE_1H_AGO service-a[101]: [ERROR] Connection refused
$DATE_1H_AGO service-c[300]: [ERROR] Out of memory
$DATE_NOW service-a[102]: [ERROR] Connection refused
EOF

cat > "$EXERCISE_DIR/04_error_challenge/README.md" << 'EOF'
# Exercise 4: The 24-Hour Error Challenge
Analyze `daily_logs.txt`.
1. Count unique services with errors.
2. Find the most frequent error message.
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "Exercise directory structure:"
ls -R "$EXERCISE_DIR"

echo ""
echo "Next steps:"
echo "1. Navigate to the exercises directory: cd $EXERCISE_DIR"
echo "2. Read the exercise_guide.md for instructions"
echo ""
echo "When finished, run cleanup_exercises.sh to remove all created files"
