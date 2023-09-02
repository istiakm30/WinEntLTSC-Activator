import file_copier
import restart_prompt
import file_checker
import command_executor
import subprocess
import re

def check_windows_activation():
    # Execute the command to get Windows activation status
    result = subprocess.run(['cscript', '//Nologo', 'C:\\Windows\\System32\\slmgr.vbs', '/dli'], capture_output=True, text=True)
    # Check the output for words that indicate activation
    is_activated = 'licensed' in result.stdout.lower() or 'permanent' in result.stdout.lower() or 'notification' in result.stdout.lower()
    # Execute the command to check if Windows is in evaluation mode
    result = subprocess.run(['cscript', '//Nologo', 'C:\\Windows\\System32\\slmgr.vbs', '/xpr'], capture_output=True, text=True)

    # Check the output for words that indicate evaluation mode
    is_evaluation = 'evaluation' in result.stdout.lower()

    return is_activated and not is_evaluation

def main():
    # # Step 0: Check if Windows is activated
    # if check_windows_activation():
    #     print("Windows is already activated.")
    #     return
    # else:
    #     print("Windows is not activated or is in evaluation mode.")

    # Step 1: Copy the current directories to the specified location
    file_copier.copy_files_to_directory()

    # Step 2: Prompt the user to restart the system
    restart_prompt.prompt_restart()

    # Step 3: Check whether the files have been copied
    if not file_checker.check_files():
        print("Error: Not all files were copied successfully.")
        return

    # Step 4: Execute the commands
    if not command_executor.execute_commands():
        print("Error: Not all commands were executed successfully.")
        return

    print("Program executed successfully.")

if __name__ == "__main__":
    main()