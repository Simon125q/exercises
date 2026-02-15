#!/bin/bash

# Cleanup script for Linux Disk Management exercises

echo "This will delete the 'exercises/' directory and all its contents."
read -p "Are you sure you want to proceed? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Cleaning up..."
    # Ensure nothing is mounted before deleting
    if mount | grep -q "exercises/"; then
        echo "Detected mounted directories. Attempting to unmount..."
        mount | grep "exercises/" | awk '{print $3}' | xargs sudo umount
    fi
    rm -rf exercises/
    echo "Cleanup complete."
else
    echo "Cleanup cancelled."
fi
