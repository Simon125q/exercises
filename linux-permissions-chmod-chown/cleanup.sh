#!/bin/bash

# Cleanup script for Linux Permissions exercises

echo "This will delete the 'exercises/' directory and all its contents."
read -p "Are you sure you want to proceed? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Cleaning up..."
    rm -rf exercises/
    echo "Cleanup complete."
else
    echo "Cleanup cancelled."
fi
