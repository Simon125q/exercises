#!/bin/bash

# Cleanup script for "Logi systemowe Linux, które MUSISZ znać!" exercises
# Generated: 2026-02-15

EXERCISE_DIR="exercises"

echo "Cleanup script for: Logi systemowe Linux, które MUSISZ znać!"
echo "================================================"
echo ""
echo "This will delete the following:"
echo "  - $EXERCISE_DIR/ directory and all contents"
echo ""
echo "⚠️  WARNING: This action cannot be undone!"
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

echo ""
echo "You can run setup_exercises.sh again to recreate the exercises."
