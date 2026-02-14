#!/bin/bash
# Cleanup script for Linux Networking Fundamentals exercises

EXERCISE_DIR="exercises"

if [ -d "$EXERCISE_DIR" ]; then
    read -p "Are you sure you want to delete the '$EXERCISE_DIR' directory and all its contents? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$EXERCISE_DIR"
        echo "✅ Exercises directory removed."
    else
        echo "Cleanup cancelled."
    fi
else
    echo "No exercises directory found to clean up."
fi
