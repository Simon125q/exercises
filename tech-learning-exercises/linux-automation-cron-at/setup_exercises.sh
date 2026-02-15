#!/bin/bash

# Setup script for "Automatyzacja zadań w Linuxie" exercises
# Generated: 2026-02-15

set -e  # Exit on error

EXERCISE_DIR="exercises"

echo "Setting up exercises for: Automatyzacja zadań w Linuxie"
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

# --- Exercise 1: Cron Basics ---
mkdir -p "$EXERCISE_DIR/01_cron_basics"
cat > "$EXERCISE_DIR/01_cron_basics/backup.sh" << 'EOF'
#!/bin/bash
# Simple backup script
BACKUP_DIR="/home/ubuntu/backups"
mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/backup_$(date +%Y%m%d).tar.gz" /home/ubuntu/exercises/01_cron_basics/data
echo "Backup completed at $(date)"
EOF
chmod +x "$EXERCISE_DIR/01_cron_basics/backup.sh"
mkdir -p "$EXERCISE_DIR/01_cron_basics/data"
touch "$EXERCISE_DIR/01_cron_basics/data/file1.txt" "$EXERCISE_DIR/01_cron_basics/data/file2.txt"

# --- Exercise 2: At Basics ---
mkdir -p "$EXERCISE_DIR/02_at_basics"
cat > "$EXERCISE_DIR/02_at_basics/update.sh" << 'EOF'
#!/bin/bash
echo "System update simulation started at $(date)"
sleep 2
echo "System update completed."
EOF
chmod +x "$EXERCISE_DIR/02_at_basics/update.sh"

# --- Exercise 3: Debugging Cron ---
# We simulate a log file for this exercise
mkdir -p "$EXERCISE_DIR/03_cron_debug"
cat > "$EXERCISE_DIR/03_cron_debug/mock_journal.txt" << EOF
Feb 15 10:00:01 sandbox cron[1234]: (ubuntu) RELOAD (crontab)
Feb 15 10:05:01 sandbox cron[1234]: (ubuntu) CMD (/usr/local/bin/cleanup.sh)
Feb 15 10:05:01 sandbox cron[1234]: (ubuntu) CAN'T OPEN /etc/cron.d/cleanup: Permission denied
EOF

# --- Exercise 4: Special Strings ---
mkdir -p "$EXERCISE_DIR/04_special_strings"
touch "$EXERCISE_DIR/04_special_strings/startup.sh"
touch "$EXERCISE_DIR/04_special_strings/daily_report.sh"
chmod +x "$EXERCISE_DIR/04_special_strings/startup.sh" "$EXERCISE_DIR/04_special_strings/daily_report.sh"

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
