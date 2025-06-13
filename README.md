XorTool - Multi Tool by Xorcode
Overview
XorTool is a modular multi-tool for Windows, written in Python, offering several network utilities and handy tools through a stylish terminal menu.

Features
[1] TCP Port Scanner
Scan open TCP ports on a target.

[2] IP Scanner
Scan an IP range to find active hosts.

[3] DNS Resolver
Resolve domain names to IP addresses.

[4] Clear Credentials
Erase stored credentials.

[5] Password Generator
Generate strong, random passwords.

[6] YouTube Downloader
Download YouTube videos using yt-dlp (requires ffmpeg).

[7] ZIP Cracker
Brute-force ZIP files protected by passwords (using zip-cracker).

[8] Credits
Display credits and used dependencies.

[9] Quit
Exit the program.

Installation (Windows Only)
1. Clone the repository
git clone https://github.com/XorcodeYt/XorTool.git
cd xortool
2. Install Python 3.x
Download and install Python 3, and ensure you check "Add Python to PATH" during installation.

3. Install Python dependencies
If you have a requirements.txt file, simply run:
pip install -r requirements.txt
If not, manually install the basics (add others as needed):
pip install yt-dlp requests
Note:
The custom modules (ports_scanner, ip_scanner, etc.) must be inside a modules/ folder at the root of your project.

4. Install FFmpeg (required for YouTube downloads)
Download a Windows build of FFmpeg from https://ffmpeg.org/download.html (→ select Windows builds, e.g., gyan.dev FFmpeg builds).

Unzip the folder (for example, C:\ffmpeg).

Add the path to the bin folder (e.g., C:\ffmpeg\bin) to your Windows Environment Variables:

Search for "Environment Variables" in the Start menu.

Edit the Path variable and add the path to C:\ffmpeg\bin.

Restart your terminal or computer for changes to take effect.

To check that ffmpeg is installed, open Command Prompt and run:

ffmpeg -version
You should see version info if it’s correctly installed.

Usage
Run the main script from Command Prompt or PowerShell:

python main.py
Follow the on-screen menu and select a tool by entering its number.

Credits
ZIP Cracker uses zip-cracker by Fresh Milkshake.
YouTube Downloader uses yt-dlp and requires ffmpeg.

Notes
Windows Only: This tool is designed to work on Windows.

For educational and personal use only.
Do not use any network tools or downloaders without permission on external machines.