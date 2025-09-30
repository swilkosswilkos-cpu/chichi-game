========================================
FASSTVIDEO - PORTABLE VIDEO DOWNLOADER
========================================

VERSION: 1.0
BUILD DATE: 2025-09-29

INSTALLATION
------------
This is a portable application - no installation required!

1. Copy the entire "FasstVideo" folder to any location on your PC
2. Navigate into the FasstVideo folder
3. Double-click "FasstVideo.exe" to run the application

REQUIREMENTS
------------
- Windows 10 or higher (64-bit)
- Internet connection for downloading videos
- Recommended: Chrome or Firefox browser installed (for browser automation features)

FEATURES
--------
- Download videos from various websites
- Real-time progress tracking
- Browser automation for complex video extraction
- yt-dlp integration for maximum compatibility
- Modern animated GUI
- Multiple download methods with automatic fallback
- Configurable download folder

FIRST RUN
---------
On first launch, you will be presented with a legal disclaimer.
Please read and accept the terms to continue using the application.

The application will check for and install any missing dependencies automatically.

USAGE
-----
1. Launch FasstVideo.exe
2. Paste a video URL into the input field
3. Select your download folder (or use the default)
4. Click "Download" to start
5. Monitor progress in the status log

DOWNLOADING TO OTHER PCS
-------------------------
To use on another PC:
1. Copy the entire "FasstVideo" folder
2. Transfer via USB drive, network share, or cloud storage
3. No additional installation needed on the target PC
4. Just run FasstVideo.exe

CHROME DRIVER
-------------
If you need browser automation features:
- The application will attempt to auto-install the Chrome driver
- Ensure Chrome browser is installed on your system
- Driver will be downloaded automatically on first use

TROUBLESHOOTING
---------------
If the application doesn't start:
- Make sure all files in the FasstVideo folder are intact
- Check that your antivirus isn't blocking the executable
- Try running as administrator (right-click > Run as administrator)

If downloads fail:
- Check your internet connection
- Ensure the video URL is valid and accessible
- Some protected content may not be downloadable
- Check the event logs for detailed error messages

If you see dependency errors:
- The app should auto-install missing dependencies
- Ensure you have internet connectivity
- Check Windows Event Viewer for Python-related errors

FOLDER STRUCTURE
----------------
FasstVideo/
  ├── FasstVideo.exe          (Main application)
  ├── _internal/              (Python runtime and dependencies)
  │   ├── Python DLLs
  │   ├── Required libraries
  │   └── Package files
  ├── Logo and image files
  └── Configuration files

FILE SIZE
---------
The complete package is approximately 400-600 MB due to:
- Python runtime environment
- Selenium and browser automation libraries
- yt-dlp and video processing libraries
- GUI libraries (tkinter, PIL)
- All dependencies bundled for portability

UPDATES
-------
To update FasstVideo:
1. Delete the old FasstVideo folder
2. Extract the new version
3. Your settings and downloads are stored separately and will be preserved

UNINSTALLATION
--------------
To remove FasstVideo:
1. Simply delete the FasstVideo folder
2. Optionally delete: C:\Users\[YourName]\.fasstvideo_settings.json
3. Optionally delete your downloads folder

LEGAL
-----
This software is provided for downloading content you have legal rights to access.
Users are responsible for complying with copyright laws and website terms of service.

By using this software, you agree to the terms presented in the legal disclaimer.

SUPPORT
-------
For issues, questions, or feature requests:
- Check the event logs in the application
- Review error messages in the status log
- Ensure you're using the latest version

BUILD INFORMATION
-----------------
- Built with PyInstaller 6.16.0
- Python 3.12.10
- Includes: selenium, requests, yt-dlp, PIL, tkinter, cryptography, psutil
- All dependencies are bundled (no external installation needed)

SECURITY
--------
- The executable is not signed (you may see Windows SmartScreen warning)
- Click "More info" > "Run anyway" if prompted
- This is normal for unsigned executables
- You can verify the contents by checking the source code

PRIVACY
-------
- No telemetry or data collection
- No internet communication except for downloading videos
- Settings stored locally only
- No user data is transmitted

========================================
Thank you for using FasstVideo!
========================================