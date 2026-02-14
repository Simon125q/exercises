# Hands-On Exercises: Process Substitution in Bash

**Source Material**: [extremely cool shell trick I did not know about](https://www.youtube.com/watch?v=2A4bs40scSo)
**Generated**: February 10, 2026
**Estimated Total Time**: 60-80 minutes

---

## Introduction

These exercises are designed to provide hands-on practice with **Process Substitution**, a powerful shell feature demonstrated in the source video. By completing these exercises, you will gain a practical understanding of how to use process substitution to write cleaner, more efficient, and more powerful shell commands.

## Setup Instructions

Before starting the exercises, run the setup script to create the necessary files and directories. This script is idempotent, meaning it is safe to run multiple times.

```bash
./setup_exercises.py
```

This will create an `exercises/` directory in your current location with all the required files and sample data for each exercise.

---

## Exercise 1: View Remote Content Without Saving

**Estimated Time**: 5-8 minutes
**Difficulty**: Easy
**Concepts**: Input Process Substitution, `curl`, `/proc` filesystem

### Objective

Use input process substitution to view remote file content directly in a text editor or pager without creating temporary files on your disk.

### Context

As a developer or system administrator, you often need to quickly review a remote configuration file, a log from a server, or documentation from a URL. Downloading these files just to view them once can clutter your filesystem. Process substitution provides a cleaner and more efficient workflow.

### Tasks

1.  Navigate into the `exercises/01_view_remote_content` directory.
2.  Use process substitution with `curl` to open one of the remote text files listed in `urls.txt` directly in your default editor (e.g., `vim`, `nano`) or a pager (e.g., `less`).
3.  While the file is open, open a second terminal and explore the `/proc/self/fd/` directory to see the temporary file descriptor created by the shell.
4.  Experiment by opening multiple remote files simultaneously in the same command.

### Reference

This exercise is based on the first example in the video, which demonstrates `v <(curl [URL])` to open remote content in Vim.

### Validation

You'll know you've succeeded when:

*   You can successfully view the content of a remote URL in your chosen editor or pager.
*   No new files are created in your working directory.
*   You can locate the file descriptor in the `/proc` filesystem that corresponds to the open stream.

### Hints

<details>
<summary>Click to reveal hints</summary>

*   The basic syntax is `<editor> <(curl <URL>)`. For example: `less <(curl https://www.gnu.org/licenses/gpl-3.0.txt)`.
*   Use `curl -s` to run `curl` in silent mode, which hides the progress meter.
*   In a separate terminal, run `ls -l /proc/$(pgrep less)/fd` to inspect the file descriptors of the `less` process.

</details>

---

## Exercise 2: Compare Sorted Files Without Temporary Files

**Estimated Time**: 8-12 minutes
**Difficulty**: Easy
**Concepts**: Input Process Substitution, `diff`, `sort`, `comm`

### Objective

Use process substitution to compare transformed versions of two files without creating intermediate temporary files.

### Context

Imagine you are a data analyst comparing two lists of user IDs from different systems. The lists are not in the same order, and you need to find out which users are unique to each list. Creating sorted copies of each file is inefficient, especially for large files.

### Tasks

1.  Navigate into the `exercises/02_compare_sorted_files` directory.
2.  Use the `diff` command with process substitution to compare the sorted versions of `system1_users.txt` and `system2_users.txt`.
3.  Identify which users exist in `system1_users.txt` but not in `system2_users.txt`.
4.  Use the `comm` command with process substitution for a more direct way to find users unique to each file.

### Reference

This exercise builds on the video example `diff <(sort file1) <(sort file2)`, which shows how to compare two sorted files on the fly.

### Validation

You'll know you've succeeded when:

*   You can correctly identify all users that are unique to each of the two lists.
*   No temporary sorted files are created in your working directory.
*   You can explain the difference in output between `diff` and `comm` for this task.

### Hints

<details>
<summary>Click to reveal hints</summary>

*   The `diff` syntax is `diff -u <(sort system1_users.txt) <(sort system2_users.txt)`. The `-u` flag provides a unified, easier-to-read output.
*   The `comm` command is designed for comparing sorted files. `comm -23 <(sort file1) <(sort file2)` will show lines unique to `file1`.
*   Remember that both `diff` and `comm` rely on the input being sorted.

</details>

---

## Exercise 3: Preview Text Transformations Before Applying

**Estimated Time**: 10-15 minutes
**Difficulty**: Medium
**Concepts**: Input Process Substitution, `sed`, `diff`

### Objective

Use process substitution to safely preview the effects of text transformations with `sed` before modifying the original file.

### Context

As a DevOps engineer, you need to update a service's configuration file. Making a mistake in a configuration file can cause service outages. Before applying any changes, you want to see exactly what the `sed` command will do.

### Tasks

1.  Navigate into the `exercises/03_preview_transformations` directory.
2.  Use `diff` with process substitution to preview the following `sed` transformations on the `app_config.conf` file:
    *   Change all occurrences of `development` to `production`.
    *   Change the server `port` from `8080` to `9090`.
    *   Comment out all lines containing the word `debug`.
3.  Review the `diff` output to ensure the changes are correct and have no unintended side effects.
4.  Once you are confident in a change, apply it to the file permanently. Remember to create a backup first!

### Reference

This exercise is based on the video example `diff file1 <(sed s/rabbit/groundhog/I file1)`, which demonstrates how to preview changes from a `sed` command.

### Validation

You'll know you've succeeded when:

*   You can successfully generate a `diff` that shows the proposed changes without modifying the original file.
*   You can apply the changes to the file to create a new, updated configuration.
*   The final configuration file is valid and reflects the intended changes.

### Hints

<details>
<summary>Click to reveal hints</summary>

*   The `diff` syntax is `diff -u app_config.conf <(sed 's/old/new/g' app_config.conf)`.
*   To comment out lines containing a pattern, use a `sed` command like `sed '/debug/s/^/#/'`.
*   To apply changes in place, use the `-i` flag with `sed`: `sed -i.bak 's/old/new/g' app_config.conf`. This also creates a backup file with the `.bak` extension.

</details>

---

## Exercise 4: Dual Output Logging

**Estimated Time**: 15-20 minutes
**Difficulty**: Medium
**Concepts**: Output Process Substitution, `tee`, I/O Redirection

### Objective

Use output process substitution to send a command's standard output (`stdout`) and standard error (`stderr`) to different destinations simultaneously.

### Context

You are running a long-running data processing script. You want to watch the normal progress output in real-time, but you also want to capture any error messages to a separate log file for later analysis. This is a common requirement for monitoring production systems.

### Tasks

1.  Navigate into the `exercises/04_dual_output_logging` directory.
2.  Run the `generate_output.sh` script and observe its mixed output.
3.  Execute the script again, but this time use process substitution to redirect its `stdout` to `less` for interactive viewing, while simultaneously redirecting its `stderr` to `tee` to both display it on the screen and log it to a file named `errors.txt`.
4.  Verify that the `errors.txt` file contains only the error and warning messages.

### Reference

This exercise is based on the video example `example > >(less) 2> >(tee errors.txt)`, which shows how to split `stdout` and `stderr` to different processes.

### Validation

You'll know you've succeeded when:

*   You can view the standard output of the script in `less`.
*   The error messages are displayed on your terminal and also saved to `errors.txt`.
*   No output from the script is lost.

### Hints

<details>
<summary>Click to reveal hints</summary>

*   The syntax is `./generate_output.sh > >(less) 2> >(tee errors.txt)`.
*   Remember that `tee` writes to both the screen and a file.
*   You can also redirect `stdout` and `stderr` to two separate files using a similar technique: `... > >(tee stdout.log) 2> >(tee stderr.log)`.

</details>

---

## Exercise 5: Parallel Data Distribution

**Estimated Time**: 20-25 minutes
**Difficulty**: Hard
**Concepts**: Output Process Substitution, `tar`, `tee`, Pipelines

### Objective

Use process substitution with `tee` and `tar` to send a data stream to multiple destinations simultaneously, simulating a parallel deployment.

### Context

As a site reliability engineer, you need to deploy a new version of an application to multiple servers at once. Creating a tarball, copying it to each server, and then extracting it is slow and sequential. A more efficient method is to create the tarball on the fly and stream it to all servers in parallel.

### Tasks

1.  Navigate into the `exercises/05_parallel_distribution` directory.
2.  Create three destination directories: `dest1`, `dest2`, and `dest3`.
3.  Construct a single command that archives the `sample_data/` directory and, using a pipeline with `tee` and process substitution, extracts that archive into all three destination directories simultaneously.
4.  Verify that all three destination directories contain an identical copy of the `sample_data/` directory.
5.  (Bonus) Modify the command to compress the archive with `gzip` on the fly during distribution.

### Reference

This exercise is an advanced application of the final example in the video: `tar cf - directory | tee >(ssh server1 tar xf -) >(ssh server2 tar xf -) > /dev/null`. We simulate the `ssh` commands by writing to local directories.

### Validation

You'll know you've succeeded when:

*   All three destination directories are successfully created and populated.
*   The contents of `dest1`, `dest2`, and `dest3` are identical to the `sample_data` directory.
*   No intermediate tarball file is saved to disk.

### Hints

<details>
<summary>Click to reveal hints</summary>

*   The core of the command is `tar cf - sample_data | tee >(...) >(...) | ...`.
*   Each process substitution will contain a `tar xf - -C <destination>` command to extract the stream into a different directory.
*   The final command in the pipeline will handle the last copy. For example: `... | tar xf - -C dest3`.
*   The full command might look like: `tar cf - sample_data | tee >(tar xf - -C dest1) >(tar xf - -C dest2) | tar xf - -C dest3`.
*   To verify, use `diff -r dest1 dest2` and `diff -r dest2 dest3`. There should be no output.
*   For the bonus, use the `z` flag in your `tar` commands (e.g., `tar czf - ...` and `tar xzf - ...`).

</details>

---

## Cleanup

After completing all exercises, you can run the cleanup script to remove all the files and directories created by the setup script.

```bash
./cleanup_exercises.sh
```

**Warning**: This will permanently delete the `exercises/` directory and all its contents. Make sure to save any work you want to keep before running this script.
