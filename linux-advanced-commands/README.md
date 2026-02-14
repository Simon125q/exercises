# Advanced Linux File Management Exercises

Based on the video: [Przestań się męczyć z plikami w Linux! (6 komend które ratuje życie)](https://www.youtube.com/watch?v=NhDZC3X4gtY)
Date: February 14, 2026
Total Estimated Time: 60-75 minutes

## Overview
These exercises focus on advanced usage of core Linux commands (`ls`, `mkdir`, `cp`, `rm`, `find`) for efficient file management. As an intermediate user, you will focus on powerful flags and real-world scenarios rather than basic syntax.

---

## Exercise 1: Deep Inspection and Sorting (Apply)
**Estimated Time**: 10 minutes
**Objective**: Use advanced `ls` flags to identify specific files in a cluttered directory.
**Context**: You've inherited a legacy log directory and need to find the largest files and the most recently modified ones to troubleshoot a disk space issue.

### Tasks:
1. Navigate to `exercises/01_inspection/data`.
2. List all files (including hidden ones) with human-readable sizes.
3. Sort the files by size (largest first) to identify potential space hogs.
4. Sort the files by modification time (newest first) to see recent activity.
5. **Challenge**: Combine flags to show detailed information, human-readable sizes, and sort by time in a single command.

**Validation**: You should see `.hidden_config` and identify `huge_log.log` as the largest file.

---

## Exercise 2: Structured Deployment (Adapt)
**Estimated Time**: 15 minutes
**Objective**: Use `mkdir -p` and `cp -p` to replicate a production environment structure while preserving metadata.
**Context**: You need to prepare a backup structure for a multi-service application. It's critical that file permissions and timestamps are preserved for audit purposes.

### Tasks:
1. Create a nested directory structure `backups/nginx/config`, `backups/nginx/logs`, and `backups/db/data` using a **single command**.
2. Copy the configuration files from `exercises/02_deployment/src` to their respective backup folders.
3. Ensure that the copied files retain their original timestamps and permissions (use the `-p` flag).
4. Verify that the timestamps in the `backups` directory match the originals in `src`.

**Validation**: Running `ls -l` on both source and backup should show identical timestamps and permissions.

---

## Exercise 3: Precision Cleanup (Extend)
**Estimated Time**: 15 minutes
**Objective**: Safely remove specific directory structures using `rm` with interactive and recursive flags.
**Context**: You are cleaning up old build artifacts. To avoid accidental deletion of critical files, you must use interactive mode for sensitive areas.

### Tasks:
1. Navigate to `exercises/03_cleanup`.
2. Delete the `temp_builds` directory and all its contents recursively.
3. In the `protected_configs` directory, delete files but use the `-i` flag to confirm each deletion.
4. **Challenge**: Try to delete a non-empty directory without `-r` and observe the error, then fix it.

**Validation**: The `temp_builds` directory should be gone, and you should have selectively deleted files in `protected_configs`.

---

## Exercise 4: Advanced Search and Action (Extend)
**Estimated Time**: 25 minutes
**Objective**: Master the `find` command to locate files based on complex criteria.
**Context**: A security audit requires you to find all scripts modified in the last 24 hours that are larger than a certain size, and identify files belonging to a specific naming pattern.

### Tasks:
1. Find all files in `exercises/04_search` that have ".sh" extension.
2. Find all files larger than 100KB.
3. Find files that were modified less than 1 day ago (`-mtime`).
4. **Challenge**: Combine these! Find files that are *both* larger than 10KB *and* were modified in the last 24 hours.
5. **Pro Tip**: Use `-type f` to ensure you are only looking for files, not directories.

**Validation**: You should find `recent_script.sh` and `large_data.bin` based on your search criteria.

---

## Getting Started
1. Run the setup script: `python3 setup_exercises.py`
2. Follow the tasks in each exercise directory's README.
3. When finished, you can run `bash cleanup.sh` to remove the exercise files.
