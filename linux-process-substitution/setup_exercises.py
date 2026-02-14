#!/usr/bin/env python3
"""
Setup script for Process Substitution exercises
Based on: "extremely cool shell trick I did not know about"
Source: https://www.youtube.com/watch?v=2A4bs40scSo
Generated: February 10, 2026
"""

import os
import sys
import random
import shutil
from pathlib import Path
from datetime import datetime, timedelta


EXERCISE_DIR = Path("exercises")


def create_directory_structure():
    """Create the main directory structure for exercises."""
    print(f"Creating exercise directory: {EXERCISE_DIR}")
    
    if EXERCISE_DIR.exists():
        response = input(f"Warning: {EXERCISE_DIR} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            sys.exit(1)
        shutil.rmtree(EXERCISE_DIR)
    
    EXERCISE_DIR.mkdir()


def setup_exercise_01():
    """Setup files for Exercise 1: View Remote Content Without Saving."""
    ex_dir = EXERCISE_DIR / "01_view_remote_content"
    ex_dir.mkdir()
    
    # Create README
    readme = """# Exercise 1: View Remote Content Without Saving

**Estimated time**: 5-8 minutes

## Objective
Use input process substitution to view remote file content directly in an editor without creating temporary files.

## Context
You need to quickly review remote configuration files or documentation without cluttering your filesystem with temporary downloads. This is especially useful when inspecting files on remote servers or reviewing documentation.

## Tasks
1. Use process substitution with `curl` to open a remote text file directly in your default editor (vim, nano, less, etc.)
2. While the file is open, explore the `/proc/self/fd/` directory to see the temporary file descriptor created by the shell
3. Try opening multiple remote files simultaneously and observe how the shell manages file descriptors
4. Compare this approach to the traditional download-then-open workflow in terms of steps and disk usage

## Reference
This builds on the video example: `v <(curl [URL])`

## Sample URLs
Use the URLs provided in `urls.txt` for this exercise. These point to various README files and configuration samples.

## Validation
- You successfully view remote content in your editor without creating any files in your current directory
- You understand how the shell creates temporary file descriptors in `/proc/self/fd/`
- You can explain when this technique is more efficient than downloading files

## Hints
- The syntax is: `<editor> <(curl <URL>)`
- Try `ls -l /proc/self/fd/` in another terminal while the file is open
- Use `curl -s` for silent mode (no progress bar)
"""
    (ex_dir / "README.md").write_text(readme)
    
    # Create URLs file
    urls = """# Sample URLs for Exercise 1

## GitHub README files (public, no auth required)
https://raw.githubusercontent.com/torvalds/linux/master/README
https://raw.githubusercontent.com/git/git/master/README.md
https://raw.githubusercontent.com/python/cpython/main/README.rst

## Configuration samples
https://raw.githubusercontent.com/nginx/nginx/master/conf/nginx.conf
https://raw.githubusercontent.com/redis/redis/7.0/redis.conf

## Documentation
https://www.gnu.org/licenses/gpl-3.0.txt

## Tips
- Start with smaller files (README files)
- Try the nginx.conf or redis.conf for more complex examples
- Use vim, less, or your preferred pager/editor
"""
    (ex_dir / "urls.txt").write_text(urls)
    
    print(f"  ✓ Created {ex_dir.name}")


def setup_exercise_02():
    """Setup files for Exercise 2: Compare Sorted Files Without Temporary Files."""
    ex_dir = EXERCISE_DIR / "02_compare_sorted_files"
    ex_dir.mkdir()
    
    # Create README
    readme = """# Exercise 2: Compare Sorted Files Without Temporary Files

**Estimated time**: 8-12 minutes

## Objective
Use process substitution to compare transformed versions of files without creating intermediate files.

## Context
You have two user lists from different systems that need to be compared, but they're in different orders. You want to identify differences without creating sorted copies that clutter your filesystem.

## Tasks
1. Use `diff` with process substitution to compare sorted versions of the two user list files
2. Identify which users exist in `system1_users.txt` but not in `system2_users.txt`
3. Identify which users exist in `system2_users.txt` but not in `system1_users.txt`
4. Calculate how much disk space you saved by not creating temporary sorted files
5. Measure the time difference between using process substitution vs creating temporary files

## Reference
This builds on the video example: `diff <(sort file1) <(sort file2)`

## Files
- `system1_users.txt`: User list from System 1 (unsorted)
- `system2_users.txt`: User list from System 2 (unsorted)

## Validation
- You correctly identify all users unique to each system
- No temporary files are created in your working directory
- You understand when process substitution is more efficient than temporary files

## Hints
- Basic syntax: `diff <(sort file1) <(sort file2)`
- Use `diff -u` for unified format (easier to read)
- Use `comm` command for set operations: `comm -23 <(sort file1) <(sort file2)` shows lines only in file1
- To measure disk usage: `du -sh` before and after
"""
    (ex_dir / "README.md").write_text(readme)
    
    # Generate user lists with some overlap
    system1_users = [
        "alice", "bob", "charlie", "david", "eve", "frank", "grace",
        "henry", "iris", "jack", "karen", "leo", "mary", "nathan",
        "olivia", "peter", "quinn", "rachel", "steve", "tina"
    ]
    
    system2_users = [
        "alice", "bob", "charlie", "emily", "frank", "george", "grace",
        "hannah", "iris", "james", "kate", "leo", "mike", "nancy",
        "olivia", "paul", "quinn", "rita", "sam", "tina"
    ]
    
    # Shuffle to make them unsorted
    random.shuffle(system1_users)
    random.shuffle(system2_users)
    
    (ex_dir / "system1_users.txt").write_text("\n".join(system1_users) + "\n")
    (ex_dir / "system2_users.txt").write_text("\n".join(system2_users) + "\n")
    
    print(f"  ✓ Created {ex_dir.name}")


def setup_exercise_03():
    """Setup files for Exercise 3: Preview Text Transformations Before Applying."""
    ex_dir = EXERCISE_DIR / "03_preview_transformations"
    ex_dir.mkdir()
    
    # Create README
    readme = """# Exercise 3: Preview Text Transformations Before Applying

**Estimated time**: 10-15 minutes

## Objective
Use process substitution to preview the effects of sed/awk transformations before modifying the original file.

## Context
You need to perform bulk text replacements in a configuration file but want to verify the changes are correct before applying them permanently. Making mistakes in config files can break applications, so previewing changes is critical.

## Tasks
1. Use `diff` with process substitution to preview sed transformations on `app_config.conf`
2. Test these transformations:
   - Change all occurrences of "development" to "production"
   - Change port 8080 to 9090
   - Comment out all lines containing "debug"
   - Change "localhost" to "prod-server.example.com"
3. Identify any unintended changes that would break the configuration
4. Once satisfied with a transformation, apply it permanently to the file
5. Create a backup before applying permanent changes

## Reference
This builds on the video example: `diff file1 <(sed s/rabbit/groundhog/I file1)`

## Files
- `app_config.conf`: Sample application configuration file

## Validation
- You successfully preview all transformations before applying them
- You identify at least one transformation that would cause unintended changes
- You create backups before making permanent changes
- The final configuration file works correctly (all settings are valid)

## Hints
- Basic syntax: `diff app_config.conf <(sed 's/old/new/g' app_config.conf)`
- Use `diff -u` for unified format (shows context)
- Use `diff --color` for colored output (easier to read)
- To comment out lines: `sed '/pattern/s/^/# /'`
- Always backup: `cp file file.bak` before applying changes
- Apply changes: `sed -i 's/old/new/g' file` (use `-i.bak` to auto-backup)
"""
    (ex_dir / "README.md").write_text(readme)
    
    # Create sample configuration file
    config = """# Application Configuration File
# Environment: development

[server]
host = localhost
port = 8080
environment = development
debug = true
log_level = debug

[database]
host = localhost
port = 5432
database = app_development
user = dev_user
password = dev_password123
debug_queries = true

[cache]
host = localhost
port = 6379
environment = development

[api]
endpoint = http://localhost:8080/api
timeout = 30
debug_mode = true
environment = development

[logging]
level = debug
output = /var/log/app_development.log
debug_sql = true

[features]
enable_debug_toolbar = true
enable_profiling = true
environment = development
"""
    (ex_dir / "app_config.conf").write_text(config)
    
    print(f"  ✓ Created {ex_dir.name}")


def setup_exercise_04():
    """Setup files for Exercise 4: Dual Output Logging."""
    ex_dir = EXERCISE_DIR / "04_dual_output_logging"
    ex_dir.mkdir()
    
    # Create README
    readme = """# Exercise 4: Dual Output Logging

**Estimated time**: 15-20 minutes

## Objective
Use output process substitution to send stdout and stderr to different destinations simultaneously.

## Context
You're running a long-running script and want to view output in real-time while also logging errors to a file for later analysis. This is common in production environments where you need both immediate feedback and persistent error logs.

## Tasks
1. Run the provided `generate_output.sh` script that generates both normal output and errors
2. Use process substitution to send stdout to `less` for real-time viewing
3. Simultaneously send stderr to `tee` to both display and log errors to `errors.txt`
4. Verify that both outputs are captured correctly
5. Modify the approach to log stdout to one file and stderr to another, while still displaying both
6. Test with a real command that generates both stdout and stderr (e.g., a find command)

## Reference
This builds on the video example: `example > >(less) 2> >(tee errors.txt)`

## Files
- `generate_output.sh`: Script that generates mixed stdout/stderr output

## Validation
- Real-time viewing of stdout works correctly
- Error log file contains all error messages
- No output is lost in the process
- You can explain when this technique is useful in production environments

## Hints
- Basic syntax: `command > >(process1) 2> >(process2)`
- For `less`, you may need to use `cat` instead for non-interactive testing
- To log both streams: `command > >(tee stdout.log) 2> >(tee stderr.log)`
- To display and log: `command 2>&1 | tee output.log` (simpler alternative for combined output)
- Press 'q' to quit `less`
"""
    (ex_dir / "README.md").write_text(readme)
    
    # Create output generation script
    script = """#!/bin/bash
# Script that generates both stdout and stderr output

echo "Starting process..."
echo "ERROR: Configuration file not found" >&2
sleep 1

echo "Loading modules..."
echo "WARNING: Module 'optional_feature' not available" >&2
sleep 1

echo "Connecting to database..."
echo "ERROR: Connection timeout after 30 seconds" >&2
sleep 1

echo "Retrying connection..."
echo "INFO: Connection established"
sleep 1

echo "Processing records..."
for i in {1..10}; do
    echo "Processed record $i"
    if [ $((i % 3)) -eq 0 ]; then
        echo "WARNING: Record $i has missing fields" >&2
    fi
    sleep 0.5
done

echo "Process complete"
echo "ERROR: 3 records failed validation" >&2
"""
    script_path = ex_dir / "generate_output.sh"
    script_path.write_text(script)
    script_path.chmod(0o755)
    
    print(f"  ✓ Created {ex_dir.name}")


def setup_exercise_05():
    """Setup files for Exercise 5: Parallel Data Distribution."""
    ex_dir = EXERCISE_DIR / "05_parallel_distribution"
    ex_dir.mkdir()
    
    # Create README
    readme = """# Exercise 5: Parallel Data Distribution

**Estimated time**: 20-25 minutes

## Objective
Use process substitution with `tee` to send data to multiple destinations simultaneously without creating temporary files.

## Context
You need to deploy a backup archive to multiple servers at once, or distribute log files to multiple processing pipelines without storing intermediate copies. This technique is crucial for efficient data distribution in production environments.

## Tasks
1. Create a tar archive of the `sample_data/` directory
2. Use `tee` with process substitution to extract the archive to three different destination directories simultaneously (simulating three remote servers)
3. Verify that all three destinations contain identical extracted data
4. Compare the performance and disk usage of this approach vs creating an archive file first, then extracting it three times
5. Measure the time difference between parallel and sequential distribution
6. Bonus: Modify the approach to compress the archive on-the-fly while distributing

## Reference
This builds on the video example: `tar cf - directory | tee >(ssh server1 tar xf -) >(ssh server2 tar xf -) > /dev/null`

## Files
- `sample_data/`: Directory containing sample files to archive and distribute

## Validation
- All three destination directories contain identical extracted data
- No local archive file is created (unless you create one for comparison)
- You understand the performance benefits of parallel distribution
- You can explain when this technique is more efficient than sequential distribution

## Hints
- Create destination directories first: `mkdir dest1 dest2 dest3`
- Basic syntax: `tar cf - source_dir | tee >(tar xf - -C dest1) >(tar xf - -C dest2) | tar xf - -C dest3`
- The final `> /dev/null` or `| tar xf - -C dest3` handles the remaining output from `tee`
- To verify: `diff -r dest1 dest2` and `diff -r dest2 dest3`
- To measure time: `time <command>`
- For compression: `tar czf - source_dir` (add 'z' flag)
- To see disk usage: `du -sh dest1 dest2 dest3`
"""
    (ex_dir / "README.md").write_text(readme)
    
    # Create sample data directory
    data_dir = ex_dir / "sample_data"
    data_dir.mkdir()
    
    # Create various sample files
    (data_dir / "config.json").write_text("""{
  "application": "sample-app",
  "version": "1.0.0",
  "environment": "production",
  "database": {
    "host": "db.example.com",
    "port": 5432
  }
}
""")
    
    (data_dir / "README.md").write_text("""# Sample Application

This is a sample application for demonstrating parallel distribution.

## Features
- Feature 1
- Feature 2
- Feature 3
""")
    
    # Create a subdirectory with more files
    logs_dir = data_dir / "logs"
    logs_dir.mkdir()
    
    # Generate sample log files
    for i in range(1, 4):
        log_content = f"""[2026-02-10 10:00:00] INFO: Application started
[2026-02-10 10:00:01] INFO: Loading configuration from config.json
[2026-02-10 10:00:02] INFO: Database connection established
[2026-02-10 10:00:03] INFO: Processing batch {i}
[2026-02-10 10:00:04] WARNING: High memory usage detected
[2026-02-10 10:00:05] INFO: Batch {i} completed successfully
"""
        (logs_dir / f"app_{i}.log").write_text(log_content)
    
    # Create a data file
    (data_dir / "data.csv").write_text("""id,name,value,timestamp
1,item1,100,2026-02-10T10:00:00
2,item2,200,2026-02-10T10:01:00
3,item3,150,2026-02-10T10:02:00
4,item4,300,2026-02-10T10:03:00
5,item5,250,2026-02-10T10:04:00
""")
    
    print(f"  ✓ Created {ex_dir.name}")


def main():
    """Main setup function."""
    print("=" * 70)
    print("Setting up exercises for: Process Substitution in Bash")
    print("Based on: 'extremely cool shell trick I did not know about'")
    print("Source: https://www.youtube.com/watch?v=2A4bs40scSo")
    print("=" * 70)
    print()
    
    try:
        create_directory_structure()
        
        # Setup individual exercises
        setup_exercise_01()
        setup_exercise_02()
        setup_exercise_03()
        setup_exercise_04()
        setup_exercise_05()
        
        print()
        print("✅ Setup complete!")
        print()
        print(f"Exercise directory created at: {EXERCISE_DIR.absolute()}")
        print()
        print("📁 Structure:")
        print("  exercises/")
        print("  ├── 01_view_remote_content/")
        print("  ├── 02_compare_sorted_files/")
        print("  ├── 03_preview_transformations/")
        print("  ├── 04_dual_output_logging/")
        print("  └── 05_parallel_distribution/")
        print()
        print("🚀 Next steps:")
        print(f"  1. cd {EXERCISE_DIR}")
        print("  2. Read the README.md in each exercise directory")
        print("  3. Start with exercise 01 and work through them in order")
        print("  4. Each exercise builds on concepts from the video")
        print()
        print("🧹 Cleanup:")
        print("  Run ./cleanup_exercises.sh when finished to remove all files.")
        print()
        
    except Exception as e:
        print(f"❌ Error during setup: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
