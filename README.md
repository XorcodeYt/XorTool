<h1 align="center">XorTool 🛠️</h1>
<p align="center">
  <b>Modular Multi-Tool for Windows</b><br>
  <i>By Xorcode</i>
</p>

<p align="center">
  <a href="https://github.com/XorcodeYt/XorTool">
    <img src="https://img.shields.io/github/stars/XorcodeYt/XorTool?style=social" alt="GitHub stars">
  </a>
  <a href="https://github.com/XorcodeYt/XorTool/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/XorcodeYt/XorTool.svg" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Platform-Windows-blue">
</p>

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation-windows-only)
- [Usage](#usage)
- [Credits](#credits)
- [Notes](#notes)

---

## 📝 Overview

**XorTool** is a modular multi-tool for Windows, written in Python. It provides several network utilities and handy tools through a stylish terminal menu.

![Alt text](https://i.ibb.co/7JGNK7hn/tool.png)

---

## ✨ Features

- **[1] TCP Port Scanner**  
  Scan open TCP ports on a target.

- **[2] IP Scanner**  
  Scan an IP range to find active hosts.

- **[3] DNS Resolver**  
  Resolve domain names to IP addresses.

- **[4] Clear Credentials**  
  Erase stored xbox/xblticktes credentials.

- **[5] Password Generator**  
  Generate strong, random passwords.

- **[6] YouTube Downloader**  
  Download YouTube videos using [yt-dlp](https://github.com/yt-dlp/yt-dlp) *(requires ffmpeg)*.

- **[7] ZIP Cracker**  
  Brute-force ZIP files protected by passwords (using [zip-cracker](https://github.com/FreshMilkshake/zip-cracker)).

- **[8] Credits**  
  Display credits and used dependencies.

- **[9] Quit**  
  Exit the program.

## 🛠️ Installation (Windows Only)

- Download or clone the repository and open the project folder.
- Install Python 3.x (make sure Python is added to PATH).
- Install the required Python dependencies (`yt-dlp`, `requests`, or via `requirements.txt` if available).
- Ensure all custom modules are inside the `modules/` folder at the project root.
- Download and install FFmpeg (add the `bin` folder to your Windows Environment Variables).
- Restart your terminal or PC, and check FFmpeg installation by running `ffmpeg -version`.

## ▶️ Usage

- Run the main script using Command Prompt or PowerShell:  
  Start the program and follow the on-screen menu.
- Select a tool by entering its corresponding number.

## 🙏 Credits

- **ZIP Cracker** : [zip-cracker](https://github.com/FreshMilkshake/zip-cracker)
- **YouTube Downloader** : [yt-dlp](https://github.com/yt-dlp/yt-dlp) *(requires ffmpeg)*

## ⚠️ Notes

- **Windows Only:** This tool is designed specifically for Windows.
- **For educational and personal use only.**
- Do not use any network tools or downloaders without permission on external machines.