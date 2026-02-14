# Exercise 4: Signal Mastery (SIGTERM vs SIGKILL)

## Estimated time: 10 minutes

## Objective
Understand the difference between graceful shutdown and forceful termination.

## Context
Some processes handle SIGTERM to clean up resources, while others might hang and require SIGKILL.

## Tasks
1. Start two sleep processes: `sleep 2000 &` and `sleep 2001 &`.
2. Use `kill` (default SIGTERM) on the first one.
3. Use `kill -9` (SIGKILL) on the second one.
4. Use `jobs` or `ps` to verify both are terminated.
5. Research: What is the difference between signal 15 and signal 9?
