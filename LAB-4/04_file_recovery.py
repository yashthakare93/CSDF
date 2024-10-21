import os

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def simulate_file_recovery():
    """Simulate a file recovery process."""
    clear_screen()
    
    print("File Recovery Script")
    print("For Programming Wonders")
    print("The list of drives is:")
    
    # Use 'wmic' to list drives in Windows
    drives = os.popen("wmic logicaldisk get name").read()
    print(drives)

    devname = input("Enter the device to be used (e.g., E:): ").strip()
    
    # Check if the entered device name is valid
    if not os.path.exists(devname + "\\"):
        print(f"Error: {devname} is not a valid drive.")
        return
    
    imgname = input("Enter the image name (e.g., recovery.img) to save in C:\\Users\\DELL\\OneDrive\\Desktop\\CSDF\\LAB-4: ").strip()
    imgpath = os.path.join("C:\\Users\\DELL\\OneDrive\\Desktop\\CSDF\\LAB-4", imgname)

    # Simulate imaging of the drive
    print(f"Simulating imaging of {devname} to {imgpath}...")
    
    # In a real scenario, you'd create an image of the drive here
    # We will just create a dummy file to represent the image
    with open(imgpath, 'w') as img_file:
        img_file.write("Simulated disk image for drive " + devname + "\n")

    print("Simulated imaging complete. Proceeding to check for deleted files...")

    # Simulating inode display
    print("Showing simulated inode numbers (placeholders):")
    print("1. file1.txt (Deleted)")
    print("2. file2.txt (Deleted)")
    print("3. file3.txt (Active)")

    inodeno = input("Enter the inode of the deleted file (just type 1 for this simulation): ").strip()
    
    # Simulating recovery of a file
    print("Recovering file (simulation)...")
    newfile = input("Enter the name of the file where data will be stored (with extension): ").strip()
    newfile_path = os.path.join("C:\\Users\\DELL\\OneDrive\\Desktop\\CSDF\\LAB-4", newfile)

    # Write dummy recovered content to the new file
    with open(newfile_path, 'w') as f:
        f.write(f"Recovered content for inode {inodeno}\n")

    print("The contents of the file are:")
    with open(newfile_path, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    simulate_file_recovery()
