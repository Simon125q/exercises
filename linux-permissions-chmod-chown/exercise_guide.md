# Linux Permissions: chmod and chown Guide

Practical hands-on exercises based on the tutorial: [Uprawnienia Linux które MUSISZ znać - przewodnik chmod i chown](https://www.youtube.com/watch?v=pRTbfgGgZNY)

**Date**: February 15, 2026
**Total Estimated Time**: 50 minutes

---

## Exercise 1: Interpret and Fix Script Permissions (Apply)
- **Estimated Time**: 5 minutes
- **Objective**: Use the numeric method of `chmod` to make a script executable.
- **Context**: You've just created a backup script `backup.sh` in the `01_script_permissions` directory. However, when you try to run it, you get a "Permission denied" error.
- **Tasks**:
    1. Navigate to `exercises/01_script_permissions`.
    2. Use `ls -l` to check the current permissions of `backup.sh`.
    3. Use the **numeric method** of `chmod` to set the permissions to `755` (rwxr-xr-x).
    4. Verify that you can now execute the script using `./backup.sh`.
- **Reference**: Video section on `ls -la` and `chmod` numeric method (4=r, 2=w, 1=x).
- **Validation**: Running `./backup.sh` should print "Backup completed successfully!".

---

## Exercise 2: Secure Sensitive Configuration (Adapt)
- **Estimated Time**: 10 minutes
- **Objective**: Use the symbolic method of `chmod` to restrict access to sensitive files.
- **Context**: In `exercises/02_secure_config`, there is a file named `database.conf` containing sensitive credentials. Currently, it's readable by everyone on the system.
- **Tasks**:
    1. Navigate to `exercises/02_secure_config`.
    2. Use the **symbolic method** of `chmod` to remove all permissions for `group` (g) and `others` (o).
    3. Ensure the `owner` (u) still has `read` and `write` permissions.
    4. Verify the change with `ls -l`.
- **Reference**: Video section on `chmod` symbolic method (u, g, o, a and +, -, =).
- **Validation**: `ls -l database.conf` should show `-rw-------`.

---

## Exercise 3: Ownership and Permission Handover (Extend)
- **Estimated Time**: 15 minutes
- **Objective**: Change file ownership and adjust permissions for the new owner.
- **Context**: A system administrator created a report `system_report.log` in `exercises/03_ownership_handover` as `root`. You need to take ownership of this file and ensure you can edit it, while preventing others from even reading it.
- **Tasks**:
    1. Navigate to `exercises/03_ownership_handover`.
    2. Use `ls -l` to see that the file is owned by `root`.
    3. Use `sudo chown` to change the owner to your current user (use `whoami` to find your username).
    4. Use `chmod` to set permissions so only you (the owner) can read and write the file.
- **Reference**: Video section on `chown` and combining it with `chmod`.
- **Validation**: `ls -l system_report.log` should show your username as the owner and permissions as `-rw-------`.

---

## Exercise 4: The "Rescue" Operation (Real-World)
- **Estimated Time**: 20 minutes
- **Objective**: Use a recursive command to fix permissions across an entire project structure.
- **Context**: You've inherited a project directory `exercises/04_rescue_project` where permissions are a mess: some text files are executable, and some directories are missing the execute bit (preventing you from entering them).
- **Tasks**:
    1. Navigate to `exercises/04_rescue_project`.
    2. Use the "rescue command" pattern from the video using `find`:
        - Set all **files** to `644` (rw-r--r--).
        - Set all **directories** to `755` (rwxr-xr-x).
    3. Verify that you can now enter the `src` directory and that `main.c` is not executable.
- **Reference**: Video section on the "Rescue Command" using `find -type f` and `find -type d`.
- **Validation**: 
    - `ls -ld src` should show `drwxr-xr-x`.
    - `ls -l src/main.c` should show `-rw-r--r--`.

---

## Cleanup
To remove the exercise environment, run the provided `cleanup.sh` script or manually delete the `exercises/` directory.
