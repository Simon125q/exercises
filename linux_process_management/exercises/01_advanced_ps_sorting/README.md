# Exercise 1: Advanced ps Sorting

## Estimated time: 10 minutes

## Objective
Identify the top memory-consuming processes using `ps` with advanced sorting flags.

## Context
A server is sluggish, and you suspect a memory leak. You need to find the top 5 processes consuming the most resident set size (RSS) memory.

## Tasks
1. Use `ps aux` with the `--sort` flag to sort processes by memory usage (RSS) in descending order.
2. Limit the output to the top 5 processes (excluding the header).
3. Display only the PID, %MEM, RSS, and COMMAND columns.

## Validation
Your output should show 5 processes sorted by RSS memory usage.
