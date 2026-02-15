# Linux Disk Management Guide

Practical hands-on exercises based on the tutorial: [Zarządzanie dyskami w Linux, które MUSISZ znać!](https://www.youtube.com/watch?v=P7pbrEDKP8M)

**Date**: February 15, 2026
**Total Estimated Time**: 45 minutes

---

## Exercise 1: Analyze Disk and Directory Usage (Apply)
- **Estimated Time**: 10 minutes
- **Objective**: Use `df` and `du` to identify space-consuming files and partitions.
- **Context**: You received a "No space left on device" alert. You need to find out which partition is full and which specific directory is the culprit.
- **Tasks**:
    1. Use `df -h` to check the available space on all mounted filesystems.
    2. Navigate to `exercises/01_disk_usage`.
    3. Use `du -sh *` to see the size of each item in the current directory.
    4. Identify the largest directory and drill down to find the large file inside.
- **Reference**: Video section on `df` (disk free) and `du` (disk usage).
- **Validation**: You should find a file named `large_data.bin` that is consuming significant space.

---

## Exercise 2: Identify Block Devices (Apply)
- **Estimated Time**: 5 minutes
- **Objective**: Use `lsblk` and `blkid` to gather information about system storage.
- **Context**: You've plugged in a new disk and need to find its device name and UUID before you can mount it.
- **Tasks**:
    1. Use `lsblk` to list all block devices and their mount points.
    2. Use `blkid` to see the UUIDs and filesystem types of the partitions.
- **Reference**: Video section on `lsblk` and `blkid`.
- **Validation**: Identify the device name for the root partition (usually `/`).

---

## Exercise 3: Temporary Mounting (Adapt)
- **Estimated Time**: 10 minutes
- **Objective**: Manually mount and unmount a simulated disk image.
- **Context**: You have a disk image `data_disk.img` in `exercises/03_mounting` that contains important files. You need to mount it to access the data.
- **Tasks**:
    1. Navigate to `exercises/03_mounting`.
    2. Create a mount point directory: `mkdir mnt`.
    3. Use `sudo mount data_disk.img mnt` to mount the image.
    4. Verify the content inside `mnt`.
    5. Unmount the image using `sudo umount mnt`.
- **Reference**: Video section on `mount` and `umount`.
- **Validation**: `ls mnt` should show a file named `secret_plans.txt` while mounted, and the directory should be empty after unmounting.

---

## Exercise 4: Permanent Mount Configuration (Extend)
- **Estimated Time**: 20 minutes
- **Objective**: Understand how to configure `/etc/fstab` for permanent mounting.
- **Context**: You want the disk image from the previous exercise to be mounted automatically at boot.
- **Tasks**:
    1. Get the absolute path of `data_disk.img` and the mount point `mnt`.
    2. View the contents of `/etc/fstab` to understand its structure (do not modify the real system file).
    3. Create a mock fstab entry in a file named `mock_fstab` that would mount this image.
    4. Use the `mount -a` concept (theoretical) to explain how you would test the entry.
- **Reference**: Video section on `/etc/fstab`.
- **Validation**: Your `mock_fstab` should follow the format: `<device> <mount_point> <type> <options> <dump> <pass>`.

---

## Cleanup
To remove the exercise environment, run the provided `cleanup.sh` script or manually delete the `exercises/` directory.
