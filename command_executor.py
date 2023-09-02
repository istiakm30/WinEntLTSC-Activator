import os
import subprocess

def execute_commands():
    # Define the commands to be executed
    commands = [
        f'cscript.exe {os.environ["WINDIR"]}\\system32\\slmgr.vbs /rilc',
        f'cscript.exe {os.environ["WINDIR"]}\\system32\\slmgr.vbs /upk >$null 2>&1',
        f'cscript.exe {os.environ["WINDIR"]}\\system32\\slmgr.vbs /ckms >$null 2>&1',
        f'cscript.exe {os.environ["WINDIR"]}\\system32\\slmgr.vbs /cpky >$null 2>&1',
        f'cscript.exe {os.environ["WINDIR"]}\\system32\\slmgr.vbs /ipk M7XTQ-FN8P6-TTKYV-9D4CC-J462D',
        'powershell.exe Set-Service -Name LicenseManager -StartupType Automatic; Start-Service -Name LicenseManager',
        'powershell.exe Set-Service -Name wuauserv -StartupType Automatic; Start-Service -Name wuauserv',
        'clipup -v -o -altto c:\\'
    ]

    # Execute each command
    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Failed to execute command: {command}")
            print(f"Error: {stderr.decode().strip()}")
            return False

    print("Commands executed successfully.")
    return True

if __name__ == "__main__":
    execute_commands()