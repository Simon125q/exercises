#!/bin/bash

echo "This will remove the 'exercises/' directory and all its contents."
read -p "Are you sure? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    rm -rf exercises/
    echo "Cleanup complete."
else
    echo "Cleanup cancelled."
fi
