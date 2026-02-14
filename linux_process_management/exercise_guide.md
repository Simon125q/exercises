# Advanced Linux Process Management Exercises

**Source Material**: [Serwer NIE ODPOWIADA? Znajdź proces który go zabija!](https://www.youtube.com/watch?v=06NxvuTamGU)
**Date**: February 14, 2026
**Total Estimated Time**: 55 minutes

## Overview
These exercises are designed for users who are already familiar with basic Linux commands and want to master advanced process management techniques. You will learn how to efficiently identify resource-heavy processes, use interactive monitoring tools, and execute emergency recovery commands.

---

## Exercise 1: Advanced ps Sorting
- **Estimated time**: 10 minutes
- **Objective**: Identify the top memory-consuming processes using `ps` with advanced sorting flags.
- **Context**: A server is sluggish, and you suspect a memory leak. You need to find the top 5 processes consuming the most resident set size (RSS) memory.
- **Tasks**:
    1. Use `ps aux` with the `--sort` flag to sort processes by memory usage (RSS) in descending order.
    2. Limit the output to the top 5 processes (excluding the header).
    3. Display only the PID, %MEM, RSS, and COMMAND columns.
- **Validation**: Your output should show 5 processes sorted by RSS memory usage.

---

## Exercise 2: Interactive Monitoring and Management
- **Estimated time**: 15 minutes
- **Objective**: Use `top` or `htop` to identify and manage a resource-heavy process.
- **Context**: A background job is consuming significant CPU. You need to monitor it in real-time and be prepared to terminate it if it exceeds thresholds.
- **Tasks**:
    1. Launch `top`.
    2. Use interactive keys to:
        - Sort by CPU usage.
        - Sort by Memory usage.
        - Toggle the display of the command line (full path).
    3. Identify a process (e.g., a sleep command) and use the 'k' key within `top` to send a SIGTERM.
- **Setup**: Run `sleep 1000 &` in another terminal to have a process to target.

---

## Exercise 3: The Emergency Kill One-Liner
- **Estimated time**: 20 minutes
- **Objective**: Construct and execute a command chain to automatically kill the most CPU-intensive process.
- **Context**: The system is nearly unresponsive. You need a single command that finds the top CPU consumer and kills it immediately with SIGKILL (-9).
- **Tasks**:
    1. Start the provided `./rogue_process.sh &` in the exercise directory.
    2. Construct a one-liner using `ps`, `awk`, and command substitution `$(...)` to:
        - Sort by %CPU descending.
        - Get the PID of the top process (excluding headers).
        - Pass that PID to `kill -9`.
    3. Verify the rogue process is gone.
- **Reference**: This builds on the "Emergency Kill" technique shown at the end of the video.

---

## Exercise 4: Signal Mastery (SIGTERM vs SIGKILL)
- **Estimated time**: 10 minutes
- **Objective**: Understand the difference between graceful shutdown and forceful termination.
- **Context**: Some processes handle SIGTERM to clean up resources, while others might hang and require SIGKILL.
- **Tasks**:
    1. Start two sleep processes: `sleep 2000 &` and `sleep 2001 &`.
    2. Use `kill` (default SIGTERM) on the first one.
    3. Use `kill -9` (SIGKILL) on the second one.
    4. Use `jobs` or `ps` to verify both are terminated.
    5. Research: What is the difference between signal 15 and signal 9?

---

## Cleanup
To remove all exercise files, run the `cleanup.sh` script or manually delete the `exercises/` directory.
