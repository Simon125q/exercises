import os
import subprocess

def create_file(path, content, mode=0o644):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    os.chmod(path, mode)

def main():
    base_dir = "exercises"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    print(f"Creating exercise environment in {base_dir}...")

    # Exercise 1: Script Permissions
    ex1_dir = os.path.join(base_dir, "01_script_permissions")
    script_path = os.path.join(ex1_dir, "backup.sh")
    create_file(script_path, "#!/bin/bash\necho 'Backup completed successfully!'\n", 0o644)
    create_file(os.path.join(ex1_dir, "README.md"), "# Exercise 1\nMake `backup.sh` executable using `chmod 755`.\n")

    # Exercise 2: Secure Config
    ex2_dir = os.path.join(base_dir, "02_secure_config")
    config_path = os.path.join(ex2_dir, "database.conf")
    create_file(config_path, "DB_USER=admin\nDB_PASS=secret_password_123\n", 0o664)
    create_file(os.path.join(ex2_dir, "README.md"), "# Exercise 2\nSecure `database.conf` using symbolic `chmod` so only the owner can read/write it.\n")

    # Exercise 3: Ownership Handover
    ex3_dir = os.path.join(base_dir, "03_ownership_handover")
    report_path = os.path.join(ex3_dir, "system_report.log")
    # Create as root if possible, but in sandbox we might just simulate it by changing owner to root if we have sudo
    create_file(report_path, "System status: OK\nErrors: None\n", 0o644)
    try:
        subprocess.run(["sudo", "chown", "root:root", report_path], check=True)
    except Exception as e:
        print(f"Warning: Could not change ownership to root: {e}")
    create_file(os.path.join(ex3_dir, "README.md"), "# Exercise 3\nTake ownership of `system_report.log` using `chown` and set permissions to `600`.\n")

    # Exercise 4: Rescue Project
    ex4_dir = os.path.join(base_dir, "04_rescue_project")
    # Create a messy structure
    create_file(os.path.join(ex4_dir, "README.md"), "# Exercise 4\nFix the entire project permissions using the `find` rescue command.\n")
    
    src_dir = os.path.join(ex4_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    # Directory with no execute permission (can't enter)
    os.chmod(src_dir, 0o644) 
    
    create_file(os.path.join(src_dir, "main.c"), "#include <stdio.h>\nint main() { return 0; }\n", 0o777) # Executable source file (wrong)
    create_file(os.path.join(ex4_dir, "notes.txt"), "Some project notes.\n", 0o777) # Executable text file (wrong)

    print("\nSetup complete!")
    print("Navigate to the 'exercises' directory to begin.")
    print("Refer to 'exercise_guide.md' for instructions.")

if __name__ == "__main__":
    main()
