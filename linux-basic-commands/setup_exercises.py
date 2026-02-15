import os
import time
from pathlib import Path

def create_file(path, size_kb=1, mtime_offset=0):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(os.urandom(size_kb * 1024))
    
    if mtime_offset != 0:
        current_time = time.time()
        os.utime(path, (current_time + mtime_offset, current_time + mtime_offset))

def setup():
    base_dir = Path("exercises")
    if base_dir.exists():
        print("Exercises directory already exists. Please run cleanup first.")
        return

    print("Setting up exercises...")

    # Exercise 1: Inspection
    ex1_dir = base_dir / "01_inspection" / "data"
    create_file(ex1_dir / "small_log.log", 5)
    create_file(ex1_dir / "medium_log.log", 500)
    create_file(ex1_dir / "huge_log.log", 2048)
    create_file(ex1_dir / ".hidden_config", 1)
    # Set different times
    os.utime(ex1_dir / "small_log.log", (time.time() - 3600, time.time() - 3600))
    os.utime(ex1_dir / "huge_log.log", (time.time() - 7200, time.time() - 7200))

    # Exercise 2: Deployment
    ex2_src = base_dir / "02_deployment" / "src"
    create_file(ex2_src / "nginx.conf", 2)
    create_file(ex2_src / "db.env", 1)
    os.chmod(ex2_src / "db.env", 0o600)

    # Exercise 3: Cleanup
    ex3_dir = base_dir / "03_cleanup"
    create_file(ex3_dir / "temp_builds" / "build1.bin", 10)
    create_file(ex3_dir / "temp_builds" / "build2.bin", 10)
    create_file(ex3_dir / "protected_configs" / "config1.conf", 1)
    create_file(ex3_dir / "protected_configs" / "config2.conf", 1)

    # Exercise 4: Search
    ex4_dir = base_dir / "04_search"
    create_file(ex4_dir / "old_script.sh", 5, mtime_offset=-86400*2)
    create_file(ex4_dir / "recent_script.sh", 15, mtime_offset=-3600)
    create_file(ex4_dir / "large_data.bin", 150, mtime_offset=-1800)
    create_file(ex4_dir / "notes.txt", 2)

    # Create READMEs for each
    for i in range(1, 5):
        d = base_dir / f"0{i}_{['inspection', 'deployment', 'cleanup', 'search'][i-1]}"
        with open(d / "README.md", "w") as f:
            f.write(f"# Exercise {i}\nRefer to the main README.md in the root directory for tasks.")

    print("Setup complete! Navigate to the 'exercises' directory to begin.")

if __name__ == "__main__":
    setup()
