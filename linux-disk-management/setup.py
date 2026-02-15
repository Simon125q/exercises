import os
import subprocess

def create_file(path, content, size_mb=0):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if size_mb > 0:
        with open(path, 'wb') as f:
            f.write(os.urandom(size_mb * 1024 * 1024))
    else:
        with open(path, 'w') as f:
            f.write(content)

def main():
    base_dir = "exercises"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    print(f"Creating disk management exercise environment in {base_dir}...")

    # Exercise 1: Disk Usage
    ex1_dir = os.path.join(base_dir, "01_disk_usage")
    create_file(os.path.join(ex1_dir, "README.md"), "# Exercise 1\nFind the large file using `df` and `du`.\n")
    create_file(os.path.join(ex1_dir, "logs", "app.log"), "Normal log content\n" * 100)
    create_file(os.path.join(ex1_dir, "data", "large_data.bin"), "", size_mb=50)

    # Exercise 3: Mounting
    ex3_dir = os.path.join(base_dir, "03_mounting")
    img_path = os.path.join(ex3_dir, "data_disk.img")
    create_file(os.path.join(ex3_dir, "README.md"), "# Exercise 3\nMount the `data_disk.img` to a new directory.\n")
    
    # Create a small ext4 disk image
    print("Generating simulated disk image...")
    try:
        subprocess.run(["dd", "if=/dev/zero", f"of={img_path}", "bs=1M", "count=10"], check=True)
        subprocess.run(["mkfs.ext4", "-F", img_path], check=True)
        
        # Add a file inside the image by mounting it temporarily
        mnt_tmp = "/tmp/mnt_setup"
        os.makedirs(mnt_tmp, exist_ok=True)
        subprocess.run(["sudo", "mount", img_path, mnt_tmp], check=True)
        with open(os.path.join(mnt_tmp, "secret_plans.txt"), 'w') as f:
            f.write("The plans are safe.\n")
        subprocess.run(["sudo", "umount", mnt_tmp], check=True)
    except Exception as e:
        print(f"Warning: Could not fully prepare disk image (requires sudo/loop support): {e}")

    # Exercise 4: fstab
    ex4_dir = os.path.join(base_dir, "04_fstab")
    create_file(os.path.join(ex4_dir, "README.md"), "# Exercise 4\nCreate a mock fstab entry for the disk image.\n")

    print("\nSetup complete!")
    print("Navigate to the 'exercises' directory to begin.")
    print("Refer to 'exercise_guide.md' for instructions.")

if __name__ == "__main__":
    main()
