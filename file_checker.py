import os
import shutil

def check_files():
    # Define the destination directory
    destination_directory = 'C:\\Windows\\System32\\spp\\tokens\\skus'

    # Get the list of files in the destination directory
    destination_files = os.listdir(destination_directory)
    current_directory = os.getcwd()
    current_files = os.listdir(current_directory)

    folders_to_copy = ['Enterprise', 'EnterpriseS', 'IoTEnterprise']

    # Check if all files in the current directory are present in the destination directory
    for filename in current_files:
        if filename in folders_to_copy:
            if filename not in destination_files:
                print(f"Folder {filename} not found in destination directory. Copying now.")
                shutil.copytree(os.path.join(current_directory, filename), os.path.join(destination_directory, filename))
            else:
                print(f"Folder {filename} already exists in the destination directory.")
        else:
            pass

    print("All necessary folders copied successfully.")
    return True

if __name__ == "__main__":
    check_files()