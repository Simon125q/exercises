#!/bin/bash

# Cleanup script for "Automatyzacja zadań w Linuxie" exercises
# Generated: 2026-02-15

EXERCISE_DIR="exercises"

echo "Cleanup script for: Automatyzacja zadań w Linuxie"
echo "================================================"
echo ""
echo "This will delete the following:"
echo "  - $EXERCISE_DIR/ directory and all contents"
echo "  - Any crontab entries created during exercises"
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
    echo "✅ Directory removed!"
else
    echo "Directory $EXERCISE_DIR does not exist."
fi

# Optional: Clear crontab
read -p "Do you want to clear your crontab as well? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    crontab -r 2>/dev/null || echo "Crontab already empty."
    echo "✅ Crontab cleared!"
fi

echo ""
echo "Cleanup complete!"
