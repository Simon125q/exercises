# Automatyzacja zadań w Linuxie - Hands-On Exercises

**Source Material**: [https://www.youtube.com/watch?v=sINc-ovYHhg](https://www.youtube.com/watch?v=sINc-ovYHhg)
**Generated**: 2026-02-15
**Estimated Total Time**: 50 minutes

---

## Setup Instructions

Before starting the exercises, run the setup script to create the necessary files and directories:

```bash
bash setup_exercises.sh
```

This will create an `exercises/` directory with all required files and sample scripts.

---

## Exercise 1: Scheduling with Cron

**Estimated Time**: 15 minutes  
**Difficulty**: Easy  
**Concepts**: `crontab`, cron syntax, command paths

### Objective

Learn how to schedule a recurring task using the user's crontab.

### Context

You need to back up a specific directory every day at 3:00 AM. You've written a simple script, but now you need to automate its execution.

### Tasks

1. View your current crontab using `crontab -l`.
2. Edit your crontab using `crontab -e`.
3. Add a job that runs the script `/home/ubuntu/exercises/01_cron_basics/backup.sh` every day at 03:00.
4. **Crucial**: Ensure you use the full path to the script and any commands within the script.

### Reference

This exercise builds on the section where the narrator explains `crontab` syntax and the importance of using full paths.

### Validation

You'll know you've succeeded when:
- `crontab -l` shows the entry: `0 3 * * * /home/ubuntu/exercises/01_cron_basics/backup.sh`.

### Hints

<details>
<summary>Click to reveal hints</summary>

- The cron format is: `minute hour day_of_month month day_of_week command`.
- For 3:00 AM daily, use `0 3 * * *`.

</details>

---

## Exercise 2: One-Time Tasks with `at`

**Estimated Time**: 10 minutes  
**Difficulty**: Easy  
**Concepts**: `at`, `atq`, `atrm`

### Objective

Schedule a task to run once at a specific time in the future.

### Context

You need to run a system update script tonight at 11:00 PM, but you won't be at your computer.

### Tasks

1. Schedule the script `/home/ubuntu/exercises/02_at_basics/update.sh` to run at 23:00 today using the `at` command.
2. List your pending `at` jobs using `atq`.
3. Remove the job you just created using `atrm` (to avoid actually running it in this environment).

### Reference

This exercise builds on the section where the narrator demonstrates the `at` utility for one-time jobs.

### Validation

You'll know you've succeeded when:
- `atq` shows a pending job after step 1.
- `atq` shows no jobs after step 3.

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use `at 23:00` then type the command and press `Ctrl+D` to save.
- Or use: `echo "/home/ubuntu/exercises/02_at_basics/update.sh" | at 23:00`.

</details>

---

## Exercise 3: Debugging Cron Jobs

**Estimated Time**: 15 minutes  
**Difficulty**: Medium  
**Concepts**: `journalctl`, cron logs, troubleshooting

### Objective

Identify why a scheduled cron job is failing by inspecting system logs.

### Context

A cron job was supposed to clean up temporary files, but the files are still there. You need to find the error message in the logs.

### Tasks

1. Check the system logs for cron-related entries using `journalctl`.
2. Filter the logs to find errors from the last hour.
3. Identify the reason for the failure (Hint: look for "Permission denied" or "Command not found").

### Reference

This exercise builds on the section where the narrator explains how to check cron logs using `journalctl`.

### Validation

You'll know you've succeeded when:
- You find the log entry: `cron[1234]: (ubuntu) CAN'T OPEN /etc/cron.d/cleanup: Permission denied`.

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use `journalctl -u cron` or `journalctl | grep cron`.
- Check for entries around the time the job was supposed to run.

</details>

---

## Exercise 4: Advanced Scheduling with Special Strings

**Estimated Time**: 10 minutes  
**Difficulty**: Medium  
**Concepts**: `@reboot`, `@daily`, crontab optimization

### Objective

Use special cron strings to simplify scheduling for common intervals.

### Context

You want a script to run every time the system starts up and another one to run once a day without worrying about the exact hour.

### Tasks

1. Edit your crontab.
2. Add a job to run `/home/ubuntu/exercises/04_special_strings/startup.sh` at every reboot.
3. Add a job to run `/home/ubuntu/exercises/04_special_strings/daily_report.sh` once a day using a special string.

### Reference

This exercise builds on the section where the narrator introduces special strings like `@reboot` and `@daily`.

### Validation

You'll know you've succeeded when:
- `crontab -l` contains `@reboot /home/ubuntu/exercises/04_special_strings/startup.sh`.
- `crontab -l` contains `@daily /home/ubuntu/exercises/04_special_strings/daily_report.sh`.

---

## Cleanup

After completing all exercises, you can clean up the created files:

```bash
bash cleanup_exercises.sh
```

**Warning**: This will delete all files in the `exercises/` directory. Make sure to save any work you want to keep!
