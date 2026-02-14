# Exercise 2: Interactive Monitoring and Management

## Estimated time: 15 minutes

## Objective
Use `top` or `htop` to identify and manage a resource-heavy process.

## Context
A background job is consuming significant CPU. You need to monitor it in real-time and be prepared to terminate it if it exceeds thresholds.

## Tasks
1. Launch `top`.
2. Use interactive keys to:
   - Sort by CPU usage.
   - Sort by Memory usage.
   - Toggle the display of the command line (full path).
3. Identify a process (e.g., a sleep command we will start) and use the 'k' key within `top` to send a SIGTERM.

## Setup for this exercise
Run `sleep 1000 &` in another terminal to have a process to target.
