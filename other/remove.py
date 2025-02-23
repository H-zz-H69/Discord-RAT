import os
import sys
import shutil
import winreg as reg
import subprocess
import ctypes


# This RAT is made by H-zz-H!  
# If you have any questions or need help, feel free to contact me on Discord: _h_zz_h_ or join my server: https://discord.gg/29Ya4F3CgQ.  
# On my Discord server (as of 23.02.2025), I have posted a cracked open-source Discord Stealer that would normally cost more than 120 euros for lifetime access.  
# Join my Discord server for coding help or if you encounter errors with this RAT. I am always open to new ideas, projects, or feature suggestions for this RAT.  
# If you want to add new features or improve this RAT, feel free to do so and share your work with me on Discord.  
# If I find the time, this RAT will be updated and working forever. If not, well, I don't know.  
# If you use this RAT for illegal purposes, I am not responsible for it. I am also not responsible for any damage caused by this RAT.  
# Skid from this project if you want, I don’t really care lol. Just don’t claim it as your own work.  

# Sources I skidded from:  
# https://github.com/Blank-c/Blank-Grabber (The !blocklist and !unblocklist commands are almost fully skidded. I just changed the code a bit to fit my project).  
# Tried doing it on my own (but I’m way too retarded for that).
# https://github.com/moom825/Discord-RAT (Because of this RAT, I started this project. So special thanks to moom825).  
# The !uncritproc and !critproc commands are from moom825's Discord-RAT project. Many features are quite the same as in moom825's project.  
# That’s because I needed some features I could code, and his GitHub page was full of ideas to implement.  
# Almost everything in this project is inspired by him.  

# Thanks for taking the time to read.  
# Love y’all. Bye.  
# ~~~ H-zz-H ~~~  

# This is the remove.py file. It is used to remove every trace of the auto StartUp.
# It removes the file from the StartUp folder, the registry, the RunOnce registry, the group policy, and the task scheduler.

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("If accepted UAC, should have removed every trace of the auto StartUp...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

script_path = os.path.realpath(sys.argv[0])
autohzzh = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
hzzh_path = os.path.join(autohzzh, 'Eulen.exe')

temp_folder = os.getenv('TEMP')
file_name = "Eulen.exe"
hzzh_path1 = os.path.join(temp_folder, file_name)

def remove_hzzh():
    try:
        if os.path.exists(hzzh_path):
            print(f"Removing {hzzh_path}")
            os.remove(hzzh_path)
        else:
            print(f"{hzzh_path} does not exist.")
    except Exception as e:
        print(f"Error removing {hzzh_path}: {e}")

def remove_hzzhtemp():
    try:
        if os.path.exists(hzzh_path1):
            print(f"Removing {hzzh_path1}")
            os.remove(hzzh_path1)
        else:
            print(f"{hzzh_path1} does not exist.")
    except Exception as e:
        print(f"Error removing {hzzh_path1}: {e}")

def remove_hzzhreg():
    try:
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_WRITE)
        reg.DeleteValue(registry_key, "Eulen")
        reg.CloseKey(registry_key)
        print("Removed Windows Defender from registry Run key.")
    except FileNotFoundError:
        print("Registry key Windows Defender does not exist.")
    except Exception as e:
        print(f"Error removing registry key: {e}")

def remove_hzzh_runonce():
    try:
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce", 0, reg.KEY_WRITE)
        reg.DeleteValue(registry_key, "Eulen")
        reg.CloseKey(registry_key)
        print("Removed WindowsDefender from registry RunOnce key.")
    except FileNotFoundError:
        print("Registry key WindowsDefenders does not exist in RunOnce.")
    except Exception as e:
        print(f"Error removing registry key: {e}")

def remove_hzzh_group_policy():
    try:
        if os.path.exists(r"C:\Windows\System32\gpedit.msc"):
            command = f'gpedit.msc /c "User Configuration\\Administrative Templates\\System\\Logon\\Run These Programs at User Logon" /v script /f'
            subprocess.run(command, shell=True)
            print("Removed group policy entry.")
        else:
            print("Group Policy Editor is not available on this system.")
    except Exception as e:
        print(f"Error removing group policy: {e}")

def remove_hzzh_task_scheduler():
    try:
        task_name = "WindowsDefenderTask"
        query_command = f'schtasks /query /tn "{task_name}"'
        result = subprocess.run(query_command, shell=True, capture_output=True, text=True)
        
        if "ERROR" not in result.stdout:
            delete_command = f'schtasks /delete /tn "{task_name}" /f'
            subprocess.run(delete_command, shell=True)
            print(f"Removed task scheduler entry {task_name}.")
        else:
            print(f"Task {task_name} does not exist.")
    except Exception as e:
        print(f"Error removing task scheduler entry: {e}")

def remove_all_startups():
    remove_hzzh()
    remove_hzzhtemp()
    remove_hzzhreg()
    remove_hzzh_runonce()
    remove_hzzh_group_policy()
    remove_hzzh_task_scheduler()

if __name__ == "__main__":
    remove_all_startups()
