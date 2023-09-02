import os

def prompt_restart():
    # Prompt the user to restart the system
    print("Please restart your system for the changes to take effect.")
    user_input = input("Have you restarted your system? (yes/no): ")

    # Check if the user has restarted the system
    if user_input.lower() == 'yes':
        print("System restart confirmed.")
    else:
        print("Please restart your system and run the program again.")
        os._exit(0)

if __name__ == "__main__":
    prompt_restart()
