# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import glob
import os

# Collect all image files
image_files = []
for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.ico']:
    for file in glob.glob(os.path.join('D:\\4k video downloader - Copy\\Best ASMR\\Downloader', ext)):
        if os.path.isfile(file):
            image_files.append((file, '.'))

a = Analysis(
    ['fasstvideo.py'],
    pathex=[],
    binaries=[],
    datas=image_files,
    hiddenimports=[
        'selenium',
        'selenium.webdriver',
        'selenium.webdriver.common.by',
        'selenium.webdriver.chrome.options',
        'selenium.webdriver.firefox.options',
        'selenium.webdriver.support.ui',
        'selenium.webdriver.support.expected_conditions',
        'requests',
        'urllib3',
        'certifi',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageDraw',
        'PIL.ImageFilter',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'cryptography',
        'psutil',
        'zlib',
        'marshal',
        'concurrent.futures',
        'queue',
        'threading',
        'subprocess',
        'json',
        'base64',
        'hashlib',
        'uuid',
        'tempfile',
        'webbrowser',
        'inspect',
        'ast',
        'math',
        'platform',
        'socket',
        'logging',
        'pathlib',
        'shutil',
        'glob',
        'traceback',
        'datetime',
        're',
        'urllib.request',
        'urllib.parse',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FasstVideo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to False to hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add path to .ico file if you have one
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FasstVideo',
)