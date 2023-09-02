import shutil
import os

def copy_files_to_directory():
    # Get the current working directory
    current_directory = os.getcwd()

    # Define the destination directory
    destination_directory = 'C:\\Windows\\System32\\spp\\tokens\\skus'

    # Copy each file in the current directory to the destination directory
    for filename in os.listdir(current_directory):
        if os.path.isfile(filename):
            shutil.copy2(filename, destination_directory)

    print("Files copied successfully.")

if __name__ == "__main__":
    copy_files_to_directory()
