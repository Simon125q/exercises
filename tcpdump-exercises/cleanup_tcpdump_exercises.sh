#!/bin/bash

# Cleanup script for tcpdump Network Analysis exercises
# Generated: February 10, 2026

EXERCISE_DIR="exercises"

echo "Cleanup script for: tcpdump Network Analysis"
echo "================================================"
echo ""
echo "This will delete the following:"
echo "  - $EXERCISE_DIR/ directory and all contents"
echo "  - All .pcap files created during exercises"
echo "  - All README files and scripts"
echo ""
echo "⚠️  WARNING: This action cannot be undone!"
echo "⚠️  Make sure to save any reports or work you want to keep!"
echo ""

read -p "Are you sure you want to continue? (y/n) " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleanup cancelled."
    exit 1
fi

if [ -d "$EXERCISE_DIR" ]; then
    echo "Removing $EXERCISE_DIR/..."
    rm -rf "$EXERCISE_DIR"
    echo "✅ Cleanup complete!"
else
    echo "Directory $EXERCISE_DIR does not exist. Nothing to clean up."
fi

# Also clean up any stray .pcap files in current directory
if ls *.pcap 1> /dev/null 2>&1; then
    echo ""
    read -p "Found .pcap files in current directory. Remove them too? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f *.pcap
        echo "✅ Removed .pcap files from current directory"
    fi
fi

echo ""
echo "You can run setup_tcpdump_exercises.sh again to recreate the exercises."
