# Exercise 3: The Emergency Kill One-Liner

## Estimated time: 20 minutes

## Objective
Construct and execute a command chain to automatically kill the most CPU-intensive process.

## Context
The system is nearly unresponsive. You need a single command that finds the top CPU consumer and kills it immediately with SIGKILL (-9).

## Tasks
1. Start the provided `./rogue_process.sh &` (Note: This will spike CPU usage in this sandbox).
2. Construct a one-liner using `ps`, `awk`, and command substitution `$(...)` to:
   - Sort by %CPU descending.
   - Get the PID of the top process (excluding headers).
   - Pass that PID to `kill -9`.
3. Verify the rogue process is gone.

## Reference
This builds on the "Emergency Kill" technique shown at the end of the video.
