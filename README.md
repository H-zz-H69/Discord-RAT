# Hello ❤

## On Every 5 Stars an big Update will be dropped.
# ~~5~~, ~~10~~, ~~15~~, ~~20~~, ~~25~~, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80

# Educational RAT – Proof-of-Concept

⚠️ This project is for **educational purposes only**.  
It is intended to be used **only in a controlled, isolated test environment** (e.g., Virtual Machine).  
**Any unauthorized use** on real systems or networks is **strictly prohibited and illegal**

🚨 **Warning:** This tool contains potentially dangerous features (e.g., keyloggers, Defender Bypasses). Unauthorized use of these features is prohibited, and may lead to serious legal and ethical consequences. Use at your own risk.

By using this software, you agree that you will only run it in safe, legal environments and will not misuse it in any way. The creator is not responsible for any damage caused by the misuse of this project.

# In the near Future; (Features in next update have an "X" on the end)

- RAT Builder with GUI 🎁  
- Plugin options to add custom features 🍕🍕  
- `!browser` – Steals passwords, history, cookies, and more 🦕🦖  
- On first-time startup, it automatically steals data ⚡  
- Discord injection to capture password changes and token 🗝                                                 
- Get Discord account info using the `!token` command 🔑
- Discord !token command doesnt work smh lol 💀
- Add UAC bypass to get admin access without a prompt 🔒  
- Spreads via Discord token (spamming in random servers and DMs) 📲  
- Known bug: RAT may crash when sending fake error message boxes 🛠️                                            
- Cryptocurrency stealer 💰  
- Launch a child process for each command (helps avoid antivirus detection by respawning if killed) 🔄  
- Cryptocurrency mining on victim’s PC 💻  
- Launch a rootkit 🕵️‍♂️  
- Delete System32 💣  
- Reinstall Windows 🔄💻  
- Uninstall Windows and launch a Linux distro 🐧
- Start an steam game ❌   ❌   ❌    ❌    ❌    ❌    ❌    ❌                                                                      
- Create and change to new Desktop.   ❌    ❌    ❌    ❌    ❌ 
- Move Folders around by command   ❌    ❌    ❌    ❌    ❌    ❌ 
- taskkill random programs with custom interval   ❌    ❌    ❌    ❌ 
- Toggle command which closes every program entered   ❌    ❌    ❌    ❌ 
- Change Res and layout of Victims Monitor   ❌    ❌    ❌    ❌    ❌ 
- Ratelimit check on many ratted PCS by not sending every message 20 times   ❌    ❌    ❌    ❌ 
- Undetected on Virustotal (https://www.virustotal.com/gui/file/343bd77b607f12754a2a58fea41f08e3e1c7326207f5fb4798cc217325fca4a4?nocache=1)
  
## [Setup](https://www.youtube.com/watch?v=3AtgXzT03hU):
Install [Python 3.9.11](https://www.python.org/downloads/release/python-3911/)


Change the token on line 146, and you're good to go! ⚡

If you want, feel free to read through the details below. 📖

---

## About This RAT

This RAT was created by H-zz-H.

If you have any questions or need assistance, you can reach me on Discord, join my server: [Discord Server](https://discord.gg/29Ya4F3CgQ).

Join my Discord for:

- Coding help 🤖
- Troubleshooting errors related to this RAT 🛠️
- New ideas, projects, or feature suggestions 💡

If you'd like to add new features or improve this RAT, go ahead! Feel free to share your work with me on Discord. 🙌

I will update and maintain this project as long as I have time. If I stop, well... I don’t know. ⏳

---

# Virustotal:
- ## https://www.virustotal.com/gui/file/343bd77b607f12754a2a58fea41f08e3e1c7326207f5fb4798cc217325fca4a4?nocache=1

## Disclaimer

- I am not responsible for any misuse of this RAT. ⚠️
- I am not liable for any damage caused by this software. 💥
- Use it at your own risk. ⚡

---

## Skidded Sources

I’ve used some code from the following sources:

- [Blank Grabber](https://github.com/Blank-c/Blank-Grabber) – The !blocklist and !unblocklist commands are almost fully skidded, with some modifications to fit my project. 🔄
- [Discord-RAT by moom825](https://github.com/moom825/Discord-RAT) – This project inspired me to start mine. Special thanks to moom825. 👏
- [Roblox Stealer](https://github.com/Ramona-Flower/Roblox-Client-Cookie-Stealer/tree/main) - Completely stolen 💙❤💙
- [Chat GPT](https://chatgpt.com/) – The !floatpic !cd !floatpic !rec commands and !list commands are ChatGPT generated 🙄

The !uncritproc and !critproc commands are directly from moom825’s RAT. 💻

Many features are similar because I needed working implementations, and his GitHub page was full of great ideas. 💡

---

## Final Words

Thanks for taking the time to read this. ❤️

Love y’all. Bye. 👋

~~~
H-zz-H - https://discord.gg/29Ya4F3CgQ
~~~

---

# Features:

## 📊 System Info & Monitoring
- `!information` — Sends system info 🖥️  
- `!disk` — Disk space 📦  
- `!cpu` — CPU usage ⚙️  
- `!ram` — RAM usage 💾  
- `!overview` — CPU, RAM, Disk overview 🛠️  
- `!battery` — Battery status 🔋  
- `!publicip` — Victim's public IP 🌐  

---

## 🌐 Network
- `!network` — List WiFi networks with saved passwords 🌐  
- `!net_pass (wifi_name)` — Get password for specific WiFi 🌐  
- `!net` — Create/Recreate botnet channel ⚡  
- `!botnet (ip) (time) (method)` — Start DDoS attack ⚡  
- `hwid` — Get hardware ID 🍕🍕  

---

## 📷 Visual Capture
- `!screen` — Take a screenshot 🖼️  
- `!webcam` — Capture webcam image 📸  
- `!recscreen (sec)` — Record screen for X seconds  
- `!recwebcam (sec)` — Record webcam for X seconds  
- `!recaudio (sec)` — Record audio for X seconds 🎤  

---

## 📁 File & Directory
- `!list` — List files in current directory 📂  
- `!cd (path)` — Change directory  
- `!download (path)` — Download file (10MB limit) 📥  
- `!download_ext (file.png)` — Download large file (100MB) 📥  
- `!upload (attachment) (!path!)` — Upload file (10MB limit) 📤  
- `!upload_ext (URL) (!path!)` — Upload from URL (no limit) 📤  
- `!exec (path)` — Execute file  
- `!encrypt (*) or (file.ext)` — Encrypt files to `.hzzh` ⚽  

---

## ⌨️ Keylogger
- `!keylog_start` — Start keylogger  
- `!keylog_dump` — Dump logged keys  
- `!keylog_stop` — Stop keylogger  

---

## 🎭 Execution & Tricks
- `!error (Title | Text)` — Show fake error ⚠️  
- `!web_open (url)` — Open a URL 🌍  
- `!command (cmd)` — Execute command 💻  
- `!shell (cmd)` — Execute PowerShell 💻  
- `!tasks` — List running tasks 📝  
- `!taskkill` — Kill task by name  
- `!fakecmd (amount)` — Flash fake CMDs 💻  
- `!cmdspam` — Spam CMDs until crash 💻
- `!closeexplorer` - Kill Windows Explorer (hides desktop & taskbar) 🤯
- `!minimize` - Simulate Win+D (show desktop) 👩‍💻
- `!clipboard` - Show clipboard contents 📋 (Missing)
- `!wallpaper (attachment.png)` -  Change wallpaper 🖼️ (Missing)
- `!steam` - Gets Steam Username & ID + all games installed with ID 🍕
- `!roblox` - Steal Roblox cookie 🎮🕹

---

## 🔧 Persistence & Privilege
- `!startup` — Add to startup 🐀  
- `!smartup` — Unknown startup path 🐀  
- `!getadmin` — Request Admin via UAC spam  
- `!admin` — Check admin status 🛠️  
- `!closesession` — Close other user sessions 💻
- `!selfdestruct` - Remove RAT and traces 💣

---

## 🔐 Admin-Only
- `!taskmgr` — Disable Task Manager 🎰  
- `!taskmgr_enable` — Enable Task Manager 🎰  
- `!blocklist` — Block AV-related sites 🦠  
- `!unblocklist` — Unblock AV-related sites 🦠  
- `!nostartup` — Hide Startup folder access 🔒🗂️  
- `!nostartup_disable` — Restore Startup folder access 🔓🗂️  
- `!critproc` — Make process critical (BSOD on kill) 🆙  
- `!uncritproc` — Remove critical status 🆙  
- `!windef` — Disable Windows Defender 🛡️  
- `!exclude_exe` — Exclude all `.exe` from Defender 🐀  
- `!block` — Block/Unblock input devices 🖱️⌨️  

---

## 🧪 Troll Features
- `!screensaver` — Activate fake screensaver  
- `!floatpic (sec) (url)` — Floating unclosable image  
- `!logout` — Log out user (Win+L)  
- `!reverse` — Reverse mouse movement 🖱️🔄  
- `!jumpscare` — Loud scary popup 😱🔊  
- `!cpufuck` — Max CPU to 100% ⚡💻  
- `!bluescreen` — Trigger BSOD 💥🖥️  
- `!shaking` — Mouse shake effect 💥🖱️  
- `playmp3` - Play attached MP3 file 🎵

---

## 💬 Discord Management
- `!purge (amount)` — Delete messages 🚮  
- `!recreate (#channel)` — Delete & recreate channel 🔄  

---
Made with ❤ by H-zz-H

### Example Images:

#### Discord Chat Interaction
![Discord Chat Interaction](other/rat.png)

This image shows someone using the commands, and the bot responding to them.

#### Startup Message
![Startup Message](other/rat1.png)

This image shows the startup message of someone starting the RAT—looks hot! 🔥
