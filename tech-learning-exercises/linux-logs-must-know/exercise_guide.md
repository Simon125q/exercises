# Logi systemowe Linux, które MUSISZ znać! - Hands-On Exercises

**Source Material**: [https://www.youtube.com/watch?v=IIk-Be3h1eU](https://www.youtube.com/watch?v=IIk-Be3h1eU)
**Generated**: 2026-02-15
**Estimated Total Time**: 60 minutes

---

## Setup Instructions

Before starting the exercises, run the setup script to create the necessary files and directories:

```bash
bash setup_exercises.sh
```

This will create an `exercises/` directory with all required files and sample data.

---

## Exercise 1: Basic Journal Inspection

**Estimated Time**: 10 minutes  
**Difficulty**: Easy  
**Concepts**: `journalctl`, basic filtering

### Objective

Learn how to navigate the systemd journal and find specific messages from a recent time frame.

### Context

You've been told that a service had issues earlier today. You need to quickly find all log entries from the last hour to see if anything stands out.

### Tasks

1. List all journal entries from the last 60 minutes.
2. Filter the output to show only entries with a priority of "err" (error) or higher.
3. Find the specific error message related to the "mock-auth" service.

### Reference

This exercise builds on the section where the narrator explains how to use `journalctl` with time filters and priority levels.

### Validation

You'll know you've succeeded when:
- You can see a list of errors from the last hour.
- You identify the "mock-auth" service error: "Invalid configuration: missing secret key".

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use `journalctl --since "1 hour ago"`
- Use the `-p` flag for priority (e.g., `-p err`)
- You can combine flags: `journalctl --since "1 hour ago" -p err`

</details>

---

## Exercise 2: Troubleshooting a Failing Service

**Estimated Time**: 20 minutes  
**Difficulty**: Medium  
**Concepts**: `systemctl status`, `journalctl -u`, service debugging

### Objective

Diagnose and fix a service that fails to start by analyzing its specific logs.

### Context

The `web-portal` service is failing to start. Your task is to find out why, fix the configuration, and successfully start the service.

### Tasks

1. Check the status of the `web-portal` service using `systemctl`.
2. Use `journalctl` to view only the logs for the `web-portal` unit.
3. Identify the error in the configuration file located at `/etc/web-portal/config.conf` (simulated in `exercises/02_service_debug/etc/config.conf`).
4. Fix the error (a typo in the port number) and "restart" the service (verify the fix).

### Reference

This exercise builds on the practical scenario in the video where the narrator diagnoses a failing Nginx service.

### Validation

You'll know you've succeeded when:
- You find the error: "Invalid port: 8080a".
- You correct the port to "8080" in the config file.
- The logs no longer show the port error when you "check" again.

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use `systemctl status web-portal` (Note: in this sandbox, we use simulated files).
- Use `journalctl -u web-portal` to see service-specific logs.
- Look for "syntax error" or "invalid value" in the log output.

</details>

---

## Exercise 3: Kernel and Hardware Diagnostics

**Estimated Time**: 15 minutes  
**Difficulty**: Medium  
**Concepts**: `dmesg`, `/var/log/syslog`, hardware logs

### Objective

Distinguish between system logs and kernel logs to identify hardware-related issues.

### Context

A user reports that their external drive is behaving strangely. You need to check the kernel ring buffer to see if there are any I/O errors or hardware resets.

### Tasks

1. Use `dmesg` to view the latest kernel messages.
2. Filter `dmesg` output to find any mentions of "usb" or "sda".
3. Check the traditional `/var/log/syslog` (simulated) to see if the kernel messages are also being recorded there.

### Reference

This exercise builds on the section where the narrator explains `dmesg` and the difference between `/var/log` and the journal.

### Validation

You'll know you've succeeded when:
- You find the kernel message: "usb 1-1: device descriptor read/64, error -110".
- You can locate the same timestamped entry in the simulated `syslog` file.

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use `dmesg | grep -i usb`
- The simulated syslog is at `exercises/03_hardware_logs/var/log/syslog`.

</details>

---

## Exercise 4: The "24-Hour Error" Challenge

**Estimated Time**: 15 minutes  
**Difficulty**: Hard  
**Concepts**: Advanced `journalctl`, piping, log analysis

### Objective

Create a summary of all system errors from the last 24 hours to present in a daily stand-up meeting.

### Tasks

1. Run a single command to find all errors from the last 24 hours.
2. Count how many unique services reported errors.
3. Identify the most frequent error message.

### Reference

This exercise builds on the "powerful one-liner" demonstrated at the end of the video.

### Validation

You'll know you've succeeded when:
- You have a count of unique services (should be 3 in the provided data).
- You identify "Connection refused" as the most frequent error.

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use `journalctl --since "24 hours ago" -p err`
- Pipe to `awk` or `cut` to extract the service name, then `sort | uniq -c`.

</details>

---

## Cleanup

After completing all exercises, you can clean up the created files:

```bash
bash cleanup_exercises.sh
```

**Warning**: This will delete all files in the `exercises/` directory. Make sure to save any work you want to keep!

---

## Notes

- All exercises are independent and can be completed in any order.
- Refer back to the source material if you get stuck.
- Try to solve exercises without looking at hints first.
- The goal is to understand *when* and *why* to use these techniques, not just *how*.
