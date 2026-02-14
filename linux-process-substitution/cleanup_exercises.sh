#!/bin/bash

# Cleanup script for Process Substitution exercises
# Based on: "extremely cool shell trick I did not know about"
# Source: https://www.youtube.com/watch?v=2A4bs40scSo
# Generated: February 10, 2026

EXERCISE_DIR="exercises"

echo "Cleanup script for: Process Substitution Exercises"
echo "================================================"
echo ""
echo "This will delete the following:"
echo "  - $EXERCISE_DIR/ directory and all contents"
echo ""
echo "⚠️  WARNING: This action cannot be undone!"
echo "⚠️  Make sure to backup any work you want to keep!"
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
    echo ""
    echo "All exercise files have been removed."
else
    echo "Directory $EXERCISE_DIR does not exist. Nothing to clean up."
fi

echo ""
echo "You can run ./setup_exercises.py again to recreate the exercises."
