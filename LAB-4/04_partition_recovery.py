import os
import subprocess

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(command, check=True, shell=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return None

def generate_diskpart_script(devname, action='list', size_mb=None):
    """Generate a diskpart script for the selected action (list or create partition)."""
    script_content = ""
    
    if action == 'list':
        script_content = f"""
        select disk {devname}
        list partition
        exit
        """
    elif action == 'create' and size_mb:
        script_content = f"""
        select disk {devname}
        create partition primary size={size_mb}
        assign letter={devname}
        exit
        """

    script_file = f"{devname}_diskpart_script.txt"
    with open(script_file, 'w') as file:
        file.write(script_content)

    return script_file

def partition_recovery():
    """Partition recovery script."""
    print("Partition Recovery Script")

    # List available disks using diskpart
    print("Listing available disks...")
    print(run_command("diskpart /s list_disk.txt"))

    # User selects a disk
    devname = input("Enter the disk number (e.g., 0 for Disk 0): ").strip()

    # Show the list of partitions on the selected disk
    print("Showing partition table for Disk", devname)
    script_file = generate_diskpart_script(devname, action='list')
    print(run_command(f"diskpart /s {script_file}"))

    # Optionally create a new partition
    if input("Do you want to create a new partition? (yes/no): ").lower() == 'yes':
        size_mb = input("Enter the partition size (in MB): ").strip()
        script_file = generate_diskpart_script(devname, action='create', size_mb=size_mb)
        print(run_command(f"diskpart /s {script_file}"))

if __name__ == "__main__":
    partition_recovery()
