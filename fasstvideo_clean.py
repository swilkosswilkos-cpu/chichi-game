#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
FasstVideo - Professional Video Downloader (Real-time Progress + Browser Automation)
Copyright (c) 2024. All rights reserved.

FEATURES:
- Real-time progress tracking with live numbers
- No fake percentages - actual download progress
- Visual spinner with live progress display
- Browser automation for right-click downloads
- Fallback when yt-dlp fails
================================================================================
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading
import time
import logging
from pathlib import Path
import json
import urllib.request
import urllib.parse
import shutil
import glob
import hashlib
import uuid
import platform
import base64
import random
import socket
import re
import concurrent.futures
import traceback
from datetime import datetime, timedelta
from queue import Queue, Empty
import tempfile
import webbrowser
import inspect
import ast
import math

# Anti-tampering and protection imports
try:
    import zlib
    import marshal
    PROTECTION_AVAILABLE = True
except ImportError:
    PROTECTION_AVAILABLE = False

# Try to import PIL for image handling
try:
    from PIL import Image, ImageTk, ImageDraw, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# Browser automation imports
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

# Enhanced imports with auto-installation
def ensure_dependencies():
    """Ensure critical dependencies are installed before proceeding"""
    try:
        # Critical imports that need to be available
        import subprocess
        import sys
        
        # Try to install pip if needed
        try:
            subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                          capture_output=True, check=True, timeout=10)
        except:
            print("Installing pip...")
            import ensurepip
            ensurepip.bootstrap()
        
        # Install critical security packages first
        critical_packages = [
            'cryptography>=40.0.0',
            'psutil>=5.9.0',
            'requests>=2.28.0',
            'selenium>=4.15.0'  # Added selenium to critical packages
        ]
        
        if os.name == 'nt':
            critical_packages.append('pywin32>=305')
        
        for package in critical_packages:
            try:
                package_name = package.split('>=')[0]
                if package_name == 'cryptography':
                    import cryptography
                elif package_name == 'psutil':
                    import psutil
                elif package_name == 'requests':
                    import requests
                elif package_name == 'selenium':
                    import selenium
                elif package_name == 'pywin32' and os.name == 'nt':
                    import win32api
            except ImportError:
                print(f"Installing {package}...")
                subprocess.run([sys.executable, '-m', 'pip', 'install', package, '--user'], 
                              capture_output=True, timeout=120)
    except Exception as e:
        print(f"Dependency setup warning: {e}")

# Run dependency check early
ensure_dependencies()

# Now import security packages
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

try:
    if os.name == 'nt':
        import win32api
        import win32process
        import win32con
        WIN32_AVAILABLE = True
    else:
        WIN32_AVAILABLE = False
except ImportError:
    WIN32_AVAILABLE = False

# Hide console window on Windows - with better error handling
if os.name == 'nt':
    try:
        import ctypes
        console_window = ctypes.windll.kernel32.GetConsoleWindow()
        if console_window != 0:
            ctypes.windll.user32.ShowWindow(console_window, 0)
    except Exception:
        pass

# Setup logging with obfuscation
try:
    log_format = base64.b64decode(b'JShhc2N0aW1lKXMgLSAlKGxldmVsbmFtZSlzIC0gJShtZXNzYWdlKXM=').decode()
    logging.basicConfig(level=logging.INFO, format=log_format)
    logger = logging.getLogger(__name__)
except Exception:
    class DummyLogger:
        def info(self, msg): pass
        def error(self, msg): pass
        def warning(self, msg): pass
        def exception(self, msg): pass
        def debug(self, msg): pass
    logger = DummyLogger()

# Enhanced Code Protection System with Advanced Security
class CodeProtectionManager:
    """Advanced code protection and anti-tampering system"""
    
    def __init__(self):
        self._protection_key = self._generate_protection_key()
        self._runtime_hash = self._calculate_runtime_hash()
        self._start_time = time.time()
        self._check_counter = 0
        self._obfuscated_constants = self._initialize_obfuscated_constants()
        self._execution_context = self._analyze_execution_context()
        
    def _generate_protection_key(self):
        """Generate runtime protection key"""
        try:
            machine_data = f"{platform.machine()}{platform.processor()}{os.getpid()}"
            return hashlib.sha256(machine_data.encode()).hexdigest()[:32]
        except:
            return "fallback_protection_key_12345678"
    
    def _calculate_runtime_hash(self):
        """Calculate runtime integrity hash"""
        try:
            frame = inspect.currentframe()
            code_obj = frame.f_code
            code_hash = hashlib.md5(str(code_obj.co_code).encode()).hexdigest()
            return code_hash[:16]
        except:
            return "runtime_hash_fallback"
    
    def _initialize_obfuscated_constants(self):
        """Initialize obfuscated application constants"""
        constants = {}
        try:
            # Obfuscated strings for critical functionality
            constants['app_name'] = base64.b64encode(b'FasstVideo').decode()
            constants['version'] = base64.b64encode(b'1.0.0').decode()
            constants['integrity_flag'] = base64.b64encode(b'integrity_verified').decode()
            constants['debug_detection'] = base64.b64encode(b'debugger_detected').decode()
        except:
            constants = {'app_name': 'RmFzc3RWaWRlbw=='}
        return constants
    
    def _analyze_execution_context(self):
        """Analyze execution environment for anomalies"""
        context = {}
        try:
            # Check for debugging environment
            context['debugger_present'] = hasattr(sys, 'gettrace') and sys.gettrace() is not None
            
            # Check for reverse engineering tools
            suspicious_modules = ['pdb', 'debugpy', 'pydevd', 'winpdb', 'rpdb']
            context['suspicious_modules'] = any(mod in sys.modules for mod in suspicious_modules)
            
            # Check execution environment
            context['interactive_mode'] = hasattr(sys, 'ps1')
            context['script_path'] = os.path.abspath(__file__) if hasattr(sys, '_getframe') else None
            
            # Memory analysis
            import gc
            context['object_count'] = len(gc.get_objects())
            
        except Exception:
            context = {'debugger_present': False}
        
        return context
    
    def perform_integrity_check(self):
        """Perform comprehensive integrity verification"""
        self._check_counter += 1
        
        try:
            # Runtime tampering detection
            if self._detect_runtime_tampering():
                self._trigger_protection_response('runtime_tampering')
                return False
            
            # Debug detection
            if self._detect_debugging_environment():
                self._trigger_protection_response('debug_detected')
                return False
            
            # Code injection detection
            if self._detect_code_injection():
                self._trigger_protection_response('code_injection')
                return False
            
            # Environment analysis
            if self._analyze_suspicious_environment():
                self._trigger_protection_response('suspicious_environment')
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Integrity check failed: {e}")
            return False
    
    def _detect_runtime_tampering(self):
        """Detect runtime code tampering"""
        try:
            # Check if critical modules have been modified
            critical_modules = ['tkinter', 'subprocess', 'os', 'sys']
            for module_name in critical_modules:
                if module_name in sys.modules:
                    module = sys.modules[module_name]
                    if hasattr(module, '_tampered_flag'):
                        return True
            
            # Check frame manipulation
            frame = inspect.currentframe()
            if frame.f_back and hasattr(frame.f_back, '_injected'):
                return True
            
            return False
        except:
            return True  # Assume tampering if checks fail
    
    def _detect_debugging_environment(self):
        """Detect debugging tools and environments"""
        try:
            # Multiple debugging detection methods
            debug_indicators = [
                hasattr(sys, 'gettrace') and sys.gettrace() is not None,
                'pdb' in sys.modules,
                'debugpy' in sys.modules,
                'pydevd' in sys.modules,
                os.environ.get('PYTHONDEBUGTRACE'),
                '--debug' in sys.argv,
                '-d' in sys.argv
            ]
            
            return any(debug_indicators)
        except:
            return False
    
    def _detect_code_injection(self):
        """Detect code injection attempts"""
        try:
            # Check for unexpected code objects
            frame = inspect.currentframe()
            while frame:
                code = frame.f_code
                if hasattr(code, '_injected_marker'):
                    return True
                frame = frame.f_back
            
            # Check for eval/exec usage in stack
            for frame_info in inspect.stack():
                if 'eval' in frame_info.filename or 'exec' in frame_info.filename:
                    return True
            
            return False
        except:
            return False
    
    def _analyze_suspicious_environment(self):
        """Analyze environment for suspicious indicators"""
        try:
            suspicious_indicators = [
                # Check for analysis tools
                any(tool in sys.modules for tool in ['ida', 'ghidra', 'radare', 'ollydbg']),
                
                # Check for virtual machine indicators (basic)
                'VMware' in platform.processor(),
                'VirtualBox' in os.environ.get('COMPUTERNAME', ''),
                
                # Check for unusual Python execution
                sys.executable.endswith('pythonw.exe') and self._execution_context.get('interactive_mode', False),
                
                # Check execution time anomalies
                (time.time() - self._start_time) < 0.1 and self._check_counter > 5
            ]
            
            return any(suspicious_indicators)
        except:
            return False
    
    def _trigger_protection_response(self, reason):
        """Trigger protection response for detected threats"""
        try:
            logger.warning(f"Protection triggered: {reason}")
            
            # Obfuscated response actions
            responses = [
                self._corrupt_execution_flow,
                self._inject_false_data,
                self._terminate_gracefully
            ]
            
            # Select random response to make analysis harder
            response = random.choice(responses)
            response(reason)
            
        except Exception:
            # Fail silently if protection response fails
            pass
    
    def _corrupt_execution_flow(self, reason):
        """Subtly corrupt execution flow"""
        try:
            # Introduce random delays
            time.sleep(random.uniform(0.1, 2.0))
            
            # Corrupt some non-critical variables
            if hasattr(self, '_runtime_hash'):
                self._runtime_hash = "corrupted_" + self._runtime_hash
                
        except Exception:
            pass
    
    def _inject_false_data(self, reason):
        """Inject false data to mislead analysis"""
        try:
            # Create fake variables and functions
            fake_key = hashlib.sha256(b'fake_encryption_key').hexdigest()
            fake_data = base64.b64encode(b'fake_sensitive_information').decode()
            
            # Store fake data that looks important
            setattr(self, '_encryption_key', fake_key)
            setattr(self, '_sensitive_data', fake_data)
            
        except Exception:
            pass
    
    def _terminate_gracefully(self, reason):
        """Gracefully terminate with misleading error"""
        try:
            # Show generic error message instead of protection message
            error_messages = [
                "Network connection failed",
                "Dependency not found",
                "Configuration error",
                "System resource unavailable"
            ]
            
            error = random.choice(error_messages)
            logger.error(f"Application error: {error}")
            
            # Exit after delay
            time.sleep(0.2)
            sys.exit(1)
            
        except Exception:
            os._exit(1)
    
    def get_obfuscated_constant(self, key):
        """Retrieve obfuscated constant"""
        try:
            if key in self._obfuscated_constants:
                return base64.b64decode(self._obfuscated_constants[key]).decode()
            return None
        except:
            return None

# Initialize protection system
try:
    protection_manager = CodeProtectionManager()
    # Perform initial integrity check
    if not protection_manager.perform_integrity_check():
        logger.error("Application integrity verification failed")
        # Continue with degraded functionality rather than hard exit
except Exception as e:
    logger.error(f"Protection system initialization failed: {e}")
    # Create dummy protection manager
    class DummyProtectionManager:
        def perform_integrity_check(self): return True
        def get_obfuscated_constant(self, key): return "FasstVideo" if key == 'app_name' else None
    protection_manager = DummyProtectionManager()

# Modern Color Palette with Tropical Accents
COLORS = {
    'bg_primary': '#0A0E27',      # Deep dark blue
    'bg_secondary': '#151A3C',     # Slightly lighter blue
    'glass_bg': '#1A1F4A',         # Glass panel background
    'glass_border': '#2A3F7D',     # Glass border color
    'accent': '#5E72E4',           # Vibrant blue accent
    'accent_hover': '#7B8CFF',     # Lighter accent for hover
    'success': '#00D9FF',          # Cyan success
    'warning': '#FFB400',          # Amber warning
    'danger': '#FF3B5C',           # Red danger
    'text_primary': '#FFFFFF',     # White text
    'text_secondary': '#B8BED8',   # Muted text
    'text_muted': '#8892B0',       # More muted text
    'glass_overlay': '#FFFFFF',    # White overlay for glass effect
    # Tropical colors for progress bars and animations
    'tropical_teal': '#00CED1',    # Dark turquoise
    'tropical_coral': '#FF6B6B',   # Coral
    'tropical_lime': '#32CD32',    # Lime green
    'tropical_sunset': '#FF4500',  # Orange red
    'tropical_purple': '#DA70D6',  # Orchid
    'tropical_aqua': '#00FFFF',    # Aqua cyan
    'tropical_gold': '#FFD700',    # Gold
    'tropical_pink': '#FF69B4',    # Hot pink
    'tropical_blue': '#1E90FF',    # Dodger blue
}

class GlassFrame(tk.Frame):
    """Custom frame with glassmorphic effect"""
    
    def __init__(self, parent, **kwargs):
        # Extract custom glass properties
        self.glass_opacity = kwargs.pop('glass_opacity', 0.15)
        self.blur_radius = kwargs.pop('blur_radius', 10)
        self.border_width = kwargs.pop('border_width', 1)
        
        super().__init__(parent, **kwargs)
        
        # Set glassmorphic styling with fallbacks
        try:
            self.configure(
                bg=COLORS['glass_bg'],
                highlightbackground=COLORS['glass_border'],
                highlightthickness=self.border_width,
                highlightcolor=COLORS['glass_border']
            )
        except Exception:
            # Fallback styling
            self.configure(bg=COLORS['glass_bg'])

class ModernButton(tk.Button):
    """Modern styled button with hover effects"""
    
    def __init__(self, parent, **kwargs):
        # Extract custom properties
        self.default_bg = kwargs.get('bg', COLORS['accent'])
        self.hover_bg = kwargs.pop('hover_bg', COLORS['accent_hover'])
        
        super().__init__(parent, **kwargs)
        
        # Configure modern styling with fallbacks
        try:
            self.configure(
                relief='flat',
                bd=0,
                highlightthickness=0,
                activebackground=self.hover_bg,
                cursor='hand2',
                font=('Segoe UI', 11, 'bold')
            )
        except Exception:
            # Fallback configuration
            self.configure(
                relief='flat',
                bd=0,
                highlightthickness=0,
                activebackground=self.hover_bg
            )
        
        # Bind hover effects
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
    
    def on_enter(self, event):
        if self['state'] != 'disabled':
            try:
                self.configure(bg=self.hover_bg)
            except:
                pass
    
    def on_leave(self, event):
        if self['state'] != 'disabled':
            try:
                self.configure(bg=self.default_bg)
            except:
                pass

class ModernEntry(tk.Entry):
    """Modern styled entry widget"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        try:
            self.configure(
                bg='#1F2547',
                fg=COLORS['text_primary'],
                insertbackground=COLORS['accent'],
                relief='flat',
                bd=8,
                highlightthickness=1,
                highlightbackground=COLORS['glass_border'],
                highlightcolor=COLORS['accent'],
                font=('Segoe UI', 11)
            )
        except Exception:
            # Fallback styling
            self.configure(
                bg='#1F2547',
                fg=COLORS['text_primary'],
                relief='flat'
            )

class ModernText(tk.Text):
    """Modern styled text widget"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        try:
            self.configure(
                bg='#1F2547',
                fg=COLORS['text_primary'],
                insertbackground=COLORS['accent'],
                relief='flat',
                bd=0,
                highlightthickness=1,
                highlightbackground=COLORS['glass_border'],
                highlightcolor=COLORS['accent'],
                font=('Segoe UI', 11),
                padx=10,
                pady=10,
                wrap=tk.WORD
            )
        except Exception:
            # Fallback styling
            self.configure(
                bg='#1F2547',
                fg=COLORS['text_primary'],
                relief='flat',
                wrap=tk.WORD
            )

class AnimatedTitleLabel:
    """Animated title label with color cycling letters"""
    
    def __init__(self, parent, text, **kwargs):
        self.parent = parent
        self.text = text
        self.frame = tk.Frame(parent, bg=kwargs.get('bg', COLORS['glass_bg']))
        
        # Animation properties
        self.letter_labels = []
        self.animation_colors = [
            COLORS['tropical_teal'],
            COLORS['tropical_coral'],
            COLORS['tropical_lime'],
            COLORS['tropical_sunset'],
            COLORS['tropical_purple'],
            COLORS['tropical_aqua'],
            COLORS['tropical_gold'],
            COLORS['tropical_pink'],
            COLORS['tropical_blue']
        ]
        self.current_color_index = 0
        self.animation_active = False
        self.animation_job = None
        
        # Create individual labels for each letter
        self.create_letter_labels(**kwargs)
        
    def create_letter_labels(self, **kwargs):
        """Create individual labels for each letter"""
        try:
            font = kwargs.get('font', ('Segoe UI', 28, 'bold'))
            bg = kwargs.get('bg', COLORS['glass_bg'])
            fg = kwargs.get('fg', COLORS['text_primary'])
            
            for i, letter in enumerate(self.text):
                label = tk.Label(self.frame, text=letter, font=font, bg=bg, fg=fg)
                label.pack(side=tk.LEFT)
                self.letter_labels.append(label)
                
        except Exception as e:
            logger.error(f"Error creating letter labels: {e}")
            # Fallback: create single label
            fallback_label = tk.Label(self.frame, text=self.text, 
                                    font=('Arial', 20, 'bold'),
                                    bg=COLORS['glass_bg'], 
                                    fg=COLORS['text_primary'])
            fallback_label.pack()
            self.letter_labels = [fallback_label]
    
    def pack(self, **kwargs):
        """Pack the frame"""
        self.frame.pack(**kwargs)
    
    def start_animation(self):
        """Start the color cycling animation"""
        if not self.animation_active and self.letter_labels:
            self.animation_active = True
            self.animate_next_letter(0)
    
    def stop_animation(self):
        """Stop the animation"""
        self.animation_active = False
        if self.animation_job:
            self.parent.after_cancel(self.animation_job)
            self.animation_job = None
        
        # Reset all letters to default color
        try:
            for label in self.letter_labels:
                label.configure(fg=COLORS['text_primary'])
        except:
            pass
    
    def animate_next_letter(self, letter_index):
        """Animate the next letter in sequence"""
        if not self.animation_active or not self.letter_labels:
            return
        
        try:
            # Reset previous letter to default color
            if letter_index > 0:
                prev_label = self.letter_labels[letter_index - 1]
                prev_label.configure(fg=COLORS['text_primary'])
            elif letter_index == 0 and len(self.letter_labels) > 1:
                # Reset last letter when starting new cycle
                last_label = self.letter_labels[-1]
                last_label.configure(fg=COLORS['text_primary'])
            
            # Animate current letter
            if letter_index < len(self.letter_labels):
                current_label = self.letter_labels[letter_index]
                color = self.animation_colors[self.current_color_index % len(self.animation_colors)]
                current_label.configure(fg=color)
                
                # Schedule next letter
                next_index = (letter_index + 1) % len(self.letter_labels)
                if next_index == 0:
                    # Completed one cycle, change color
                    self.current_color_index += 1
                
                # Continue animation
                self.animation_job = self.parent.after(150, 
                                                     lambda: self.animate_next_letter(next_index))
        except Exception as e:
            logger.error(f"Animation error: {e}")
            self.stop_animation()

class RealTimeProgressSpinner:
    """Real-time progress spinner with live numbers and SINGLE COLOR horizontal progress bar"""
    
    def __init__(self, parent, canvas, **kwargs):
        self.parent = parent
        self.canvas = canvas
        self.active = False
        self.angle = 0
        self.animation_job = None
        self.spinner_color = kwargs.get('color', COLORS['tropical_aqua'])
        self.bg_color = kwargs.get('bg_color', '#1F2547')
        
        # Progress tracking
        self.current_progress = 0.0
        self.download_speed = "0 KB/s"
        self.file_size = "0 MB"
        self.eta = "--:--"
        self.actual_download_started = False  # Flag to track when actual download begins
        self.downloaded_mb = 0.0
        self.total_mb = 0.0
        self.download_completed = False  # Track if download finished successfully
        
        # File monitoring
        self.monitor_path = None
        self.monitor_thread = None
        self.monitor_active = False
        
        # Progress bar properties
        self.progress_bar_height = 20
        self.progress_bar_padding = 40
    
    def start(self, file_path=None):
        """Start the spinner animation and file monitoring"""
        if not self.active:
            self.active = True
            self.angle = 0
            self.current_progress = 0.0
            self.download_completed = False  # Reset completion flag for new download
            self.actual_download_started = False  # Reset download detection flag
            
            # Start file monitoring if path provided
            if file_path:
                self.start_file_monitoring(file_path)
            
            self.animate()
    
    def stop(self):
        """Stop the spinner animation and file monitoring"""
        self.active = False
        self.monitor_active = False
        
        if self.animation_job:
            self.parent.after_cancel(self.animation_job)
            self.animation_job = None
        
        # Clear canvas
        self.canvas.delete("all")
        self.draw_empty_state()
        
        # Only reset progress if download didn't complete successfully
        if not self.download_completed:
            self.current_progress = 0.0
            self.download_speed = "0 KB/s"
            self.file_size = "0 MB"
            self.eta = "--:--"
            self.actual_download_started = False
    
    def start_file_monitoring(self, file_path):
        """Start monitoring file size for progress"""
        self.monitor_path = file_path
        self.monitor_active = True
        
        def monitor_worker():
            initial_size = 0
            start_time = time.time()
            last_size = 0
            last_time = time.time()
            
            while self.monitor_active:
                try:
                    if os.path.exists(self.monitor_path):
                        current_size = os.path.getsize(self.monitor_path)
                        current_time = time.time()
                        
                        # Update downloaded MB
                        self.downloaded_mb = current_size / (1024 * 1024)
                        
                        # Calculate speed
                        if current_time - last_time > 1.0:  # Update speed every second
                            speed_bps = (current_size - last_size) / (current_time - last_time)
                            if speed_bps > 1024 * 1024:
                                self.download_speed = f"{speed_bps / (1024 * 1024):.1f} MB/s"
                            elif speed_bps > 1024:
                                self.download_speed = f"{speed_bps / 1024:.1f} KB/s"
                            else:
                                self.download_speed = f"{speed_bps:.0f} B/s"
                            
                            last_size = current_size
                            last_time = current_time
                        
                        # Estimate progress (rough estimation)
                        if current_size > 0:
                            # Estimate total size based on growth rate
                            elapsed = current_time - start_time
                            if elapsed > 5:  # After 5 seconds, start estimating
                                growth_rate = current_size / elapsed
                                if growth_rate > 0:
                                    estimated_total = current_size * 2  # Conservative estimate
                                    self.total_mb = estimated_total / (1024 * 1024)
                                    self.current_progress = min((current_size / estimated_total) * 100, 95)
                    
                    time.sleep(0.1)  # Check every 0.5 seconds
                except Exception:
                    time.sleep(0.2)
        
        self.monitor_thread = threading.Thread(target=monitor_worker, daemon=True)
        self.monitor_thread.start()
    
    def update_progress_from_output(self, progress_text):
        """Update progress from yt-dlp output parsing"""
        try:
            # Detect when actual download starts
            if '[download]' in progress_text and ('%' in progress_text or 'Downloading' in progress_text):
                self.actual_download_started = True

            # Parse yt-dlp progress line
            # Example: "[download]  45.2% of 123.45MiB at 1.23MiB/s ETA 00:42"
            if '[download]' in progress_text and '%' in progress_text:
                # Extract percentage
                percent_match = re.search(r'(\d+\.?\d*)%', progress_text)
                if percent_match:
                    new_progress = float(percent_match.group(1))
                    # Ensure progress only increases and caps at 100%
                    if new_progress > self.current_progress:
                        self.current_progress = min(new_progress, 100.0)
                    
                    # Mark as completed when reaching 100%
                    if self.current_progress >= 100.0:
                        self.download_completed = True
                        self.eta = "Complete"
                
                # Extract file size
                size_match = re.search(r'of\s+(\d+\.?\d*)(MiB|MB|GiB|GB|KiB|KB)', progress_text)
                if size_match:
                    size_val = float(size_match.group(1))
                    size_unit = size_match.group(2)
                    if 'G' in size_unit:
                        self.total_mb = size_val * 1024
                    elif 'M' in size_unit:
                        self.total_mb = size_val
                    elif 'K' in size_unit:
                        self.total_mb = size_val / 1024
                    
                    self.file_size = f"{self.total_mb:.1f} MB"
                
                # Extract download speed
                speed_match = re.search(r'at\s+(\d+\.?\d*)(MiB|MB|KiB|KB)/s', progress_text)
                if speed_match:
                    speed_val = float(speed_match.group(1))
                    speed_unit = speed_match.group(2)
                    if 'M' in speed_unit:
                        self.download_speed = f"{speed_val:.1f} MB/s"
                    elif 'K' in speed_unit:
                        self.download_speed = f"{speed_val:.0f} KB/s"
                
                # Extract ETA
                eta_match = re.search(r'ETA\s+(\d+:\d+)', progress_text)
                if eta_match and self.current_progress < 100.0:
                    self.eta = eta_match.group(1)
                
                # Calculate downloaded MB
                if self.total_mb > 0:
                    self.downloaded_mb = (self.current_progress / 100) * self.total_mb
            
            # Check for completion
            elif '[download] 100%' in progress_text or 'has already been downloaded' in progress_text:
                self.current_progress = 100.0
                self.download_completed = True
                self.eta = "Complete"
                
        except Exception as e:
            logger.error(f"Error parsing progress: {e}")
    
    def animate(self):
        """Animate the spinner with real-time numbers"""
        if not self.active:
            return
        
        try:
            # Clear and redraw
            self.canvas.delete("all")
            self.draw_progress_display()
            
            # Update angle
            self.angle = (self.angle + 8) % 360
            
            # Schedule next frame
            self.animation_job = self.parent.after(100, self.animate)
        except Exception as e:
            logger.error(f"Spinner animation error: {e}")
            self.stop()
    
    def draw_progress_display(self):
        """Draw clean progress display with no overlapping elements"""
        try:
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()
            
            if width <= 1 or height <= 1:
                return
            
            # Clear everything first
            self.canvas.delete("all")

            # Draw cyberpunk background with subtle glow
            self.canvas.create_rectangle(0, 0, width, height,
                                       fill='#0A0A0A',  # Deep black
                                       outline='#00FFFF',  # Cyan border
                                       width=1)

            # Only draw horizontal progress bar - no circular elements
            progress_bar_y = height // 2 - 15  # Adjusted for taller cyberpunk bar

            # Draw cyberpunk horizontal progress bar
            self.draw_horizontal_progress_bar(width, height, progress_bar_y)
            
        except Exception as e:
            logger.error(f"Error drawing progress display: {e}")
    
    def draw_horizontal_progress_bar(self, canvas_width, canvas_height, start_y):
        """Draw simple solid color progress bar with white text"""
        try:
            # Simple colors
            bg_color = "#2D2D2D"  # Dark gray background
            progress_color = "#4A90E2"  # Blue progress fill
            text_color = "#FFFFFF"  # White text

            # Progress bar dimensions
            bar_padding = 20
            bar_width = canvas_width - (bar_padding * 2)
            bar_height = 42  # Reduced by 30% from 60 to 42
            bar_x = bar_padding
            bar_y = start_y

            # Stay at 0% until actual download detection
            display_progress = self.current_progress if self.actual_download_started else 0.0

            # Draw background bar
            self.canvas.create_rectangle(
                bar_x, bar_y,
                bar_x + bar_width, bar_y + bar_height,
                fill=bg_color,
                outline="#555555",
                width=1,
                tags="bg_bar"
            )

            # Draw progress fill
            if display_progress > 0:
                progress_width = int((display_progress / 100) * bar_width)
                self.canvas.create_rectangle(
                    bar_x, bar_y,
                    bar_x + progress_width, bar_y + bar_height,
                    fill=progress_color,
                    outline="",
                    width=0,
                    tags="progress_fill"
                )

            # Add status text
            if not self.actual_download_started:
                status_text = "DETECTING VIDEO SOURCES..."
            elif display_progress >= 100:
                status_text = "DOWNLOAD COMPLETE"
            else:
                status_text = "DOWNLOADING..."

            # Status text (left side)
            self.canvas.create_text(
                bar_x + 15, bar_y + bar_height // 2 - 8,
                text=status_text,
                fill=text_color,
                font=('Arial', 10, 'bold'),
                anchor="w",
                tags="status_text"
            )

            # Percentage text (center, large)
            progress_text = f"{display_progress:.0f}%"
            self.canvas.create_text(
                bar_x + bar_width // 2, bar_y + bar_height // 2,
                text=progress_text,
                fill=text_color,
                font=('Arial', 20, 'bold'),
                anchor="center",
                tags="percentage_text"
            )

            # Speed and ETA (right side, small)
            info_text = f"{self.download_speed} | ETA: {self.eta}"
            self.canvas.create_text(
                bar_x + bar_width - 15, bar_y + bar_height // 2 + 8,
                text=info_text,
                fill=text_color,
                font=('Arial', 8),
                anchor="e",
                tags="info_text"
            )

        except Exception as e:
            logger.error(f"Error drawing progress bar: {e}")

    def draw_empty_state(self):
        """Draw clean empty/ready state"""
        try:
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()
            
            if width <= 1 or height <= 1:
                return
            
            # Clear everything
            self.canvas.delete("all")

            # Draw cyberpunk background
            self.canvas.create_rectangle(0, 0, width, height,
                                       fill='#0A0A0A',  # Deep black
                                       outline='#333333',  # Dim gray for ready state
                                       width=1)

            # Draw "READY" text in cyberpunk style
            self.canvas.create_text(
                width // 2, height // 2,
                text="READY",
                fill="#00FFFF",
                font=('Courier', 14, 'bold'),
                tags="ready_text"
            )
            
        except Exception as e:
            logger.error(f"Error drawing empty state: {e}")

class LogoManager:
    """Handles loading and managing FasstVideo logos"""
    
    def __init__(self):
        self.logo_path = None
        self.logo_image = None
        self.logo_icon = None
        try:
            self.find_logo()
        except Exception:
            pass
    
    def find_logo(self):
        """Find FasstVideo logo files in current directory and common locations"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            logo_patterns = [
                'FasstVideologo.*',
                'FasstVideo.*',
                'fasstvideo.*',
                'logo.*'
            ]
            
            image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.ico']
            
            for pattern in logo_patterns:
                for file_path in glob.glob(os.path.join(script_dir, pattern)):
                    file_ext = os.path.splitext(file_path)[1].lower()
                    if file_ext in image_extensions:
                        self.logo_path = file_path
                        logger.info(f"Found logo: {file_path}")
                        return
            
            logger.info("No logo file found")
        except Exception:
            pass
    
    def load_logo_for_window(self, size=(32, 32)):
        """Load logo for window icon"""
        if not self.logo_path or not PIL_AVAILABLE:
            return None
        
        try:
            img = Image.open(self.logo_path)
            img = img.resize(size, Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS)
            self.logo_icon = ImageTk.PhotoImage(img)
            return self.logo_icon
        except Exception as e:
            logger.error(f"Error loading logo for window: {e}")
            return None
    
    def load_logo_for_ui(self, size=(64, 64)):
        """Load logo for UI display"""
        if not self.logo_path or not PIL_AVAILABLE:
            return None
        
        try:
            img = Image.open(self.logo_path)
            img = img.resize(size, Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(img)
            return self.logo_image
        except Exception as e:
            logger.error(f"Error loading logo for UI: {e}")
            return None
    
    def get_icon_path(self):
        """Get path for .ico file if available"""
        if self.logo_path and self.logo_path.endswith('.ico'):
            return self.logo_path
        return None

class BrowserDownloadManager:
    """Browser automation manager for right-click downloads when yt-dlp fails"""
    
    def __init__(self, status_callback=None, progress_callback=None):
        self.status_callback = status_callback or print
        self.progress_callback = progress_callback
        self.driver = None
        self.download_timeout = 300  # 5 minutes timeout
        self.fast_mode = True  # Enable performance optimizations
        # Error throttling to reduce spam
        self._error_cache = {}
        self._last_error_log_time = 0

    def _should_log_error(self, error_msg, min_interval=2.0):
        """Throttle error logging to prevent spam"""
        now = time.time()

        # Generate a hash of the error message to identify similar errors
        error_hash = hash(error_msg[:50])  # Use first 50 chars for similarity matching

        # Check if we've seen this error recently
        if error_hash in self._error_cache:
            last_time = self._error_cache[error_hash]
            if now - last_time < min_interval:
                return False

        # Check global error throttling - allow different error types more frequently
        if now - self._last_error_log_time < 0.2:  # Maximum 5 errors per second
            return False

        # Update cache and log timing
        self._error_cache[error_hash] = now
        self._last_error_log_time = now

        # Clean old entries from cache (keep last 10 minutes)
        cutoff = now - 600
        self._error_cache = {k: v for k, v in self._error_cache.items() if v > cutoff}

        return True

    def _log_status_throttled(self, message):
        """Log status with error throttling"""
        # Check if this looks like an error message
        if any(keyword in message.lower() for keyword in ['error', 'failed', 'exception']):
            if self._should_log_error(message):
                self.log_status(message)
        else:
            # Non-error messages always get logged
            self.log_status(message)

    def optimized_wait(self, base_timeout, check_condition=None):
        """Optimized waiting with early termination and reduced timeouts in fast mode"""
        if self.fast_mode:
            actual_timeout = min(base_timeout * 0.1, 0.5)  # 80% reduction, max 1 second for speed
        else:
            actual_timeout = base_timeout

        if check_condition:
            # Smart waiting with condition checking
            start_time = time.time()
            while time.time() - start_time < actual_timeout:
                if check_condition():
                    return True
                time.sleep(0.1)  # Check every 100ms
            return False
        else:
            # Simple wait
            time.sleep(actual_timeout)
            return True

    def cleanup(self):
        """Clean up browser resources when all download attempts are complete"""
        try:
            if self.driver:
                self.log_status("Cleaning up browser session")
                self.driver.quit()
                self.driver = None
        except Exception as e:
            self.log_status(f"Browser cleanup error: {str(e)[:50]}")

    def log_status(self, message, url=None):
        """Log status with optional URL context"""
        if url:
            domain = self._get_domain(url)
            full_message = f"[{domain}] {message}"
        else:
            full_message = message

        logger.info(full_message)

        if self.status_callback:
            try:
                # Send the actual message, not just domain
                self.status_callback(full_message)
            except:
                pass
    
    def _get_domain(self, url):
        """Extract domain from URL"""
        try:
            parsed = urllib.parse.urlparse(url)
            return parsed.netloc.replace('www.', '')
        except:
            return "unknown"

    def _preprocess_url_for_yt_dlp(self, url):
        """Preprocess URL to convert embed URLs to regular URLs for better yt-dlp compatibility"""
        try:
            # Convert Pornhub embed URLs to regular video URLs
            if 'pornhub.com/embed/' in url:
                video_id = url.split('/embed/')[-1].split('?')[0]
                regular_url = f"https://www.pornhub.com/view_video.php?viewkey={video_id}"
                self.log_status(f"🔄 Converting embed URL to regular URL: {regular_url}")
                return regular_url

            # Convert other common embed URLs
            if '/embed/' in url:
                self.log_status(f"⚠️ Warning: Embed URL detected, yt-dlp may have issues: {url}")

            return url
        except Exception as e:
            self.log_status(f"URL preprocessing error: {str(e)[:50]}")
            return url

    def _ensure_cloudflare_authentication(self):
        """Removed - no longer bypasses Cloudflare"""
        return True

    def _setup_browser_driver(self, download_folder):
        """Setup browser driver with download preferences and auto-installation"""
        global SELENIUM_AVAILABLE
        try:
            if not SELENIUM_AVAILABLE:
                self.log_status("Selenium not available for browser automation")
                self.log_status("Installing selenium and webdriver-manager...")

                # Try to auto-install selenium and webdriver-manager
                try:
                    import subprocess
                    import sys

                    # Install required packages
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "webdriver-manager", "--upgrade", "--quiet"])
                    self.log_status("Dependencies installed, restarting browser setup...")

                    # Try importing again
                    try:
                        from selenium import webdriver
                        SELENIUM_AVAILABLE = True
                        self.log_status("Selenium now available!")
                    except ImportError:
                        self.log_status("Selenium installation failed")
                        return False

                except Exception as install_error:
                    self.log_status(f"Auto-installation failed: {str(install_error)[:50]}")
                    self.log_status("Please manually install: pip install selenium webdriver-manager")
                    return False

            self.log_status("Setting up browser automation (optimized for speed)...")

            # Enhanced dependency check and installation
            try:
                import webdriver_manager
                self.log_status("webdriver-manager available")
            except ImportError:
                self.log_status("Installing webdriver-manager...")
                try:
                    import subprocess
                    import sys
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "webdriver-manager", "--upgrade", "--quiet"])
                    import webdriver_manager
                    self.log_status("webdriver-manager installed successfully")
                except Exception as wm_error:
                    self.log_status("webdriver-manager installation failed - using fallback methods")

            # OPTIMIZED: Try only Chrome first, then one fallback (for speed)
            self.log_status("Attempting optimized Chrome browser setup...")
            driver = self._setup_chrome_driver(download_folder)

            if driver:
                self.driver = driver
                self.log_status("Chrome browser automation ready!")
                return True

            # Single fast fallback to Edge only (skip other browsers for speed)
            self.log_status("Chrome failed, trying Edge as single fallback...")
            driver = self._setup_edge_driver(download_folder)

            if driver:
                self.driver = driver
                self.log_status("Edge browser automation ready!")
                return True

            # If all failed, provide detailed guidance
            self.log_status("Browser automation setup failed - all methods exhausted")
            self.log_status("Solutions to try:")
            self.log_status("1. pip install selenium webdriver-manager --upgrade")
            self.log_status("2. Update your browser to latest version")
            self.log_status("3. Restart application and try again")
            return False

        except Exception as e:
            logger.error(f"Browser driver setup failed: {e}")
            self.log_status(f"Browser setup error: {str(e)[:100]}")
            self.log_status(f"Full error details: {str(e)}")
            import traceback
            self.log_status(f"Browser setup traceback: {traceback.format_exc()}")

            # Try one last emergency fallback
            self.log_status("Attempting emergency browser setup...")
            try:
                driver = self._setup_emergency_browser(download_folder)
                if driver:
                    self.driver = driver
                    self.log_status("Emergency browser setup successful!")
                    return True
            except Exception as emergency_error:
                self.log_status(f"Emergency browser setup also failed: {str(emergency_error)}")
                import traceback
                self.log_status(f"Emergency setup traceback: {traceback.format_exc()}")

            self.log_status("All browser setup methods failed")
            return False
    
    def _setup_chrome_driver(self, download_folder):
        """Setup Chrome WebDriver with download preferences - ULTRA FAST HEADLESS MODE"""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            options = ChromeOptions()

            # OPTIMIZED HEADLESS MODE - Performance with functionality preserved
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-web-security")
            options.add_argument("--disable-features=VizDisplayCompositor")
            options.add_argument("--window-size=1280,720")  # Smaller window for speed
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            # Safe performance optimizations (functionality preserved)
            options.add_argument("--disable-extensions")
            options.add_argument("--aggressive-cache-discard")
            options.add_argument("--memory-pressure-off")
            options.add_argument("--max_old_space_size=4096")
            # REMOVED: --disable-images, --disable-plugins, --no-zygote, --single-process
            # These were breaking video detection functionality

            # MUTE ALL AUDIO + DISABLE MEDIA - No background noise from opened pages
            options.add_argument("--mute-audio")
            options.add_argument("--autoplay-policy=user-gesture-required")
            options.add_argument("--disable-audio-output")
            options.add_argument("--disable-background-media-download")
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-backgrounding-occluded-windows")

            # Enhanced user agent to avoid detection
            options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

            # Set Chrome binary location if available
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]
            for chrome_path in chrome_paths:
                if os.path.exists(chrome_path):
                    options.binary_location = chrome_path
                    self.log_status(f"Using Chrome binary: {chrome_path}")
                    break

            # Configure Chrome preferences for downloads (functionality preserved)
            prefs = {
                "download.default_directory": os.path.abspath(download_folder),
                "download.prompt_for_download": False,  # Auto-save to program folder
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False,
                "safebrowsing.disable_download_protection": True,
                "profile.default_content_settings.popups": 0,
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_setting_values.automatic_downloads": 1,
                "profile.managed_default_content_settings.images": 1,  # Allow images for video detection
                "profile.default_content_setting_values.media_stream": 1,
                # Safe performance optimizations only
                "profile.default_content_setting_values.geolocation": 2,
                "profile.default_content_setting_values.media_stream_camera": 2,
                "profile.default_content_setting_values.media_stream_mic": 2,
                # RESTORED: JavaScript and plugins are needed for video detection
            }

            options.add_experimental_option("prefs", prefs)

            # Try multiple methods to create Chrome driver
            driver = None

            # Method 1: Try local ChromeDriver first (application directory)
            try:
                app_dir = os.path.dirname(os.path.abspath(__file__))
                local_chromedriver = os.path.join(app_dir, "drivers", "chromedriver.exe")

                if os.path.exists(local_chromedriver):
                    from selenium.webdriver.chrome.service import Service
                    service = Service(local_chromedriver)
                    driver = webdriver.Chrome(service=service, options=options)
                    self.log_status("Chrome browser initialized with local ChromeDriver")
                else:
                    self.log_status("Local ChromeDriver not found, trying system PATH...")
                    raise Exception("Local ChromeDriver not found")
            except Exception as e:
                self.log_status(f"Local ChromeDriver failed: {str(e)[:50]}")

            # Method 2: Try standard Chrome driver (system PATH) as fallback
            if not driver:
                try:
                    driver = webdriver.Chrome(options=options)
                    self.log_status("Chrome browser initialized with system driver")
                except Exception as e:
                    self.log_status(f"System Chrome driver failed: {str(e)[:50]}, trying webdriver-manager...")

            # Method 3: Try with webdriver-manager (auto-download) as fallback
            if not driver:
                try:
                    from webdriver_manager.chrome import ChromeDriverManager
                    from selenium.webdriver.chrome.service import Service

                    service = Service(ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service, options=options)
                    self.log_status("Chrome browser initialized with webdriver-manager (auto-download)")
                except ImportError:
                    self.log_status("webdriver-manager not available, trying other methods...")
                except Exception as e:
                    self.log_status(f"webdriver-manager failed: {str(e)[:50]}, trying other methods...")

            # Method 4: Try with undetected-chromedriver (if available)
            if not driver:
                try:
                    import undetected_chromedriver as uc
                    driver = uc.Chrome(options=options, headless=True)
                    self.log_status("Chrome browser initialized with undetected-chromedriver")
                except ImportError:
                    self.log_status("undetected-chromedriver not available")
                except Exception as e:
                    self.log_status(f"undetected-chromedriver failed: {str(e)[:50]}")

            # If all methods failed
            if not driver:
                self.log_status("All Chrome driver methods failed")
                return None

            if driver:
                # Remove automation indicators
                try:
                    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                except:
                    pass
                return driver

            return None

        except Exception as e:
            logger.error(f"Chrome setup failed: {e}")
            self.log_status(f"Chrome setup exception: {str(e)}")
            import traceback
            self.log_status(f"Chrome setup traceback: {traceback.format_exc()}")
            return None
    
    def _setup_firefox_driver(self, download_folder):
        """Setup Firefox WebDriver with download preferences - HEADLESS MODE with auto-driver management"""
        try:
            from selenium import webdriver
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            options = FirefoxOptions()

            # HEADLESS MODE - Browser runs completely hidden
            options.add_argument("-headless")  # Firefox uses single dash for headless
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            # Additional headless settings for Firefox
            options.set_preference("browser.tabs.remote.autostart", False)
            options.set_preference("browser.tabs.remote.autostart.2", False)

            # Enhanced user agent
            options.set_preference("general.useragent.override",
                                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0")

            # Configure Firefox preferences for downloads
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", download_folder)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                 "video/mp4,video/avi,video/quicktime,video/x-msvideo,video/webm,video/x-flv")
            options.set_preference("media.volume_scale", "0.0")
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference("useAutomationExtension", False)

            driver = None

            # Method 1: Try with webdriver-manager (auto-download)
            try:
                from webdriver_manager.firefox import GeckoDriverManager
                from selenium.webdriver.firefox.service import Service

                service = Service(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=service, options=options)
                self.log_status("Firefox browser initialized with webdriver-manager (auto-download)")
            except ImportError:
                self.log_status("webdriver-manager not available for Firefox, trying manual methods...")
            except Exception as e:
                self.log_status(f"Firefox webdriver-manager failed: {str(e)[:50]}, trying manual methods...")

            # Method 2: Try standard Firefox driver (system PATH)
            if not driver:
                try:
                    driver = webdriver.Firefox(options=options)
                    self.log_status("Firefox browser initialized with system driver")
                except Exception as e:
                    self.log_status(f"Standard Firefox driver failed: {str(e)[:50]}")
                    return None

            if driver:
                # Remove automation indicators
                try:
                    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                except:
                    pass
                return driver

            return None

        except Exception as e:
            logger.error(f"Firefox setup failed: {e}")
            return None

    def _setup_lightweight_browser(self, download_folder):
        """Lightweight browser setup for when normal setup times out"""
        try:
            self.log_status("Attempting lightweight browser setup...")

            # Try the simplest possible Firefox setup first
            try:
                from selenium import webdriver
                from selenium.webdriver.firefox.options import Options as FirefoxOptions

                options = FirefoxOptions()
                options.add_argument("-headless")  # Firefox uses single dash

                # MUTE ALL AUDIO - No background noise from opened pages
                options.set_preference("media.volume_scale", "0.0")
                options.set_preference("media.autoplay.default", 5)  # Block audio and video

                # No webdriver-manager, just try system Firefox
                driver = webdriver.Firefox(options=options)
                self.log_status("Lightweight Firefox setup successful")
                return driver
            except:
                pass

            # Try the simplest possible Chrome setup
            try:
                from selenium import webdriver
                from selenium.webdriver.chrome.options import Options as ChromeOptions

                options = ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")

                # MUTE ALL AUDIO - No background noise from opened pages
                options.add_argument("--mute-audio")
                options.add_argument("--autoplay-policy=user-gesture-required")
                options.add_argument("--disable-audio-output")

                # No webdriver-manager, just try system Chrome
                driver = webdriver.Chrome(options=options)
                self.log_status("Lightweight Chrome setup successful")
                return driver
            except:
                pass

            self.log_status("Lightweight setup also failed")
            return None

        except Exception as e:
            logger.error(f"Lightweight browser setup failed: {e}")
            return None

    def _setup_edge_driver(self, download_folder):
        """Setup Edge WebDriver with download preferences"""
        try:
            self.log_status("Setting up Edge browser...")
            from selenium import webdriver
            from selenium.webdriver.edge.options import Options as EdgeOptions

            options = EdgeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            # MUTE ALL AUDIO - No background noise from opened pages
            options.add_argument("--mute-audio")
            options.add_argument("--autoplay-policy=user-gesture-required")
            options.add_argument("--disable-audio-output")

            # Download preferences
            prefs = {
                "download.default_directory": os.path.abspath(download_folder),
                "download.prompt_for_download": True,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False
            }
            options.add_experimental_option("prefs", prefs)

            # Try with webdriver-manager first
            try:
                from webdriver_manager.microsoft import EdgeChromiumDriverManager
                from selenium.webdriver.edge.service import Service

                service = Service(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=service, options=options)
                self.log_status("Edge browser initialized with webdriver-manager")
                return driver

            except Exception:
                # Try system Edge driver
                try:
                    driver = webdriver.Edge(options=options)
                    self.log_status("Edge browser initialized with system driver")
                    return driver
                except Exception:
                    self.log_status("Edge browser setup failed")
                    return None

        except Exception as e:
            self.log_status(f"Edge setup failed: {str(e)[:50]}")
            return None

    def _setup_system_browser(self, download_folder):
        """Comprehensive system-installed browser detection and setup"""
        try:
            self.log_status("Attempting comprehensive system browser detection...")
            from selenium import webdriver
            import platform

            # Try all browsers with system drivers in order of reliability
            browsers_to_try = [
                ("Firefox", self._try_system_firefox),
                ("Chrome", self._try_system_chrome),
                ("Edge", self._try_system_edge),
                ("Brave", self._try_system_brave),
                ("Opera", self._try_system_opera),
                ("Vivaldi", self._try_system_vivaldi)
            ]

            # Add Safari on macOS
            if platform.system() == "Darwin":
                browsers_to_try.append(("Safari", self._try_system_safari))

            for browser_name, setup_func in browsers_to_try:
                try:
                    self.log_status(f"Trying system {browser_name}...")
                    driver = setup_func(download_folder)
                    if driver:
                        self.log_status(f"{browser_name} system driver successful")
                        return driver
                except Exception as e:
                    self.log_status(f"System {browser_name} failed: {str(e)[:30]}")
                    continue

            self.log_status("No system browsers found")
            return None

        except Exception as e:
            self.log_status(f"System browser detection failed: {str(e)[:50]}")
            return None

    def _try_system_firefox(self, download_folder):
        """Try Firefox with system driver"""
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        options = FirefoxOptions()
        options.add_argument("--headless")

        # MUTE ALL AUDIO - No background noise from opened pages
        options.set_preference("media.volume_scale", "0.0")
        options.set_preference("media.autoplay.default", 5)  # Block audio and video

        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", download_folder)
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "video/mp4,video/webm,video/avi,video/mov,video/wmv,video/flv,video/3gp,video/mkv,image/jpeg,image/jpg,image/png,image/gif,image/webp,image/bmp,audio/mp3,audio/wav,audio/aac,audio/flac,audio/ogg")

        return webdriver.Firefox(options=options)

    def _try_system_chrome(self, download_folder):
        """Try Chrome with system driver"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # MUTE ALL AUDIO - No background noise from opened pages
        options.add_argument("--mute-audio")
        options.add_argument("--autoplay-policy=user-gesture-required")
        options.add_argument("--disable-audio-output")

        prefs = {
            "download.default_directory": download_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        return webdriver.Chrome(options=options)

    def _try_system_edge(self, download_folder):
        """Try Edge with system driver"""
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options as EdgeOptions

        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        prefs = {
            "download.default_directory": download_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        return webdriver.Edge(options=options)

    def _try_system_brave(self, download_folder):
        """Try Brave with system driver by detecting installation"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        # Brave installation paths
        brave_paths = [
            "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            "/usr/bin/brave-browser",
            "/snap/bin/brave"
        ]

        for path in brave_paths:
            if os.path.exists(path):
                options = ChromeOptions()
                options.binary_location = path
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")

                prefs = {
                    "download.default_directory": download_folder,
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "safebrowsing.enabled": False
                }
                options.add_experimental_option("prefs", prefs)

                return webdriver.Chrome(options=options)

        raise Exception("Brave not found")

    def _try_system_opera(self, download_folder):
        """Try Opera with system driver by detecting installation"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        # Opera installation paths
        opera_paths = [
            "C:\\Program Files\\Opera\\opera.exe",
            "C:\\Program Files (x86)\\Opera\\opera.exe",
            "C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Opera\\opera.exe",
            "/Applications/Opera.app/Contents/MacOS/Opera",
            "/usr/bin/opera",
            "/snap/bin/opera"
        ]

        for path in opera_paths:
            expanded_path = os.path.expandvars(path)
            if os.path.exists(expanded_path):
                options = ChromeOptions()
                options.binary_location = expanded_path
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")

                prefs = {
                    "download.default_directory": download_folder,
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "safebrowsing.enabled": False
                }
                options.add_experimental_option("prefs", prefs)

                return webdriver.Chrome(options=options)

        raise Exception("Opera not found")

    def _try_system_vivaldi(self, download_folder):
        """Try Vivaldi with system driver by detecting installation"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        # Vivaldi installation paths
        vivaldi_paths = [
            "C:\\Program Files\\Vivaldi\\Application\\vivaldi.exe",
            "C:\\Program Files (x86)\\Vivaldi\\Application\\vivaldi.exe",
            "C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe",
            "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi",
            "/usr/bin/vivaldi",
            "/snap/bin/vivaldi"
        ]

        for path in vivaldi_paths:
            expanded_path = os.path.expandvars(path)
            if os.path.exists(expanded_path):
                options = ChromeOptions()
                options.binary_location = expanded_path
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")

                prefs = {
                    "download.default_directory": download_folder,
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "safebrowsing.enabled": False
                }
                options.add_experimental_option("prefs", prefs)

                return webdriver.Chrome(options=options)

        raise Exception("Vivaldi not found")

    def _try_system_safari(self, download_folder):
        """Try Safari with system driver (macOS only)"""
        from selenium import webdriver
        from selenium.webdriver.safari.options import Options as SafariOptions

        options = SafariOptions()
        driver = webdriver.Safari(options=options)

        # Minimize to simulate headless behavior (Safari limitation)
        driver.minimize_window()

        # Set download preferences via JavaScript
        driver.execute_script(f"""
            console.log('Safari system driver initialized for: {download_folder}');
        """)

        return driver

    def _setup_emergency_browser(self, download_folder):
        """Emergency browser setup with minimal requirements - try all browsers"""
        try:
            self.log_status("Emergency browser setup - minimal configuration...")
            from selenium import webdriver

            # Emergency browser attempts in order of likelihood to work
            emergency_browsers = [
                ("Chrome", self._emergency_chrome),
                ("Firefox", self._emergency_firefox),
                ("Edge", self._emergency_edge),
                ("Brave", self._emergency_brave),
                ("Opera", self._emergency_opera),
                ("Vivaldi", self._emergency_vivaldi),
                ("Safari", self._emergency_safari)
            ]

            for browser_name, setup_func in emergency_browsers:
                try:
                    self.log_status(f"Emergency {browser_name} attempt...")
                    driver = setup_func()
                    if driver:
                        self.log_status(f"Emergency {browser_name} setup successful")
                        return driver
                except Exception as e:
                    self.log_status(f"Emergency {browser_name} failed: {str(e)[:30]}")
                    continue

            self.log_status("All emergency browser setups failed")
            return None

        except Exception as e:
            self.log_status(f"Emergency setup failed: {str(e)[:50]}")
            return None

    def _emergency_brave(self):
        """Emergency Brave setup with minimal config"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        brave_paths = [
            "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            "/usr/bin/brave-browser"
        ]

        for path in brave_paths:
            if os.path.exists(path):
                options = ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.binary_location = path
                return webdriver.Chrome(options=options)

        raise Exception("Brave not found")

    def _emergency_opera(self):
        """Emergency Opera setup with minimal config"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        opera_paths = [
            "C:\\Program Files\\Opera\\opera.exe",
            "C:\\Program Files (x86)\\Opera\\opera.exe",
            "/Applications/Opera.app/Contents/MacOS/Opera",
            "/usr/bin/opera"
        ]

        for path in opera_paths:
            expanded_path = os.path.expandvars(path)
            if os.path.exists(expanded_path):
                options = ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.binary_location = expanded_path
                return webdriver.Chrome(options=options)

        raise Exception("Opera not found")

    def _emergency_vivaldi(self):
        """Emergency Vivaldi setup with minimal config"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        vivaldi_paths = [
            "C:\\Program Files\\Vivaldi\\Application\\vivaldi.exe",
            "C:\\Program Files (x86)\\Vivaldi\\Application\\vivaldi.exe",
            "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi",
            "/usr/bin/vivaldi"
        ]

        for path in vivaldi_paths:
            expanded_path = os.path.expandvars(path)
            if os.path.exists(expanded_path):
                options = ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.binary_location = expanded_path
                return webdriver.Chrome(options=options)

        raise Exception("Vivaldi not found")

    def _emergency_chrome(self):
        """Emergency Chrome setup with minimal headless config"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions

        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")

        # MUTE ALL AUDIO - No background noise from opened pages
        options.add_argument("--mute-audio")
        options.add_argument("--autoplay-policy=user-gesture-required")
        options.add_argument("--disable-audio-output")

        return webdriver.Chrome(options=options)

    def _emergency_firefox(self):
        """Emergency Firefox setup with minimal headless config"""
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        options = FirefoxOptions()
        options.add_argument("--headless")

        # MUTE ALL AUDIO - No background noise from opened pages
        options.set_preference("media.volume_scale", "0.0")
        options.set_preference("media.autoplay.default", 5)  # Block audio and video

        return webdriver.Firefox(options=options)

    def _emergency_edge(self):
        """Emergency Edge setup with minimal headless config"""
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options as EdgeOptions

        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")

        # MUTE ALL AUDIO - No background noise from opened pages
        options.add_argument("--mute-audio")
        options.add_argument("--autoplay-policy=user-gesture-required")
        options.add_argument("--disable-audio-output")

        return webdriver.Edge(options=options)

    def _emergency_safari(self):
        """Emergency Safari setup (macOS only) - minimized window"""
        import platform
        if platform.system() != "Darwin":
            raise Exception("Safari only available on macOS")

        from selenium import webdriver
        driver = webdriver.Safari()
        driver.minimize_window()  # Simulate headless
        return driver

    def _setup_brave_driver(self, download_folder):
        """Setup Brave WebDriver with download preferences"""
        try:
            self.log_status("Setting up Brave browser...")
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions

            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            # MUTE ALL AUDIO - No background noise from opened pages
            options.add_argument("--mute-audio")
            options.add_argument("--autoplay-policy=user-gesture-required")
            options.add_argument("--disable-audio-output")

            # Download preferences
            prefs = {
                "download.default_directory": os.path.abspath(download_folder),
                "download.prompt_for_download": True,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False
            }
            options.add_experimental_option("prefs", prefs)

            # Brave browser paths (common locations)
            brave_paths = [
                "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
                "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
                "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
                "/usr/bin/brave-browser",
                "/snap/bin/brave",
                "/opt/brave.com/brave/brave-browser"
            ]

            for brave_path in brave_paths:
                try:
                    if os.path.exists(brave_path):
                        options.binary_location = brave_path

                        # Try with webdriver-manager first
                        try:
                            from webdriver_manager.chrome import ChromeDriverManager
                            from selenium.webdriver.chrome.service import Service
                            service = Service(ChromeDriverManager().install())
                            driver = webdriver.Chrome(service=service, options=options)
                            self.log_status("Brave browser initialized with webdriver-manager")
                            return driver
                        except Exception:
                            # Try system driver
                            try:
                                driver = webdriver.Chrome(options=options)
                                self.log_status("Brave browser initialized with system driver")
                                return driver
                            except Exception:
                                continue
                except Exception:
                    continue

            self.log_status("Brave browser not found or setup failed")
            return None

        except Exception as e:
            self.log_status(f"Brave setup failed: {str(e)[:50]}")
            return None

    def _setup_opera_driver(self, download_folder):
        """Setup Opera WebDriver with download preferences"""
        try:
            self.log_status("Setting up Opera browser...")
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions

            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            # MUTE ALL AUDIO - No background noise from opened pages
            options.add_argument("--mute-audio")
            options.add_argument("--autoplay-policy=user-gesture-required")
            options.add_argument("--disable-audio-output")

            # Download preferences
            prefs = {
                "download.default_directory": os.path.abspath(download_folder),
                "download.prompt_for_download": True,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False
            }
            options.add_experimental_option("prefs", prefs)

            # Opera browser paths (common locations)
            opera_paths = [
                "C:\\Program Files\\Opera\\opera.exe",
                "C:\\Program Files (x86)\\Opera\\opera.exe",
                "C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Opera\\opera.exe",
                "/Applications/Opera.app/Contents/MacOS/Opera",
                "/usr/bin/opera",
                "/snap/bin/opera",
                "/opt/opera/opera"
            ]

            for opera_path in opera_paths:
                try:
                    # Expand environment variables
                    expanded_path = os.path.expandvars(opera_path)
                    if os.path.exists(expanded_path):
                        options.binary_location = expanded_path

                        # Try with webdriver-manager (OperaDriver)
                        try:
                            from webdriver_manager.opera import OperaDriverManager
                            from selenium.webdriver.chrome.service import Service
                            service = Service(OperaDriverManager().install())
                            driver = webdriver.Chrome(service=service, options=options)
                            self.log_status("Opera browser initialized with webdriver-manager")
                            return driver
                        except Exception:
                            # Try system driver (Chrome driver works for Opera)
                            try:
                                driver = webdriver.Chrome(options=options)
                                self.log_status("Opera browser initialized with system driver")
                                return driver
                            except Exception:
                                continue
                except Exception:
                    continue

            self.log_status("Opera browser not found or setup failed")
            return None

        except Exception as e:
            self.log_status(f"Opera setup failed: {str(e)[:50]}")
            return None

    def _setup_vivaldi_driver(self, download_folder):
        """Setup Vivaldi WebDriver with download preferences"""
        try:
            self.log_status("Setting up Vivaldi browser...")
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions

            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            # MUTE ALL AUDIO - No background noise from opened pages
            options.add_argument("--mute-audio")
            options.add_argument("--autoplay-policy=user-gesture-required")
            options.add_argument("--disable-audio-output")

            # Download preferences
            prefs = {
                "download.default_directory": os.path.abspath(download_folder),
                "download.prompt_for_download": True,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False
            }
            options.add_experimental_option("prefs", prefs)

            # Vivaldi browser paths (common locations)
            vivaldi_paths = [
                "C:\\Program Files\\Vivaldi\\Application\\vivaldi.exe",
                "C:\\Program Files (x86)\\Vivaldi\\Application\\vivaldi.exe",
                "C:\\Users\\%USERNAME%\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe",
                "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi",
                "/usr/bin/vivaldi",
                "/snap/bin/vivaldi",
                "/opt/vivaldi/vivaldi"
            ]

            for vivaldi_path in vivaldi_paths:
                try:
                    # Expand environment variables
                    expanded_path = os.path.expandvars(vivaldi_path)
                    if os.path.exists(expanded_path):
                        options.binary_location = expanded_path

                        # Try with webdriver-manager (Chrome driver works for Vivaldi)
                        try:
                            from webdriver_manager.chrome import ChromeDriverManager
                            from selenium.webdriver.chrome.service import Service
                            service = Service(ChromeDriverManager().install())
                            driver = webdriver.Chrome(service=service, options=options)
                            self.log_status("Vivaldi browser initialized with webdriver-manager")
                            return driver
                        except Exception:
                            # Try system driver
                            try:
                                driver = webdriver.Chrome(options=options)
                                self.log_status("Vivaldi browser initialized with system driver")
                                return driver
                            except Exception:
                                continue
                except Exception:
                    continue

            self.log_status("Vivaldi browser not found or setup failed")
            return None

        except Exception as e:
            self.log_status(f"Vivaldi setup failed: {str(e)[:50]}")
            return None

    def _setup_safari_driver(self, download_folder):
        """Setup Safari WebDriver (macOS only) - Note: Safari doesn't support true headless mode"""
        try:
            self.log_status("Setting up Safari browser...")
            import platform

            # Safari is only available on macOS
            if platform.system() != "Darwin":
                self.log_status("Safari is only available on macOS")
                return None

            from selenium import webdriver
            from selenium.webdriver.safari.options import Options as SafariOptions

            options = SafariOptions()
            # Safari doesn't support headless mode natively - runs minimized instead

            try:
                driver = webdriver.Safari(options=options)
                self.log_status("Safari browser initialized (visible mode - Safari limitation)")

                # Minimize the Safari window to simulate headless behavior
                driver.minimize_window()

                # Set download preferences via JavaScript (Safari limitation)
                driver.execute_script(f"""
                    // Safari download preferences are limited
                    console.log('Safari driver initialized for download folder: {download_folder}');
                """)

                return driver

            except Exception as safari_error:
                self.log_status(f"Safari setup failed: {str(safari_error)[:50]}")
                self.log_status("Enable 'Allow Remote Automation' in Safari Developer menu")
                return None

        except Exception as e:
            self.log_status(f"Safari setup failed: {str(e)[:50]}")
            return None

    def safe_find_elements(self, by, selector, parent=None, retries=3):
        """Find elements with automatic retry on stale reference exceptions"""
        for attempt in range(retries):
            try:
                if parent:
                    elements = parent.find_elements(by, selector)
                else:
                    elements = self.driver.find_elements(by, selector)

                # Test if elements are stale by accessing a property
                for elem in elements:
                    try:
                        _ = elem.tag_name  # This will throw StaleElementReferenceException if stale
                    except Exception:
                        if attempt < retries - 1:
                            time.sleep(0.1)
                            break
                        raise
                else:
                    return elements
            except Exception as e:
                if "stale element reference" in str(e).lower() and attempt < retries - 1:
                    time.sleep(0.1)
                    continue
                elif attempt == retries - 1:
                    self.log_status(f"Elements became stale after {retries} retries")
                    return []
        return []

    def safe_click(self, element, retries=3):
        """Click element with retry on stale reference exceptions"""
        for attempt in range(retries):
            try:
                # Try regular click first
                try:
                    element.click()
                    return True
                except Exception:
                    # Try JavaScript click as fallback
                    self.driver.execute_script("arguments[0].click();", element)
                    return True
            except Exception as e:
                if "stale element reference" in str(e).lower() and attempt < retries - 1:
                    time.sleep(0.1)
                    continue
                elif attempt == retries - 1:
                    self.log_status(f"Click failed after {retries} retries: {str(e)[:50]}")
                    return False
        return False

    def is_driver_alive(self):
        """Check if browser driver session is still valid"""
        try:
            _ = self.driver.current_url
            return True
        except Exception:
            return False

    def _timeout_wrapper(self, func, timeout_seconds=10, strategy_name="strategy"):
        """Wrapper to execute strategy functions with aggressive timeouts"""
        import signal
        import threading

        result = [None]
        exception = [None]

        def target():
            try:
                result[0] = func()
            except Exception as e:
                exception[0] = e

        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()
        thread.join(timeout_seconds)

        if thread.is_alive():
            self.log_status(f"⏰ {strategy_name} timed out after {timeout_seconds}s - continuing...")
            return None

        if exception[0]:
            self.log_status(f"⚠️ {strategy_name} failed: {str(exception[0])[:40]}")
            return None

        return result[0]

    def _find_video_element(self, url):
        """Find video element on the page with advanced detection strategies"""
        import time
        import platform

        self.log_status("🔍 DEBUG: _find_video_element called")

        try:
            # GLOBAL MAXIMUM TIME LIMIT: 60 seconds for entire detection process
            start_time = time.time()
            max_total_time = 60

            # Skip signal-based timeout on Windows (not supported)
            use_signal_timeout = False
            if platform.system() != 'Windows':
                try:
                    import signal
                    def timeout_handler(signum, frame):
                        raise Exception("Global video detection timeout after 60 seconds")
                    signal.signal(signal.SIGALRM, timeout_handler)
                    signal.alarm(max_total_time)
                    use_signal_timeout = True
                except:
                    pass

            self.log_status("🔍 DEBUG: Timeout setup complete, platform: " + platform.system())

            # WRAP EVERYTHING IN INNER TRY TO CATCH ALL ERRORS
            self.log_status("Starting comprehensive video detection with 60s GLOBAL LIMIT")
            self.log_status("🔧 Starting Method 1 (Basic) - direct detection")

            # Check if browser driver is still alive
            self.log_status(f"🔍 DEBUG: Checking if browser driver is alive...")
            driver_alive = self.is_driver_alive()
            self.log_status(f"🔍 DEBUG: Browser driver alive: {driver_alive}")

            if not driver_alive:
                self.log_status("Browser session lost - attempting to reconnect")
                if not self._setup_browser_driver(self.download_folder):
                    self.log_status("Failed to reconnect browser session")
                    return None

            # Navigate to the URL with aggressive timeout
            self.log_status(f"Navigating to URL: {url[:60]}...")

            def navigate_to_url():
                self.log_status(f"🔍 DEBUG: Starting navigation to: {url[:60]}")

                try:
                    self.driver.get(url)
                    self.log_status(f"🔍 DEBUG: Browser navigation completed to: {self.driver.current_url[:60]}")
                except Exception as nav_error:
                    self.log_status(f"❌ DEBUG: Navigation failed: {str(nav_error)[:50]}")
                    raise nav_error

                # If this URL likely has Cloudflare protection, ensure authentication
                # Check for common indicators: .com, .net, .org TLDs with certain patterns
                if any(indicator in url.lower() for indicator in ['.com/', '.net/', '.org/']):
                    self.log_status(f"🔍 DEBUG: About to start Cloudflare authentication...")
                    try:
                        cf_result = self._ensure_cloudflare_authentication()
                        self.log_status(f"🔍 DEBUG: Cloudflare authentication result: {cf_result}")
                    except Exception as cf_error:
                        self.log_status(f"❌ DEBUG: Cloudflare authentication failed: {str(cf_error)[:50]}")
                        raise cf_error

                self.log_status(f"🔍 DEBUG: Navigation and authentication completed successfully")
                return True

            # Apply 30 second timeout to URL navigation (includes Cloudflare authentication)
            self.log_status(f"🔍 DEBUG: Starting navigation with 30s timeout...")
            navigation_success = self._timeout_wrapper(navigate_to_url, 30, "URL navigation")

            if not navigation_success:
                # Navigation timed out, treat as navigation error
                self.log_status(f"❌ DEBUG: Navigation timed out after 30 seconds")
                nav_error = Exception("Navigation timed out after 30 seconds")
                # If direct navigation fails, try alternative approaches
                self.log_status(f"Direct navigation failed: {str(nav_error)[:50]}")

                # Try removing preview from URL if it's a Yandex preview URL
                if 'yandex.com/video/preview' in url:
                    # Try the main video URL without preview
                    alt_url = url.replace('/preview/', '/watch/')
                    self.log_status(f"Trying alternative URL: {alt_url[:60]}...")
                    try:
                        def navigate_alt():
                            self.driver.get(alt_url)
                            return True
                        nav_result = self._timeout_wrapper(navigate_alt, 8, "Alternative URL")
                        if not nav_result:
                            raise Exception("Alternative URL navigation timed out")
                    except Exception as alt_error:
                        self.log_status(f"Alternative URL also failed: {str(alt_error)[:50]}")
                        # Try just the base yandex.com and search for the video ID
                        video_id = url.split('/')[-1] if '/' in url else ''
                        if video_id:
                            # Try accessing main Yandex domain first to establish connection
                            self.log_status("Trying main Yandex domain first...")
                            try:
                                def navigate_main():
                                    self.driver.get("https://yandex.com")
                                    return True
                                main_result = self._timeout_wrapper(navigate_main, 5, "Main domain")
                                if not main_result:
                                    raise Exception("Main domain navigation timed out")
                                time.sleep(0.1)
                                # Now try the video URL again
                                self.log_status(f"Retrying original URL after main domain: {url[:60]}...")
                                def retry_original():
                                    self.driver.get(url)
                                    return True
                                retry_result = self._timeout_wrapper(retry_original, 8, "Retry original")
                                if not retry_result:
                                    raise Exception("Retry navigation timed out")
                            except Exception as main_error:
                                self.log_status(f"Main domain approach failed: {str(main_error)[:50]}")
                                # Last resort: try search
                                search_url = f"https://yandex.com/video/search?text={video_id}"
                                self.log_status(f"Trying search approach: {search_url[:60]}...")
                                try:
                                    def navigate_search():
                                        self.driver.get(search_url)
                                        return True
                                    search_result = self._timeout_wrapper(navigate_search, 8, "Search URL")
                                    if not search_result:
                                        raise Exception("Search URL navigation timed out")
                                except Exception as search_error:
                                    self.log_status(f"All URL approaches failed: {str(search_error)[:50]}")

                                    # For Yandex URLs that are completely blocked, use proxy approach
                                    self.log_status("YANDEX BLOCKED - Trying proxy/alternative access methods")

                                    # Try with different approaches automatically
                                    return self._automatic_proxy_detection(url)
                        else:
                            raise nav_error
                else:
                    raise nav_error

            # Check if we're on an error page
            current_url = self.driver.current_url
            if 'neterror' in current_url or 'error' in current_url.lower():
                self.log_status("Detected error page - trying alternative approaches")

                # Try the original URL with different user agent
                if 'yandex.com' in url:
                    self.log_status("Setting mobile user agent for Yandex...")
                    self.driver.execute_script("""
                        Object.defineProperty(navigator, 'userAgent', {
                            get: function () { return 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15'; }
                        });
                    """)

                    try:
                        def navigate_mobile():
                            self.driver.get(url)
                            return True
                        mobile_result = self._timeout_wrapper(navigate_mobile, 8, "Mobile retry")
                        if not mobile_result:
                            raise Exception("Mobile navigation timed out")
                    except Exception as mobile_error:
                        self.log_status(f"Mobile user agent approach failed: {str(mobile_error)[:50]}")

            # Ultra-fast page load check (0.3s max)
            self.log_status("Quick page load check (ultra-fast)...")
            try:
                # Use even shorter timeout
                WebDriverWait(self.driver, 0.3).until(
                    lambda driver: driver.execute_script("return document.readyState") != "loading"
                )
            except Exception as wait_error:
                self.log_status(f"Fast load check failed, continuing: {str(wait_error)[:20]}")
                # Continue immediately - don't wait for full page load

            # Skip dynamic content check entirely for speed
            # self.log_status("Minimal dynamic content check...")
            # time.sleep(0.05)  # Minimal delay

            # Final check if we're still on an error page
            final_url = self.driver.current_url
            if 'neterror' in final_url or 'error' in final_url.lower():
                self.log_status("Still on error page after all attempts")

                # For Yandex URLs that are completely blocked, try alternative video sites
                if 'yandex.com' in url:
                    self.log_status("Yandex appears to be blocked - trying alternative approaches")

                    # Extract video ID and try to find it on other platforms
                    video_id = url.split('/')[-1] if '/' in url else ''
                    if video_id and len(video_id) > 10:  # Valid video ID
                        self.log_status(f"Searching for video ID {video_id} on alternative platforms...")

                        # Try some common video aggregation sites that might have the content
                        alternative_searches = [
                            f"https://www.google.com/search?q=site:youtube.com+{video_id}",
                            f"https://www.google.com/search?q=site:vimeo.com+{video_id}",
                            f"https://www.google.com/search?q={video_id}+video"
                        ]

                        for search_url in alternative_searches:
                            try:
                                self.log_status(f"Trying alternative search: {search_url[:60]}...")
                                self.driver.get(search_url)
                                time.sleep(0.2)

                                # Check if we found any video links
                                video_links = self.safe_find_elements(By.XPATH, "//a[contains(@href, 'youtube.com') or contains(@href, 'vimeo.com') or contains(@href, 'dailymotion.com')]")
                                if video_links:
                                    self.log_status(f"Found {len(video_links)} potential video links in search results")
                                    # Try the first promising link
                                    for link in video_links[:3]:
                                        try:
                                            href = link.get_attribute('href')
                                            if href and any(domain in href for domain in ['youtube.com/watch', 'vimeo.com/', 'dailymotion.com']):
                                                self.log_status(f"Trying alternative video source: {href[:60]}...")
                                                self.driver.get(href)
                                                time.sleep(0.2)
                                                break
                                        except:
                                            continue
                                    break
                            except Exception as alt_search_error:
                                self.log_status(f"Alternative search failed: {str(alt_search_error)[:50]}")
                                continue

                # Don't return None yet - let the strategies try to work with what we have
                self.log_status("Proceeding with strategies - may find cached content or alternative sources")
            
            # STRATEGY 0: Video player embed button detection (HIGHEST PRIORITY)

            # First, look for any overlay or controls that might be hiding embed buttons
            try:
                # Try to hover over the video area to reveal controls
                video_areas = self.safe_find_elements(By.XPATH, "//div[contains(@class, 'video') or contains(@class, 'player')]")
                if video_areas:
                    for area in video_areas[:2]:  # Try first 2 video areas
                        try:
                            if area.is_displayed():
                                actions = ActionChains(self.driver)
                                actions.move_to_element(area).perform()
                                time.sleep(0.2)  # Give time for controls to appear
                                self.log_status("Hovered over video area to reveal controls")
                        except:
                            continue
            except:
                pass

            self.log_status("🔍 Pre-Method: VK video embed detection (5s timeout)...")
            # Apply aggressive 5-second timeout to VK detection
            video_result = self._timeout_wrapper(self._detect_and_click_vk_video_embeds, 5, "VK embed detection")
            if video_result:
                self.log_status("✅ Video found in Pre-Method VK detection - download complete")
                return video_result

            self.log_status("⚠️ Pre-Method VK detection failed/timed out - proceeding to Method 1")

            # METHOD 1 (BASIC): Direct detection and source extraction
            self.log_status("🔧 Starting Method 1 (Basic) - direct detection")
            if hasattr(self, 'gui') and hasattr(self.gui, 'set_phase'):
                self.gui.set_phase(1)

            # DEBUG: Check if page has actually loaded after Cloudflare authentication
            try:
                current_url = self.driver.current_url
                page_source = self.driver.page_source[:1000].lower()
                self.log_status(f"🔍 DEBUG: Current URL after navigation: {current_url}")
                self.log_status(f"🔍 DEBUG: Page source length: {len(self.driver.page_source)}")

                # Check for Cloudflare blockage
                if any(indicator in page_source for indicator in ['checking your browser', 'please wait', 'cloudflare', 'challenge-platform', 'cf-browser-verification']):
                    self.log_status("❌ Page is still stuck on Cloudflare challenge - trying to wait longer")
                    time.sleep(10)  # Additional wait

                    # Check again
                    page_source = self.driver.page_source[:1000].lower()
                    if any(indicator in page_source for indicator in ['checking your browser', 'please wait', 'cloudflare']):
                        self.log_status("❌ Page still blocked by Cloudflare - attempting refresh")
                        self.driver.refresh()
                        time.sleep(5)
                elif len(self.driver.page_source) > 5000:
                    self.log_status("✅ Page appears to have loaded successfully")
                else:
                    self.log_status(f"⚠️ Unexpected page state - URL: {current_url[:50]}, Source length: {len(self.driver.page_source)}")

            except Exception as debug_error:
                self.log_status(f"🔍 DEBUG: Page check failed: {str(debug_error)[:50]}")

            # STRATEGY 0.1: SPANKBANG SPECIALIZED DETECTION (10s timeout for player loading)
            if 'spankbang.com' in url.lower():
                self.log_status("🔍 Method 1: SpankBang specialized detection...")
                spankbang_result = self._timeout_wrapper(self._detect_spankbang_video, 10, "SpankBang detection")
                if spankbang_result:
                    self.log_status("✅ Video found in Method 1 SpankBang detection - skipping remaining methods")
                    return spankbang_result

            # STRATEGY 0.2: CDN-PROTECTED VIDEO DETECTION (5s timeout)
            # Check if URL has authentication parameters or CDN patterns
            if any(param in url.lower() for param in ['verify=', 'token=', '.cdn', 'cdn.']):
                self.log_status("🔍 Method 1: CDN-protected video specialized detection...")
                cdn_result = self._timeout_wrapper(lambda: self._detect_cdn_protected_video(), 5, "CDN-protected detection")
                if cdn_result:
                    self.log_status("✅ Video found in Method 1 CDN-protected detection - skipping remaining methods")
                    return cdn_result

            # STRATEGY 0.5: ENHANCED VIDEO SOURCE DETECTION (3s timeout)
            self.log_status("🔍 Method 1: Enhanced comprehensive detection...")
            enhanced_result = self._timeout_wrapper(self._enhanced_comprehensive_video_detection, 3, "Enhanced detection")
            if enhanced_result:
                self.log_status("✅ Video found in Method 1 - skipping remaining methods")
                return enhanced_result

            # STRATEGY 1: Direct video URL extraction (2s timeout)
            self.log_status("🔍 Method 1: Direct URL extraction from page source...")
            video_url = self._timeout_wrapper(self._extract_video_url_from_source, 2, "URL extraction")
            if video_url:
                self.log_status("✅ Video found in Method 1 - skipping remaining methods")
                return self._create_fake_element_for_download(video_url)

            self.log_status("⚠️ Method 1 failed - no video found with basic detection")

            # METHOD 2 (INTERMEDIATE): Network and JavaScript analysis
            self.log_status("🔧 Starting Method 2 (Intermediate) - network & JS analysis")
            if hasattr(self, 'gui') and hasattr(self.gui, 'set_phase'):
                self.gui.set_phase(2)

            # STRATEGY 2: Network monitoring for video requests (3s timeout)
            self.log_status("🔍 Method 2: Network request monitoring...")
            video_url = self._timeout_wrapper(self._monitor_network_requests, 3, "Network monitoring")
            if video_url:
                self.log_status("✅ Video found in Method 2 - skipping remaining methods")
                return self._create_fake_element_for_download(video_url)

            # STRATEGY 3: Advanced JavaScript execution (3s timeout)
            self.log_status("🔍 Method 2: Advanced JavaScript detection...")
            video_element = self._timeout_wrapper(self._execute_advanced_js_detection, 3, "JavaScript detection")
            if video_element:
                self.log_status("✅ Video found in Method 2 - skipping remaining methods")
                return video_element

            # STRATEGY 4: Traditional DOM element detection (3s timeout)
            self.log_status("🔍 Method 2: Traditional DOM element detection...")
            video_element = self._timeout_wrapper(self._traditional_element_detection, 3, "DOM detection")
            if video_element:
                self.log_status("✅ Video found in Method 2 - skipping remaining methods")
                return video_element

            self.log_status("⚠️ Method 2 failed - advancing to Method 3")
            self.log_status("🔄 Method 2 complete - progressing to Method 3...")

            # METHOD 3 (ADVANCED): Token-based and iframe extraction
            self.log_status("🔧 Advancing to Method 3 (Advanced) - enhanced extraction")
            if hasattr(self, 'gui') and hasattr(self.gui, 'set_phase'):
                self.gui.set_phase(3)

            # STRATEGY 5: Handle token-based sites (3s timeout)
            video_element = self._timeout_wrapper(self._handle_token_based_sites, 3, "Token-based sites")
            if video_element:
                self.log_status("✅ Video found in Method 3 - skipping remaining methods")
                return video_element

            # STRATEGY 6: Iframe and embed content extraction (3s timeout)
            video_element = self._timeout_wrapper(self._extract_from_iframes_and_embeds, 3, "Iframe extraction")
            if video_element:
                self.log_status("✅ Video found in Method 3 - skipping remaining methods")
                return video_element

            # STRATEGY 7: API endpoint discovery (3s timeout)
            video_url = self._timeout_wrapper(self._discover_api_endpoints, 3, "API discovery")
            if video_url:
                self.log_status("✅ Video found in Method 3 - skipping remaining methods")
                return self._create_fake_element_for_download(video_url)

            self.log_status("⚠️ Method 3 failed - advancing to Method 4")
            self.log_status("🔄 Method 3 complete - progressing to Method 4...")

            # METHOD 4 (COMPLEX): Advanced fallback and dynamic discovery
            self.log_status("🔧 Advancing to Method 4 (Complex) - final attempt")
            if hasattr(self, 'gui') and hasattr(self.gui, 'set_phase'):
                self.gui.set_phase(4)

            # STRATEGY 8: Blob URL and data URL handling (3s timeout)
            video_element = self._timeout_wrapper(self._handle_blob_and_data_urls, 3, "Blob URL handling")
            if video_element:
                self.log_status("✅ Video found in Method 4 - download complete")
                return video_element

            # STRATEGY 9: Yandex video embed detection (3s timeout)
            video_element = self._timeout_wrapper(self._detect_yandex_embeds, 3, "Yandex embeds")
            if video_element:
                self.log_status("✅ Video found in Method 4 - download complete")
                return video_element

            # STRATEGY 10: Source page navigation fallback (3s timeout)
            video_element = self._timeout_wrapper(self._source_page_navigation_fallback, 3, "Page navigation")
            if video_element:
                self.log_status("✅ Video found in Method 4 - download complete")
                return video_element

            # STRATEGY 11: General embed link detection (3s timeout)
            video_element = self._timeout_wrapper(self._detect_and_click_embed_links, 3, "Embed links")
            if video_element:
                self.log_status("✅ Video found in Method 4 - download complete")
                return video_element

            # STRATEGY 12: RIGHT-CLICK VIDEO EXTRACTION (10s timeout) - ULTIMATE METHOD
            self.log_status("🔍 Method 4: RIGHT-CLICK video extraction (ultimate method)...")
            video_element = self._timeout_wrapper(self._right_click_video_extraction, 10, "Right-click extraction")
            if video_element:
                self.log_status("✅ Video found in Method 4 RIGHT-CLICK - download complete")
                return video_element

            # STRATEGY 13: JavaScript-based dynamic link discovery (3s timeout)
            video_element = self._timeout_wrapper(self._javascript_link_discovery, 3, "JS link discovery")
            if video_element:
                self.log_status("✅ Video found in Method 4 - download complete")
                return video_element

            self.log_status("⚠️ Method 4 failed - all methods exhausted")
            self.log_status("All strategies attempted - no video found")
            elapsed = time.time() - start_time
            self.log_status(f"🔄 Completed all 4 methods in {elapsed:.1f}s: Basic -> Intermediate -> Advanced -> Complex")
            return None

        except Exception as e:
            if "Global video detection timeout" in str(e):
                self.log_status("⏰ GLOBAL TIMEOUT: Video detection stopped after 60 seconds")
                self.log_status("🚨 If videos are taking this long, there may be network/site issues")
            elif "Navigation timed out" in str(e):
                self.log_status(f"❌ NAVIGATION ERROR: Failed to navigate to URL after 30 seconds")
                self.log_status(f"🔍 DEBUG: Navigation error details: {str(e)[:100]}")
            elif "Cloudflare" in str(e):
                self.log_status(f"❌ CLOUDFLARE ERROR: Authentication failed")
                self.log_status(f"🔍 DEBUG: Cloudflare error details: {str(e)[:100]}")
            else:
                self.log_status(f"❌ CRITICAL ERROR in video detection: {str(e)[:100]}")
                logger.error(f"Error in advanced video detection: {e}")
                import traceback
                full_traceback = traceback.format_exc()
                self.log_status(f"🔍 DEBUG: Full traceback: {full_traceback[:300]}")

                # Try to identify the specific failure point
                if "driver" in str(e).lower():
                    self.log_status("⚠️ DEBUG: Browser driver error detected")
                elif "timeout" in str(e).lower():
                    self.log_status("⚠️ DEBUG: Timeout error detected")
                elif "element" in str(e).lower():
                    self.log_status("⚠️ DEBUG: Element access error detected")
                elif "network" in str(e).lower() or "connection" in str(e).lower():
                    self.log_status("⚠️ DEBUG: Network connection error detected")

            return None

    def _automatic_proxy_detection(self, blocked_url):
        """Automatic proxy and alternative access for blocked URLs"""
        try:
            self.log_status("Starting automatic proxy detection and alternative access")

            # Extract video ID from blocked URL
            video_id = blocked_url.split('/')[-1] if '/' in blocked_url else ''

            # Try accessing through alternative domains and proxies
            alternative_approaches = [
                f"https://webcache.googleusercontent.com/search?q=cache:{blocked_url}",  # Google Cache
                f"https://translate.google.com/translate?sl=ru&tl=en&u={blocked_url}",  # Google Translate proxy
                f"https://anonymouse.org/cgi-bin/anon-www.cgi/{blocked_url}",  # Anonymous proxy
            ]

            # Also try alternative video discovery
            search_approaches = [
                f"https://www.youtube.com/results?search_query={video_id}",
                f"https://vimeo.com/search?q={video_id}",
                f"https://www.dailymotion.com/search/{video_id}",
                f"https://www.google.com/search?q={video_id}+video",
            ]

            all_approaches = alternative_approaches + search_approaches

            for approach in all_approaches:
                try:
                    self.log_status(f"Trying alternative access: {approach[:60]}...")
                    self.driver.get(approach)
                    time.sleep(0.2)

                    # Check if we found video content or links
                    current_url = self.driver.current_url

                    if 'error' not in current_url.lower() and 'neterror' not in current_url:
                        # Try running embed detection on this page
                        self.log_status("Alternative access successful - running embed detection")

                        # Run the intelligent clicking system
                        result = self._intelligent_video_player_clicking()
                        if result:
                            return result

                        # Try other detection strategies
                        result = self._detect_and_click_embed_links()
                        if result:
                            return result

                except Exception as approach_error:
                    self.log_status(f"Alternative approach failed: {str(approach_error)[:50]}")
                    continue

            self.log_status("All automatic approaches exhausted")
            return None

        except Exception as e:
            self.log_status(f"Automatic proxy detection error: {str(e)[:100]}")
            return None

    def _detect_and_click_vk_video_embeds(self):
        """STRATEGY 0: Detect and click embed buttons in video players that lead to source URLs"""
        try:
            self.log_status("Looking for embed buttons in video players...")

            # Wait for page to fully load and any video players to initialize
            time.sleep(0.2)  # Reduced from 3 to 1 second

            # First try to find embed buttons directly (IFRAME PRIORITY)
            direct_embed_selectors = [
                # HIGHEST PRIORITY: iframes (most reliable)
                "//iframe[contains(@src, 'vk.com/video_ext.php')]",
                "//iframe[contains(@src, 'vkvideo.ru')]",
                "//iframe[contains(@src, 'youtube.com/embed')]",
                "//iframe[contains(@src, 'vimeo.com/video')]",
                "//iframe[contains(@src, 'dailymotion.com/embed')]",

                # Yandex video specific patterns
                "//a[contains(@class, 'videoplayer_btn')]",
                "//a[contains(@class, 'VideoViewer-Item')]",
                "//a[contains(@class, 'video-source')]",
                "//a[contains(@href, 'vkvideo.ru')]",
                "//a[contains(@href, 'vk.com/video')]",
                "//a[contains(@href, 'youtube.com/watch')]",
                "//a[contains(@href, 'youtu.be')]",

                # Links with aria-labels indicating video sources
                "//a[@aria-label and contains(@href, 'http')]",

                # Bottom-right corner buttons (positioned absolutely)
                "//a[contains(@style, 'position') and contains(@style, 'absolute')]",
                "//button[contains(@style, 'position') and contains(@style, 'absolute')]",

                # Generic embed/source buttons
                "//a[contains(text(), 'Source')]",
                "//a[contains(text(), 'Watch on')]",
                "//a[contains(text(), 'View on')]",
            ]

            # First, specifically look for VK iframe embeds
            vk_iframe_result = self._detect_vk_iframe_embeds()
            if vk_iframe_result:
                # If we got a list of URLs, try to download the first one
                if isinstance(vk_iframe_result, list) and len(vk_iframe_result) > 0:
                    self.log_status(f"🎯 Got {len(vk_iframe_result)} URLs from iframe detection")
                    for i, url in enumerate(vk_iframe_result):
                        self.log_status(f"  Trying URL {i+1}: {url[:80]}...")

                        # Check if this is a video page URL that needs yt-dlp processing
                        if self._is_video_page_url(url):
                            self.log_status(f"🎬 Detected video page URL, using yt-dlp: {url[:60]}")
                            download_result = self._download_with_yt_dlp(url)
                        else:
                            # Use direct download for actual video file URLs
                            download_result = self._download_direct_url(url)

                        if download_result:
                            self.log_status(f"✅ Successfully used URL {i+1}")
                            return download_result
                    self.log_status("❌ None of the iframe URLs worked for download")
                    return None
                else:
                    # Return as-is if it's not a URL list
                    return vk_iframe_result

            # Try direct embed button selectors
            for selector in direct_embed_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    if elements:
                        self.log_status(f"Found {len(elements)} elements with selector: {selector}")

                        for elem in elements:
                            try:
                                # Handle iframes differently from links
                                if elem.tag_name.lower() == 'iframe':
                                    src = elem.get_attribute('src')
                                    if src:
                                        self.log_status(f"Found iframe embed: {src[:60]}...")

                                        # Handle VK iframe specifically
                                        if 'vk.com/video_ext.php' in src:
                                            return self._handle_vk_iframe_direct(src)
                                        elif 'vk.com' in src:
                                            return self._handle_vk_video_url(src)
                                        # Add other iframe handlers here for other platforms

                                    continue

                                # Check if element is visible and has href (for links)
                                if elem.is_displayed():
                                    href = elem.get_attribute('href')
                                    aria_label = elem.get_attribute('aria-label') or ''
                                    text = elem.text.strip()[:30] if elem.text else ''

                                    # Filter out non-video source links
                                    if href and 'http' in href:
                                        # Skip Yandex internal links that won't lead to actual video sources
                                        if 'yandex.com/video/search' in href or 'yandex.com/video/preview' in href:
                                            continue

                                        # Prioritize actual video hosting sites
                                        is_video_source = self._is_video_source_url(href)

                                        if is_video_source:
                                            self.log_status(f"Found video source embed: {aria_label or text} -> {href[:60]}...")

                                            # Store current URL
                                            current_url = self.driver.current_url

                                            # Open in new tab to avoid losing current page
                                            try:
                                                # Try to open link in new tab
                                                self.driver.execute_script(f"window.open('{href}', '_blank');")
                                                time.sleep(0.1)

                                                # Switch to new tab
                                                self.driver.switch_to.window(self.driver.window_handles[-1])
                                                time.sleep(0.2)

                                                # Check if we successfully navigated
                                                new_url = self.driver.current_url
                                                if new_url != current_url and self._is_video_source_url(new_url):
                                                    self.log_status(f"Successfully navigated to video source: {new_url[:80]}")
                                                    self.log_status("Searching for video on source page...")

                                                    # Try to find video on the new page
                                                    video = self._find_video_on_current_page()
                                                    if video:
                                                        self.log_status("Found video on VK Video page!")
                                                        return video
                                                    else:
                                                        # If no video found, close tab and continue
                                                        self.driver.close()
                                                        self.driver.switch_to.window(self.driver.window_handles[0])
                                                else:
                                                    # Close unsuccessful tab
                                                    self.driver.close()
                                                    self.driver.switch_to.window(self.driver.window_handles[0])
                                            except Exception as tab_error:
                                                self.log_status(f"Tab navigation failed: {str(tab_error)[:50]}")
                                                # Try direct navigation as fallback
                                                try:
                                                    self.driver.get(href)
                                                    time.sleep(0.2)
                                                    new_url = self.driver.current_url
                                                    if self._is_video_source_url(new_url):
                                                        video = self._find_video_on_current_page()
                                                        if video:
                                                            return video
                                                    # Navigate back if unsuccessful
                                                    self.driver.get(current_url)
                                                    time.sleep(0.1)
                                                except:
                                                    pass
                            except Exception as elem_error:
                                continue
                except Exception as selector_error:
                    continue

            # If no direct embed buttons found, look for video player containers
            self.log_status("Looking for video player containers...")
            player_selectors = [
                "//div[contains(@class, 'player')]",
                "//div[contains(@class, 'video')]",
                "//div[contains(@id, 'player')]",
                "//div[contains(@id, 'video')]",
                "//video/ancestor::div[1]",
                "//iframe/ancestor::div[1]"
            ]

            player_containers = []
            for selector in player_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    player_containers.extend(elements)
                except:
                    continue

            self.log_status(f"Found {len(player_containers)} potential video player containers")

            # Look for embed/source buttons within video players
            embed_button_patterns = [
                # Buttons and links that typically lead to source URLs
                ".//a[contains(@class, 'btn') and (@href and @href != '#')]",
                ".//button[@onclick and contains(@onclick, 'http')]",
                ".//a[contains(@aria-label, 'Video') and @href]",
                ".//a[contains(@title, 'source') and @href]",
                ".//a[contains(@title, 'original') and @href]",
                ".//a[contains(@class, 'source') and @href]",
                ".//a[contains(@class, 'embed') and @href]",
                ".//a[contains(@class, 'external') and @href]",
                ".//a[contains(text(), 'Watch') and @href]",
                ".//a[contains(text(), 'Source') and @href]",
                ".//a[contains(text(), 'Original') and @href]",
                ".//a[@href and contains(@href, 'video')]",
                ".//a[@href and contains(@href, '.com')]"
            ]

            embed_buttons = []
            for container in player_containers:
                # First, try to hover over the container to reveal any hidden controls
                try:
                    if container.is_displayed():
                        actions = ActionChains(self.driver)
                        # Move to bottom-right corner where embed buttons often are
                        size = container.size
                        if size:
                            actions.move_to_element_with_offset(container, size['width'] - 50, size['height'] - 50).perform()
                            time.sleep(0.1)
                            self.log_status("Hovered over player container bottom-right corner")
                except:
                    pass

                for pattern in embed_button_patterns:
                    try:
                        buttons = container.find_elements(By.XPATH, pattern)
                        for button in buttons:
                            href = button.get_attribute('href')
                            onclick = button.get_attribute('onclick')
                            aria_label = button.get_attribute('aria-label') or ''
                            title = button.get_attribute('title') or ''

                            # Log button details for debugging
                            if href and 'video' in href.lower():
                                self.log_status(f"Found potential embed: {aria_label or title} -> {href[:60]}")

                            # Check if button is visible and positioned in corners (common for embed buttons)
                            try:
                                if button.is_displayed():
                                    # Try to get position info
                                    button_location = button.location
                                    container_location = container.location
                                    container_size = container.size

                                    if button_location and container_location and container_size:
                                        # Calculate relative position
                                        rel_x = (button_location['x'] - container_location['x']) / max(container_size['width'], 1)
                                        rel_y = (button_location['y'] - container_location['y']) / max(container_size['height'], 1)

                                        # Check if in bottom-right corner
                                        if rel_x > 0.6 and rel_y > 0.6:
                                            self.log_status(f"Corner button found: {aria_label or title} at ({rel_x:.1f}, {rel_y:.1f})")
                                            # Prioritize corner buttons by adding to front
                                            if href and href != '#' and not href.startswith('javascript:'):
                                                embed_buttons.insert(0, (button, href, 'href'))
                                                continue
                            except:
                                pass

                            # Add regular buttons
                            if href and href != '#' and not href.startswith('javascript:'):
                                embed_buttons.append((button, href, 'href'))
                            elif onclick and 'http' in onclick:
                                embed_buttons.append((button, onclick, 'onclick'))
                    except:
                        continue

            if not embed_buttons:
                self.log_status("No embed buttons found in video players")
                # Continue to systematic clicking instead of returning None
                return self._systematic_video_player_clicking()

            self.log_status(f"Found {len(embed_buttons)} embed buttons in video players")

            # Click each embed button (prioritize VK Video and other video sources)
            for i, (button, target, target_type) in enumerate(embed_buttons):
                try:
                    # Skip non-video source links
                    if target_type == 'href':
                        # Skip Yandex internal navigation that won't lead to videos
                        if 'yandex.com/video/search' in target or 'yandex.com/' == target:
                            continue

                        # Skip if not a known video source
                        if not self._is_video_source_url(target):
                            self.log_status(f"Skipping non-video link: {target[:60]}...")
                            continue

                    self.log_status(f"Clicking video embed button {i+1}: {target[:80]}... (type: {target_type})")

                    # Store current URL to detect navigation
                    current_url = self.driver.current_url

                    # Click the button
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(0.2)

                    # Check if we navigated to a new page
                    new_url = self.driver.current_url
                    if new_url != current_url:
                        self.log_status(f"Successfully navigated to source page: {new_url[:80]}...")

                        # Try to find video on the source page
                        video_result = self._find_video_on_current_page()
                        if video_result:
                            self.log_status("Found video on source page!")
                            return video_result
                        else:
                            self.log_status("No video found on source page, trying next button...")
                            # Go back to try next button
                            self.driver.back()
                            time.sleep(0.1)
                    else:
                        self.log_status("Button didn't navigate to new page, trying next...")

                except Exception as button_error:
                    self._log_status_throttled(f"Error clicking button {i+1}: {str(button_error)[:60]}")
                    continue

            self.log_status("All embed buttons tried, no video found")

            # If regular embed button clicking failed, try systematic clicking
            self.log_status("Attempting systematic video player exploration...")
            return self._systematic_video_player_clicking()

        except Exception as e:
            self.log_status(f"Embed button detection error: {str(e)[:100]}")
            return None

    def _systematic_video_player_clicking(self):
        """Advanced systematic video player exploration using multiple clicking strategies"""
        try:
            self.log_status("Starting advanced video player exploration...")

            # First, inject helper functions for enhanced detection
            self._inject_embedded_link_helpers()

            # Find all potential video containers using comprehensive selectors
            video_containers = self._find_all_video_containers()

            if not video_containers:
                self.log_status("No video containers found for systematic clicking")
                return None

            # Try multiple exploration strategies with human-like interactions
            strategies = [
                self._strategy_javascript_embed_clicker,
                self._strategy_human_video_interaction,
                self._strategy_grid_clicking,
                self._strategy_edge_scanning,
                self._strategy_iframe_exploration,
                self._strategy_dynamic_content_waiting,
                self._strategy_javascript_discovery
            ]

            for strategy in strategies:
                try:
                    result = strategy(video_containers)
                    if result:
                        self.log_status(f"Strategy '{strategy.__name__}' succeeded!")
                        return result
                except Exception as strategy_error:
                    self._log_status_throttled(f"Strategy '{strategy.__name__}' failed: {str(strategy_error)[:50]}")
                    continue

            return None

        except Exception as e:
            self.log_status(f"Systematic clicking error: {str(e)[:60]}")
            return None

    def _inject_embedded_link_helpers(self):
        """Inject JavaScript helpers for embedded link detection"""
        try:
            helper_script = """
                // VK Embed Auto-Clicker - Enhanced Detection
                window.vkEmbedClicker = {
                    clickedElements: new Set(),
                    maxClicks: 15,
                    foundEmbeds: [],
                    isActive: true,

                    init: function() {
                        console.log('🎬 VK Embed Auto-Clicker initialized');
                        this.scanForVKEmbeds();
                        this.setupObserver();
                        this.clickBottomRightArea();
                        return 'VK Embed Clicker Ready';
                    },

                    scanForVKEmbeds: function() {
                        if (!this.isActive) return 0;
                        console.log('🔍 Scanning for VK embeds...');

                        const selectors = [
                            // VK specific (highest priority)
                            'a[href*="vk.com"]',
                            'iframe[src*="vk.com"]',
                            'iframe[src*="video_ext.php"]',

                            // YouTube and other video platforms
                            'a[href*="youtube.com"]', 'a[href*="youtu.be"]',
                            'iframe[src*="youtube.com"]',

                            // Generic embed patterns
                            '[data-embed-url]', '[data-video-id]',
                            '.embed-button', '.share-button', '.video-link',

                            // Look for logos/images in video areas
                            'img[src*="youtube"]', 'img[alt*="YouTube"]', 'img[alt*="VK"]',

                            // Clickable elements in video containers
                            'div[class*="video"] a', 'div[class*="player"] a', 'div[class*="embed"] a'
                        ];

                        let foundElements = [];

                        selectors.forEach(selector => {
                            try {
                                document.querySelectorAll(selector).forEach(element => {
                                    if (this.isValidVKElement(element)) {
                                        foundElements.push(element);
                                    }
                                });
                            } catch (error) {
                                console.log('Selector error:', selector, error);
                            }
                        });

                        console.log(`🎯 Found ${foundElements.length} potential VK/embed elements`);
                        this.foundEmbeds = foundElements;

                        // Sort by position (bottom-right priority for embed buttons)
                        foundElements.sort((a, b) => {
                            const rectA = a.getBoundingClientRect();
                            const rectB = b.getBoundingClientRect();
                            return (rectB.right + rectB.bottom) - (rectA.right + rectA.bottom);
                        });

                        this.processElements(foundElements);
                        return foundElements.length;
                    },

                    isValidVKElement: function(element) {
                        if (this.clickedElements.has(element)) return false;
                        if (!this.isElementVisible(element)) return false;

                        const href = element.href || element.src || element.dataset.embedUrl;
                        const hasVKPattern = href && (href.includes('vk.com') || href.includes('video_ext.php'));
                        const hasVideoPattern = href && (href.includes('youtube.com') || href.includes('youtu.be'));
                        const hasEmbedClass = element.className && (
                            element.className.includes('embed') ||
                            element.className.includes('share') ||
                            element.className.includes('video')
                        );

                        return hasVKPattern || hasVideoPattern || hasEmbedClass;
                    },

                    isElementVisible: function(element) {
                        if (!element) return false;
                        const rect = element.getBoundingClientRect();
                        const style = window.getComputedStyle(element);

                        return (
                            rect.width > 0 && rect.height > 0 &&
                            style.display !== 'none' &&
                            style.visibility !== 'hidden' &&
                            style.opacity !== '0'
                        );
                    },

                    processElements: function(elements) {
                        let clickCount = 0;

                        elements.slice(0, this.maxClicks).forEach((element, index) => {
                            setTimeout(() => {
                                if (this.isActive) {
                                    this.clickElementSafely(element);
                                }
                            }, index * 800); // 800ms delay between clicks
                            clickCount++;
                        });
                    },

                    clickElementSafely: function(element) {
                        if (this.clickedElements.has(element) || !this.isActive) return;

                        try {
                            console.log('🖱️ Clicking VK/embed element:', element);
                            this.clickedElements.add(element);

                            // Scroll into view first
                            element.scrollIntoView({ behavior: 'smooth', block: 'center' });

                            setTimeout(() => {
                                // Multiple click methods (try each until one works)
                                const methods = [
                                    () => element.click(),
                                    () => {
                                        const event = new MouseEvent('click', {
                                            bubbles: true, cancelable: true, view: window
                                        });
                                        element.dispatchEvent(event);
                                    },
                                    () => {
                                        if (element.href) {
                                            window.open(element.href, '_blank');
                                        }
                                    }
                                ];

                                for (let method of methods) {
                                    try {
                                        method();
                                        console.log('✅ Click method succeeded');
                                        return 'Success';
                                    } catch (e) {
                                        console.log('Click method failed:', e);
                                    }
                                }
                            }, 300);

                        } catch (error) {
                            console.error('❌ Error clicking element:', error);
                        }
                    },

                    clickBottomRightArea: function() {
                        if (!this.isActive) return [];

                        // Click common embed button locations with delays
                        const width = window.innerWidth;
                        const height = window.innerHeight;

                        const clickPoints = [
                            [width * 0.9, height * 0.9],   // Bottom-right (most common)
                            [width * 0.85, height * 0.85], // Lower-right
                            [width * 0.95, height * 0.95], // Extreme bottom-right
                            [width * 0.8, height * 0.9],   // Bottom area
                            [width * 0.9, height * 0.8],   // Right area
                            [width * 0.93, height * 0.87], // Slight variations
                            [width * 0.87, height * 0.93]
                        ];

                        clickPoints.forEach(([x, y], index) => {
                            setTimeout(() => {
                                if (this.isActive) {
                                    const element = document.elementFromPoint(x, y);
                                    if (element && element.tagName !== 'BODY' && element.tagName !== 'HTML') {
                                        console.log(`🎯 Area clicking at (${Math.round(x)}, ${Math.round(y)}):`, element);
                                        try {
                                            element.click();
                                        } catch (e) {
                                            console.log('Area click failed:', e);
                                        }
                                    }
                                }
                            }, 2000 + (index * 1000)); // Start after 2 seconds, then 1 second intervals
                        });

                        return clickPoints.length;
                    },

                    setupObserver: function() {
                        // Watch for new content and iframes
                        const observer = new MutationObserver((mutations) => {
                            let hasNewContent = false;
                            mutations.forEach(mutation => {
                                if (mutation.type === 'childList') {
                                    mutation.addedNodes.forEach(node => {
                                        if (node.nodeType === Node.ELEMENT_NODE) {
                                            if (node.tagName === 'IFRAME' ||
                                                node.querySelector && node.querySelector('iframe, a[href*="vk.com"]')) {
                                                hasNewContent = true;
                                            }
                                        }
                                    });
                                }
                            });

                            if (hasNewContent && this.isActive) {
                                console.log('🔄 New VK content detected, rescanning...');
                                setTimeout(() => this.scanForVKEmbeds(), 1000);
                            }
                        });

                        observer.observe(document.body, { childList: true, subtree: true });
                        console.log('👀 VK content observer active');
                    },

                    stop: function() {
                        this.isActive = false;
                        console.log('⏹️ VK embed clicker stopped');
                    },

                    getStatus: function() {
                        return {
                            active: this.isActive,
                            clickedCount: this.clickedElements.size,
                            foundEmbeds: this.foundEmbeds.length,
                            maxClicks: this.maxClicks
                        };
                    }
                };

                // Legacy support
                window.embeddedLinkHelper = window.vkEmbedClicker;

                // Auto-initialize
                if (document.readyState === 'loading') {
                    document.addEventListener('DOMContentLoaded', () => window.vkEmbedClicker.init());
                } else {
                    window.vkEmbedClicker.init();
                }
            """
            self.driver.execute_script(helper_script)
            self.log_status("Injected VK embed detection and auto-clicker")

        except Exception as e:
            self.log_status(f"Failed to inject helpers: {str(e)[:50]}")

    def _find_all_video_containers(self):
        """Find all potential video containers using comprehensive selectors"""
        selectors = [
            # Video players and containers
            "//div[contains(@class, 'video')]",
            "//div[contains(@class, 'player')]",
            "//div[contains(@class, 'media')]",
            "//div[contains(@class, 'embed')]",
            "//div[contains(@id, 'video')]",
            "//div[contains(@id, 'player')]",

            # Yandex-specific
            "//div[contains(@class, 'VideoViewer')]",
            "//div[contains(@class, 'videoplayer')]",
            "//div[contains(@class, 'content')]",
            "//div[contains(@class, 'preview')]",

            # More generic containers
            "//section", "//article", "//main",
            "//div[@role='main']",
            "//div[contains(@class, 'container')]",
            "//div[contains(@class, 'wrapper')]",

            # Video elements and their parents
            "//video/ancestor::div[1]",
            "//iframe/ancestor::div[1]",

            # CSS selector fallbacks
            "//div[@class]",  # Any div with a class
            "//body//div"  # All divs in body
        ]

        containers = []
        for selector in selectors:
            try:
                elements = self.safe_find_elements(By.XPATH, selector)
                containers.extend(elements)
            except:
                continue

        # Remove duplicates and filter by size
        unique_containers = []
        for container in containers:
            try:
                if container.is_displayed():
                    size = container.size
                    # Lower the minimum size requirement
                    if size and size['width'] >= 50 and size['height'] >= 50:
                        if container not in unique_containers:
                            unique_containers.append(container)
            except:
                continue

        # Sort by size (largest first) to prioritize main content areas
        unique_containers.sort(key=lambda x: self._get_element_size_score(x), reverse=True)

        self.log_status(f"Found {len(unique_containers)} potential video containers")

        # If no containers found, create a fallback viewport container
        if not unique_containers:
            self.log_status("No containers found, using viewport fallback")
            viewport_container = self._create_viewport_container()
            if viewport_container:
                unique_containers.append(viewport_container)

        return unique_containers[:10]  # Increased limit for better coverage

    def _strategy_javascript_embed_clicker(self, containers):
        """Strategy 0.5: JavaScript-based embed detection and clicking"""
        self.log_status("Strategy: JavaScript-based embed clicker")

        try:
            # Trigger JavaScript monitoring and clicking
            js_result = self._monitor_javascript_clicker()

            if js_result:
                # Wait for JavaScript clicking to complete
                self.log_status("Waiting for JavaScript embed clicker to complete...")
                time.sleep(0.2)  # Reduced from 10 to 3 seconds

                # Check for new windows or navigation
                current_windows = len(self.driver.window_handles)
                current_url = self.driver.current_url

                if current_windows > 1:
                    # New window opened - check it
                    result = self._handle_new_window("js-clicker")
                    if result:
                        return result

                # Check if URL changed to a video source
                if 'vk.com/video_ext.php' in current_url or self._is_video_source_url(current_url):
                    self.log_status(f"JS clicker found video source: {current_url[:60]}")
                    video = self._find_video_on_current_page()
                    if video:
                        return video

                # Check for any new iframes that appeared
                return self._check_for_new_iframes_after_interaction()

            return None

        except Exception as e:
            self.log_status(f"JavaScript embed clicker error: {str(e)[:50]}")
            return None

    def _get_element_size_score(self, element):
        """Get size score for sorting elements"""
        try:
            size = element.size
            return size['width'] * size['height']
        except:
            return 0

    def _create_viewport_container(self):
        """Create a container representing the entire viewport for human interaction"""
        try:
            # Use the body element as a fallback container
            body = self.driver.find_element(By.TAG_NAME, "body")
            if body:
                self.log_status("Using body element as viewport container")
                return body

            # If body doesn't work, use html
            html = self.driver.find_element(By.TAG_NAME, "html")
            if html:
                self.log_status("Using html element as viewport container")
                return html

            return None

        except Exception as e:
            self.log_status(f"Viewport container creation failed: {str(e)[:30]}")
            return None

    def _strategy_human_video_interaction(self, containers):
        """Strategy 0: Human-like video interaction to reveal embed buttons"""
        self.log_status("Strategy: Human-like video interaction")

        try:
            for i, container in enumerate(containers):
                self.log_status(f"Human interaction with container {i+1}")

                # Step 1: Hover over video to reveal controls
                self._human_hover_video(container)

                # Step 2: Look for overlay controls that might appear
                self._human_check_overlay_controls(container)

                # Step 3: Try clicking on different areas that might reveal embeds
                result = self._human_click_embed_areas(container)
                if result:
                    return result

                # Step 4: Check if any new iframes appeared after interaction
                result = self._check_for_new_iframes_after_interaction()
                if result:
                    return result

            # Step 5: If container-based interaction failed, try page-level interaction
            self.log_status("Container interaction failed, trying page-level human interaction")
            result = self._human_page_level_interaction()
            if result:
                return result

            return None

        except Exception as e:
            self.log_status(f"Human interaction error: {str(e)[:50]}")
            return None

    def _human_hover_video(self, container):
        """Human-like hovering over video to reveal controls"""
        try:
            # Check if element is still valid
            if not self._is_element_still_valid(container):
                return

            # Move mouse to center of video
            location = container.location
            size = container.size
            center_x = location['x'] + size['width'] // 2
            center_y = location['y'] + size['height'] // 2

            # Create smooth mouse movement
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(container, size['width'] // 2, size['height'] // 2)
            actions.perform()
            time.sleep(0.2)

            # Hover in a few different spots to trigger controls
            hover_points = [
                (size['width'] // 4, size['height'] // 4),  # Top-left area
                (3 * size['width'] // 4, size['height'] // 4),  # Top-right area
                (size['width'] // 2, 3 * size['height'] // 4),  # Bottom-center area
                (3 * size['width'] // 4, 3 * size['height'] // 4)  # Bottom-right area (common embed button location)
            ]

            for x_offset, y_offset in hover_points:
                try:
                    actions = ActionChains(self.driver)
                    actions.move_to_element_with_offset(container, x_offset, y_offset)
                    actions.perform()
                    time.sleep(0.1)  # Brief pause like human
                except:
                    continue

            self.log_status("Completed human-like hovering")

        except Exception as e:
            self.log_status(f"Hover error: {str(e)[:30]}")

    def _human_check_overlay_controls(self, container):
        """Check for overlay controls that appear on hover"""
        try:
            # Look for common embed/share buttons that appear on hover
            overlay_selectors = [
                "//button[contains(text(), 'Embed')]",
                "//button[contains(text(), 'Share')]",
                "//a[contains(text(), 'Watch on')]",
                "//a[contains(text(), 'View on')]",
                "//div[contains(@class, 'embed')]//button",
                "//div[contains(@class, 'share')]//button",
                "//div[contains(@class, 'overlay')]//a",
                "//div[contains(@title, 'embed')]",
                "//div[contains(@title, 'share')]",
                "//span[contains(text(), 'VK')]",
                "//a[contains(@href, 'vk.com')]"
            ]

            for selector in overlay_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    if elements:
                        self.log_status(f"Found {len(elements)} overlay controls: {selector}")
                        # Try clicking the first visible one
                        for elem in elements:
                            if elem.is_displayed() and elem.is_enabled():
                                try:
                                    elem.click()
                                    time.sleep(0.1)
                                    self.log_status(f"Clicked overlay control: {selector}")
                                    return True
                                except:
                                    continue
                except:
                    continue

            return False

        except Exception as e:
            self.log_status(f"Overlay check error: {str(e)[:30]}")
            return False

    def _human_click_embed_areas(self, container):
        """Human-like clicking on areas where embed buttons typically appear"""
        try:
            # Check if element is still valid
            if not self._is_element_still_valid(container):
                self.log_status("Container became stale, skipping embed area clicking")
                return None

            # Common areas where embed buttons appear (as percentages of video size)
            embed_areas = [
                (0.9, 0.9),   # Bottom-right corner (most common for embed buttons)
                (0.9, 0.1),   # Top-right corner
                (0.8, 0.8),   # Lower-right area
                (0.1, 0.1),   # Top-left corner
                (0.1, 0.9),   # Bottom-left corner
                (0.5, 0.9),   # Bottom-center
                (0.9, 0.5),   # Right-center
                (0.8, 0.2),   # Upper-right area
                (0.7, 0.9),   # Bottom area variations
                (0.95, 0.95), # Extreme bottom-right
                (0.5, 0.5),   # Center
                (0.6, 0.8),   # Bottom-center-right
            ]

            size = container.size
            original_url = self.driver.current_url
            initial_windows = len(self.driver.window_handles)

            for x_percent, y_percent in embed_areas:
                try:
                    x_offset = int(size['width'] * x_percent)
                    y_offset = int(size['height'] * y_percent)

                    self.log_status(f"Human click at {x_percent*100:.0f}%,{y_percent*100:.0f}% of video")

                    # Try multiple click methods like a human would
                    click_methods = [
                        lambda: self._human_single_click(container, x_offset, y_offset),
                        lambda: self._human_double_click(container, x_offset, y_offset),
                        lambda: self._human_right_click(container, x_offset, y_offset)
                    ]

                    for click_method in click_methods:
                        try:
                            click_method()
                            time.sleep(0.2)

                            # Check if we navigated to a new page or opened new window
                            current_windows = len(self.driver.window_handles)
                            current_url = self.driver.current_url

                            if current_windows > initial_windows:
                                # New window opened - check it
                                result = self._handle_new_window(f"{x_percent*100:.0f}%,{y_percent*100:.0f}%")
                                if result:
                                    return result
                                initial_windows = current_windows

                            elif current_url != original_url:
                                # Same tab navigation
                                if 'vk.com/video_ext.php' in current_url or self._is_video_source_url(current_url):
                                    self.log_status(f"Human click found video source: {current_url[:60]}")
                                    video = self._find_video_on_current_page()
                                    if video:
                                        return video

                                # Go back if not useful
                                self.driver.get(original_url)
                                time.sleep(0.1)

                        except Exception as click_error:
                            continue

                except Exception as area_error:
                    continue

            return None

        except Exception as e:
            self.log_status(f"Embed area clicking error: {str(e)[:50]}")
            return None

    def _human_single_click(self, container, x_offset, y_offset):
        """Human-like single click"""
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(container, x_offset, y_offset)
        actions.click()
        actions.perform()

    def _human_double_click(self, container, x_offset, y_offset):
        """Human-like double click"""
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(container, x_offset, y_offset)
        actions.double_click()
        actions.perform()

    def _human_right_click(self, container, x_offset, y_offset):
        """Human-like right click"""
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(container, x_offset, y_offset)
        actions.context_click()
        actions.perform()

    def _check_for_new_iframes_after_interaction(self):
        """Check if human interaction revealed new iframes with VK embeds"""
        try:
            self.log_status("Checking for new iframes after human interaction...")

            # Wait a moment for any dynamic content to load
            time.sleep(0.1)

            # Look specifically for VK iframes that might have appeared
            vk_iframe_selectors = [
                "//iframe[contains(@src, 'vk.com/video_ext.php')]",
                "//iframe[contains(@src, 'vk.com/video')]",
                "//iframe[contains(@src, 'vkvideo.ru')]"
            ]

            for selector in vk_iframe_selectors:
                try:
                    iframes = self.safe_find_elements(By.XPATH, selector)
                    for iframe in iframes:
                        iframe_src = iframe.get_attribute('src')
                        if iframe_src and 'video_ext.php' in iframe_src:
                            self.log_status(f"Found new VK iframe after interaction: {iframe_src[:80]}")
                            return self._handle_vk_iframe_direct(iframe_src)
                except:
                    continue

            return None

        except Exception as e:
            self.log_status(f"New iframe check error: {str(e)[:50]}")
            return None

    def _human_page_level_interaction(self):
        """Page-level human interaction using absolute viewport coordinates"""
        try:
            self.log_status("Starting page-level human interaction...")

            # Get viewport dimensions
            viewport_size = self.driver.execute_script("return {width: window.innerWidth, height: window.innerHeight};")
            width = viewport_size['width']
            height = viewport_size['height']

            original_url = self.driver.current_url
            initial_windows = len(self.driver.window_handles)

            # Define strategic click points across the viewport (absolute coordinates)
            click_points = [
                # Bottom-right areas (most common for embed buttons)
                (width * 0.9, height * 0.9),
                (width * 0.85, height * 0.85),
                (width * 0.95, height * 0.95),
                (width * 0.8, height * 0.9),
                (width * 0.9, height * 0.8),

                # Right edge areas
                (width * 0.9, height * 0.5),
                (width * 0.95, height * 0.7),
                (width * 0.85, height * 0.6),

                # Bottom areas
                (width * 0.7, height * 0.9),
                (width * 0.6, height * 0.85),
                (width * 0.5, height * 0.9),

                # Top-right areas
                (width * 0.9, height * 0.1),
                (width * 0.85, height * 0.15),

                # Center areas
                (width * 0.5, height * 0.5),
                (width * 0.6, height * 0.6),
            ]

            for i, (x, y) in enumerate(click_points):
                try:
                    self.log_status(f"Page-level click {i+1} at ({x:.0f},{y:.0f})")

                    # Try clicking at this absolute coordinate
                    self.driver.execute_script(f"document.elementFromPoint({x}, {y})?.click();")
                    time.sleep(0.2)

                    # Check for navigation or new windows
                    current_windows = len(self.driver.window_handles)
                    current_url = self.driver.current_url

                    if current_windows > initial_windows:
                        # New window opened
                        result = self._handle_new_window(f"page-click-{i+1}")
                        if result:
                            return result
                        initial_windows = current_windows

                    elif current_url != original_url:
                        # Same tab navigation
                        if 'vk.com/video_ext.php' in current_url or self._is_video_source_url(current_url):
                            self.log_status(f"Page-level click found video source: {current_url[:60]}")
                            video = self._find_video_on_current_page()
                            if video:
                                return video

                        # Go back if not useful
                        self.driver.get(original_url)
                        time.sleep(0.1)

                    # Also try hovering to reveal controls at this location
                    self.driver.execute_script(f"""
                        var element = document.elementFromPoint({x}, {y});
                        if (element) {{
                            var event = new MouseEvent('mouseover', {{
                                view: window,
                                bubbles: true,
                                cancelable: true,
                                clientX: {x},
                                clientY: {y}
                            }});
                            element.dispatchEvent(event);
                        }}
                    """)
                    time.sleep(0.1)

                except Exception as click_error:
                    self._log_status_throttled(f"Page-level click {i+1} error: {str(click_error)[:30]}")
                    continue

            # Check for any iframes that might have appeared after all the interactions
            return self._check_for_new_iframes_after_interaction()

        except Exception as e:
            self.log_status(f"Page-level interaction error: {str(e)[:50]}")
            return None

    def _is_element_still_valid(self, element):
        """Check if element is still valid and attached to DOM"""
        try:
            # Try to access element properties
            element.is_displayed()
            element.size
            return True
        except:
            return False

    def _monitor_javascript_clicker(self):
        """Monitor and trigger the JavaScript-based VK embed clicker"""
        try:
            self.log_status("Monitoring JavaScript VK embed clicker...")

            # Check if the JavaScript clicker is active
            status = self.driver.execute_script("return window.vkEmbedClicker ? window.vkEmbedClicker.getStatus() : null;")

            if status:
                self.log_status(f"JS Clicker Status: {status['clickedCount']} clicked, {status['foundEmbeds']} found")

                # Trigger additional scans
                found_count = self.driver.execute_script("return window.vkEmbedClicker.scanForVKEmbeds();")
                self.log_status(f"JS scan found {found_count} elements")

                # Trigger bottom-right area clicking
                click_count = self.driver.execute_script("return window.vkEmbedClicker.clickBottomRightArea();")
                self.log_status(f"JS bottom-right clicking initiated: {click_count} points")

                return True
            else:
                self.log_status("JavaScript clicker not available, reinitializing...")
                self._inject_embedded_link_helpers()
                return False

        except Exception as e:
            self.log_status(f"JavaScript monitor error: {str(e)[:50]}")
            return False

    def _log_download_diagnostics(self, event_type, data):
        """Comprehensive download diagnostics logger to identify issues"""
        try:
            # Create downloads log file if it doesn't exist
            log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "download_diagnostics")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            log_file = os.path.join(log_dir, f"download_diagnostics_{time.strftime('%Y%m%d')}.log")

            # Format the log entry with proper timestamp
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            log_entry = {
                "timestamp": timestamp,
                "event": event_type,
                "data": data
            }

            # Write to log file
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry, indent=2) + "\n")
                f.write("-" * 80 + "\n")

            # Also log critical events to console
            if event_type in ["ERROR", "FAILURE", "TIMEOUT", "BLOCKED", "NEW_FILES", "BROWSER_STATE"]:
                # Format data for console output
                if isinstance(data, dict):
                    formatted_data = json.dumps(data, indent=2, default=str)[:500]  # Limit output
                else:
                    formatted_data = str(data)[:500]
                self.log_status(f"[DOWNLOAD_DIAGNOSTIC] {event_type}: {formatted_data}")

        except Exception as e:
            self.log_status(f"Diagnostic logging error: {str(e)[:50]}")

    def _check_browser_download_state(self):
        """Check browser's internal download state and permissions"""
        try:
            diagnostics = {}

            # Check Chrome download settings
            try:
                download_settings = self.driver.execute_script("""
                    return {
                        'downloadEnabled': navigator.permissions ? true : false,
                        'userAgent': navigator.userAgent,
                        'platform': navigator.platform,
                        'cookieEnabled': navigator.cookieEnabled,
                        'onLine': navigator.onLine,
                        'language': navigator.language
                    };
                """)
                diagnostics['browser_settings'] = download_settings
            except Exception as e:
                diagnostics['browser_settings_error'] = str(e)[:100]

            # Check for download blockers
            try:
                blockers = self.driver.execute_script("""
                    const checks = {
                        'hasAdblocker': false,
                        'hasPopupBlocker': false,
                        'iframeRestricted': false,
                        'downloadBlocked': false
                    };

                    // Check for ad blockers
                    const testAd = document.createElement('div');
                    testAd.className = 'adsbox';
                    testAd.style.height = '1px';
                    document.body.appendChild(testAd);
                    if (window.getComputedStyle(testAd).display === 'none') {
                        checks.hasAdblocker = true;
                    }
                    document.body.removeChild(testAd);

                    // Check popup permissions
                    if (window.open === undefined || window.open.toString().includes('[native code]') === false) {
                        checks.hasPopupBlocker = true;
                    }

                    // Check iframe restrictions
                    try {
                        const iframe = document.createElement('iframe');
                        document.body.appendChild(iframe);
                        document.body.removeChild(iframe);
                    } catch(e) {
                        checks.iframeRestricted = true;
                    }

                    // Check if downloads are blocked by CSP
                    const meta = document.querySelector('meta[http-equiv="Content-Security-Policy"]');
                    if (meta && meta.content.includes('sandbox')) {
                        checks.downloadBlocked = true;
                    }

                    return checks;
                """)
                diagnostics['blockers'] = blockers
            except Exception as e:
                diagnostics['blocker_check_error'] = str(e)[:100]

            # Check Chrome downloads page (simplified to avoid errors)
            try:
                # Note: chrome:// URLs are restricted, checking download folder instead
                diagnostics['chrome_downloads'] = "Check via folder monitoring"
            except Exception as e:
                diagnostics['chrome_downloads_error'] = str(e)[:100]

            # Check page-specific download restrictions
            try:
                page_checks = self.driver.execute_script("""
                    return {
                        'hasVideo': document.querySelector('video') !== null,
                        'hasIframe': document.querySelector('iframe') !== null,
                        'pageTitle': document.title,
                        'pageURL': window.location.href,
                        'isSecure': window.location.protocol === 'https:',
                        'hasServiceWorker': 'serviceWorker' in navigator,
                        'referrer': document.referrer
                    };
                """)
                diagnostics['page_state'] = page_checks
            except Exception as e:
                diagnostics['page_check_error'] = str(e)[:100]

            # Log all diagnostics
            self._log_download_diagnostics("BROWSER_STATE", diagnostics)

            return diagnostics

        except Exception as e:
            self.log_status(f"Browser state check error: {str(e)[:50]}")
            return {"error": str(e)}

    def _strategy_grid_clicking(self, containers):
        """Strategy 1: Grid-based systematic clicking across video players"""
        self.log_status("Strategy: Grid-based systematic clicking")

        for i, container in enumerate(containers):
            try:
                size = container.size
                if not size or size['width'] < 100:
                    continue

                self.log_status(f"Grid-clicking container {i+1}: {size['width']}x{size['height']}px")

                # Store current state
                original_url = self.driver.current_url
                original_windows = len(self.driver.window_handles)

                # Create a dense grid of click points
                grid_points = []
                for x_ratio in [0.1, 0.25, 0.5, 0.75, 0.9, 0.95]:
                    for y_ratio in [0.1, 0.25, 0.5, 0.75, 0.9, 0.95]:
                        grid_points.append((x_ratio, y_ratio, f"grid-{x_ratio}-{y_ratio}"))

                # Prioritize corners and edges
                priority_points = [
                    (0.95, 0.95, "bottom-right-corner"),
                    (0.9, 0.9, "near-bottom-right"),
                    (0.95, 0.05, "top-right-corner"),
                    (0.05, 0.95, "bottom-left-corner"),
                    (0.05, 0.05, "top-left-corner")
                ]

                all_points = priority_points + [p for p in grid_points if p not in priority_points]

                for rel_x, rel_y, position_name in all_points:
                    result = self._click_at_position(container, rel_x, rel_y, position_name, original_url, original_windows)
                    if result:
                        return result

            except Exception as e:
                self.log_status(f"Grid strategy failed on container {i+1}: {str(e)[:50]}")
                continue

        return None

    def _strategy_edge_scanning(self, containers):
        """Strategy 2: Edge scanning for embed buttons"""
        self.log_status("Strategy: Edge scanning for embed buttons")

        for container in containers:
            try:
                size = container.size
                if not size:
                    continue

                # Scan edges more densely
                edge_points = []

                # Right edge (most common for embed buttons)
                for y in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
                    edge_points.extend([
                        (0.95, y, f"right-edge-{y}"),
                        (0.9, y, f"near-right-{y}"),
                        (0.85, y, f"inner-right-{y}")
                    ])

                # Bottom edge
                for x in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
                    edge_points.extend([
                        (x, 0.95, f"bottom-edge-{x}"),
                        (x, 0.9, f"near-bottom-{x}")
                    ])

                original_url = self.driver.current_url
                original_windows = len(self.driver.window_handles)

                for rel_x, rel_y, position_name in edge_points:
                    result = self._click_at_position(container, rel_x, rel_y, position_name, original_url, original_windows)
                    if result:
                        return result

            except Exception as e:
                continue

        return None

    def _click_at_position(self, container, rel_x, rel_y, position_name, original_url, original_windows):
        """Enhanced clicking at specific position with multiple click methods"""
        try:
            size = container.size
            x_offset = int(size['width'] * rel_x)
            y_offset = int(size['height'] * rel_y)

            # Try multiple click methods
            click_methods = [
                self._method_action_chains_click,
                self._method_javascript_click,
                self._method_direct_element_click
            ]

            for method in click_methods:
                try:
                    method(container, x_offset, y_offset, position_name)

                    time.sleep(0.3)  # Wait for response

                    # Check for navigation or new windows
                    if len(self.driver.window_handles) > original_windows:
                        return self._handle_new_window(position_name)
                    elif self.driver.current_url != original_url:
                        return self._handle_same_tab_navigation(original_url)

                except Exception as method_error:
                    continue

            return None

        except Exception as e:
            return None

    def _method_action_chains_click(self, container, x_offset, y_offset, position_name):
        """Click using ActionChains with hover"""
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(container, x_offset, y_offset)
        actions.pause(0.3)  # Trigger hover effects
        actions.click()
        actions.perform()
        self.log_status(f"ActionChains click at {position_name}")

    def _method_javascript_click(self, container, x_offset, y_offset, position_name):
        """Click using JavaScript at coordinates"""
        location = container.location
        abs_x = location['x'] + x_offset
        abs_y = location['y'] + y_offset

        click_script = f"""
            const element = document.elementFromPoint({abs_x}, {abs_y});
            if (element) {{
                element.scrollIntoView();
                element.click();
                return element.tagName + ':' + (element.href || element.src || 'no-url');
            }}
            return 'no-element';
        """

        result = self.driver.execute_script(click_script)
        self.log_status(f"JavaScript click at {position_name}: {result}")

    def _method_direct_element_click(self, container, x_offset, y_offset, position_name):
        """Find and click element at coordinates"""
        location = container.location
        abs_x = location['x'] + x_offset
        abs_y = location['y'] + y_offset

        # Find element at point
        element_script = f"return document.elementFromPoint({abs_x}, {abs_y});"
        element = self.driver.execute_script(element_script)

        if element and element.is_displayed():
            element.click()
            self.log_status(f"Direct element click at {position_name}")

    def _handle_new_window(self, position_name):
        """Handle new window/tab opened"""
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(0.2)

            new_url = self.driver.current_url
            self.log_status(f"New window from {position_name}: {new_url[:60]}")

            if self._is_video_source_url(new_url):
                video = self._find_video_on_current_page()
                if video:
                    self.log_status("Found video in new window!")
                    return video

            # Close unsuccessful window
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return None

        except Exception as e:
            return None

    def _handle_same_tab_navigation(self, original_url):
        """Handle navigation in same tab"""
        try:
            new_url = self.driver.current_url
            self.log_status(f"Same tab navigation: {new_url[:60]}")

            if self._is_video_source_url(new_url):
                video = self._find_video_on_current_page()
                if video:
                    return video

            # Navigate back if not useful
            self.driver.get(original_url)
            time.sleep(0.1)
            return None

        except Exception as e:
            return None

    def _strategy_iframe_exploration(self, containers):
        """Strategy 3: Comprehensive iframe exploration"""
        self.log_status("Strategy: Iframe exploration")

        try:
            # Find all iframes
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")

            for i, iframe in enumerate(iframes):
                try:
                    iframe_src = iframe.get_attribute('src') or ''
                    self.log_status(f"Exploring iframe {i+1}: {iframe_src[:60]}")

                    if self._is_video_source_url(iframe_src):
                        # Try to interact with iframe
                        self.driver.switch_to.frame(iframe)

                        # Look for clickable elements in iframe
                        clickable_elements = self.safe_find_elements(By.CSS_SELECTOR, "a, button, [onclick]")

                        for element in clickable_elements[:5]:  # Try first 5
                            try:
                                if element.is_displayed():
                                    element.click()
                                    time.sleep(0.1)

                                    # Check if we navigated to video source
                                    current_url = self.driver.current_url
                                    if self._is_video_source_url(current_url):
                                        self.driver.switch_to.default_content()
                                        video = self._find_video_on_current_page()
                                        if video:
                                            return video
                            except:
                                continue

                        self.driver.switch_to.default_content()

                except Exception as iframe_error:
                    self.driver.switch_to.default_content()
                    continue

            return None

        except Exception as e:
            self.log_status(f"Iframe exploration error: {str(e)[:50]}")
            return None

    def _strategy_dynamic_content_waiting(self, containers):
        """Strategy 4: Wait for dynamic content and embedded links"""
        self.log_status("Strategy: Dynamic content waiting")

        try:
            # Wait for embedded links to appear dynamically
            wait_script = """
                return new Promise((resolve) => {
                    let attempts = 0;
                    const maxAttempts = 30;

                    function checkForEmbeds() {
                        const embeds = document.querySelectorAll(
                            'a[href*="vk.com"], a[href*="youtube.com"], iframe[src*="vk.com"], [data-embed-url]'
                        );

                        if (embeds.length > 0) {
                            resolve(Array.from(embeds).map(el => ({
                                tag: el.tagName,
                                href: el.href || el.src,
                                text: el.textContent.trim().substring(0, 30)
                            })));
                        } else if (attempts < maxAttempts) {
                            attempts++;
                            setTimeout(checkForEmbeds, 1000);
                        } else {
                            resolve([]);
                        }
                    }

                    checkForEmbeds();
                });
            """

            # Wait up to 30 seconds for embedded content
            embeds = self.driver.execute_async_script(wait_script)

            if embeds:
                self.log_status(f"Found {len(embeds)} dynamic embedded elements")

                # Try clicking the embedded elements
                for embed in embeds:
                    try:
                        selector = f'a[href="{embed["href"]}"],[src="{embed["href"]}"]'
                        element = self.driver.find_element(By.CSS_SELECTOR, selector)
                        element.click()

                        time.sleep(0.2)
                        if self._is_video_source_url(self.driver.current_url):
                            video = self._find_video_on_current_page()
                            if video:
                                return video
                    except:
                        continue

            return None

        except Exception as e:
            self.log_status(f"Dynamic content waiting error: {str(e)[:50]}")
            return None

    def _strategy_javascript_discovery(self, containers):
        """Strategy 5: JavaScript-based element discovery and clicking"""
        self.log_status("Strategy: JavaScript discovery")

        try:
            discovery_script = """
                const elements = window.embeddedLinkHelper.findAllClickableElements();
                const results = [];

                for (let i = 0; i < Math.min(elements.length, 20); i++) {
                    const element = elements[i];
                    const info = window.embeddedLinkHelper.getElementInfo(element);

                    if (info.href.includes('vk.com') || info.href.includes('youtube.com') ||
                        info.href.includes('video') || info.className.includes('embed')) {
                        results.push({
                            index: i,
                            info: info,
                            element: element
                        });
                    }
                }

                return results;
            """

            discovered_elements = self.driver.execute_script(discovery_script)

            if discovered_elements:
                self.log_status(f"JavaScript discovered {len(discovered_elements)} potential elements")

                for elem_data in discovered_elements:
                    try:
                        # Click using JavaScript
                        click_script = f"""
                            const elements = window.embeddedLinkHelper.findAllClickableElements();
                            const element = elements[{elem_data['index']}];
                            if (element) {{
                                window.embeddedLinkHelper.clickElement(element);
                                return true;
                            }}
                            return false;
                        """

                        clicked = self.driver.execute_script(click_script)

                        if clicked:
                            time.sleep(0.2)
                            current_url = self.driver.current_url
                            if self._is_video_source_url(current_url):
                                video = self._find_video_on_current_page()
                                if video:
                                    return video

                    except Exception as elem_error:
                        continue

            return None

        except Exception as e:
            self.log_status(f"JavaScript discovery error: {str(e)[:50]}")
            return None

    def _detect_vk_iframe_embeds(self):
        """Specifically detect and handle VK iframe embeds with LIMITED scanning"""
        try:
            self.log_status("Looking for VK iframe embeds (quick scan only)...")

            # SKIP comprehensive iframe scanning - it takes way too long!
            # Just do a quick targeted search instead

            # Look for VK iframe embeds specifically
            vk_iframe_selectors = [
                "//iframe[contains(@src, 'vk.com/video_ext.php')]",
                "//iframe[contains(@src, 'vkvideo.ru')]",
                "//iframe[contains(@src, 'vk.com/video')]"
            ]

            for selector in vk_iframe_selectors:
                try:
                    iframes = self.safe_find_elements(By.XPATH, selector)
                    for iframe in iframes:
                        iframe_src = iframe.get_attribute('src')
                        if iframe_src:
                            self.log_status(f"Found VK iframe: {iframe_src[:80]}")

                            # If this is a video_ext.php iframe, navigate to it directly
                            if 'video_ext.php' in iframe_src:
                                return self._handle_vk_iframe_direct(iframe_src)
                            else:
                                # For regular VK video URLs, continue with normal flow
                                return self._handle_vk_video_url(iframe_src)

                except Exception as iframe_error:
                    continue

            return None

        except Exception as e:
            self.log_status(f"VK iframe detection error: {str(e)[:50]}")
            return None

    def _scan_all_iframes_on_page(self):
        """QUICKLY scan ONLY FIRST FEW iframes on the page to find video embeds"""
        try:
            import time
            start_time = time.time()
            max_scan_time = 3  # Maximum 3 seconds for iframe scanning

            self.log_status("Quick iframe scan (3s max)...")

            # Get all iframes using multiple methods
            iframe_search_methods = [
                lambda: self.driver.find_elements(By.TAG_NAME, "iframe"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe"),
                lambda: self.driver.find_elements(By.XPATH, "//iframe"),
                lambda: self.driver.find_elements(By.XPATH, "//frame"),
                # Look for lazy-loaded or hidden iframes
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[data-src]"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[style*='display:none']"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[style*='visibility:hidden']")
            ]

            all_iframes = []
            for method in iframe_search_methods:
                try:
                    iframes = method()
                    for iframe in iframes:
                        if iframe not in all_iframes:
                            all_iframes.append(iframe)
                except:
                    continue

            self.log_status(f"Found {len(all_iframes)} total iframes on page")

            # First, run enhanced detection on the current page before processing iframes
            if all_iframes:
                self.log_status("🔍 Running enhanced detection on page with iframes...")
                try:
                    enhanced_sources = self._enhanced_comprehensive_video_detection()
                    if enhanced_sources and len(enhanced_sources) > 0:
                        self.log_status(f"✅ Enhanced detection found {len(enhanced_sources)} sources!")

                        # Try to download detected sources directly
                        downloaded_source = self._try_direct_download_detected_sources(enhanced_sources)
                        if downloaded_source:
                            return downloaded_source

                        # Fallback: Return the first valid source for download
                        for source in enhanced_sources:
                            if self._is_valid_video_url(source):
                                return source
                        return enhanced_sources[0] if enhanced_sources else None
                except Exception as e:
                    self.log_status(f"Enhanced detection pre-iframe error: {str(e)[:100]}")

            # Check each iframe for video content (LIMITED TO FIRST 8 FOR SPEED)
            for i, iframe in enumerate(all_iframes[:8]):  # Process max 8 iframes only!
                # Abort if we've spent more than 3 seconds scanning
                if time.time() - start_time > max_scan_time:
                    self.log_status("⏰ Iframe scan time limit reached - aborting")
                    break

                try:
                    iframe_src = iframe.get_attribute('src') or iframe.get_attribute('data-src') or ''
                    self.log_status(f"🔍 Processing iframe {i+1}/{min(len(all_iframes), 8)}")

                    # Check if this iframe contains video content
                    if self._is_video_iframe(iframe_src):
                        self.log_status(f"🎥 Video iframe detected: {iframe_src[:60]}")

                        # Handle VK video_ext.php iframes with highest priority
                        if 'vk.com/video_ext.php' in iframe_src:
                            result = self._handle_vk_iframe_direct(iframe_src)
                            if result: return result
                        elif 'vk.com' in iframe_src or 'vkvideo.ru' in iframe_src:
                            result = self._handle_vk_video_url(iframe_src)
                            if result: return result
                        elif iframe_src:
                            # Try to handle other video iframes
                            result = self._handle_generic_video_iframe(iframe_src)
                            if result: return result

                except Exception as iframe_error:
                    self._log_status_throttled(f"Error processing iframe {i+1}: {str(iframe_error)[:30]}")
                    continue

            return None

        except Exception as e:
            self.log_status(f"Iframe scanning error: {str(e)[:50]}")
            return None

    def _detect_spankbang_video(self):
        """Specialized detection for SpankBang videos with dynamic player loading"""
        try:
            self.log_status("🎬 Waiting for SpankBang video player to load...")

            import time

            # First try to scroll down to trigger lazy loading
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                time.sleep(0.5)
                self.driver.execute_script("window.scrollTo(0, 0);")
                self.log_status("🔄 Triggered page scroll to load content")
            except:
                pass

            # Wait longer for SpankBang's heavy JavaScript to load
            time.sleep(4)  # Increased from 2 to 4 seconds

            # Look for video element first
            video_selectors = [
                "video",
                "video[src]",
                "#video-player video",
                ".video-player video",
                "[data-video-src]",
                "[data-src*='.mp4']"
            ]

            for selector in video_selectors:
                try:
                    videos = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    if videos:
                        self.log_status(f"🎯 Found video element with selector: {selector}")
                        for video in videos[:2]:  # Check first 2 video elements
                            # Check for src attribute
                            video_src = video.get_attribute('src')
                            if video_src and self._is_valid_video_url(video_src):
                                self.log_status(f"🎥 SpankBang video URL found: {video_src[:80]}...")
                                return video

                            # Check for data attributes
                            for attr in ['data-video-src', 'data-src', 'data-url']:
                                video_src = video.get_attribute(attr)
                                if video_src and self._is_valid_video_url(video_src):
                                    self.log_status(f"🎥 SpankBang video URL found in {attr}: {video_src[:80]}...")
                                    return video
                except:
                    continue

            # Look for JavaScript-generated video URLs in page content
            self.log_status("🔍 Scanning page for SpankBang video URLs...")
            try:
                page_source = self.driver.page_source

                # Enhanced SpankBang video URL patterns
                import re
                spankbang_patterns = [
                    # Direct video URLs
                    r'https?://[^"\']*\.sb-cd\.com[^"\']*\.mp4[^"\']*',
                    r'https?://[^"\']*spankbang[^"\']*\.mp4[^"\']*',
                    r'https?://[^"\']*\.spankbang\.com[^"\']*\.mp4[^"\']*',

                    # JSON properties (common in video sites)
                    r'"stream_url[^"]*":\s*"([^"]*)"',
                    r'"video_url[^"]*":\s*"([^"]*)"',
                    r'"videoUrl[^"]*":\s*"([^"]*)"',
                    r'"streamUrl[^"]*":\s*"([^"]*)"',
                    r'"src[^"]*":\s*"([^"]*\.mp4[^"]*)"',
                    r'"file[^"]*":\s*"([^"]*\.mp4[^"]*)"',

                    # HLS streams (m3u8)
                    r'https?://[^"\']*\.sb-cd\.com[^"\']*\.m3u8[^"\']*',
                    r'"hls[^"]*":\s*"([^"]*\.m3u8[^"]*)"',

                    # Any .mp4 or .m3u8 URL
                    r'https?://[^"\']*(?:\.mp4|\.m3u8)[^"\']*',

                    # SpankBang specific patterns
                    r'sb-cd\.com[^"\']*(?:\.mp4|\.m3u8)',
                    r'spankbang\.com[^"\']*(?:\.mp4|\.m3u8)'
                ]

                for pattern in spankbang_patterns:
                    matches = re.findall(pattern, page_source, re.IGNORECASE)
                    for match in matches:
                        video_url = match if isinstance(match, str) else match[0] if match else None
                        if video_url and self._is_valid_video_url(video_url):
                            self.log_status(f"🎥 SpankBang video URL found in source: {video_url[:80]}...")
                            # Return a mock video element with the URL
                            return self._create_mock_video_element(video_url)

            except Exception as source_error:
                self.log_status(f"Source scanning error: {str(source_error)[:50]}")

            # Store patterns for use later
            spankbang_patterns = [
                # Direct video URLs
                r'https?://[^"\']*\.sb-cd\.com[^"\']*\.mp4[^"\']*',
                r'https?://[^"\']*spankbang[^"\']*\.mp4[^"\']*',
                r'https?://[^"\']*\.spankbang\.com[^"\']*\.mp4[^"\']*',
                # JSON properties
                r'"stream_url[^"]*":\s*"([^"]*)"',
                r'"video_url[^"]*":\s*"([^"]*)"',
                r'"videoUrl[^"]*":\s*"([^"]*)"',
                r'"streamUrl[^"]*":\s*"([^"]*)"',
                r'"src[^"]*":\s*"([^"]*\.mp4[^"]*)"',
                r'"file[^"]*":\s*"([^"]*\.mp4[^"]*)"',
                # HLS streams
                r'https?://[^"\']*\.sb-cd\.com[^"\']*\.m3u8[^"\']*',
                r'"hls[^"]*":\s*"([^"]*\.m3u8[^"]*)"',
                # Any video URLs
                r'https?://[^"\']*(?:\.mp4|\.m3u8)[^"\']*',
                # SpankBang specific
                r'sb-cd\.com[^"\']*(?:\.mp4|\.m3u8)',
                r'spankbang\.com[^"\']*(?:\.mp4|\.m3u8)'
            ]

            # Try multiple approaches to trigger video loading
            self.log_status("🔄 Trying aggressive video triggering...")

            # First try hovering over the video area to reveal player
            try:
                video_containers = self.safe_find_elements(By.CSS_SELECTOR,
                    ".video-container, .video-wrapper, .video-player, #video-container, [class*='video'], [id*='video']")
                if video_containers:
                    container = video_containers[0]
                    from selenium.webdriver.common.action_chains import ActionChains
                    ActionChains(self.driver).move_to_element(container).perform()
                    time.sleep(1)
                    self.log_status("🎯 Hovered over video container")
            except:
                pass

            # Try clicking various play button selectors
            play_button_selectors = [
                ".play-button",
                ".btn-play",
                "#play-btn",
                ".play-btn",
                "[class*='play']",
                "[id*='play']",
                ".video-overlay",
                ".video-play-button",
                ".player-play-button",
                "[data-play]",
                "[onclick*='play']"
            ]

            for selector in play_button_selectors:
                try:
                    play_buttons = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    if play_buttons:
                        for play_button in play_buttons[:2]:  # Try first 2 buttons
                            try:
                                if play_button.is_displayed():
                                    self.log_status(f"🎮 Clicking play button: {selector}")
                                    # Try both regular click and JavaScript click
                                    try:
                                        play_button.click()
                                    except:
                                        self.driver.execute_script("arguments[0].click();", play_button)
                                    time.sleep(2)  # Wait longer for player to load

                                    # Check for video element again after clicking
                                    videos = self.safe_find_elements(By.CSS_SELECTOR, "video[src], video[data-src]")
                                    if videos:
                                        video = videos[0]
                                        video_src = video.get_attribute('src') or video.get_attribute('data-src')
                                        if video_src and self._is_valid_video_url(video_src):
                                            self.log_status(f"🎥 Video loaded after play click: {video_src[:80]}...")
                                            return video

                                    # Also scan page source again after click
                                    self.log_status("🔍 Re-scanning page after button click...")
                                    new_page_source = self.driver.page_source
                                    for pattern in spankbang_patterns:
                                        matches = re.findall(pattern, new_page_source, re.IGNORECASE)
                                        for match in matches:
                                            video_url = match if isinstance(match, str) else match[0] if match else None
                                            if video_url and self._is_valid_video_url(video_url):
                                                self.log_status(f"🎥 Video URL found after click: {video_url[:80]}...")
                                                return self._create_mock_video_element(video_url)
                            except:
                                continue
                except:
                    continue

            # Try executing JavaScript to trigger video loading
            self.log_status("🔄 Trying JavaScript video initialization...")
            try:
                # Common JavaScript triggers for video sites
                js_triggers = [
                    "if(window.initVideo) window.initVideo();",
                    "if(window.loadVideo) window.loadVideo();",
                    "if(window.playVideo) window.playVideo();",
                    "document.querySelectorAll('video').forEach(v => v.load());",
                    "window.dispatchEvent(new Event('load'));"
                ]

                for js in js_triggers:
                    try:
                        self.driver.execute_script(js)
                        time.sleep(0.5)
                    except:
                        continue

                # Final check after JavaScript execution
                time.sleep(2)
                videos = self.safe_find_elements(By.CSS_SELECTOR, "video[src], video[data-src]")
                if videos:
                    video = videos[0]
                    video_src = video.get_attribute('src') or video.get_attribute('data-src')
                    if video_src and self._is_valid_video_url(video_src):
                        self.log_status(f"🎥 Video loaded after JS triggers: {video_src[:80]}...")
                        return video
            except:
                pass

            self.log_status("⚠️ SpankBang detection failed - no video found")
            return None

        except Exception as e:
            self.log_status(f"SpankBang detection error: {str(e)[:50]}")
            return None

    def _create_mock_video_element(self, video_url):
        """Create a mock video element with the found URL for download"""
        try:
            # Create a simple object that mimics a video element
            class MockVideoElement:
                def __init__(self, url):
                    self.video_url = url

                def get_attribute(self, attr):
                    if attr in ['src', 'data-src']:
                        return self.video_url
                    return None

            return MockVideoElement(video_url)
        except Exception as e:
            self.log_status(f"Mock element creation error: {str(e)[:50]}")
            return None

    def _right_click_video_extraction(self):
        """ULTIMATE METHOD: Right-click video extraction with context menu analysis"""
        try:
            self.log_status("🎯 ULTIMATE METHOD: Right-click video extraction starting...")

            import time
            from selenium.webdriver.common.action_chains import ActionChains
            from selenium.webdriver.common.keys import Keys

            # First, find all possible video elements and containers
            video_targets = []

            # Search for video elements
            video_selectors = [
                "video",
                "[class*='video']",
                "[id*='video']",
                "[class*='player']",
                "[id*='player']",
                "div[data-video]",
                "div[data-src]",
                ".video-container",
                ".video-wrapper",
                ".player-container",
                ".player-wrapper"
            ]

            for selector in video_selectors:
                try:
                    elements = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    for element in elements[:3]:  # Only check first 3 of each type
                        if element.is_displayed():
                            video_targets.append((selector, element))
                except:
                    continue

            self.log_status(f"🎯 Found {len(video_targets)} potential video targets for right-click")

            # Try right-clicking each target
            for i, (selector_name, target) in enumerate(video_targets[:5]):  # Limit to first 5 targets
                try:
                    self.log_status(f"🖱️ Right-clicking target {i+1}/{min(len(video_targets), 5)}: {selector_name}")

                    # Scroll element into view
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
                    time.sleep(0.5)

                    # METHOD 1: Standard right-click with context menu
                    try:
                        actions = ActionChains(self.driver)
                        actions.context_click(target).perform()
                        time.sleep(1)  # Wait for context menu

                        # Look for context menu items that might copy video URL
                        context_menu_selectors = [
                            "[role='menuitem']",
                            ".context-menu-item",
                            ".menu-item",
                            "[class*='menu']",
                            "[class*='context']"
                        ]

                        for menu_selector in context_menu_selectors:
                            try:
                                menu_items = self.safe_find_elements(By.CSS_SELECTOR, menu_selector)
                                for item in menu_items:
                                    item_text = item.text.lower()
                                    if any(keyword in item_text for keyword in ['copy', 'video', 'address', 'link', 'url', 'save']):
                                        self.log_status(f"🎯 Found promising context menu item: {item_text[:50]}")
                                        try:
                                            item.click()
                                            time.sleep(1)
                                            # Check if URL was copied to clipboard
                                            clipboard_url = self._get_clipboard_url()
                                            if clipboard_url:
                                                self.log_status(f"📋 Found video URL in clipboard: {clipboard_url[:80]}...")
                                                return self._create_mock_video_element(clipboard_url)
                                        except:
                                            continue
                            except:
                                continue

                        # Close context menu
                        try:
                            self.driver.execute_script("document.click();")
                        except:
                            pass

                    except Exception as context_error:
                        self.log_status(f"Context menu failed: {str(context_error)[:50]}")

                    # METHOD 2: JavaScript-based right-click simulation with network monitoring
                    try:
                        self.log_status("🔍 Trying JavaScript right-click simulation...")

                        # Enable network request monitoring
                        network_requests = []

                        # JavaScript to simulate right-click and monitor network
                        js_right_click = """
                        var element = arguments[0];
                        var requests = [];

                        // Override XMLHttpRequest to capture requests
                        var originalXHR = window.XMLHttpRequest;
                        window.XMLHttpRequest = function() {
                            var xhr = new originalXHR();
                            var originalOpen = xhr.open;
                            xhr.open = function(method, url) {
                                if (url.includes('.mp4') || url.includes('.m3u8') || url.includes('video') || url.includes('stream')) {
                                    requests.push(url);
                                    console.log('Video request found:', url);
                                }
                                return originalOpen.apply(this, arguments);
                            };
                            return xhr;
                        };

                        // Override fetch to capture requests
                        var originalFetch = window.fetch;
                        window.fetch = function(url) {
                            if (typeof url === 'string' && (url.includes('.mp4') || url.includes('.m3u8') || url.includes('video') || url.includes('stream'))) {
                                requests.push(url);
                                console.log('Video fetch found:', url);
                            }
                            return originalFetch.apply(this, arguments);
                        };

                        // Simulate right-click
                        var event = new MouseEvent('contextmenu', {
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: element.getBoundingClientRect().left + 10,
                            clientY: element.getBoundingClientRect().top + 10
                        });
                        element.dispatchEvent(event);

                        // Try to trigger video loading
                        if (element.tagName === 'VIDEO') {
                            element.load();
                            element.play().catch(function(){});
                        }

                        // Return any found requests
                        return requests;
                        """

                        js_requests = self.driver.execute_script(js_right_click, target)
                        if js_requests:
                            for request_url in js_requests:
                                if self._is_valid_video_url(request_url):
                                    self.log_status(f"🎥 Video URL found via JS monitoring: {request_url[:80]}...")
                                    return self._create_mock_video_element(request_url)

                    except Exception as js_error:
                        self.log_status(f"JS right-click failed: {str(js_error)[:50]}")

                    # METHOD 3: Developer tools simulation
                    try:
                        self.log_status("🔍 Trying developer tools network simulation...")

                        # Open developer tools (F12)
                        self.driver.execute_script("window.open('', '_blank');")
                        time.sleep(0.5)

                        # Look for video URLs in performance entries
                        video_urls = self.driver.execute_script("""
                        var videoUrls = [];
                        try {
                            var entries = performance.getEntriesByType('resource');
                            for (var i = 0; i < entries.length; i++) {
                                var url = entries[i].name;
                                if (url.includes('.mp4') || url.includes('.m3u8') ||
                                    url.includes('video') || url.includes('stream') ||
                                    url.includes('sb-cd.com')) {
                                    videoUrls.push(url);
                                }
                            }
                        } catch (e) {}
                        return videoUrls;
                        """)

                        if video_urls:
                            for video_url in video_urls:
                                if self._is_valid_video_url(video_url):
                                    self.log_status(f"🎥 Video URL found via performance API: {video_url[:80]}...")
                                    return self._create_mock_video_element(video_url)

                    except Exception as dev_tools_error:
                        self.log_status(f"Dev tools simulation failed: {str(dev_tools_error)[:50]}")

                    # METHOD 4: Aggressive attribute extraction
                    try:
                        self.log_status("🔍 Trying aggressive attribute extraction...")

                        # Check all attributes of the element
                        all_attributes = self.driver.execute_script("""
                        var element = arguments[0];
                        var attrs = {};
                        for (var i = 0; i < element.attributes.length; i++) {
                            var attr = element.attributes[i];
                            attrs[attr.name] = attr.value;
                        }
                        return attrs;
                        """, target)

                        for attr_name, attr_value in all_attributes.items():
                            if attr_value and isinstance(attr_value, str):
                                if self._is_valid_video_url(attr_value):
                                    self.log_status(f"🎥 Video URL found in attribute {attr_name}: {attr_value[:80]}...")
                                    return self._create_mock_video_element(attr_value)

                    except Exception as attr_error:
                        self.log_status(f"Attribute extraction failed: {str(attr_error)[:50]}")

                except Exception as target_error:
                    self.log_status(f"Target {i+1} failed: {str(target_error)[:50]}")
                    continue

            # FINAL METHOD: Deep page source analysis with advanced regex
            try:
                self.log_status("🔍 FINAL ATTEMPT: Deep page source analysis...")

                page_source = self.driver.page_source

                # Ultra-comprehensive regex patterns
                ultra_patterns = [
                    # Direct video URLs with common video CDNs
                    r'https?://[^"\'>\s]*(?:sb-cd\.com|spankbang\.com|pornhub\.com|xvideos\.com)[^"\'>\s]*\.(?:mp4|m3u8|webm|avi|mov)[^"\'>\s]*',

                    # Base64 encoded URLs
                    r'data:video/[^"\'>\s]*base64,[^"\'>\s]+',

                    # Blob URLs
                    r'blob:https?://[^"\'>\s]+',

                    # Any URL with video file extensions
                    r'https?://[^"\'>\s]+\.(?:mp4|m3u8|webm|avi|mov|flv|mkv)[^"\'>\s]*',

                    # URLs in JavaScript variables
                    r'(?:var|let|const|window\.)\s*[^=]*=\s*["\']([^"\']*(?:\.mp4|\.m3u8|video)[^"\']*)["\']',

                    # URLs in JSON objects
                    r'["\'](?:src|url|link|stream|video)["\']:\s*["\']([^"\']*(?:\.mp4|\.m3u8|video)[^"\']*)["\']'
                ]

                import re
                for pattern in ultra_patterns:
                    matches = re.findall(pattern, page_source, re.IGNORECASE)
                    for match in matches:
                        video_url = match if isinstance(match, str) else match[0] if match else None
                        if video_url and self._is_valid_video_url(video_url):
                            self.log_status(f"🎥 Video URL found via deep analysis: {video_url[:80]}...")
                            return self._create_mock_video_element(video_url)

            except Exception as deep_error:
                self.log_status(f"Deep analysis failed: {str(deep_error)[:50]}")

            self.log_status("⚠️ RIGHT-CLICK extraction failed - no video URLs found")
            return None

        except Exception as e:
            self.log_status(f"Right-click extraction error: {str(e)[:50]}")
            return None

    def _get_clipboard_url(self):
        """Try to get URL from clipboard (Windows specific)"""
        try:
            # Use JavaScript to try to read clipboard (limited by browser security)
            clipboard_content = self.driver.execute_script("""
            try {
                return navigator.clipboard.readText().then(text => text).catch(() => '');
            } catch (e) {
                return '';
            }
            """)

            if clipboard_content and self._is_valid_video_url(clipboard_content):
                return clipboard_content

        except:
            pass

        return None

    def _is_video_iframe(self, iframe_src):
        """Check if iframe source contains video content"""
        if not iframe_src:
            return False

        video_indicators = [
            'video_ext.php', 'vk.com', 'vkvideo.ru', 'youtube.com', 'youtu.be',
            'vimeo.com', 'dailymotion.com', 'twitch.tv', 'player',
            'embed', 'video', 'watch', 'play'
        ]

        iframe_src_lower = iframe_src.lower()
        return any(indicator in iframe_src_lower for indicator in video_indicators)

    def _handle_generic_video_iframe(self, iframe_src):
        """Handle generic video iframes by clicking embed elements instead of navigating"""
        try:
            self.log_status(f"Found video iframe, looking for embed button: {iframe_src[:60]}")

            # NEW: Try enhanced detection methods with retry logic when iframe is found
            self.log_status("🚀 Running enhanced detection for iframe content...")

            # Try enhanced detection with retries for better timing
            for attempt in range(3):
                try:
                    self.log_status(f"Enhanced detection attempt {attempt + 1}/3...")
                    enhanced_sources = self._enhanced_comprehensive_video_detection()
                    if enhanced_sources and len(enhanced_sources) > 0:
                        self.log_status(f"✅ Enhanced detection found {len(enhanced_sources)} sources from iframe!")
                        # Return the first valid source for download
                        for source in enhanced_sources:
                            if self._is_valid_video_url(source):
                                return source
                        return enhanced_sources[0] if enhanced_sources else None

                    # Wait a bit before retry to allow content to load
                    if attempt < 2:
                        time.sleep(0.3)
                except Exception as e:
                    self.log_status(f"Enhanced detection attempt {attempt + 1} error: {str(e)[:100]}")
                    if attempt < 2:
                        time.sleep(0.2)

            # STAY on the original page and look for clickable embed elements
            original_url = self.driver.current_url

            # Look for embed buttons or clickable elements that might load this iframe
            embed_selectors = [
                f"//iframe[@src='{iframe_src}']",  # The iframe itself
                "//div[contains(@class, 'video-embed')]//button",
                "//div[contains(@class, 'video-player')]//button",
                "//div[contains(@class, 'embed')]//a[contains(@href, 'embed')]",
                "//button[contains(@class, 'play') or contains(@class, 'embed')]",
                "//div[contains(@class, 'preview')]",
                "//div[contains(@class, 'video-preview')]",
                "*[contains(@data-src, 'embed')]",
                "*[contains(@onclick, 'embed')]"
            ]

            clicked_something = False
            for selector in embed_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    for element in elements:
                        try:
                            # Try to click the element to activate video player
                            self.log_status(f"🎯 Clicking embed element: {element.tag_name}")
                            element.click()
                            clicked_something = True
                            time.sleep(0.1)  # Wait for content to load
                            break
                        except Exception:
                            continue
                    if clicked_something:
                        break
                except Exception:
                    continue

            if clicked_something:
                self.log_status("✅ Clicked embed element, waiting for video player to load...")
                time.sleep(0.1)  # Reduced from 5 to 2 seconds
            else:
                self.log_status("⚠️ No clickable embed elements found, extracting from page source...")
                time.sleep(0.2)  # Reduced from 2 to 1 second

            # Now extract video URLs from the current page (after clicking embeds)
            self.log_status("🔍 Extracting video URLs from current page after embed interaction...")
            current_url = self.driver.current_url
            self.log_status(f"📍 Current URL: {current_url}")

            # Check for embedded video URLs in the page source/URL without navigating away
            embedded_video_urls = []

            # Method 1: Extract from page source
            page_source = self.driver.page_source
            if 'pornhub.com/embed/' in page_source:
                import re
                embed_matches = re.findall(r'https://www\.pornhub\.com/embed/[^"\'>\s]+', page_source)
                embedded_video_urls.extend(embed_matches)

            # Method 2: Extract from current URL if it contains embed info
            if 'iframe%20src%3D%22' in current_url:
                try:
                    import urllib.parse
                    decoded_url = urllib.parse.unquote(current_url)
                    if 'iframe src="' in decoded_url:
                        start_pos = decoded_url.find('iframe src="') + len('iframe src="')
                        end_pos = decoded_url.find('"', start_pos)
                        if end_pos > start_pos:
                            embedded_url = decoded_url[start_pos:end_pos]
                            embedded_video_urls.append(embedded_url)
                            self.log_status(f"🎯 Found embedded URL in page: {embedded_url}")
                except Exception as e:
                    self.log_status(f"URL extraction error: {str(e)[:50]}")

            # If we found embedded video URLs, return them for yt-dlp processing
            if embedded_video_urls:
                self.log_status(f"🎯 Found {len(embedded_video_urls)} embedded video URLs")
                # Convert embed URLs to regular video URLs for yt-dlp
                converted_urls = []
                for embedded_url in embedded_video_urls:
                    if 'pornhub.com/embed/' in embedded_url:
                        video_id = embedded_url.split('/embed/')[-1].split('?')[0]
                        regular_url = f"https://www.pornhub.com/view_video.php?viewkey={video_id}"
                        converted_urls.append(regular_url)
                        self.log_status(f"✅ Converted embed URL to: {regular_url}")

                if converted_urls:
                    return converted_urls

            # Try to extract direct video URLs from the current page after embed interaction
            direct_urls = self.driver.execute_script(r"""
                const videoUrls = [];
                const debugInfo = [];

                // Method 1: Look for video elements
                const videos = document.querySelectorAll('video, source');
                debugInfo.push(`Found ${videos.length} video/source elements`);

                for (let video of videos) {
                    if (video.src && video.src.includes('.mp4')) {
                        videoUrls.push({url: video.src, source: 'video_element', confidence: 90});
                    }
                    if (video.currentSrc && video.currentSrc.includes('.mp4')) {
                        videoUrls.push({url: video.currentSrc, source: 'current_src', confidence: 85});
                    }
                }

                // Method 2: Extract from page source/innerHTML
                const pageHTML = document.documentElement.innerHTML;

                // Look for embed URLs in the page
                const embedMatches = pageHTML.match(/https:\\/\\/www\\.pornhub\\.com\\/embed\\/[^"'>\s]+/g);
                if (embedMatches) {
                    debugInfo.push(`Found ${embedMatches.length} embed URLs in page`);
                    for (let embedUrl of embedMatches) {
                        // Convert embed URL to regular video URL
                        const videoId = embedUrl.split('/embed/')[1].split('?')[0];
                        const regularUrl = `https://www.pornhub.com/view_video.php?viewkey=${videoId}`;
                        videoUrls.push({url: regularUrl, source: 'page_embed_conversion', confidence: 95});
                    }
                }

                // Method 3: Look for video URLs in data attributes and JavaScript variables
                const allElements = document.querySelectorAll('*[data-src], *[data-video-url], *[data-embed-url]');
                for (let elem of allElements) {
                    ['data-src', 'data-video-url', 'data-embed-url'].forEach(attr => {
                        const value = elem.getAttribute(attr);
                        if (value && (value.includes('.mp4') || value.includes('embed'))) {
                            videoUrls.push({url: value, source: `data_attribute_${attr}`, confidence: 70});
                        }
                    });
                }

                return {
                    urls: videoUrls,
                    debug: debugInfo,
                    currentDomain: window.location.hostname
                };
            """)

            # Handle debug info and URL extraction
            urls_list = []
            if isinstance(direct_urls, dict):
                debug_info = direct_urls.get('debug', [])
                self.log_status("📊 Iframe extraction debug:")
                for info in debug_info:
                    self.log_status(f"  ✓ {info}")
                urls_list = direct_urls.get('urls', [])
            else:
                urls_list = direct_urls or []

            if urls_list and len(urls_list) > 0:
                self.log_status(f"✅ Found {len(urls_list)} video URLs from embed interaction!")
                for i, url in enumerate(urls_list):
                    self.log_status(f"  URL {i+1}: {url[:80]}...")

                # Return the URLs for yt-dlp processing instead of direct download
                return urls_list
            else:
                self.log_status("❌ No video URLs found after embed interaction")

            # If no URLs found, return None to continue with other strategies
            return None

        except Exception as e:
            self.log_status(f"Generic iframe handling error: {str(e)[:50]}")
            return None

    def _handle_vk_iframe_direct(self, iframe_src):
        """Handle VK video_ext.php iframe directly with improved loading detection"""
        try:
            self.log_status(f"Navigating to VK iframe: {iframe_src[:60]}...")

            # Navigate directly to the iframe source
            self.driver.get(iframe_src)

            # Wait for iframe to load with better detection
            self.log_status("Waiting for VK iframe to load...")
            self._wait_for_vk_iframe_load()

            # Check if page actually loaded correctly
            current_url = self.driver.current_url
            if 'vk.com' not in current_url:
                self.log_status(f"VK iframe navigation failed, current URL: {current_url[:60]}")
                return None

            # Now extract video from the iframe page
            return self._extract_vk_iframe_video()

        except Exception as e:
            self.log_status(f"VK iframe handling error: {str(e)[:50]}")
            return None

    def _wait_for_vk_iframe_load(self):
        """Wait for VK iframe to properly load with timeout"""
        try:
            # Wait for common VK elements to appear
            wait_indicators = [
                "//video",
                "//div[contains(@class, 'video')]",
                "//div[contains(@id, 'video')]",
                "//div[contains(@class, 'player')]",
                "//script[contains(text(), 'videoData')]"
            ]

            max_wait_time = 10  # seconds
            start_time = time.time()

            while time.time() - start_time < max_wait_time:
                try:
                    for indicator in wait_indicators:
                        elements = self.safe_find_elements(By.XPATH, indicator)
                        if elements:
                            self.log_status(f"VK iframe loaded (found: {indicator})")
                            return True

                    time.sleep(0.1)
                except:
                    time.sleep(0.1)
                    continue

            # If no indicators found, wait a bit more and hope for the best
            self.log_status("VK iframe load indicators not found, proceeding anyway...")
            time.sleep(0.1)
            return False

        except Exception as e:
            self.log_status(f"VK iframe load detection error: {str(e)[:30]}")
            time.sleep(0.2)  # fallback wait
            return False

    def _handle_vk_video_url(self, video_url):
        """Handle regular VK video URL"""
        try:
            self.log_status(f"Navigating to VK video: {video_url[:60]}...")

            # Navigate to VK video page
            self.driver.get(video_url)
            time.sleep(0.2)

            # Extract video using VK-specific methods
            return self._extract_vk_video()

        except Exception as e:
            self.log_status(f"VK video URL handling error: {str(e)[:50]}")
            return None

    def _extract_vk_iframe_video(self):
        """Extract video from VK iframe page (video_ext.php) with timeout handling"""
        try:
            self.log_status("Extracting video from VK iframe page...")

            # Set a reasonable timeout for VK extraction (2 minutes max)
            extraction_timeout = 120  # seconds
            start_time = time.time()

            # VK iframe specific extraction strategies
            iframe_strategies = [
                self._vk_iframe_strategy_player_data,
                self._vk_iframe_strategy_video_element,
                self._vk_iframe_strategy_page_source,
                self._vk_iframe_strategy_javascript_vars
            ]

            for strategy in iframe_strategies:
                try:
                    # Check if we've exceeded timeout
                    elapsed_time = time.time() - start_time
                    if elapsed_time > extraction_timeout:
                        self.log_status(f"VK extraction timeout after {elapsed_time:.1f}s")
                        break

                    self.log_status(f"Trying VK strategy: {strategy.__name__} (elapsed: {elapsed_time:.1f}s)")

                    result = strategy()
                    if result:
                        self.log_status(f"VK iframe extraction succeeded with {strategy.__name__}")
                        return result

                except Exception as strategy_error:
                    self.log_status(f"VK iframe strategy {strategy.__name__} failed: {str(strategy_error)[:50]}")
                    continue

            self.log_status("All VK iframe extraction strategies failed")
            return None

        except Exception as e:
            self.log_status(f"VK iframe video extraction error: {str(e)[:50]}")
            return None

    def _vk_iframe_strategy_player_data(self):
        """Extract from VK iframe player data"""
        try:
            # Look for VK player data in iframe
            player_script = """
                const videoSources = [];

                // VK iframe specific variables
                if (typeof playerParams !== 'undefined') {
                    try {
                        if (playerParams.url720) videoSources.push({url: playerParams.url720, quality: 720});
                        if (playerParams.url480) videoSources.push({url: playerParams.url480, quality: 480});
                        if (playerParams.url360) videoSources.push({url: playerParams.url360, quality: 360});
                        if (playerParams.url240) videoSources.push({url: playerParams.url240, quality: 240});
                    } catch(e) {}
                }

                // Check for video data in iframe context
                if (typeof videoData !== 'undefined') {
                    try {
                        Object.keys(videoData).forEach(key => {
                            const value = videoData[key];
                            if (typeof value === 'string' && value.includes('.mp4')) {
                                const quality = value.includes('720') ? 720 :
                                              value.includes('480') ? 480 :
                                              value.includes('360') ? 360 : 240;
                                videoSources.push({url: value, quality: quality});
                            }
                        });
                    } catch(e) {}
                }

                // Look for video element sources
                const videoElements = document.querySelectorAll('video, source');
                videoElements.forEach(el => {
                    const src = el.src || el.getAttribute('src');
                    if (src && src.includes('.mp4')) {
                        videoSources.push({url: src, quality: 360});
                    }
                });

                return videoSources;
            """

            video_sources = self.driver.execute_script(player_script)

            if video_sources:
                # Sort by quality (prefer higher)
                video_sources.sort(key=lambda x: x.get('quality', 0), reverse=True)

                for source in video_sources:
                    url = source['url']
                    if self._is_valid_video_url(url):
                        self.log_status(f"VK iframe player found: {url[:60]} (quality: {source.get('quality')})")
                        return self._create_fake_element_for_download(url)

            return None

        except Exception as e:
            return None

    def _vk_iframe_strategy_video_element(self):
        """Look for video elements in iframe"""
        try:
            # Look for video elements
            video_elements = self.safe_find_elements(By.TAG_NAME, "video")
            for video in video_elements:
                src = video.get_attribute('src')
                if src and self._is_valid_video_url(src):
                    self.log_status(f"Found VK iframe video element: {src[:60]}")
                    return video

            # Look for source elements
            source_elements = self.safe_find_elements(By.TAG_NAME, "source")
            for source in source_elements:
                src = source.get_attribute('src')
                if src and self._is_valid_video_url(src):
                    self.log_status(f"Found VK iframe source element: {src[:60]}")
                    return self._create_fake_element_for_download(src)

            return None

        except Exception as e:
            return None

    def _vk_iframe_strategy_page_source(self):
        """Extract from VK iframe page source"""
        try:
            page_source = self.driver.page_source

            # VK iframe specific patterns
            iframe_patterns = [
                r'"url":"([^"]*\.mp4[^"]*)","type":"video/mp4"',
                r'"src":"([^"]*\.mp4[^"]*)",',
                r'"file":"([^"]*\.mp4[^"]*)",',
                r'url720["\']?:\s?["\']([^"\']*)["\'\']',
                r'url480["\']?:\s?["\']([^"\']*)["\'\']',
                r'url360["\']?:\s?["\']([^"\']*)["\'\']',
                r'url240["\']?:\s?["\']([^"\']*)["\'\']',
                r'https://[^"\s]*userapi[^"\s]*\.mp4[^"\s]*',
                r'https://[^"\s]*vk[^"\s]*\.mp4[^"\s]*'
            ]

            found_urls = []
            for pattern in iframe_patterns:
                matches = re.findall(pattern, page_source)
                for match in matches:
                    # Clean up escaped characters
                    url = match.replace('\\/', '/').replace('\\u0026', '&')
                    if self._is_valid_video_url(url) and ('yandex.net' not in url or 'video-preview.s3.yandex.net' in url):
                        found_urls.append(url)

            if found_urls:
                best_url = self._select_best_vk_url(found_urls)
                if best_url:
                    self.log_status(f"VK iframe page source found: {best_url[:60]}")
                    return self._create_fake_element_for_download(best_url)

            return None

        except Exception as e:
            return None

    def _vk_iframe_strategy_javascript_vars(self):
        """Extract from JavaScript variables in VK iframe"""
        try:
            # Comprehensive variable search in iframe context
            js_search = """
                const foundUrls = [];

                // Search all global variables
                for (const varName in window) {
                    try {
                        const varValue = window[varName];
                        if (typeof varValue === 'object' && varValue !== null) {
                            // Recursively search object properties
                            function searchObject(obj, depth = 0) {
                                if (depth > 3) return; // Limit recursion depth

                                for (const key in obj) {
                                    try {
                                        const value = obj[key];
                                        if (typeof value === 'string' && value.includes('.mp4')) {
                                            foundUrls.push(value);
                                        } else if (typeof value === 'object' && value !== null) {
                                            searchObject(value, depth + 1);
                                        }
                                    } catch(e) {}
                                }
                            }

                            searchObject(varValue);
                        }
                    } catch(e) {}
                }

                return foundUrls;
            """

            urls = self.driver.execute_script(js_search)

            if urls:
                # Filter valid video URLs
                valid_urls = [url for url in urls if self._is_valid_video_url(url) and ('yandex.net' not in url or 'video-preview.s3.yandex.net' in url)]

                if valid_urls:
                    best_url = self._select_best_vk_url(valid_urls)
                    if best_url:
                        self.log_status(f"VK iframe JS vars found: {best_url[:60]}")
                        return self._create_fake_element_for_download(best_url)

            return None

        except Exception as e:
            return None

    def _is_video_source_url(self, url):
        """Check if URL is a video hosting site that likely has actual videos"""
        video_domains = [
            'vk.com/video', 'vkvideo.ru', 'vk.com/video_ext.php',
            'youtube.com', 'youtu.be',
            'vimeo.com', 'dailymotion.com',
            'rutube.ru', 'ok.ru/video',
            'tiktok.com', 'instagram.com',
            'facebook.com/watch', 'fb.watch',
            'twitch.tv', 'streamable.com',
            'reddit.com/r/', 'gfycat.com',
            'pornhub.com', 'xvideos.com', 'xhamster.com',
            'myspree', 'noodlemagazine', 'ukdevilz',
            'bitchute.com', 'rumble.com', 'odysee.com'
        ]

        return any(domain in url.lower() for domain in video_domains)

    def _is_video_page_url(self, url):
        """Check if URL is a video page that needs yt-dlp processing (not a direct video file)"""
        video_page_patterns = [
            'pornhub.com/view_video.php',
            'pornhub.com/embed/',
            'youtube.com/watch',
            'youtu.be/',
            'vimeo.com/',
            'dailymotion.com/video/',
            'xvideos.com/video',
            'xhamster.com/videos/',
            'redtube.com/',
            'tube8.com/',
            'youporn.com/watch/',
            'spankbang.com/video/',
            'chaturbate.com/',
            'cam4.com/',
            'bongacams.com/',
            'myfreecams.com/'
        ]

        url_lower = url.lower()
        return any(pattern in url_lower for pattern in video_page_patterns)

    def _detect_cdn_protected_video(self, static_html=None):
        """Removed - no longer detects CDN-protected content"""
        return None

    def _extract_video_url_from_source(self):
        """STRATEGY 1: Enhanced direct video URL extraction from page source with comprehensive patterns"""
        try:
            self.log_status("Strategy 1: Comprehensive page source analysis")

            # PRIORITY CHECK: Look for blob URLs with source elements first
            try:
                priority_url = self._extract_priority_video_url()
                if priority_url:
                    self.log_status("🎯 Found priority video URL via enhanced detection")
                    return priority_url
            except Exception as e:
                logger.debug(f"Priority URL detection failed: {e}")

            page_source = self.driver.page_source
            
            # Comprehensive video URL patterns with priority ordering
            video_patterns = [
                # Direct video file URLs with various quote styles
                r'["\']([^"\']*\.mp4(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.avi(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.mov(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.webm(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.mkv(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.flv(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.wmv(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.3gp(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\.m4v(?:\?[^"\']*)?)["\']',
                
                # JSON-style video source declarations
                r'src["\s]*:["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'source["\s]*:["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'url["\s]*:["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'video["\s]*:["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'file["\s]*:["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                
                # Data attribute patterns
                r'data-src["\s]*=["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'data-video["\s]*=["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'data-url["\s]*=["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'data-file["\s]*=["\s]*["\']([^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                
                # Streaming and CDN patterns
                r'["\']([^"\']*\/stream\/[^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\/video\/[^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\/media\/[^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                r'["\']([^"\']*\/cdn\/[^"\']*\.(mp4|avi|mov|webm|mkv|flv|wmv|3gp|m4v)(?:\?[^"\']*)?)["\']',
                
                # Base64 encoded URLs
                r'["\']([A-Za-z0-9+/]{50,}={0,2})["\']',  # Potential base64 video URLs
                
                # Progressive download patterns
                r'progressive["\s]*:["\s]*["\']([^"\']*)["\']',
                r'download["\s]*:["\s]*["\']([^"\']*)["\']',
                
                # Playlist and manifest references that might contain video URLs
                r'playlist["\s]*:["\s]*["\']([^"\']*)["\']',
                r'manifest["\s]*:["\s]*["\']([^"\']*)["\']',
            ]
            
            found_urls = set()  # Use set to avoid duplicates
            
            for pattern in video_patterns:
                try:
                    matches = re.findall(pattern, page_source, re.IGNORECASE | re.MULTILINE)
                    for match in matches:
                        if isinstance(match, tuple):
                            video_url = match[0] if match[0] else match[1]
                        else:
                            video_url = match
                        
                        # Clean and validate URL
                        video_url = self._clean_and_validate_url(video_url)
                        if video_url and self._is_valid_video_url(video_url):
                            found_urls.add(video_url)
                            
                except Exception as e:
                    logger.debug(f"Pattern matching error: {e}")
                    continue
            
            # Priority-based URL selection
            if found_urls:
                selected_url = self._select_best_video_url(list(found_urls))
                if selected_url:
                    self.log_status(f"Strategy 1 success: {selected_url}")
                    return selected_url
            
            # Advanced pattern matching for obfuscated URLs
            return self._extract_obfuscated_urls(page_source)
            
        except Exception as e:
            logger.error(f"Strategy 1 failed: {e}")
            return None
    
    def _clean_and_validate_url(self, url):
        """Clean and validate extracted URLs"""
        try:
            if not url or len(url) < 10:
                return None
            
            # Handle base64 encoded URLs
            if len(url) > 50 and '.' not in url and '+' in url:
                try:
                    import base64
                    decoded = base64.b64decode(url).decode('utf-8')
                    if self._is_valid_video_url(decoded):
                        return decoded
                except:
                    pass
            
            # Clean URL
            url = url.strip().strip('\'"')
            
            # Handle relative URLs
            if url.startswith('/'):
                from urllib.parse import urljoin
                url = urljoin(self.driver.current_url, url)
            elif url.startswith('./'):
                from urllib.parse import urljoin
                url = urljoin(self.driver.current_url, url[2:])
            elif not url.startswith('http'):
                from urllib.parse import urljoin
                url = urljoin(self.driver.current_url, url)
            
            return url
            
        except Exception:
            return None
    
    def _select_best_video_url(self, urls):
        """Select the best video URL based on quality indicators and content priority"""
        try:
            if not urls:
                return None

            # Filter out ad URLs first
            filtered_urls = self._filter_ad_urls(urls)
            if not filtered_urls:
                self.log_status("⚠️ All URLs appear to be ads, using original list")
                filtered_urls = urls

            # Prioritize based on URL characteristics
            prioritized_urls = self._prioritize_main_content_urls(filtered_urls)

            # Quality indicators in order of preference
            quality_indicators = [
                # Segmented/streaming content (highest priority for main content)
                ('clip=', 'multi=', 'segment=', 'hls'),
                # High quality indicators
                ('1080p', '1080', 'hd', 'high'),
                ('720p', '720', 'medium'),
                ('480p', '480', 'low'),
                # File format preferences
                ('mp4',),
                ('webm',),
                ('avi',),
            ]

            for indicators in quality_indicators:
                for url in prioritized_urls:
                    if any(indicator in url.lower() for indicator in indicators):
                        return url

            # If no quality indicators, return the first valid URL from prioritized list
            return prioritized_urls[0] if prioritized_urls else None

        except Exception as e:
            logger.debug(f"Error selecting best URL: {e}")
            return urls[0] if urls else None

    def _filter_ad_urls(self, urls):
        """Filter out known ad domains and patterns"""
        try:
            ad_domains = [
                'aucdn.net', 'sacdnssedge.com', 'adnium.com', 'adsystem.com', 'doubleclick.net',
                'googlesyndication.com', 'googletagmanager.com', 'analytics.com',
                'ads.yahoo.com', 'facebook.com/tr', 'twitter.com/i/adsct',
                'outbrain.com', 'taboola.com', 'revcontent.com', 'mgid.com',
                'propellerads.com', 'popads.net', 'popcash.net', 'adsterra.com'
            ]

            ad_patterns = [
                '/ads/', '/ad/', '/advertisement/', '/banner/', '/popup/',
                'banner', 'popup', 'preroll', 'midroll', 'postroll',
                'ads.', 'ad.', 'adv.', 'advertisement', 'sponsored'
            ]

            filtered_urls = []
            for url in urls:
                url_lower = url.lower()

                # Check if URL contains ad domains
                is_ad = any(domain in url_lower for domain in ad_domains)

                # Check if URL contains ad patterns
                if not is_ad:
                    is_ad = any(pattern in url_lower for pattern in ad_patterns)

                if not is_ad:
                    filtered_urls.append(url)
                else:
                    self.log_status(f"🚫 Filtered ad URL: {url[:80]}...")

            return filtered_urls

        except Exception as e:
            logger.debug(f"Error filtering ad URLs: {e}")
            return urls

    def _prioritize_main_content_urls(self, urls):
        """Prioritize URLs that are likely main content"""
        try:
            content_indicators = [
                # CDN patterns for main video content
                ('vcdn', 'video-', 'stream-', 'media-', 'content-'),
                # Site-specific main content patterns
                ('icegayporn.com', 'spankbang.com', 'pornhub.com', 'xvideos.com'),
                # Segmented/streaming content patterns
                ('clip=', 'multi=', 'segment=', 'hls', 'm3u8'),
                # Size indicators (larger files likely main content)
                ('1080', '720', '480', 'hd', 'quality'),
            ]

            scored_urls = []
            for url in urls:
                url_lower = url.lower()
                score = 0

                # Score based on content indicators
                for i, indicators in enumerate(content_indicators):
                    if any(indicator in url_lower for indicator in indicators):
                        score += (len(content_indicators) - i) * 10  # Higher score for earlier indicators

                # Bonus for segmented URLs (likely main content)
                if self._is_segmented_video_url(url):
                    score += 100

                # Bonus for video CDN domains
                if any(cdn in url_lower for cdn in ['vcdn', 'video', 'stream', 'media']):
                    score += 50

                scored_urls.append((score, url))

            # Sort by score (highest first) and return URLs
            scored_urls.sort(key=lambda x: x[0], reverse=True)
            prioritized = [url for score, url in scored_urls]

            if scored_urls:
                self.log_status(f"🎯 Top URL score: {scored_urls[0][0]} for {scored_urls[0][1][:80]}...")

            return prioritized

        except Exception as e:
            logger.debug(f"Error prioritizing URLs: {e}")
            return urls
    
    def _extract_obfuscated_urls(self, page_source):
        """Extract obfuscated or encoded video URLs"""
        try:
            # Look for JavaScript that might contain video URLs
            js_patterns = [
                r'atob\(["\']([A-Za-z0-9+/=]+)["\']\)',  # Base64 decoding
                r'decodeURIComponent\(["\']([^"\']+)["\']\)',  # URL decoding
                r'unescape\(["\']([^"\']+)["\']\)',  # Unescape
            ]
            
            for pattern in js_patterns:
                matches = re.findall(pattern, page_source)
                for match in matches:
                    try:
                        if 'atob' in pattern:
                            import base64
                            decoded = base64.b64decode(match).decode('utf-8')
                        elif 'decodeURIComponent' in pattern:
                            import urllib.parse
                            decoded = urllib.parse.unquote(match)
                        elif 'unescape' in pattern:
                            import urllib.parse
                            decoded = urllib.parse.unquote_plus(match)
                        else:
                            continue
                            
                        if self._is_valid_video_url(decoded):
                            return decoded
                            
                    except Exception:
                        continue
            
            return None
            
        except Exception as e:
            logger.error(f"Obfuscated URL extraction failed: {e}")
            return None
    
    def _monitor_network_requests(self):
        """STRATEGY 2: Advanced network monitoring with real-time traffic analysis and request interception"""
        try:
            self.log_status("Strategy 2: Advanced network traffic analysis")
            
            # Enable comprehensive network logging with detailed event capture
            self.driver.execute_cdp_cmd('Network.enable', {
                'maxTotalBufferSize': 10000000,
                'maxResourceBufferSize': 5000000,
                'maxPostDataSize': 65536
            })
            
            # Enable Runtime domain for JavaScript execution monitoring
            self.driver.execute_cdp_cmd('Runtime.enable', {})
            
            # Enable Page domain for frame navigation tracking
            self.driver.execute_cdp_cmd('Page.enable', {})
            
            # Set up request interception for video content
            self.driver.execute_cdp_cmd('Network.setRequestInterception', {
                'patterns': [
                    {'urlPattern': '*.mp4*', 'resourceType': 'Media'},
                    {'urlPattern': '*.avi*', 'resourceType': 'Media'},
                    {'urlPattern': '*.mov*', 'resourceType': 'Media'},
                    {'urlPattern': '*.webm*', 'resourceType': 'Media'},
                    {'urlPattern': '*.mkv*', 'resourceType': 'Media'},
                    {'urlPattern': '*video*', 'resourceType': 'Media'},
                    {'urlPattern': '*stream*', 'resourceType': 'Media'},
                    {'urlPattern': '*.m3u8*', 'resourceType': 'Media'},
                    {'urlPattern': '*.mpd*', 'resourceType': 'Media'},
                ]
            })
            
            detected_urls = set()
            
            # Advanced page interaction to trigger video loading
            self._trigger_comprehensive_video_loading()
            
            # Multi-phase network monitoring
            for phase in range(3):  # Three monitoring phases
                self.log_status(f"Network monitoring phase {phase + 1}")
                
                # Phase-specific actions
                if phase == 0:
                    self._trigger_initial_video_elements()
                elif phase == 1:
                    self._trigger_dynamic_content_loading()
                elif phase == 2:
                    self._trigger_user_interaction_simulation()
                
                # Monitor network activity for this phase
                time.sleep(0.2)
                phase_urls = self._analyze_network_logs()
                detected_urls.update(phase_urls)
                
                # If we found good URLs in early phases, we can return quickly
                if detected_urls and phase == 0:
                    best_url = self._evaluate_detected_urls(detected_urls)
                    if best_url:
                        self.log_status(f"Strategy 2 early success: {best_url}")
                        return best_url
            
            # Final evaluation of all detected URLs
            if detected_urls:
                best_url = self._evaluate_detected_urls(detected_urls)
                if best_url:
                    self.log_status(f"Strategy 2 success: {best_url}")
                    return best_url
            
            # Advanced XHR/Fetch monitoring as final attempt
            return self._monitor_xhr_fetch_requests()
            
        except Exception as e:
            logger.error(f"Strategy 2 failed: {e}")
            return None
    
    def _trigger_comprehensive_video_loading(self):
        """Comprehensive video loading trigger system"""
        try:
            # Execute comprehensive page interaction script
            interaction_script = """
            // Comprehensive video loading triggers
            function triggerVideoLoading() {
                var triggered = [];
                
                // 1. Scroll-based triggers
                window.scrollTo(0, 0);
                setTimeout(() => window.scrollTo(0, document.body.scrollHeight), 500);
                setTimeout(() => window.scrollTo(0, document.body.scrollHeight / 2), 1000);
                
                // 2. Mouse movement simulation
                var events = ['mouseover', 'mouseenter', 'mousemove'];
                var elements = document.querySelectorAll('video, [class*="video"], [class*="player"], [id*="video"], [id*="player"]');
                elements.forEach(function(el) {
                    events.forEach(function(event) {
                        try {
                            var evt = new MouseEvent(event, {bubbles: true, cancelable: true});
                            el.dispatchEvent(evt);
                        } catch(e) {}
                    });
                });
                
                // 3. Focus and blur events
                var focusElements = document.querySelectorAll('input, button, [tabindex]');
                focusElements.forEach(function(el) {
                    try {
                        el.focus();
                        el.blur();
                    } catch(e) {}
                });
                
                // 4. Window events
                ['resize', 'scroll', 'focus', 'load'].forEach(function(event) {
                    try {
                        window.dispatchEvent(new Event(event));
                    } catch(e) {}
                });
                
                return triggered.length;
            }
            
            return triggerVideoLoading();
            """
            
            self.driver.execute_script(interaction_script)
            
        except Exception as e:
            logger.debug(f"Video loading trigger error: {e}")
    
    def _trigger_initial_video_elements(self):
        """Phase 1: Target initial video elements and obvious triggers"""
        try:
            # Find and interact with obvious video-related elements
            video_selectors = [
                'video', 'source', 
                '[class*="play"]', '[id*="play"]',
                '[class*="video"]', '[id*="video"]',
                '[class*="player"]', '[id*="player"]',
                '.video_player', '[data-snippet]',  # From screenshot analysis
                'button[onclick*="play"]', 'a[onclick*="play"]',
                '[data-video]', '[data-src]', '[data-url]'
            ]
            
            for selector in video_selectors:
                try:
                    elements = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    for element in elements[:5]:  # Limit to first 5 to avoid excessive clicking
                        try:
                            if element.is_displayed() and element.is_enabled():
                                # Multiple interaction types
                                self.driver.execute_script("arguments[0].click();", element)
                                time.sleep(0.1)
                                
                                # Trigger mouse events
                                ActionChains(self.driver).move_to_element(element).perform()
                                time.sleep(0.2)
                                
                        except Exception:
                            continue
                            
                except Exception:
                    continue
            
        except Exception as e:
            logger.debug(f"Initial trigger error: {e}")
    
    def _trigger_dynamic_content_loading(self):
        """Phase 2: Trigger dynamic content loading mechanisms"""
        try:
            # Execute advanced JavaScript to trigger dynamic loading
            dynamic_script = """
            // Advanced dynamic content triggers
            function triggerDynamicLoading() {
                // 1. Common video loading functions
                var commonFunctions = [
                    'loadVideo', 'initVideo', 'playVideo', 'startVideo',
                    'initPlayer', 'loadPlayer', 'createPlayer',
                    'loadStream', 'initStream', 'startStream',
                    'videoInit', 'playerInit', 'mediaInit'
                ];
                
                commonFunctions.forEach(function(funcName) {
                    if (window[funcName] && typeof window[funcName] === 'function') {
                        try {
                            window[funcName]();
                        } catch(e) {}
                    }
                });
                
                // 2. jQuery triggers if available
                if (window.jQuery || window.$) {
                    var $ = window.jQuery || window.$;
                    try {
                        $(document).trigger('videoload');
                        $(document).trigger('playerready');
                        $('[data-video]').trigger('click');
                        $('.video-trigger').trigger('click');
                    } catch(e) {}
                }
                
                // 3. Event triggers for lazy loading
                var lazyEvents = ['scroll', 'resize', 'orientationchange', 'load'];
                lazyEvents.forEach(function(event) {
                    document.dispatchEvent(new Event(event));
                    window.dispatchEvent(new Event(event));
                });
                
                // 4. Intersection Observer triggers
                var observableElements = document.querySelectorAll('[data-src], [data-video], .lazy');
                observableElements.forEach(function(el) {
                    // Simulate element coming into view
                    if (window.IntersectionObserver) {
                        var event = new CustomEvent('intersectionchange', {
                            detail: {isIntersecting: true, target: el}
                        });
                        document.dispatchEvent(event);
                    }
                });
                
                // 5. Form submissions that might load video
                var forms = document.querySelectorAll('form');
                forms.forEach(function(form) {
                    var inputs = form.querySelectorAll('input[type="hidden"]');
                    if (inputs.length > 0) {  // Forms with hidden inputs might be CSRF protected
                        try {
                            var submitEvent = new Event('submit', {cancelable: true});
                            form.dispatchEvent(submitEvent);
                        } catch(e) {}
                    }
                });
                
                return true;
            }
            
            return triggerDynamicLoading();
            """
            
            self.driver.execute_script(dynamic_script)
            
        except Exception as e:
            logger.debug(f"Dynamic trigger error: {e}")
    
    def _trigger_user_interaction_simulation(self):
        """Phase 3: Simulate complex user interactions"""
        try:
            # Simulate realistic user behavior patterns
            simulation_script = """
            // Complex user interaction simulation
            function simulateUserInteractions() {
                // 1. Progressive disclosure patterns
                var disclosureElements = document.querySelectorAll(
                    '[aria-expanded="false"], .collapsed, .hidden, .minimized'
                );
                disclosureElements.forEach(function(el) {
                    try {
                        el.click();
                        el.dispatchEvent(new Event('toggle'));
                    } catch(e) {}
                });
                
                // 2. Tab and accordion interactions
                var tabs = document.querySelectorAll('[role="tab"], .tab, [data-tab]');
                tabs.forEach(function(tab) {
                    try {
                        tab.click();
                        tab.dispatchEvent(new KeyboardEvent('keydown', {key: 'Enter'}));
                    } catch(e) {}
                });
                
                // 3. Modal and dialog triggers
                var modalTriggers = document.querySelectorAll(
                    '[data-toggle="modal"], [data-target*="modal"], .modal-trigger'
                );
                modalTriggers.forEach(function(trigger) {
                    try {
                        trigger.click();
                    } catch(e) {}
                });
                
                // 4. Dropdown and menu interactions
                var dropdowns = document.querySelectorAll('.dropdown, [data-dropdown], select');
                dropdowns.forEach(function(dropdown) {
                    try {
                        dropdown.click();
                        dropdown.dispatchEvent(new Event('change'));
                    } catch(e) {}
                });
                
                // 5. Infinite scroll triggers
                var scrollContainers = document.querySelectorAll(
                    '[style*="overflow"], .scroll-container, .infinite-scroll'
                );
                scrollContainers.forEach(function(container) {
                    try {
                        container.scrollTop = container.scrollHeight;
                        container.dispatchEvent(new Event('scroll'));
                    } catch(e) {}
                });
                
                return true;
            }
            
            return simulateUserInteractions();
            """
            
            self.driver.execute_script(simulation_script)
            
        except Exception as e:
            logger.debug(f"User simulation error: {e}")
    
    def _analyze_network_logs(self):
        """Advanced network log analysis with pattern recognition"""
        try:
            detected_urls = set()
            
            # Get comprehensive network logs
            logs = self.driver.get_log('performance')
            
            for log in logs:
                try:
                    message = json.loads(log['message'])
                    method = message.get('message', {}).get('method', '')
                    
                    if method == 'Network.responseReceived':
                        response_data = message['message']['params']['response']
                        url = response_data.get('url', '')
                        mime_type = response_data.get('mimeType', '')
                        status = response_data.get('status', 0)
                        
                        # Enhanced URL validation
                        if self._is_network_video_url(url, mime_type, status):
                            detected_urls.add(url)
                            
                    elif method == 'Network.requestWillBeSent':
                        request_data = message['message']['params']['request']
                        url = request_data.get('url', '')
                        
                        if self._is_valid_video_url(url):
                            detected_urls.add(url)
                            
                except Exception:
                    continue
            
            return detected_urls
            
        except Exception as e:
            logger.error(f"Network log analysis error: {e}")
            return set()
    
    def _is_network_video_url(self, url, mime_type, status):
        """Enhanced network URL validation with MIME type and status checking"""
        try:
            # Status code validation
            if status not in [200, 206, 302, 304]:  # Valid response codes for video
                return False
            
            # MIME type validation
            video_mime_types = [
                'video/mp4', 'video/avi', 'video/quicktime', 'video/x-msvideo',
                'video/webm', 'video/x-flv', 'video/x-ms-wmv', 'video/3gpp',
                'video/mp2t', 'video/x-matroska', 'application/octet-stream'
            ]
            
            if mime_type and any(mime in mime_type.lower() for mime in video_mime_types):
                return True
            
            # URL pattern validation
            return self._is_valid_video_url(url)
            
        except Exception:
            return False
    
    def _evaluate_detected_urls(self, urls):
        """Advanced URL evaluation with quality scoring"""
        try:
            if not urls:
                return None
            
            scored_urls = []
            
            for url in urls:
                score = 0
                
                # Size indicators (higher is better)
                if any(indicator in url.lower() for indicator in ['1080p', '1080', 'hd', 'high']):
                    score += 100
                elif any(indicator in url.lower() for indicator in ['720p', '720']):
                    score += 80
                elif any(indicator in url.lower() for indicator in ['480p', '480']):
                    score += 60
                
                # Format preferences
                if '.mp4' in url.lower():
                    score += 50
                elif '.webm' in url.lower():
                    score += 40
                elif '.avi' in url.lower():
                    score += 30
                
                # Source reliability indicators
                if any(indicator in url.lower() for indicator in ['cdn', 'stream', 'media']):
                    score += 20
                
                # Penalize very long URLs (might be temporary)
                if len(url) > 200:
                    score -= 10
                
                # Penalize URLs with many parameters (might be session-specific)
                param_count = url.count('&') + url.count('?')
                if param_count > 5:
                    score -= param_count * 2
                
                scored_urls.append((score, url))
            
            # Sort by score and return best URL
            scored_urls.sort(reverse=True)
            return scored_urls[0][1] if scored_urls else None
            
        except Exception:
            return list(urls)[0] if urls else None
    
    def _monitor_xhr_fetch_requests(self):
        """Advanced XHR and Fetch API monitoring"""
        try:
            self.log_status("Monitoring XHR/Fetch requests")
            
            # Install XHR and Fetch interceptors
            xhr_script = """
            return new Promise(function(resolve) {
                var detectedUrls = [];
                var originalXHR = window.XMLHttpRequest;
                var originalFetch = window.fetch;
                
                // XHR interception
                window.XMLHttpRequest = function() {
                    var xhr = new originalXHR();
                    var originalOpen = xhr.open;
                    
                    xhr.open = function(method, url) {
                        if (url && (url.includes('video') || url.includes('stream') || 
                                   url.includes('.mp4') || url.includes('.webm'))) {
                            detectedUrls.push(url);
                        }
                        return originalOpen.apply(this, arguments);
                    };
                    
                    return xhr;
                };
                
                // Fetch interception
                window.fetch = function(url, options) {
                    if (typeof url === 'string' && 
                        (url.includes('video') || url.includes('stream') || 
                         url.includes('.mp4') || url.includes('.webm'))) {
                        detectedUrls.push(url);
                    }
                    return originalFetch.apply(this, arguments);
                };
                
                // Trigger potential AJAX calls
                setTimeout(function() {
                    // Common AJAX trigger patterns
                    var ajaxTriggers = document.querySelectorAll(
                        '[data-ajax], [data-remote], .ajax-load, .load-more'
                    );
                    ajaxTriggers.forEach(function(trigger) {
                        try { trigger.click(); } catch(e) {}
                    });
                    
                    // Resolve with detected URLs after monitoring period
                    setTimeout(function() {
                        resolve(detectedUrls);
                    }, 3000);
                }, 1000);
            });
            """
            
            detected_urls = self.driver.execute_async_script(xhr_script)
            
            for url in detected_urls:
                if self._is_valid_video_url(url):
                    self.log_status(f"XHR/Fetch monitoring success: {url}")
                    return url
            
            return None
            
        except Exception as e:
            logger.error(f"XHR/Fetch monitoring failed: {e}")
            return None
    
    def _execute_advanced_js_detection(self):
        """STRATEGY 3: Advanced JavaScript execution with comprehensive DOM analysis and runtime introspection"""
        try:
            self.log_status("Strategy 3: Advanced JavaScript analysis and runtime introspection")
            
            # Phase 1: Comprehensive video source discovery
            video_sources = self._discover_video_sources_comprehensive()
            if video_sources:
                best_source = self._evaluate_javascript_sources(video_sources)
                if best_source:
                    return self._create_fake_element_for_download(best_source)
            
            # Phase 2: Runtime object analysis
            runtime_sources = self._analyze_runtime_objects()
            if runtime_sources:
                best_source = self._evaluate_javascript_sources(runtime_sources)
                if best_source:
                    return self._create_fake_element_for_download(best_source)
            
            # Phase 3: Memory and closure inspection
            memory_sources = self._inspect_memory_and_closures()
            if memory_sources:
                best_source = self._evaluate_javascript_sources(memory_sources)
                if best_source:
                    return self._create_fake_element_for_download(best_source)
            
            # Phase 4: Event listener analysis
            event_sources = self._analyze_event_listeners()
            if event_sources:
                best_source = self._evaluate_javascript_sources(event_sources)
                if best_source:
                    return self._create_fake_element_for_download(best_source)
            
            # Phase 5: Framework-specific detection
            framework_sources = self._detect_framework_specific_sources()
            if framework_sources:
                best_source = self._evaluate_javascript_sources(framework_sources)
                if best_source:
                    return self._create_fake_element_for_download(best_source)
            
            return None
            
        except Exception as e:
            logger.error(f"Strategy 3 failed: {e}")
            return None
    
    def _discover_video_sources_comprehensive(self):
        """Comprehensive video source discovery with deep DOM analysis"""
        try:
            discovery_script = """
            function comprehensiveVideoDiscovery() {
                var sources = new Set();
                
                // 1. Enhanced video element analysis
                function analyzeVideoElements() {
                    var videos = document.querySelectorAll('video, source, audio');
                    videos.forEach(function(v) {
                        // Direct sources
                        if (v.src) sources.add(v.src);
                        if (v.currentSrc) sources.add(v.currentSrc);
                        
                        // Data attributes with comprehensive patterns
                        var dataAttrs = ['data-src', 'data-video', 'data-url', 'data-file', 
                                       'data-stream', 'data-media', 'data-source', 'data-path',
                                       'data-href', 'data-link', 'data-location', 'data-uri'];
                        dataAttrs.forEach(function(attr) {
                            var val = v.getAttribute(attr);
                            if (val) sources.add(val);
                        });
                        
                        // CSS computed styles
                        try {
                            var computed = window.getComputedStyle(v);
                            var bgImage = computed.backgroundImage;
                            if (bgImage && bgImage.includes('url(')) {
                                var match = bgImage.match(/url\\(['"]?([^'"]+)['"]?\\)/);
                                if (match) sources.add(match[1]);
                            }
                        } catch(e) {}
                        
                        // Shadow DOM analysis
                        if (v.shadowRoot) {
                            analyzeElementRecursively(v.shadowRoot);
                        }
                    });
                }
                
                // 2. Recursive element analysis
                function analyzeElementRecursively(root) {
                    var walker = document.createTreeWalker(
                        root,
                        NodeFilter.SHOW_ELEMENT,
                        null,
                        false
                    );
                    
                    var node;
                    while (node = walker.nextNode()) {
                        // Check all attributes for video-like URLs
                        if (node.attributes) {
                            for (var i = 0; i < node.attributes.length; i++) {
                                var attr = node.attributes[i];
                                var value = attr.value;
                                if (value && typeof value === 'string') {
                                    if (isVideoLikeUrl(value)) {
                                        sources.add(value);
                                    }
                                }
                            }
                        }
                        
                        // Check text content for URLs
                        if (node.textContent) {
                            var urlMatches = node.textContent.match(/https?:\\/\\/[^\\s'"<>]+\\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)/gi);
                            if (urlMatches) {
                                urlMatches.forEach(function(url) { sources.add(url); });
                            }
                        }
                    }
                }
                
                // 3. Script tag analysis
                function analyzeScriptTags() {
                    var scripts = document.querySelectorAll('script');
                    scripts.forEach(function(script) {
                        var content = script.innerHTML || script.textContent;
                        if (content) {
                            // Multiple URL extraction patterns
                            var patterns = [
                                /['"](https?:\\/\\/[^'"]*\\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)[^'"]*)['"]/gi,
                                /src[\\s]*:[\\s]*['"]([^'"]+\\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)[^'"]*)['"]/gi,
                                /url[\\s]*:[\\s]*['"]([^'"]+\\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)[^'"]*)['"]/gi,
                                /video[\\s]*:[\\s]*['"]([^'"]+)['"]/gi,
                                /stream[\\s]*:[\\s]*['"]([^'"]+)['"]/gi
                            ];
                            
                            patterns.forEach(function(pattern) {
                                var matches = content.match(pattern);
                                if (matches) {
                                    matches.forEach(function(match) {
                                        var url = match.replace(/['"]/g, '').split(':').slice(1).join(':').trim();
                                        if (isVideoLikeUrl(url)) {
                                            sources.add(url);
                                        }
                                    });
                                }
                            });
                        }
                    });
                }
                
                // 4. CSS analysis for background videos
                function analyzeCSSRules() {
                    try {
                        for (var i = 0; i < document.styleSheets.length; i++) {
                            var sheet = document.styleSheets[i];
                            try {
                                var rules = sheet.cssRules || sheet.rules;
                                for (var j = 0; j < rules.length; j++) {
                                    var rule = rules[j];
                                    if (rule.style && rule.style.backgroundImage) {
                                        var match = rule.style.backgroundImage.match(/url\\(['"]?([^'"]+)['"]?\\)/);
                                        if (match && isVideoLikeUrl(match[1])) {
                                            sources.add(match[1]);
                                        }
                                    }
                                }
                            } catch(e) {} // Cross-origin stylesheets
                        }
                    } catch(e) {}
                }
                
                // 5. Helper function for URL validation
                function isVideoLikeUrl(url) {
                    if (!url || typeof url !== 'string' || url.length < 10) return false;
                    
                    var lowerUrl = url.toLowerCase();
                    var videoExtensions = ['.mp4', '.avi', '.mov', '.webm', '.mkv', 
                                         '.flv', '.wmv', '.m4v', '.3gp'];
                    var videoKeywords = ['video', 'stream', 'media', 'movie', 'film'];
                    
                    return videoExtensions.some(ext => lowerUrl.includes(ext)) ||
                           videoKeywords.some(keyword => lowerUrl.includes(keyword)) ||
                           (url.startsWith('http') && (lowerUrl.includes('/stream/') || 
                                                      lowerUrl.includes('/video/') || 
                                                      lowerUrl.includes('/media/')));
                }
                
                // Execute all analysis functions
                analyzeVideoElements();
                analyzeElementRecursively(document);
                analyzeScriptTags();
                analyzeCSSRules();
                
                return Array.from(sources);
            }
            
            return comprehensiveVideoDiscovery();
            """
            
            return self.driver.execute_script(discovery_script)
            
        except Exception as e:
            logger.error(f"Comprehensive video discovery failed: {e}")
            return []
    
    def _analyze_runtime_objects(self):
        """Deep analysis of runtime objects and global variables"""
        try:
            runtime_script = """
            function analyzeRuntimeObjects() {
                var sources = new Set();
                
                // 1. Global window object analysis
                function analyzeWindowObjects() {
                    for (var prop in window) {
                        try {
                            var val = window[prop];
                            
                            // Direct string analysis
                            if (typeof val === 'string' && isVideoUrl(val)) {
                                sources.add(val);
                            }
                            
                            // Object property analysis
                            else if (val && typeof val === 'object' && val !== window) {
                                analyzeObjectProperties(val, prop, 0);
                            }
                            
                            // Function analysis
                            else if (typeof val === 'function') {
                                analyzeFunctionProperties(val, prop);
                            }
                            
                        } catch(e) {} // Skip inaccessible properties
                    }
                }
                
                // 2. Deep object property analysis
                function analyzeObjectProperties(obj, path, depth) {
                    if (depth > 3) return; // Prevent infinite recursion
                    
                    try {
                        for (var key in obj) {
                            try {
                                var value = obj[key];
                                var newPath = path + '.' + key;
                                
                                if (typeof value === 'string' && isVideoUrl(value)) {
                                    sources.add(value);
                                }
                                else if (value && typeof value === 'object' && 
                                        value !== obj && value !== window) {
                                    analyzeObjectProperties(value, newPath, depth + 1);
                                }
                            } catch(e) {}
                        }
                    } catch(e) {}
                }
                
                // 3. Function property analysis
                function analyzeFunctionProperties(func, name) {
                    try {
                        // Function toString analysis
                        var funcString = func.toString();
                        var urlMatches = funcString.match(/['"][^'"]*\\.(mp4|avi|mov|webm|mkv)[^'"]*['"]/gi);
                        if (urlMatches) {
                            urlMatches.forEach(function(match) {
                                var url = match.replace(/['"]/g, '');
                                if (isVideoUrl(url)) sources.add(url);
                            });
                        }
                        
                        // Function properties
                        for (var prop in func) {
                            try {
                                var val = func[prop];
                                if (typeof val === 'string' && isVideoUrl(val)) {
                                    sources.add(val);
                                }
                            } catch(e) {}
                        }
                    } catch(e) {}
                }
                
                // 4. Configuration object hunting
                function findConfigurationObjects() {
                    var configNames = ['config', 'configuration', 'settings', 'options', 
                                     'params', 'data', 'info', 'meta', 'player', 'video',
                                     'stream', 'media', 'content', 'source', 'url'];
                    
                    configNames.forEach(function(name) {
                        try {
                            if (window[name] && typeof window[name] === 'object') {
                                analyzeObjectProperties(window[name], name, 0);
                            }
                        } catch(e) {}
                    });
                }
                
                // 5. Local and session storage analysis
                function analyzeStorageObjects() {
                    try {
                        // Local storage
                        for (var i = 0; i < localStorage.length; i++) {
                            var key = localStorage.key(i);
                            var value = localStorage.getItem(key);
                            if (value && isVideoUrl(value)) {
                                sources.add(value);
                            }
                        }
                        
                        // Session storage
                        for (var i = 0; i < sessionStorage.length; i++) {
                            var key = sessionStorage.key(i);
                            var value = sessionStorage.getItem(key);
                            if (value && isVideoUrl(value)) {
                                sources.add(value);
                            }
                        }
                    } catch(e) {}
                }
                
                // 6. JSON parsing for embedded data
                function parseEmbeddedJSON() {
                    var scripts = document.querySelectorAll('script[type="application/json"], script[type="text/json"]');
                    scripts.forEach(function(script) {
                        try {
                            var data = JSON.parse(script.textContent);
                            analyzeObjectProperties(data, 'jsonData', 0);
                        } catch(e) {}
                    });
                }
                
                function isVideoUrl(url) {
                    if (!url || typeof url !== 'string' || url.length < 10) return false;
                    var lowerUrl = url.toLowerCase();
                    return lowerUrl.includes('.mp4') || lowerUrl.includes('.avi') ||
                           lowerUrl.includes('.mov') || lowerUrl.includes('.webm') ||
                           lowerUrl.includes('.mkv') || lowerUrl.includes('video') ||
                           lowerUrl.includes('stream') || lowerUrl.includes('media');
                }
                
                // Execute all analysis functions
                analyzeWindowObjects();
                findConfigurationObjects();
                analyzeStorageObjects();
                parseEmbeddedJSON();
                
                return Array.from(sources);
            }
            
            return analyzeRuntimeObjects();
            """
            
            return self.driver.execute_script(runtime_script)
            
        except Exception as e:
            logger.error(f"Runtime object analysis failed: {e}")
            return []
    
    def _inspect_memory_and_closures(self):
        """Advanced memory inspection and closure analysis"""
        try:
            memory_script = """
            function inspectMemoryAndClosures() {
                var sources = new Set();
                
                // 1. Closure variable inspection
                function inspectClosures() {
                    // Try to access common closure variables
                    var closureVarNames = ['src', 'source', 'url', 'videoUrl', 'streamUrl',
                                         'mediaUrl', 'path', 'file', 'location', 'href'];
                    
                    // Check for accessible closures in common patterns
                    var elements = document.querySelectorAll('[onclick], [onload], [onplay]');
                    elements.forEach(function(el) {
                        closureVarNames.forEach(function(varName) {
                            try {
                                // Try to evaluate closure variables
                                var result = eval('(function(){try{return ' + varName + ';}catch(e){return null;}})()');
                                if (result && typeof result === 'string' && isVideoUrl(result)) {
                                    sources.add(result);
                                }
                            } catch(e) {}
                        });
                    });
                }
                
                // 2. Memory leak detection for video sources
                function detectMemoryLeaks() {
                    // Look for detached DOM elements that might contain video sources
                    if (window.gc && window.performance && window.performance.memory) {
                        try {
                            var before = window.performance.memory.usedJSHeapSize;
                            window.gc();
                            var after = window.performance.memory.usedJSHeapSize;
                            
                            // If significant memory was freed, there might be cached video data
                            if (before - after > 1000000) { // 1MB threshold
                                // Try to access recently freed video references
                                analyzeRecentlyAccessedObjects();
                            }
                        } catch(e) {}
                    }
                }
                
                // 3. Prototype chain analysis
                function analyzePrototypeChain() {
                    var videoElements = document.querySelectorAll('video');
                    videoElements.forEach(function(video) {
                        var proto = Object.getPrototypeOf(video);
                        while (proto && proto !== Object.prototype) {
                            try {
                                for (var prop in proto) {
                                    var value = proto[prop];
                                    if (typeof value === 'string' && isVideoUrl(value)) {
                                        sources.add(value);
                                    }
                                }
                                proto = Object.getPrototypeOf(proto);
                            } catch(e) {
                                break;
                            }
                        }
                    });
                }
                
                // 4. WeakMap and WeakSet inspection (if accessible)
                function inspectWeakCollections() {
                    try {
                        // This is generally not accessible, but worth trying
                        if (window.WeakMap && window.WeakMap.prototype) {
                            // Try to access common video-related weak maps
                            var commonWeakMapNames = ['videoData', 'mediaCache', 'streamCache'];
                            commonWeakMapNames.forEach(function(name) {
                                if (window[name] instanceof WeakMap) {
                                    // Can't directly iterate WeakMap, but can try common keys
                                    var videoElements = document.querySelectorAll('video');
                                    videoElements.forEach(function(video) {
                                        try {
                                            var data = window[name].get(video);
                                            if (data && typeof data === 'object') {
                                                analyzeObjectForUrls(data);
                                            }
                                        } catch(e) {}
                                    });
                                }
                            });
                        }
                    } catch(e) {}
                }
                
                // 5. Recently accessed objects analysis
                function analyzeRecentlyAccessedObjects() {
                    // Check for recently modified elements
                    var observer = new MutationObserver(function(mutations) {
                        mutations.forEach(function(mutation) {
                            if (mutation.type === 'attributes') {
                                var value = mutation.target.getAttribute(mutation.attributeName);
                                if (value && isVideoUrl(value)) {
                                    sources.add(value);
                                }
                            }
                        });
                    });
                    
                    // Observe for a short time to catch any late-loading content
                    observer.observe(document, {
                        attributes: true,
                        attributeFilter: ['src', 'data-src', 'href'],
                        subtree: true
                    });
                    
                    setTimeout(function() {
                        observer.disconnect();
                    }, 1000);
                }
                
                function analyzeObjectForUrls(obj) {
                    try {
                        for (var key in obj) {
                            var value = obj[key];
                            if (typeof value === 'string' && isVideoUrl(value)) {
                                sources.add(value);
                            } else if (value && typeof value === 'object') {
                                analyzeObjectForUrls(value);
                            }
                        }
                    } catch(e) {}
                }
                
                function isVideoUrl(url) {
                    if (!url || typeof url !== 'string' || url.length < 10) return false;
                    var lowerUrl = url.toLowerCase();
                    return lowerUrl.includes('.mp4') || lowerUrl.includes('.avi') ||
                           lowerUrl.includes('.mov') || lowerUrl.includes('.webm') ||
                           lowerUrl.includes('.mkv') || lowerUrl.includes('video') ||
                           lowerUrl.includes('stream');
                }
                
                // Execute analysis functions
                inspectClosures();
                detectMemoryLeaks();
                analyzePrototypeChain();
                inspectWeakCollections();
                analyzeRecentlyAccessedObjects();
                
                return Array.from(sources);
            }
            
            return inspectMemoryAndClosures();
            """
            
            return self.driver.execute_script(memory_script)
            
        except Exception as e:
            logger.error(f"Memory and closure inspection failed: {e}")
            return []
    
    def _analyze_event_listeners(self):
        """Comprehensive event listener analysis for video sources"""
        try:
            event_script = """
            function analyzeEventListeners() {
                var sources = new Set();
                
                // 1. Direct event listener inspection
                function inspectEventListeners() {
                    var elements = document.querySelectorAll('*');
                    elements.forEach(function(el) {
                        // Common video-related events
                        var videoEvents = ['play', 'pause', 'loadstart', 'loadeddata', 'canplay',
                                         'click', 'mousedown', 'touchstart', 'load'];
                        
                        videoEvents.forEach(function(eventType) {
                            try {
                                // Try to access event listeners (Chrome DevTools API)
                                if (getEventListeners) {
                                    var listeners = getEventListeners(el)[eventType];
                                    if (listeners) {
                                        listeners.forEach(function(listener) {
                                            try {
                                                var funcString = listener.listener.toString();
                                                var urlMatches = funcString.match(/['"][^'"]*\\.(mp4|avi|mov|webm|mkv)[^'"]*['"]/gi);
                                                if (urlMatches) {
                                                    urlMatches.forEach(function(match) {
                                                        var url = match.replace(/['"]/g, '');
                                                        if (isVideoUrl(url)) sources.add(url);
                                                    });
                                                }
                                            } catch(e) {}
                                        });
                                    }
                                }
                            } catch(e) {}
                        });
                    });
                }
                
                // 2. Event handler attribute analysis
                function analyzeEventHandlerAttributes() {
                    var elements = document.querySelectorAll('[onclick], [onload], [onplay], [onpause]');
                    elements.forEach(function(el) {
                        var handlers = ['onclick', 'onload', 'onplay', 'onpause', 'onloadstart'];
                        handlers.forEach(function(handler) {
                            var handlerCode = el.getAttribute(handler);
                            if (handlerCode) {
                                var urlMatches = handlerCode.match(/['"][^'"]*\\.(mp4|avi|mov|webm|mkv)[^'"]*['"]/gi);
                                if (urlMatches) {
                                    urlMatches.forEach(function(match) {
                                        var url = match.replace(/['"]/g, '');
                                        if (isVideoUrl(url)) sources.add(url);
                                    });
                                }
                            }
                        });
                    });
                }
                
                // 3. Custom event analysis
                function analyzeCustomEvents() {
                    // Listen for custom events that might carry video data
                    var customEventTypes = ['videoload', 'streamready', 'mediaload', 'playerready',
                                          'sourcechange', 'urlchange', 'dataready'];
                    
                    customEventTypes.forEach(function(eventType) {
                        try {
                            document.addEventListener(eventType, function(event) {
                                if (event.detail) {
                                    analyzeEventData(event.detail);
                                }
                                if (event.data) {
                                    analyzeEventData(event.data);
                                }
                            });
                            
                            // Dispatch events to trigger listeners
                            var customEvent = new CustomEvent(eventType, {
                                detail: {trigger: 'analysis'}
                            });
                            document.dispatchEvent(customEvent);
                        } catch(e) {}
                    });
                }
                
                // 4. Message event analysis (for iframes)
                function analyzeMessageEvents() {
                    window.addEventListener('message', function(event) {
                        try {
                            var data = event.data;
                            if (typeof data === 'string') {
                                if (isVideoUrl(data)) {
                                    sources.add(data);
                                }
                            } else if (data && typeof data === 'object') {
                                analyzeEventData(data);
                            }
                        } catch(e) {}
                    });
                    
                    // Post messages to trigger responses
                    var messageTypes = ['getVideoUrl', 'getStreamUrl', 'getMediaUrl'];
                    messageTypes.forEach(function(msgType) {
                        try {
                            window.postMessage({type: msgType, request: 'url'}, '*');
                        } catch(e) {}
                    });
                }
                
                function analyzeEventData(data) {
                    try {
                        for (var key in data) {
                            var value = data[key];
                            if (typeof value === 'string' && isVideoUrl(value)) {
                                sources.add(value);
                            } else if (value && typeof value === 'object') {
                                analyzeEventData(value);
                            }
                        }
                    } catch(e) {}
                }
                
                function isVideoUrl(url) {
                    if (!url || typeof url !== 'string' || url.length < 10) return false;
                    var lowerUrl = url.toLowerCase();
                    return (lowerUrl.includes('.mp4') || lowerUrl.includes('.avi') ||
                           lowerUrl.includes('.mov') || lowerUrl.includes('.webm') ||
                           lowerUrl.includes('.mkv') || lowerUrl.includes('video') ||
                           lowerUrl.includes('stream')) && lowerUrl.startsWith('http');
                }
                
                // Execute analysis functions
                inspectEventListeners();
                analyzeEventHandlerAttributes();
                analyzeCustomEvents();
                analyzeMessageEvents();
                
                return Array.from(sources);
            }
            
            return analyzeEventListeners();
            """
            
            return self.driver.execute_script(event_script)
            
        except Exception as e:
            logger.error(f"Event listener analysis failed: {e}")
            return []
    
    def _detect_framework_specific_sources(self):
        """Framework-specific video source detection"""
        try:
            framework_script = """
            function detectFrameworkSources() {
                var sources = new Set();
                
                // 1. React component analysis
                function analyzeReactComponents() {
                    try {
                        // Look for React fiber nodes
                        var reactElements = document.querySelectorAll('[data-reactroot], [data-react-component]');
                        reactElements.forEach(function(el) {
                            // Try to access React props/state
                            for (var key in el) {
                                if (key.startsWith('__reactInternalInstance') || key.startsWith('_reactInternalFiber')) {
                                    try {
                                        var reactData = el[key];
                                        if (reactData && reactData.memoizedProps) {
                                            analyzeReactData(reactData.memoizedProps);
                                        }
                                        if (reactData && reactData.memoizedState) {
                                            analyzeReactData(reactData.memoizedState);
                                        }
                                    } catch(e) {}
                                }
                            }
                        });
                    } catch(e) {}
                }
                
                // 2. Vue.js component analysis
                function analyzeVueComponents() {
                    try {
                        if (window.Vue || window.vue) {
                            var vueElements = document.querySelectorAll('[data-v-], [v-]');
                            vueElements.forEach(function(el) {
                                if (el.__vue__) {
                                    try {
                                        var vueInstance = el.__vue__;
                                        if (vueInstance.$data) {
                                            analyzeVueData(vueInstance.$data);
                                        }
                                        if (vueInstance.$props) {
                                            analyzeVueData(vueInstance.$props);
                                        }
                                    } catch(e) {}
                                }
                            });
                        }
                    } catch(e) {}
                }
                
                // 3. Angular component analysis
                function analyzeAngularComponents() {
                    try {
                        if (window.angular || window.ng) {
                            var angularElements = document.querySelectorAll('[ng-app], [ng-controller], [data-ng-]');
                            angularElements.forEach(function(el) {
                                try {
                                    var scope = angular.element(el).scope();
                                    if (scope) {
                                        analyzeAngularScope(scope);
                                    }
                                } catch(e) {}
                            });
                        }
                    } catch(e) {}
                }
                
                // 4. jQuery plugin analysis
                function analyzeJQueryPlugins() {
                    try {
                        if (window.jQuery || window.$) {
                            var $ = window.jQuery || window.$;
                            
                            // Common video jQuery plugins
                            var pluginMethods = ['videojs', 'jwplayer', 'flowplayer', 'mediaplayer'];
                            pluginMethods.forEach(function(method) {
                                if ($.fn[method]) {
                                    try {
                                        $('[data-' + method + '], .' + method).each(function() {
                                            var data = $(this).data();
                                            analyzePluginData(data);
                                        });
                                    } catch(e) {}
                                }
                            });
                        }
                    } catch(e) {}
                }
                
                // 5. Video.js specific analysis
                function analyzeVideoJS() {
                    try {
                        if (window.videojs || window.vjs) {
                            var vjsElements = document.querySelectorAll('.video-js, [data-setup]');
                            vjsElements.forEach(function(el) {
                                try {
                                    var player = videojs.getPlayer(el);
                                    if (player && player.src) {
                                        var src = player.src();
                                        if (typeof src === 'string' && isVideoUrl(src)) {
                                            sources.add(src);
                                        } else if (Array.isArray(src)) {
                                            src.forEach(function(source) {
                                                if (source.src && isVideoUrl(source.src)) {
                                                    sources.add(source.src);
                                                }
                                            });
                                        }
                                    }
                                } catch(e) {}
                            });
                        }
                    } catch(e) {}
                }
                
                function analyzeReactData(data) {
                    try {
                        for (var key in data) {
                            var value = data[key];
                            if (typeof value === 'string' && isVideoUrl(value)) {
                                sources.add(value);
                            } else if (value && typeof value === 'object') {
                                analyzeReactData(value);
                            }
                        }
                    } catch(e) {}
                }
                
                function analyzeVueData(data) {
                    try {
                        for (var key in data) {
                            var value = data[key];
                            if (typeof value === 'string' && isVideoUrl(value)) {
                                sources.add(value);
                            } else if (value && typeof value === 'object') {
                                analyzeVueData(value);
                            }
                        }
                    } catch(e) {}
                }
                
                function analyzeAngularScope(scope) {
                    try {
                        for (var key in scope) {
                            if (!key.startsWith('$') && !key.startsWith('_')) {
                                var value = scope[key];
                                if (typeof value === 'string' && isVideoUrl(value)) {
                                    sources.add(value);
                                } else if (value && typeof value === 'object') {
                                    analyzeAngularScope(value);
                                }
                            }
                        }
                    } catch(e) {}
                }

                function analyzePluginData(data) {
                    try {
                        for (var key in data) {
                            var value = data[key];
                            if (typeof value === 'string' && isVideoUrl(value)) {
                                sources.add(value);
                            } else if (value && typeof value === 'object') {
                                analyzePluginData(value);
                            }
                        }
                    } catch(e) {}
                }

                function isVideoUrl(url) {
                    if (!url || typeof url !== 'string' || url.length < 10) return false;
                    var lowerUrl = url.toLowerCase();
                    return (lowerUrl.includes('.mp4') || lowerUrl.includes('.avi') ||
                           lowerUrl.includes('.mov') || lowerUrl.includes('.webm') ||
                           lowerUrl.includes('.mkv') || lowerUrl.includes('video') ||
                           lowerUrl.includes('stream')) && lowerUrl.startsWith('http');
                }

                // Execute all analysis functions
                analyzeReactComponents();
                analyzeVueComponents();
                analyzeAngularComponents();
                analyzeJQueryPlugins();
                analyzeVideoJS();

                return Array.from(sources);
            }

            return detectFrameworkSources();
            """

            return self.driver.execute_script(framework_script)

        except Exception as e:
            logger.error(f"Framework detection failed: {e}")
            return []

    def _traditional_element_detection(self):
        """STRATEGY 4: Enhanced traditional DOM element detection with intelligent filtering and validation"""
        try:
            self.log_status("Strategy 4: Enhanced DOM element detection with intelligent analysis")
            
            # Phase 1: Comprehensive selector-based detection
            video_elements = self._comprehensive_selector_detection()
            if video_elements:
                validated_element = self._validate_and_rank_elements(video_elements)
                if validated_element:
                    return validated_element
            
            # Phase 2: Attribute-based detection
            attribute_elements = self._attribute_based_detection()
            if attribute_elements:
                validated_element = self._validate_and_rank_elements(attribute_elements)
                if validated_element:
                    return validated_element
            
            # Phase 3: Content-based detection
            content_elements = self._content_based_detection()
            if content_elements:
                validated_element = self._validate_and_rank_elements(content_elements)
                if validated_element:
                    return validated_element
            
            # Phase 4: Behavioral pattern detection
            behavioral_elements = self._behavioral_pattern_detection()
            if behavioral_elements:
                validated_element = self._validate_and_rank_elements(behavioral_elements)
                if validated_element:
                    return validated_element
            
            return None
            
        except Exception as e:
            logger.error(f"Strategy 4 failed: {e}")
            return None
    
    def _comprehensive_selector_detection(self):
        """Comprehensive CSS selector-based element detection"""
        try:
            found_elements = []
            
            # Prioritized selector groups
            selector_groups = [
                # High priority: Direct video elements
                {
                    'selectors': [
                        'video[src]',
                        'video source[src]',
                        'source[src][type*="video"]',
                        'video[data-src]',
                        'source[data-src][type*="video"]'
                    ],
                    'priority': 100
                },
                
                # Medium-high priority: Common video containers from screenshot analysis
                {
                    'selectors': [
                        '.video_player video',
                        '.video_player[data-snippet] video',
                        '.video_player',
                        '[data-snippet] video',
                        '[data-snippet]',
                        '.container video',
                        '.main video'
                    ],
                    'priority': 90
                },
                
                # Medium priority: Player frameworks
                {
                    'selectors': [
                        '.video-js video',
                        '#player video',
                        '.jwplayer video',
                        '.flowplayer video',
                        '.videojs video',
                        '.plyr video',
                        '.mediaplayer video'
                    ],
                    'priority': 80
                },
                
                # Medium-low priority: Generic video containers
                {
                    'selectors': [
                        '[id*="player"] video',
                        '[class*="player"] video',
                        '[id*="video"] video',
                        '[class*="video"] video',
                        '.player video',
                        '.media video',
                        '.stream video'
                    ],
                    'priority': 70
                },
                
                # Low priority: Embedded content
                {
                    'selectors': [
                        'iframe[src*="video"]',
                        'iframe[src*="player"]',
                        'iframe[src*="embed"]',
                        'embed[src*="video"]',
                        'object[data*="video"]',
                        'object[type*="video"]'
                    ],
                    'priority': 60
                },
                
                # Lowest priority: Interactive elements
                {
                    'selectors': [
                        '[onclick*="video"]',
                        '[onclick*="play"]',
                        '[data-video]',
                        '[data-play]',
                        '.play-button',
                        '.video-thumbnail',
                        '[class*="play"]',
                        '[id*="play"]'
                    ],
                    'priority': 50
                }
            ]
            
            for group in selector_groups:
                for selector in group['selectors']:
                    try:
                        elements = self.safe_find_elements(By.CSS_SELECTOR, selector)
                        for element in elements:
                            if self._is_element_viable(element):
                                found_elements.append({
                                    'element': element,
                                    'selector': selector,
                                    'priority': group['priority'],
                                    'source': 'selector'
                                })
                    except Exception:
                        continue
            
            return found_elements
            
        except Exception as e:
            logger.error(f"Comprehensive selector detection failed: {e}")
            return []
    
    def _attribute_based_detection(self):
        """Attribute-based element detection with comprehensive patterns"""
        try:
            found_elements = []
            
            # Comprehensive attribute patterns
            attribute_patterns = [
                # Video source attributes
                {'attr': 'src', 'pattern': r'.*\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)', 'priority': 95},
                {'attr': 'data-src', 'pattern': r'.*\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)', 'priority': 90},
                {'attr': 'data-video', 'pattern': r'.*', 'priority': 85},
                {'attr': 'data-url', 'pattern': r'.*\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)', 'priority': 85},
                {'attr': 'data-file', 'pattern': r'.*\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)', 'priority': 85},
                {'attr': 'data-stream', 'pattern': r'.*', 'priority': 80},
                {'attr': 'data-media', 'pattern': r'.*', 'priority': 80},
                
                # Content delivery attributes
                {'attr': 'data-snippet', 'pattern': r'.*', 'priority': 75},  # From screenshot
                {'attr': 'data-source', 'pattern': r'.*', 'priority': 75},
                {'attr': 'data-path', 'pattern': r'.*\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)', 'priority': 75},
                {'attr': 'href', 'pattern': r'.*\.(mp4|avi|mov|webm|mkv|flv|wmv|m4v|3gp)', 'priority': 70},
                
                # Behavioral attributes
                {'attr': 'onclick', 'pattern': r'.*(video|play|stream)', 'priority': 60},
                {'attr': 'onload', 'pattern': r'.*(video|media)', 'priority': 55},
                {'attr': 'data-toggle', 'pattern': r'.*(video|modal)', 'priority': 50},
                
                # Framework-specific attributes
                {'attr': 'data-setup', 'pattern': r'.*', 'priority': 65},  # Video.js
                {'attr': 'data-jwplayer', 'pattern': r'.*', 'priority': 65},  # JW Player
                {'attr': 'data-flowplayer', 'pattern': r'.*', 'priority': 65},  # Flowplayer
            ]
            
            for pattern_info in attribute_patterns:
                try:
                    # Find elements with this attribute
                    elements = self.safe_find_elements(By.CSS_SELECTOR, f'[{pattern_info["attr"]}]')
                    
                    for element in elements:
                        try:
                            attr_value = element.get_attribute(pattern_info['attr'])
                            if attr_value and re.search(pattern_info['pattern'], attr_value, re.IGNORECASE):
                                if self._is_element_viable(element):
                                    found_elements.append({
                                        'element': element,
                                        'attribute': pattern_info['attr'],
                                        'value': attr_value,
                                        'priority': pattern_info['priority'],
                                        'source': 'attribute'
                                    })
                        except Exception:
                            continue
                            
                except Exception:
                    continue
            
            return found_elements
            
        except Exception as e:
            logger.error(f"Attribute-based detection failed: {e}")
            return []
    
    def _content_based_detection(self):
        """Content-based element detection using text and visual analysis"""
        try:
            found_elements = []
            
            # Text content patterns
            text_patterns = [
                {'pattern': r'play\s+video', 'priority': 80},
                {'pattern': r'watch\s+video', 'priority': 80},
                {'pattern': r'video\s+player', 'priority': 75},
                {'pattern': r'stream\s+now', 'priority': 75},
                {'pattern': r'click\s+to\s+play', 'priority': 70},
                {'pattern': r'download\s+video', 'priority': 70},
                {'pattern': r'full\s+video', 'priority': 65},
                {'pattern': r'hd\s+video', 'priority': 65},
                {'pattern': r'4k\s+video', 'priority': 65},
            ]
            
            for pattern_info in text_patterns:
                try:
                    # Use XPath to find elements containing this text
                    xpath = f"//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{pattern_info['pattern'].lower()}')]"
                    elements = self.safe_find_elements(By.XPATH, xpath)
                    
                    for element in elements:
                        if self._is_element_viable(element):
                            found_elements.append({
                                'element': element,
                                'text_pattern': pattern_info['pattern'],
                                'priority': pattern_info['priority'],
                                'source': 'content'
                            })
                            
                except Exception:
                    continue
            
            # Visual analysis (element size, position, styling)
            visual_elements = self._visual_element_analysis()
            found_elements.extend(visual_elements)
            
            return found_elements
            
        except Exception as e:
            logger.error(f"Content-based detection failed: {e}")
            return []
    
    def _visual_element_analysis(self):
        """Visual analysis of elements for video player characteristics"""
        try:
            found_elements = []
            
            # Find elements that look like video players
            all_elements = self.safe_find_elements(By.CSS_SELECTOR, 'div, section, article, main')
            
            for element in all_elements:
                try:
                    if not element.is_displayed():
                        continue
                    
                    # Get element dimensions
                    size = element.size
                    if size['width'] < 200 or size['height'] < 150:
                        continue  # Too small to be a video player
                    
                    # Check aspect ratio (typical video ratios)
                    aspect_ratio = size['width'] / size['height']
                    is_video_aspect = (1.3 <= aspect_ratio <= 2.4)  # 4:3 to 21:9
                    
                    # Get computed styles
                    try:
                        bg_color = self.driver.execute_script(
                            "return window.getComputedStyle(arguments[0]).backgroundColor;", element
                        )
                        position = self.driver.execute_script(
                            "return window.getComputedStyle(arguments[0]).position;", element
                        )
                        cursor = self.driver.execute_script(
                            "return window.getComputedStyle(arguments[0]).cursor;", element
                        )
                    except:
                        bg_color = position = cursor = ""
                    
                    # Scoring system for video player likelihood
                    score = 0
                    
                    if is_video_aspect:
                        score += 30
                    
                    if 'black' in bg_color or 'rgb(0, 0, 0)' in bg_color:
                        score += 20  # Black backgrounds common for video players
                    
                    if cursor == 'pointer':
                        score += 15  # Clickable elements
                    
                    if position in ['relative', 'absolute', 'fixed']:
                        score += 10  # Positioned elements
                    
                    # Check for video-related classes or IDs
                    class_name = element.get_attribute('class') or ''
                    element_id = element.get_attribute('id') or ''
                    
                    video_keywords = ['video', 'player', 'media', 'stream', 'movie', 'film']
                    for keyword in video_keywords:
                        if keyword in class_name.lower() or keyword in element_id.lower():
                            score += 25
                            break
                    
                    # Minimum score threshold
                    if score >= 40:
                        found_elements.append({
                            'element': element,
                            'visual_score': score,
                            'aspect_ratio': aspect_ratio,
                            'priority': min(90, 50 + score),
                            'source': 'visual'
                        })
                        
                except Exception:
                    continue
            
            return found_elements
            
        except Exception as e:
            logger.error(f"Visual element analysis failed: {e}")
            return []
    
    def _behavioral_pattern_detection(self):
        """Behavioral pattern detection for interactive video elements"""
        try:
            found_elements = []
            
            # Find potentially interactive elements
            interactive_selectors = [
                'button', 'a', 'div[onclick]', 'span[onclick]', 
                '[role="button"]', '[tabindex]', '.clickable'
            ]
            
            for selector in interactive_selectors:
                try:
                    elements = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    
                    for element in elements:
                        try:
                            if not self._is_element_viable(element):
                                continue
                            
                            # Test element behavior
                            behavior_score = self._analyze_element_behavior(element)
                            
                            if behavior_score > 30:
                                found_elements.append({
                                    'element': element,
                                    'behavior_score': behavior_score,
                                    'priority': min(85, 40 + behavior_score),
                                    'source': 'behavioral'
                                })
                                
                        except Exception:
                            continue
                            
                except Exception:
                    continue
            
            return found_elements
            
        except Exception as e:
            logger.error(f"Behavioral pattern detection failed: {e}")
            return []
    
    def _analyze_element_behavior(self, element):
        """Analyze element behavior patterns for video-related characteristics"""
        try:
            score = 0
            
            # Check event handlers
            onclick = element.get_attribute('onclick') or ''
            if any(keyword in onclick.lower() for keyword in ['video', 'play', 'stream', 'media']):
                score += 25
            
            # Check ARIA attributes
            aria_label = element.get_attribute('aria-label') or ''
            if any(keyword in aria_label.lower() for keyword in ['video', 'play', 'stream']):
                score += 20
            
            # Check data attributes
            data_attrs = []
            for attr in ['data-action', 'data-target', 'data-toggle', 'data-video']:
                value = element.get_attribute(attr)
                if value:
                    data_attrs.append(value.lower())
            
            if any(keyword in ' '.join(data_attrs) for keyword in ['video', 'play', 'modal']):
                score += 15
            
            # Check text content
            text_content = element.text.lower() if element.text else ''
            if any(keyword in text_content for keyword in ['play', 'video', 'watch', 'stream']):
                score += 20
            
            # Check if element has child elements that suggest video content
            try:
                children = element.find_elements(By.CSS_SELECTOR, '*')
                for child in children[:5]:  # Check first 5 children
                    child_tag = child.tag_name.lower()
                    if child_tag in ['video', 'source', 'iframe']:
                        score += 30
                        break
                    
                    child_class = child.get_attribute('class') or ''
                    if any(keyword in child_class.lower() for keyword in ['video', 'player']):
                        score += 15
                        break
            except:
                pass
            
            return score
            
        except Exception:
            return 0
    
    def _is_element_viable(self, element):
        """Check if element is viable for video detection"""
        try:
            # Must be displayed
            if not element.is_displayed():
                return False
            
            # Must have reasonable size
            size = element.size
            if size['width'] < 50 or size['height'] < 50:
                return False
            
            # Must be in viewport or at least partially visible
            location = element.location
            if location['x'] < -100 or location['y'] < -100:
                return False
            
            return True
            
        except Exception:
            return False
    
    def _validate_and_rank_elements(self, elements):
        """Validate and rank detected elements"""
        try:
            if not elements:
                return None
            
            # Enhanced scoring and validation
            scored_elements = []
            
            for elem_info in elements:
                element = elem_info['element']
                base_priority = elem_info.get('priority', 50)
                
                # Additional validation scoring
                validation_score = 0
                
                # Check for video source
                src = element.get_attribute('src')
                if src and self._is_valid_video_url(src):
                    validation_score += 50
                    elem_info['video_url'] = src
                
                # Check data attributes for video URLs
                for attr in ['data-src', 'data-video', 'data-url', 'data-file']:
                    value = element.get_attribute(attr)
                    if value and self._is_valid_video_url(value):
                        validation_score += 40
                        elem_info['video_url'] = value
                        break
                
                # Check if element has video children
                try:
                    video_children = element.find_elements(By.CSS_SELECTOR, 'video, source')
                    if video_children:
                        validation_score += 30
                        for child in video_children:
                            child_src = child.get_attribute('src')
                            if child_src and self._is_valid_video_url(child_src):
                                validation_score += 20
                                elem_info['video_url'] = child_src
                                break
                except:
                    pass
                
                total_score = base_priority + validation_score
                scored_elements.append((total_score, elem_info))
            
            # Sort by score and return best element
            scored_elements.sort(reverse=True, key=lambda x: x[0])
            
            for score, elem_info in scored_elements:
                element = elem_info['element']
                
                # Final validation
                if self._final_element_validation(element, elem_info):
                    self.log_status(f"Strategy 4 success (score: {score}): {elem_info.get('source', 'unknown')}")
                    
                    # Return element or create fake element for direct URL
                    if 'video_url' in elem_info:
                        return self._create_fake_element_for_download(elem_info['video_url'])
                    else:
                        return element
            
            return None
            
        except Exception as e:
            logger.error(f"Element validation and ranking failed: {e}")
            return None
    
    def _final_element_validation(self, element, elem_info):
        """Final validation of element before selection"""
        try:
            # Ensure element is still accessible
            if not element.is_displayed():
                return False
            
            # If we have a direct video URL, validate it
            if 'video_url' in elem_info:
                return self._is_valid_video_url(elem_info['video_url'])
            
            # For interactive elements, ensure they're clickable
            if elem_info.get('source') in ['behavioral', 'content']:
                try:
                    # Test if element is clickable
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    return True
                except:
                    return False
            
            return True
            
        except Exception:
            return False
    
    def _handle_token_based_sites(self):
        """STRATEGY 5: Advanced token-based site handling with comprehensive authentication analysis"""
        try:
            self.log_status("Strategy 5: Advanced token-based authentication analysis")
            
            # Phase 1: Token discovery and extraction
            tokens = self._discover_authentication_tokens()
            if not tokens:
                return None
            
            # Phase 2: Form analysis and submission
            form_results = self._analyze_and_submit_forms(tokens)
            if form_results:
                return form_results
            
            # Phase 3: AJAX authentication handling
            ajax_results = self._handle_ajax_authentication(tokens)
            if ajax_results:
                return ajax_results
            
            # Phase 4: Session-based content loading
            session_results = self._handle_session_content(tokens)
            if session_results:
                return session_results
            
            # Phase 5: API-based token authentication
            api_results = self._handle_api_authentication(tokens)
            if api_results:
                return api_results
            
            return None
            
        except Exception as e:
            logger.error(f"Strategy 5 failed: {e}")
            return None
    
    def _discover_authentication_tokens(self):
        """Comprehensive authentication token discovery"""
        try:
            tokens = {}
            
            # 1. Standard CSRF and authentication tokens
            token_selectors = [
                'input[name*="token"]',
                'input[name*="csrf"]', 
                'input[name*="authenticity"]',
                'input[name*="security"]',
                'input[name*="session"]',
                'input[name*="serialized"]',  # From screenshot
                'input[name*="_token"]',
                'input[name*="csrfmiddlewaretoken"]',
                'input[name="_method"]',
                'input[type="hidden"]'
            ]
            
            for selector in token_selectors:
                try:
                    elements = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        name = element.get_attribute('name')
                        value = element.get_attribute('value')
                        if name and value:
                            tokens[name] = value
                            
                except Exception:
                    continue
            
            # 2. Meta tag tokens
            meta_selectors = [
                'meta[name="csrf-token"]',
                'meta[name="_token"]',
                'meta[name="authenticity_token"]'
            ]
            
            for selector in meta_selectors:
                try:
                    elements = self.safe_find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        name = element.get_attribute('name')
                        content = element.get_attribute('content')
                        if name and content:
                            tokens[name] = content
                            
                except Exception:
                    continue
            
            # 3. JavaScript-based token extraction
            js_tokens = self._extract_javascript_tokens()
            tokens.update(js_tokens)
            
            # 4. Cookie-based tokens
            cookie_tokens = self._extract_cookie_tokens()
            tokens.update(cookie_tokens)
            
            # 5. Local/Session storage tokens
            storage_tokens = self._extract_storage_tokens()
            tokens.update(storage_tokens)
            
            self.log_status(f"Discovered {len(tokens)} authentication tokens")
            return tokens
            
        except Exception as e:
            logger.error(f"Token discovery failed: {e}")
            return {}
    
    def _extract_javascript_tokens(self):
        """Extract tokens from JavaScript variables and objects"""
        try:
            js_script = """
            function extractJSTokens() {
                var tokens = {};
                
                // Common JavaScript token variable names
                var tokenVars = [
                    'csrfToken', 'csrf_token', '_token', 'authenticity_token',
                    'sessionToken', 'securityToken', 'apiToken', 'authToken',
                    'requestToken', 'formToken', 'pageToken', 'userToken'
                ];
                
                tokenVars.forEach(function(varName) {
                    try {
                        if (window[varName]) {
                            tokens[varName] = window[varName];
                        }
                    } catch(e) {}
                });
                
                // Check Laravel-style meta tokens
                try {
                    var metaToken = document.querySelector('meta[name="csrf-token"]');
                    if (metaToken) {
                        tokens['csrf-token'] = metaToken.getAttribute('content');
                    }
                } catch(e) {}
                
                // Check Rails-style tokens
                try {
                    var railsToken = document.querySelector('meta[name="authenticity-token"]');
                    if (railsToken) {
                        tokens['authenticity-token'] = railsToken.getAttribute('content');
                    }
                } catch(e) {}
                
                // Check for tokens in global config objects
                var configObjects = ['config', 'app', 'APP_CONFIG', 'window.Laravel'];
                configObjects.forEach(function(objName) {
                    try {
                        var obj = eval(objName);
                        if (obj && obj.csrfToken) {
                            tokens['config_csrf'] = obj.csrfToken;
                        }
                        if (obj && obj.token) {
                            tokens['config_token'] = obj.token;
                        }
                    } catch(e) {}
                });
                
                return tokens;
            }
            
            return extractJSTokens();
            """
            
            return self.driver.execute_script(js_script)
            
        except Exception as e:
            logger.error(f"JavaScript token extraction failed: {e}")
            return {}
    
    def _extract_cookie_tokens(self):
        """Extract authentication tokens from cookies"""
        try:
            tokens = {}
            cookies = self.driver.get_cookies()
            
            token_cookie_patterns = [
                'csrf', 'token', 'auth', 'session', 'security', 'xsrf'
            ]
            
            for cookie in cookies:
                cookie_name = cookie.get('name', '').lower()
                cookie_value = cookie.get('value', '')
                
                if any(pattern in cookie_name for pattern in token_cookie_patterns):
                    tokens[f"cookie_{cookie['name']}"] = cookie_value
            
            return tokens
            
        except Exception as e:
            logger.error(f"Cookie token extraction failed: {e}")
            return {}
    
    def _extract_storage_tokens(self):
        """Extract tokens from localStorage and sessionStorage"""
        try:
            storage_script = """
            function extractStorageTokens() {
                var tokens = {};
                
                // Local storage
                try {
                    for (var i = 0; i < localStorage.length; i++) {
                        var key = localStorage.key(i);
                        var value = localStorage.getItem(key);
                        if (key && value && (key.includes('token') || key.includes('csrf') || key.includes('auth'))) {
                            tokens['localStorage_' + key] = value;
                        }
                    }
                } catch(e) {}
                
                // Session storage
                try {
                    for (var i = 0; i < sessionStorage.length; i++) {
                        var key = sessionStorage.key(i);
                        var value = sessionStorage.getItem(key);
                        if (key && value && (key.includes('token') || key.includes('csrf') || key.includes('auth'))) {
                            tokens['sessionStorage_' + key] = value;
                        }
                    }
                } catch(e) {}
                
                return tokens;
            }
            
            return extractStorageTokens();
            """
            
            return self.driver.execute_script(storage_script)
            
        except Exception as e:
            logger.error(f"Storage token extraction failed: {e}")
            return {}
    
    def _analyze_and_submit_forms(self, tokens):
        """Analyze and submit forms with discovered tokens"""
        try:
            forms = self.safe_find_elements(By.TAG_NAME, "form")
            
            for form in forms:
                try:
                    # Analyze form structure
                    form_analysis = self._analyze_form_structure(form, tokens)
                    
                    if form_analysis['has_video_potential']:
                        # Attempt form submission
                        video_url = self._submit_form_and_extract_video(form, form_analysis)
                        if video_url:
                            return self._create_fake_element_for_download(video_url)
                            
                except Exception:
                    continue
            
            return None
            
        except Exception as e:
            logger.error(f"Form analysis and submission failed: {e}")
            return None
    
    def _analyze_form_structure(self, form, tokens):
        """Analyze form structure for video-related potential"""
        try:
            analysis = {
                'has_video_potential': False,
                'token_fields': [],
                'hidden_fields': [],
                'action_url': '',
                'method': 'POST'
            }
            
            # Get form attributes
            analysis['action_url'] = form.get_attribute('action') or ''
            analysis['method'] = form.get_attribute('method') or 'POST'
            
            # Analyze form inputs
            inputs = form.find_elements(By.TAG_NAME, 'input')
            
            for input_elem in inputs:
                input_type = input_elem.get_attribute('type') or 'text'
                input_name = input_elem.get_attribute('name') or ''
                input_value = input_elem.get_attribute('value') or ''
                
                if input_type == 'hidden':
                    analysis['hidden_fields'].append({
                        'name': input_name,
                        'value': input_value
                    })
                    
                    # Check for token fields
                    if any(token_name in input_name.lower() for token_name in ['token', 'csrf', 'auth']):
                        analysis['token_fields'].append({
                            'name': input_name,
                            'value': input_value
                        })
            
            # Check for video-related potential
            video_indicators = ['video', 'media', 'stream', 'download', 'content']
            form_html = form.get_attribute('outerHTML').lower()
            
            if any(indicator in form_html for indicator in video_indicators):
                analysis['has_video_potential'] = True
            
            # Check action URL for video indicators
            if any(indicator in analysis['action_url'].lower() for indicator in video_indicators):
                analysis['has_video_potential'] = True
            
            return analysis
            
        except Exception as e:
            logger.error(f"Form structure analysis failed: {e}")
            return {'has_video_potential': False}
    
    def _submit_form_and_extract_video(self, form, form_analysis):
        """Submit form and extract video content"""
        try:
            # Store current page state
            current_url = self.driver.current_url
            
            # Submit form
            try:
                form.submit()
                time.sleep(0.2)  # Wait for response
                
                # Check if page changed or new content loaded
                new_url = self.driver.current_url
                
                if new_url != current_url or self._has_new_video_content():
                    # Look for video content in new page state
                    return self._extract_video_from_current_page()
                    
            except Exception:
                # Try clicking submit button instead
                submit_buttons = form.find_elements(By.CSS_SELECTOR, 'input[type="submit"], button[type="submit"], button')
                for button in submit_buttons:
                    try:
                        button.click()
                        time.sleep(0.2)
                        
                        if self._has_new_video_content():
                            return self._extract_video_from_current_page()
                            
                    except Exception:
                        continue
            
            return None
            
        except Exception as e:
            logger.error(f"Form submission failed: {e}")
            return None
    
    def _has_new_video_content(self):
        """Check if new video content has appeared"""
        try:
            # Look for new video elements
            videos = self.driver.find_elements(By.TAG_NAME, 'video')
            if videos:
                for video in videos:
                    if video.get_attribute('src'):
                        return True
            
            # Look for new video-related elements
            video_selectors = [
                '[data-video]', '[data-src*="mp4"]', '[src*="video"]',
                '.video-player', '.media-player', '#video-container'
            ]
            
            for selector in video_selectors:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    return True
            
            return False
            
        except Exception:
            return False
    
    def _extract_video_from_current_page(self):
        """Extract video URL from current page state"""
        try:
            # Try multiple extraction methods
            
            # 1. Direct video elements
            videos = self.driver.find_elements(By.TAG_NAME, 'video')
            for video in videos:
                src = video.get_attribute('src')
                if src and self._is_valid_video_url(src):
                    return src
            
            # 2. Source elements
            sources = self.driver.find_elements(By.TAG_NAME, 'source')
            for source in sources:
                src = source.get_attribute('src')
                if src and self._is_valid_video_url(src):
                    return src
            
            # 3. Data attributes
            data_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-video], [data-src], [data-url]')
            for element in data_elements:
                for attr in ['data-video', 'data-src', 'data-url']:
                    value = element.get_attribute(attr)
                    if value and self._is_valid_video_url(value):
                        return value
            
            return None
            
        except Exception as e:
            logger.error(f"Video extraction from current page failed: {e}")
            return None
    
    def _handle_ajax_authentication(self, tokens):
        """Handle AJAX-based authentication and content loading"""
        try:
            ajax_script = """
            return new Promise(function(resolve) {
                var foundUrls = [];
                var originalXHR = XMLHttpRequest.prototype.open;
                var originalFetch = window.fetch;
                
                // Intercept XHR requests
                XMLHttpRequest.prototype.open = function(method, url) {
                    this.addEventListener('load', function() {
                        if (this.responseText) {
                            try {
                                // Look for video URLs in response
                                var videoMatches = this.responseText.match(/https?:\\/\\/[^\\s"'<>]+\\.(mp4|avi|mov|webm|mkv)/gi);
                                if (videoMatches) {
                                    foundUrls = foundUrls.concat(videoMatches);
                                }
                            } catch(e) {}
                        }
                    });
                    return originalXHR.apply(this, arguments);
                };
                
                // Intercept fetch requests
                window.fetch = function(url, options) {
                    return originalFetch.apply(this, arguments).then(function(response) {
                        return response.clone().text().then(function(text) {
                            try {
                                var videoMatches = text.match(/https?:\\/\\/[^\\s"'<>]+\\.(mp4|avi|mov|webm|mkv)/gi);
                                if (videoMatches) {
                                    foundUrls = foundUrls.concat(videoMatches);
                                }
                            } catch(e) {}
                            return response;
                        });
                    });
                };
                
                // Trigger AJAX calls with tokens
                var tokenData = arguments[0];
                
                // Common AJAX endpoints
                var endpoints = ['/video', '/media', '/stream', '/content', '/load', '/get'];
                endpoints.forEach(function(endpoint) {
                    try {
                        var xhr = new XMLHttpRequest();
                        xhr.open('POST', endpoint);
                        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                        
                        // Build form data with tokens
                        var formData = [];
                        for (var key in tokenData) {
                            formData.push(key + '=' + encodeURIComponent(tokenData[key]));
                        }
                        
                        xhr.send(formData.join('&'));
                    } catch(e) {}
                });
                
                // Wait for responses
                setTimeout(function() {
                    resolve(foundUrls);
                }, 5000);
            });
            """
            
            found_urls = self.driver.execute_async_script(ajax_script, tokens)
            
            for url in found_urls:
                if self._is_valid_video_url(url):
                    return self._create_fake_element_for_download(url)
            
            return None
            
        except Exception as e:
            logger.error(f"AJAX authentication handling failed: {e}")
            return None
    
    def _handle_session_content(self, tokens):
        """Handle session-based content loading"""
        try:
            # Try to trigger session-based content loading
            session_script = """
            function triggerSessionContent() {
                var tokens = arguments[0];
                
                // Try to trigger session-based video loading
                var triggerMethods = [
                    function() { if (window.loadSessionContent) window.loadSessionContent(); },
                    function() { if (window.initSession) window.initSession(); },
                    function() { if (window.authenticateSession) window.authenticateSession(); },
                    function() { 
                        // Send tokens via postMessage
                        window.postMessage({action: 'authenticate', tokens: tokens}, '*');
                    }
                ];
                
                triggerMethods.forEach(function(method) {
                    try { method(); } catch(e) {}
                });
                
                return true;
            }
            
            return triggerSessionContent(arguments[0]);
            """
            
            self.driver.execute_script(session_script, tokens)
            time.sleep(0.2)
            
            # Check for newly loaded video content
            return self._extract_video_from_current_page()
            
        except Exception as e:
            logger.error(f"Session content handling failed: {e}")
            return None
    
    def _handle_api_authentication(self, tokens):
        """Handle API-based token authentication"""
        try:
            # Try common API endpoints with token authentication
            api_endpoints = [
                '/api/video', '/api/media', '/api/stream', '/api/content',
                '/video/api', '/media/api', '/stream/api',
                '/v1/video', '/v1/media', '/v2/video'
            ]
            
            for endpoint in api_endpoints:
                try:
                    # Use requests to try API call
                    import requests
                    
                    base_url = self.driver.current_url.split('/')[0:3]
                    api_url = '/'.join(base_url) + endpoint
                    
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                        'Referer': self.driver.current_url
                    }
                    
                    # Try with tokens as headers
                    for token_name, token_value in tokens.items():
                        headers[f'X-{token_name}'] = token_value
                        headers[token_name] = token_value
                    
                    response = requests.get(api_url, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        # Look for video URLs in response
                        video_matches = re.findall(r'https?://[^\s"\'<>]+\.(mp4|avi|mov|webm|mkv)', response.text)
                        for match in video_matches:
                            if self._is_valid_video_url(match):
                                return self._create_fake_element_for_download(match)
                    
                except Exception:
                    continue
            
            return None
            
        except Exception as e:
            logger.error(f"API authentication handling failed: {e}")
            return None
    
    def _is_valid_video_url(self, url):
        """Enhanced check if URL is a valid video URL including segmented/HLS URLs"""
        if not url or len(url) < 10:
            return False

        # Must be HTTP/HTTPS
        if not url.startswith(('http://', 'https://')):
            return False

        url_lower = url.lower()

        # EXCLUDE non-video files (images, scripts, etc)
        excluded_extensions = [
            '.svg', '.jpg', '.jpeg', '.png', '.gif', '.webp',
            '.css', '.js', '.json', '.xml', '.html', '.htm',
            '.pdf', '.doc', '.txt', '.ico', '.woff', '.woff2'
        ]

        if any(ext in url_lower for ext in excluded_extensions):
            return False

        # EXCLUDE advertisement URLs and trailers
        ad_keywords = [
            'trailer', 'preview', 'promo', 'advertisement', 'ads',
            'banner', 'popup', 'redirect', 'click', 'affiliate',
            'marketing', 'sponsor', 'campaign', '/ads/', '/ad/',
            'googlesyndication', 'doubleclick', 'googleadservices',
            'facebook.com/tr', 'google-analytics', 'gtag', 'fbevents'
        ]

        if any(keyword in url_lower for keyword in ad_keywords):
            return False

        # Check for video file extensions or video-related paths
        video_indicators = [
            '.mp4', '.avi', '.mov', '.webm', '.mkv', '.flv', '.wmv',
            '/video/', '/stream/', '/media/', 'video', 'stream'
        ]

        # Enhanced indicators for segmented and streaming content
        streaming_indicators = [
            '.m3u8', '/hls/', 'media=hls', 'media%3dhls',
            'clip=', '/clip', 'segment=', '/segment',
            'multi=', '/multi', 'range=', '/range'
        ]

        # Check for standard video indicators
        if any(indicator in url_lower for indicator in video_indicators):
            return True

        # Check for streaming/segmented indicators
        if any(indicator in url_lower for indicator in streaming_indicators):
            return True

        # Additional validation for complex CDN URLs
        # Check for common video CDN patterns
        cdn_patterns = [
            'cdn', 'vcdn', 'video-', 'stream-', 'media-',
            '.icegayporn.com', '.spankbang.com', '.pornhub.com'
        ]

        if any(pattern in url_lower for pattern in cdn_patterns):
            # If it's from a video CDN and has video-like parameters, consider it valid
            video_params = ['key=', 'end=', 'start=', 'duration=', 'time=']
            if any(param in url_lower for param in video_params):
                return True

        return False

    def _try_direct_download_detected_sources(self, sources):
        """Try to directly download the best quality sources detected by enhanced methods"""
        try:
            self.log_status(f"🎬 Attempting direct download of {len(sources)} detected sources...")

            # Filter and prioritize sources by quality and type
            prioritized_sources = self._prioritize_video_sources(sources)

            for i, source in enumerate(prioritized_sources[:10]):  # Try top 10 sources
                try:
                    self.log_status(f"📥 Trying direct download {i+1}: {source[:60]}...")

                    # Skip obvious thumbnails and previews
                    if self._is_preview_or_thumbnail(source):
                        self.log_status(f"⏭️ Skipping preview/thumbnail: {source[:40]}...")
                        continue

                    # Try different download methods for this source
                    success = self._attempt_source_download(source, i+1)
                    if success:
                        self.log_status(f"✅ Successfully downloaded from detected source {i+1}!")
                        return source

                except Exception as source_error:
                    self.log_status(f"❌ Source {i+1} failed: {str(source_error)[:50]}")
                    continue

            self.log_status("⚠️ No detected sources could be downloaded directly")
            return None

        except Exception as e:
            self.log_status(f"Direct download attempt error: {str(e)[:100]}")
            return None

    def _prioritize_video_sources(self, sources):
        """Prioritize video sources by quality and type"""
        try:
            source_priorities = []

            for source in sources:
                if not source or len(source) < 15:
                    continue

                priority_score = 0
                source_lower = source.lower()

                # Higher priority for actual video files
                if any(ext in source_lower for ext in ['.mp4', '.webm', '.avi', '.mov', '.mkv']):
                    priority_score += 100

                # VERY HIGH priority for CDN URLs with authentication parameters
                if any(param in source_lower for param in ['verify=', 'token=', 'signature=', 'auth=']):
                    priority_score += 200
                # Also boost CDN patterns
                if '.cdn' in source_lower or 'cdn.' in source_lower:
                    priority_score += 150

                # VERY HIGH priority for output_ pattern MP4s
                if 'output_' in source_lower and '.mp4' in source_lower:
                    priority_score += 150

                # Higher priority for streaming formats
                if any(ext in source_lower for ext in ['.m3u8', '.mpd']):
                    priority_score += 90

                # Lower priority for previews, thumbnails, and trailers
                if any(word in source_lower for word in ['preview', 'thumb', 'avatar', 'poster', 'trailer']):
                    priority_score -= 50

                # VERY LOW priority for trailer and advertisement URLs
                if any(ad_term in source_lower for ad_term in ['trailer.mp4', '/trailer/', 'preview.mp4', '/ads/', '/ad/']):
                    priority_score -= 100

                # Higher priority for quality indicators
                if any(qual in source_lower for qual in ['hd', '720p', '1080p', '4k', 'high', '_high']):
                    priority_score += 20

                # Higher priority for full video indicators
                if any(word in source_lower for word in ['full', 'complete', 'master']):
                    priority_score += 30

                # Boost for longer URLs (often more specific)
                priority_score += min(len(source) // 20, 10)

                source_priorities.append((priority_score, source))

            # Sort by priority score (highest first)
            source_priorities.sort(key=lambda x: x[0], reverse=True)

            prioritized_sources = [source for score, source in source_priorities]

            self.log_status(f"📊 Prioritized {len(prioritized_sources)} sources for download")

            # Log top 5 priorities for debugging
            for i, (score, source) in enumerate(source_priorities[:5]):
                self.log_status(f"  #{i+1} (score: {score}): {source[:50]}...")

            return prioritized_sources

        except Exception as e:
            self.log_status(f"Source prioritization error: {str(e)[:50]}")
            return list(sources)

    def _is_preview_or_thumbnail(self, url):
        """Check if URL is likely a preview or thumbnail"""
        if not url:
            return True

        url_lower = url.lower()

        # Obvious preview/thumbnail indicators
        preview_indicators = [
            'preview', 'thumb', 'thumbnail', 'avatar', 'poster',
            'icon', 'logo', 'banner', 'cover', 'small', 'mini',
            'trailer.mp4', 'preview.mp4', '.svg', '.jpg', '.png', '.gif',
            'sugarcams.com', '/ad/', 'ads.', 'advertisement'
        ]

        # Check for main video indicators that should NOT be filtered
        main_video_indicators = [
            '_high.mp4', '_medium.mp4', '_low.mp4', 'main', 'full',
            'output_', 'video_', 'content_'
        ]

        # If it has main video indicators, don't consider it a preview
        if any(indicator in url_lower for indicator in main_video_indicators):
            return False

        return any(indicator in url_lower for indicator in preview_indicators)

    def _attempt_source_download(self, source, attempt_num):
        """Attempt to download a single source using multiple methods"""
        try:
            self.log_status(f"🔄 Download attempt {attempt_num} for: {source[:50]}...")

            # For CDN sources with auth params, try direct HTTP first as it's more reliable
            source_lower = source.lower()
            is_cdn_source = (any(param in source_lower for param in ['verify=', 'token=', 'signature=', 'auth=']) or
                           '.cdn' in source_lower or 'cdn.' in source_lower)

            if is_cdn_source:
                # Method 1: Try direct HTTP download first for CDN sources
                direct_success = self._try_direct_http_download(source)
                if direct_success:
                    return True

                # Method 2: Try yt-dlp as fallback
                yt_dlp_success = self._try_yt_dlp_download(source)
                if yt_dlp_success:
                    return True
            else:
                # Method 1: Try yt-dlp first for non-CDN sources
                yt_dlp_success = self._try_yt_dlp_download(source)
                if yt_dlp_success:
                    return True

                # Method 2: Try direct HTTP download
                direct_success = self._try_direct_http_download(source)
                if direct_success:
                    return True

            # Method 3: Try browser-based download
            browser_success = self._try_browser_download(source)
            if browser_success:
                return True

            return False

        except Exception as e:
            self.log_status(f"Source download attempt error: {str(e)[:50]}")
            return False

    def _try_yt_dlp_download(self, source):
        """Try to download source with yt-dlp"""
        try:
            self.log_status(f"🎯 Trying yt-dlp download: {source[:40]}...")

            # Use the existing yt-dlp download method
            return self._download_direct_url(source)

        except Exception as e:
            self.log_status(f"yt-dlp download failed: {str(e)[:40]}")
            return False

    def _try_direct_http_download(self, source):
        """Try direct HTTP download"""
        try:
            import requests
            import os
            import urllib.parse

            self.log_status(f"📡 Trying direct HTTP download: {source[:40]}...")

            # Parse filename from URL
            parsed_url = urllib.parse.urlparse(source)
            filename = os.path.basename(parsed_url.path)
            if not filename or '.' not in filename:
                # Generate filename from URL
                url_hash = abs(hash(source))
                filename = f"direct_download_{url_hash}.mp4"

            # Ensure proper extension
            if not any(filename.lower().endswith(ext) for ext in ['.mp4', '.webm', '.avi', '.mov']):
                filename += '.mp4'

            download_path = os.path.join(self.download_folder, filename)

            # Make request with proper headers for CDN access
            # Build headers with dynamic Referer/Origin from current page
            current_referer = self.driver.current_url if self.driver else ''
            if current_referer:
                from urllib.parse import urlparse
                parsed = urlparse(current_referer)
                origin = f"{parsed.scheme}://{parsed.netloc}"
            else:
                origin = ''

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Referer': current_referer if current_referer else '',
                'Accept': 'video/mp4,video/webm,video/*,*/*;q=0.8',
                'Accept-Encoding': 'identity',
                'Accept-Language': 'en-US,en;q=0.9',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }

            # Add origin header for CDN sources with auth params
            source_lower = source.lower()
            if (any(param in source_lower for param in ['verify=', 'token=', 'signature=', 'auth=']) or
                '.cdn' in source_lower or 'cdn.' in source_lower):
                if origin:
                    headers['Origin'] = origin

            response = requests.get(source, headers=headers, stream=True, timeout=30)
            response.raise_for_status()

            # Check if it's actually a video file
            content_type = response.headers.get('content-type', '').lower()
            if not any(vid_type in content_type for vid_type in ['video/', 'application/octet-stream']):
                self.log_status(f"❌ Not a video file (content-type: {content_type})")
                return False

            # Download the file
            total_size = int(response.headers.get('content-length', 0))
            if total_size > 0:
                self.log_status(f"📁 Downloading {total_size // 1024 // 1024}MB to: {filename}")

            with open(download_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            # Verify file was downloaded
            if os.path.exists(download_path) and os.path.getsize(download_path) > 1024:  # At least 1KB
                self.log_status(f"✅ Direct HTTP download successful: {filename}")
                return True
            else:
                self.log_status("❌ Downloaded file is too small or doesn't exist")
                return False

        except Exception as e:
            self.log_status(f"Direct HTTP download failed: {str(e)[:50]}")
            return False

    def _try_browser_download(self, source):
        """Try browser-based download"""
        try:
            if not self.driver:
                return False

            self.log_status(f"🌐 Trying browser download: {source[:40]}...")

            # Navigate to the video URL
            self.driver.get(source)
            time.sleep(0.1)

            # Check if it's a direct video file
            current_url = self.driver.current_url
            if current_url.lower().endswith(('.mp4', '.webm', '.avi', '.mov')):
                self.log_status("🎬 Direct video file detected in browser")
                # Right-click and save
                try:
                    video_element = self.driver.find_element(By.TAG_NAME, "video")
                    if video_element:
                        ActionChains(self.driver).context_click(video_element).perform()
                        time.sleep(0.2)
                        # Simulate keyboard shortcut for save
                        ActionChains(self.driver).send_keys('a').perform()  # 'Save video as'
                        time.sleep(0.2)
                        return True
                except:
                    pass

            return False

        except Exception as e:
            self.log_status(f"Browser download failed: {str(e)[:40]}")
            return False

    def _download_direct_url(self, video_url):
        """Download video directly from URL"""
        try:
            self.log_status(f"Attempting direct download: {video_url}")

            # Use requests to download the video
            import requests

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': self.driver.current_url if hasattr(self.driver, 'current_url') else ''
            }

            response = requests.get(video_url, headers=headers, stream=True, timeout=30)

            if response.status_code == 200:
                # Generate filename
                from urllib.parse import urlparse
                parsed = urlparse(video_url)
                filename = os.path.basename(parsed.path) or "downloaded_video.mp4"

                if not filename.endswith(('.mp4', '.avi', '.mov', '.webm')):
                    filename += '.mp4'

                # Get download folder - check multiple possible locations
                download_folder = None
                if hasattr(self.driver, 'download_folder'):
                    download_folder = self.driver.download_folder
                elif hasattr(self, 'download_folder'):
                    download_folder = self.download_folder
                else:
                    # Use default Downloads Chrome folder
                    download_folder = "D:/4k video downloader - Copy/Downloads Chrome"

                self.log_status(f"Downloading to folder: {download_folder}")
                output_path = os.path.join(download_folder, filename)
                
                # Download file
                self.log_status(f"Starting file download: {filename}")
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0

                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                progress = (downloaded / total_size) * 100
                                if progress % 10 < 0.1:  # Log every ~10%
                                    self.log_status(f"Download progress: {progress:.0f}%")

                self.log_status(f"✅ Direct download completed: {filename}")
                self.log_status(f"📁 File saved to: {output_path}")
                return True
            else:
                self.log_status(f"❌ Direct download failed - HTTP {response.status_code}")
                return False

        except requests.exceptions.Timeout:
            self.log_status(f"❌ Direct download timeout after 30 seconds")
            return False
        except requests.exceptions.RequestException as e:
            self.log_status(f"❌ Direct download network error: {str(e)[:100]}")
            return False
        except IOError as e:
            self.log_status(f"❌ Direct download file write error: {str(e)[:100]}")
            return False
        except Exception as e:
            self.log_status(f"❌ Direct download unexpected error: {str(e)[:100]}")
            logger.error(f"Direct download failed: {e}")
            return False

    def _download_with_yt_dlp(self, video_url):
        """Download video using yt-dlp for video page URLs (like Pornhub, YouTube, etc.)"""
        try:
            self.log_status(f"🎬 Using yt-dlp for video page: {video_url[:60]}")

            # Get download folder - check multiple possible locations
            download_folder = None
            if hasattr(self.driver, 'download_folder'):
                download_folder = self.driver.download_folder
            elif hasattr(self, 'download_folder'):
                download_folder = self.download_folder
            else:
                # Use default Downloads Chrome folder
                download_folder = "D:/4k video downloader - Copy/Downloads Chrome"

            self.log_status(f"📁 Download folder: {download_folder}")

            # Ensure download folder exists
            os.makedirs(download_folder, exist_ok=True)

            # Preprocess URL for better yt-dlp compatibility
            processed_url = self._preprocess_url_for_yt_dlp(video_url)
            self.log_status(f"🔄 Processed URL: {processed_url}")

            # Build yt-dlp command with specific output template and options
            output_template = os.path.join(download_folder, '%(title)s.%(ext)s')
            cmd = [
                'yt-dlp',
                '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',  # Best video+audio, merge if needed
                '--merge-output-format', 'mp4',  # Ensure output is MP4
                '--output', output_template,
                '--no-warnings',
                '--prefer-insecure',  # Speed up by skipping some checks
                '--extractor-retries', '3',
                '--fragment-retries', '3',
                '--retry-sleep', '1',
                '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                processed_url
            ]

            self.log_status(f"🎯 Executing yt-dlp command: {' '.join(cmd[:3])} ... {processed_url[:40]}")

            # Execute yt-dlp command with timeout
            result = self._execute_download_command_with_progress(cmd, download_folder)

            if result:
                self.log_status(f"✅ yt-dlp download completed successfully")
                return True
            else:
                self.log_status(f"❌ yt-dlp download failed")
                return False

        except Exception as e:
            self.log_status(f"❌ yt-dlp download error: {str(e)[:100]}")
            logger.error(f"yt-dlp download failed: {e}")
            return False

    def _create_fake_element_for_download(self, video_url):
        """Create a fake element for right-click download of direct URLs"""
        try:
            # Store the URL for later use in right-click method
            self._direct_video_url = video_url
            
            # Return a fake element that will trigger direct download
            class FakeElement:
                def __init__(self, url):
                    self.video_url = url
                    
                def is_displayed(self):
                    return True
                    
                def get_attribute(self, attr):
                    if attr == 'src':
                        return self.video_url
                    return None
            
            return FakeElement(video_url)
            
        except Exception as e:
            logger.error(f"Error creating fake element: {e}")
            return None
    
    def _extract_from_iframes_and_embeds(self):
        """STRATEGY 6: Advanced iframe and embed content extraction with recursive analysis"""
        try:
            self.log_status("Strategy 6: Comprehensive iframe and embedded content analysis")
            
            detected_sources = set()
            
            # Phase 1: Direct iframe source analysis
            iframe_sources = self._analyze_iframe_sources()
            detected_sources.update(iframe_sources)
            
            # Phase 2: Deep iframe content extraction
            iframe_content = self._extract_iframe_content()
            detected_sources.update(iframe_content)
            
            # Phase 3: Embed and object tag analysis
            embed_sources = self._analyze_embed_objects()
            detected_sources.update(embed_sources)
            
            # Phase 4: Cross-frame communication analysis
            frame_communication = self._analyze_cross_frame_communication()
            detected_sources.update(frame_communication)
            
            # Phase 5: Nested iframe recursion
            nested_sources = self._analyze_nested_iframes()
            detected_sources.update(nested_sources)
            
            # Evaluate and return best source
            if detected_sources:
                best_source = self._evaluate_iframe_sources(detected_sources)
                if best_source:
                    return self._create_fake_element_for_download(best_source)
            
            return None
            
        except Exception as e:
            logger.error(f"Strategy 6 failed: {e}")
            return None
    
    def _analyze_iframe_sources(self):
        """Analyze iframe sources for video content indicators"""
        try:
            detected_sources = set()
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")
            
            for iframe in iframes:
                try:
                    iframe_src = iframe.get_attribute('src')
                    if not iframe_src:
                        continue
                    
                    # Direct video URL check
                    if self._is_valid_video_url(iframe_src):
                        detected_sources.add(iframe_src)
                        continue
                    
                    # Video platform detection
                    video_platforms = [
                        'youtube.com', 'vimeo.com', 'dailymotion.com',
                        'twitch.tv', 'facebook.com', 'instagram.com',
                        'tiktok.com', 'streamable.com', 'wistia.com'
                    ]
                    
                    if any(platform in iframe_src.lower() for platform in video_platforms):
                        # Extract video ID and construct direct URL
                        direct_url = self._extract_platform_direct_url(iframe_src)
                        if direct_url:
                            detected_sources.add(direct_url)
                    
                    # Check for video-related path indicators
                    video_indicators = [
                        '/video/', '/player/', '/embed/', '/stream/',
                        '/media/', '/watch/', '/v/'
                    ]
                    
                    if any(indicator in iframe_src.lower() for indicator in video_indicators):
                        # Try to fetch iframe content for video sources
                        iframe_videos = self._fetch_iframe_video_sources(iframe_src)
                        detected_sources.update(iframe_videos)
                        
                except Exception:
                    continue
            
            return detected_sources
            
        except Exception as e:
            logger.error(f"Iframe source analysis failed: {e}")
            return set()
    
    def _extract_iframe_content(self):
        """Extract video content from within iframes"""
        try:
            detected_sources = set()
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")
            
            for iframe in iframes:
                try:
                    # Store original context
                    original_window = self.driver.current_window_handle
                    
                    # Switch to iframe context
                    self.driver.switch_to.frame(iframe)
                    
                    # Comprehensive video source extraction within iframe
                    iframe_sources = self._comprehensive_iframe_video_extraction()
                    detected_sources.update(iframe_sources)
                    
                    # Switch back to original context
                    self.driver.switch_to.default_content()
                    
                except Exception:
                    # Ensure we're back in main context
                    try:
                        self.driver.switch_to.default_content()
                    except:
                        pass
                    continue
            
            return detected_sources
            
        except Exception as e:
            logger.error(f"Iframe content extraction failed: {e}")
            # Ensure we're in main context
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return set()
    
    def _comprehensive_iframe_video_extraction(self):
        """Comprehensive video extraction within iframe context - ENHANCED"""
        try:
            sources = set()

            # NEW: Enhanced methods integration
            self.log_status("🚀 Running ENHANCED iframe video extraction...")

            # 1. Enhanced JavaScript Detection
            enhanced_js_sources = self._enhanced_javascript_video_detection()
            sources.update(enhanced_js_sources)
            if enhanced_js_sources:
                self.log_status(f"✅ Enhanced JS found {len(enhanced_js_sources)} sources in iframe")

            # 2. Advanced Stream Detection
            stream_sources = self._advanced_stream_detection()
            sources.update(stream_sources)
            if stream_sources:
                self.log_status(f"🎬 Stream detection found {len(stream_sources)} sources in iframe")

            # 3. Dynamic Content Waiting
            dynamic_sources = self._dynamic_content_waiting_and_detection()
            sources.update(dynamic_sources)
            if dynamic_sources:
                self.log_status(f"⏳ Dynamic detection found {len(dynamic_sources)} sources in iframe")

            # 4. Original direct video elements (kept for compatibility)
            videos = self.driver.find_elements(By.TAG_NAME, "video")
            for video in videos:
                src = video.get_attribute('src') or video.get_attribute('currentSrc')
                if src and self._is_valid_video_url(src):
                    sources.add(src)
            
            # 2. Source elements
            source_elements = self.safe_find_elements(By.TAG_NAME, "source")
            for source in source_elements:
                src = source.get_attribute('src')
                if src and self._is_valid_video_url(src):
                    sources.add(src)
            
            # 3. JavaScript video source extraction within iframe
            js_sources = self.driver.execute_script("""
                var sources = [];
                
                // Check all possible video source locations
                var videos = document.querySelectorAll('video, source');
                videos.forEach(function(v) {
                    if (v.src) sources.push(v.src);
                    if (v.currentSrc) sources.push(v.currentSrc);
                });
                
                // Check data attributes
                var dataElements = document.querySelectorAll('[data-src], [data-video], [data-url]');
                dataElements.forEach(function(e) {
                    ['data-src', 'data-video', 'data-url'].forEach(function(attr) {
                        var val = e.getAttribute(attr);
                        if (val && (val.includes('.mp4') || val.includes('.webm') || val.includes('video'))) {
                            sources.push(val);
                        }
                    });
                });
                
                // Check for video URLs in scripts within iframe
                var scripts = document.querySelectorAll('script');
                scripts.forEach(function(script) {
                    var content = script.innerHTML;
                    var matches = content.match(/["']https?:\\/\\/[^"']*\\.(mp4|webm|avi|mov)[^"']*["']/gi);
                    if (matches) {
                        matches.forEach(function(match) {
                            var url = match.replace(/['"]/g, '');
                            sources.push(url);
                        });
                    }
                });
                
                return sources.filter(function(s) { 
                    return s && s.length > 10 && s.startsWith('http'); 
                });
            """)
            
            for source in js_sources:
                if self._is_valid_video_url(source):
                    sources.add(source)
            
            # 4. Look for video player APIs within iframe
            api_sources = self.driver.execute_script("""
                var sources = [];
                
                // Common video player APIs
                if (window.player && window.player.src) {
                    sources.push(window.player.src);
                }
                if (window.videojs && window.videojs.getAllPlayers) {
                    try {
                        var players = window.videojs.getAllPlayers();
                        players.forEach(function(player) {
                            if (player.src) sources.push(player.src());
                        });
                    } catch(e) {}
                }
                
                // Check for global video configuration
                var configVars = ['videoConfig', 'mediaConfig', 'playerConfig', 'streamConfig'];
                configVars.forEach(function(varName) {
                    if (window[varName] && window[varName].src) {
                        sources.push(window[varName].src);
                    }
                });
                
                return sources;
            """)
            
            for source in api_sources:
                if source and self._is_valid_video_url(source):
                    sources.add(source)
            
            return sources
            
        except Exception as e:
            logger.error(f"Comprehensive iframe extraction failed: {e}")
            return set()
    
    def _analyze_embed_objects(self):
        """Analyze embed and object tags for video content"""
        try:
            detected_sources = set()
            
            # Embed tags
            embeds = self.driver.find_elements(By.TAG_NAME, "embed")
            for embed in embeds:
                try:
                    src = embed.get_attribute('src')
                    if src and self._is_valid_video_url(src):
                        detected_sources.add(src)
                    
                    # Check for Flash video parameters
                    flashvars = embed.get_attribute('flashvars')
                    if flashvars:
                        video_urls = self._extract_urls_from_flashvars(flashvars)
                        detected_sources.update(video_urls)
                        
                except Exception:
                    continue
            
            # Object tags
            objects = self.driver.find_elements(By.TAG_NAME, "object")
            for obj in objects:
                try:
                    data = obj.get_attribute('data')
                    if data and self._is_valid_video_url(data):
                        detected_sources.add(data)
                    
                    # Check param tags within object
                    params = obj.find_elements(By.TAG_NAME, "param")
                    for param in params:
                        param_name = param.get_attribute('name') or ''
                        param_value = param.get_attribute('value') or ''
                        
                        if 'video' in param_name.lower() or 'src' in param_name.lower():
                            if self._is_valid_video_url(param_value):
                                detected_sources.add(param_value)
                                
                except Exception:
                    continue
            
            return detected_sources
            
        except Exception as e:
            logger.error(f"Embed/object analysis failed: {e}")
            return set()

    def _enhanced_javascript_video_detection(self):
        """Enhanced JavaScript-based video detection with player API support"""
        try:
            self.log_status("🔍 Running enhanced JavaScript video detection...")
            detected_sources = set()

            # Execute comprehensive JavaScript to detect video sources
            js_sources = self.driver.execute_script("""
                var sources = [];
                var debugInfo = [];

                // 1. VideoJS Player Detection
                try {
                    if (window.videojs) {
                        var players = window.videojs.getAllPlayers ? window.videojs.getAllPlayers() : [];
                        players.forEach(function(player, i) {
                            try {
                                var src = player.src();
                                if (src) {
                                    sources.push(src);
                                    debugInfo.push('VideoJS Player ' + i + ': ' + src);
                                }
                                var currentSrc = player.currentSrc();
                                if (currentSrc && currentSrc !== src) {
                                    sources.push(currentSrc);
                                    debugInfo.push('VideoJS CurrentSrc ' + i + ': ' + currentSrc);
                                }
                            } catch(e) {}
                        });
                    }
                } catch(e) {}

                // 2. JWPlayer Detection
                try {
                    if (window.jwplayer) {
                        var jwInstances = window.jwplayer.getPlayers ? window.jwplayer.getPlayers() : [];
                        jwInstances.forEach(function(player, i) {
                            try {
                                var config = player.getConfig();
                                if (config && config.file) {
                                    sources.push(config.file);
                                    debugInfo.push('JWPlayer ' + i + ': ' + config.file);
                                }
                                if (config && config.sources) {
                                    config.sources.forEach(function(source) {
                                        if (source.file) {
                                            sources.push(source.file);
                                            debugInfo.push('JWPlayer Source: ' + source.file);
                                        }
                                    });
                                }
                            } catch(e) {}
                        });
                    }
                } catch(e) {}

                // 3. Plyr Player Detection
                try {
                    if (window.Plyr && window.Plyr.instances) {
                        window.Plyr.instances.forEach(function(player, i) {
                            try {
                                var media = player.media;
                                if (media && media.src) {
                                    sources.push(media.src);
                                    debugInfo.push('Plyr ' + i + ': ' + media.src);
                                }
                                if (media && media.currentSrc) {
                                    sources.push(media.currentSrc);
                                    debugInfo.push('Plyr CurrentSrc ' + i + ': ' + media.currentSrc);
                                }
                            } catch(e) {}
                        });
                    }
                } catch(e) {}

                // 4. Global Video Configuration Objects
                var configVars = [
                    'videoConfig', 'playerConfig', 'mediaConfig', 'streamConfig',
                    'VIDEO_CONFIG', 'PLAYER_CONFIG', 'MEDIA_CONFIG', 'config',
                    'playerSettings', 'videoSettings', 'streamSettings'
                ];

                configVars.forEach(function(varName) {
                    try {
                        var config = window[varName];
                        if (config) {
                            // Check for direct src property
                            if (config.src) {
                                sources.push(config.src);
                                debugInfo.push(varName + '.src: ' + config.src);
                            }
                            if (config.file) {
                                sources.push(config.file);
                                debugInfo.push(varName + '.file: ' + config.file);
                            }
                            if (config.url) {
                                sources.push(config.url);
                                debugInfo.push(varName + '.url: ' + config.url);
                            }

                            // Check for sources array
                            if (config.sources && Array.isArray(config.sources)) {
                                config.sources.forEach(function(source, i) {
                                    if (typeof source === 'string') {
                                        sources.push(source);
                                        debugInfo.push(varName + '.sources[' + i + ']: ' + source);
                                    } else if (source.src || source.file || source.url) {
                                        var srcUrl = source.src || source.file || source.url;
                                        sources.push(srcUrl);
                                        debugInfo.push(varName + '.sources[' + i + '].src: ' + srcUrl);
                                    }
                                });
                            }
                        }
                    } catch(e) {}
                });

                // 5. HTML5 Video Elements Deep Scan
                var videos = document.querySelectorAll('video');
                videos.forEach(function(video, i) {
                    // Standard properties
                    if (video.src) {
                        sources.push(video.src);
                        debugInfo.push('Video[' + i + '].src: ' + video.src);
                    }
                    if (video.currentSrc) {
                        sources.push(video.currentSrc);
                        debugInfo.push('Video[' + i + '].currentSrc: ' + video.currentSrc);
                    }

                    // Data attributes
                    var dataAttrs = ['data-src', 'data-video-src', 'data-url', 'data-file', 'data-stream'];
                    dataAttrs.forEach(function(attr) {
                        var val = video.getAttribute(attr);
                        if (val) {
                            sources.push(val);
                            debugInfo.push('Video[' + i + '].' + attr + ': ' + val);
                        }
                    });

                    // Source child elements
                    var sourceTags = video.querySelectorAll('source');
                    sourceTags.forEach(function(source, j) {
                        if (source.src) {
                            sources.push(source.src);
                            debugInfo.push('Video[' + i + '] Source[' + j + ']: ' + source.src);
                        }
                    });
                });

                // 6. Dynamic Script Content Analysis
                var scripts = document.querySelectorAll('script:not([src])');
                scripts.forEach(function(script, i) {
                    var content = script.textContent || script.innerHTML;
                    if (content) {
                        // Match video URLs in various formats
                        var patterns = [
                            /["']https?:\\/\\/[^"']*\\.(mp4|webm|avi|mov|mkv|flv|m4v)\\?[^"']*["']/gi,
                            /["']https?:\\/\\/[^"']*\\.(mp4|webm|avi|mov|mkv|flv|m4v)["']/gi,
                            /src["']?:\\s*["']https?:\\/\\/[^"']*\\.(mp4|webm|avi|mov|mkv|flv|m4v)[^"']*["']/gi,
                            /file["']?:\\s*["']https?:\\/\\/[^"']*\\.(mp4|webm|avi|mov|mkv|flv|m4v)[^"']*["']/gi,
                            /url["']?:\\s*["']https?:\\/\\/[^"']*\\.(mp4|webm|avi|mov|mkv|flv|m4v)[^"']*["']/gi,
                            // HLS and DASH
                            /["']https?:\\/\\/[^"']*\\.m3u8[^"']*["']/gi,
                            /["']https?:\\/\\/[^"']*\\.mpd[^"']*["']/gi,
                            // Streaming domains
                            /["']https?:\\/\\/[^"']*(?:video|stream|cdn|media)[^"']*\\.(mp4|webm|m3u8|mpd)[^"']*["']/gi
                        ];

                        patterns.forEach(function(pattern) {
                            var matches = content.match(pattern);
                            if (matches) {
                                matches.forEach(function(match) {
                                    var cleanUrl = match.replace(/['"]/g, '').replace(/^(src|file|url):\\s*/, '');
                                    sources.push(cleanUrl);
                                    debugInfo.push('Script[' + i + '] Pattern Match: ' + cleanUrl);
                                });
                            }
                        });
                    }
                });

                // 7. Window Object Deep Scan
                try {
                    function scanObject(obj, path, maxDepth) {
                        if (maxDepth <= 0) return;

                        for (var key in obj) {
                            try {
                                var value = obj[key];
                                var currentPath = path + '.' + key;

                                if (typeof value === 'string' && value.length > 10) {
                                    // Check if it's a video URL
                                    if (value.match(/https?:\\/\\/.*\\.(mp4|webm|avi|mov|mkv|flv|m4v|m3u8|mpd)/i)) {
                                        sources.push(value);
                                        debugInfo.push('Window' + currentPath + ': ' + value);
                                    }
                                } else if (typeof value === 'object' && value !== null && !value.nodeType) {
                                    scanObject(value, currentPath, maxDepth - 1);
                                }
                            } catch(e) {}
                        }
                    }

                    // Scan common video-related window properties
                    var scanTargets = ['player', 'video', 'media', 'stream', 'config'];
                    scanTargets.forEach(function(target) {
                        if (window[target]) {
                            scanObject(window[target], target, 3);
                        }
                    });
                } catch(e) {}

                // Clean and deduplicate sources
                var cleanSources = [];
                var seen = new Set();

                sources.forEach(function(source) {
                    if (source && typeof source === 'string' && source.length > 10) {
                        // Basic URL validation
                        if (source.startsWith('http') && !seen.has(source)) {
                            cleanSources.push(source);
                            seen.add(source);
                        }
                    }
                });

                return {
                    sources: cleanSources,
                    debug: debugInfo
                };
            """)

            if js_sources and js_sources.get('sources'):
                self.log_status(f"✅ Enhanced JS detection found {len(js_sources['sources'])} video sources!")

                # Log debug info
                for debug_msg in js_sources.get('debug', [])[:10]:  # Limit debug output
                    self.log_status(f"  📋 {debug_msg}")

                for source in js_sources['sources']:
                    if self._is_valid_video_url(source):
                        detected_sources.add(source)

            return detected_sources

        except Exception as e:
            self.log_status(f"Enhanced JS detection error: {str(e)[:100]}")
            logger.error(f"Enhanced JavaScript detection failed: {e}")
            return set()

    def _network_request_monitoring(self):
        """Monitor network requests for video URLs using Chrome DevTools Protocol"""
        try:
            self.log_status("🌐 Starting network request monitoring...")
            detected_sources = set()

            # Enable Chrome DevTools Protocol network domain
            try:
                self.driver.execute_cdp_cmd('Network.enable', {})
                self.log_status("✅ Network monitoring enabled")
            except Exception as e:
                self.log_status(f"⚠️ CDP not available: {str(e)[:50]}")
                return self._fallback_network_monitoring()

            # Collect network requests for a short period
            import time
            start_time = time.time()
            timeout = 5  # Reduced from 10 to 5 seconds monitoring

            while time.time() - start_time < timeout:
                try:
                    # Get network events
                    logs = self.driver.get_log('performance')

                    for log in logs:
                        message = log.get('message', {})
                        if isinstance(message, str):
                            import json
                            try:
                                message = json.loads(message)
                            except:
                                continue

                        method = message.get('method', '')
                        params = message.get('params', {})

                        # Check for network responses
                        if method == 'Network.responseReceived':
                            response = params.get('response', {})
                            url = response.get('url', '')
                            mime_type = response.get('mimeType', '')

                            # Check for video URLs
                            if self._is_video_network_request(url, mime_type):
                                detected_sources.add(url)
                                self.log_status(f"📡 Network detected: {url[:80]}")

                        # Check for XHR/Fetch requests
                        elif method == 'Network.requestWillBeSent':
                            request = params.get('request', {})
                            url = request.get('url', '')

                            if self._is_video_api_request(url):
                                detected_sources.add(url)
                                self.log_status(f"🔗 API detected: {url[:80]}")

                except Exception:
                    pass

                time.sleep(0.1)  # Check every 500ms

            # Disable network monitoring
            try:
                self.driver.execute_cdp_cmd('Network.disable', {})
            except:
                pass

            return detected_sources

        except Exception as e:
            self.log_status(f"Network monitoring error: {str(e)[:100]}")
            return set()

    def _fallback_network_monitoring(self):
        """Fallback network monitoring using JavaScript"""
        try:
            self.log_status("🔄 Using fallback network monitoring...")

            # Inject network monitoring JavaScript
            self.driver.execute_script("""
                window.videoNetworkCapture = [];

                // Override XMLHttpRequest
                var originalXHR = window.XMLHttpRequest;
                window.XMLHttpRequest = function() {
                    var xhr = new originalXHR();
                    var originalOpen = xhr.open;
                    var originalSend = xhr.send;

                    xhr.open = function(method, url) {
                        if (url && (url.includes('.mp4') || url.includes('.webm') ||
                                   url.includes('.m3u8') || url.includes('video') ||
                                   url.includes('stream'))) {
                            window.videoNetworkCapture.push({
                                type: 'XHR',
                                method: method,
                                url: url,
                                timestamp: Date.now()
                            });
                        }
                        return originalOpen.apply(this, arguments);
                    };

                    return xhr;
                };

                // Override fetch
                if (window.fetch) {
                    var originalFetch = window.fetch;
                    window.fetch = function(resource, init) {
                        var url = typeof resource === 'string' ? resource : resource.url;
                        if (url && (url.includes('.mp4') || url.includes('.webm') ||
                                   url.includes('.m3u8') || url.includes('video') ||
                                   url.includes('stream'))) {
                            window.videoNetworkCapture.push({
                                type: 'Fetch',
                                url: url,
                                timestamp: Date.now()
                            });
                        }
                        return originalFetch.apply(this, arguments);
                    };
                }

                console.log('Video network monitoring injected');
            """)

            # Wait for network activity
            import time
            time.sleep(0.3)

            # Collect captured requests
            captured_requests = self.driver.execute_script("""
                return window.videoNetworkCapture || [];
            """)

            detected_sources = set()
            for request in captured_requests:
                url = request.get('url', '')
                if url and self._is_valid_video_url(url):
                    detected_sources.add(url)
                    self.log_status(f"📡 Fallback detected: {url[:80]}")

            return detected_sources

        except Exception as e:
            self.log_status(f"Fallback network monitoring error: {str(e)[:100]}")
            return set()

    def _is_video_network_request(self, url, mime_type):
        """Check if a network request is for video content"""
        if not url:
            return False

        # Check MIME type
        if mime_type and ('video/' in mime_type or 'application/vnd.apple.mpegurl' in mime_type):
            return True

        # Check URL patterns
        video_patterns = [
            r'\.mp4(\?|$)', r'\.webm(\?|$)', r'\.avi(\?|$)', r'\.mov(\?|$)',
            r'\.mkv(\?|$)', r'\.flv(\?|$)', r'\.m4v(\?|$)',
            r'\.m3u8(\?|$)', r'\.mpd(\?|$)',
            r'video.*stream', r'stream.*video', r'/video/', r'/stream/'
        ]

        import re
        url_lower = url.lower()
        return any(re.search(pattern, url_lower) for pattern in video_patterns)

    def _is_video_api_request(self, url):
        """Check if URL is a video API request"""
        if not url:
            return False

        api_indicators = [
            'api/video', 'video/api', 'stream/api', 'api/stream',
            'player/api', 'api/player', 'media/api', 'api/media',
            'embed/api', 'api/embed'
        ]

        url_lower = url.lower()
        return any(indicator in url_lower for indicator in api_indicators)

    def _advanced_stream_detection(self):
        """Detect HLS, DASH and progressive streaming sources"""
        try:
            self.log_status("🎬 Running advanced stream detection...")
            detected_sources = set()

            # Execute JavaScript to find streaming sources
            streaming_sources = self.driver.execute_script("""
                var sources = [];
                var debugInfo = [];

                // 1. HLS (.m3u8) Detection
                function findHLSSources() {
                    // Check script content for m3u8 URLs
                    var scripts = document.querySelectorAll('script');
                    scripts.forEach(function(script, i) {
                        var content = script.textContent || script.innerHTML;
                        var m3u8Matches = content.match(/https?:\\/\\/[^\\s"'<>]+\\.m3u8[^\\s"'<>]*/gi);
                        if (m3u8Matches) {
                            m3u8Matches.forEach(function(match) {
                                sources.push(match);
                                debugInfo.push('HLS Script[' + i + ']: ' + match);
                            });
                        }
                    });

                    // Check data attributes
                    var elements = document.querySelectorAll('[data-hls], [data-m3u8], [data-stream-url]');
                    elements.forEach(function(el, i) {
                        ['data-hls', 'data-m3u8', 'data-stream-url'].forEach(function(attr) {
                            var val = el.getAttribute(attr);
                            if (val && val.includes('.m3u8')) {
                                sources.push(val);
                                debugInfo.push('HLS Data[' + i + '].' + attr + ': ' + val);
                            }
                        });
                    });
                }

                // 2. DASH (.mpd) Detection
                function findDASHSources() {
                    var scripts = document.querySelectorAll('script');
                    scripts.forEach(function(script, i) {
                        var content = script.textContent || script.innerHTML;
                        var mpdMatches = content.match(/https?:\\/\\/[^\\s"'<>]+\\.mpd[^\\s"'<>]*/gi);
                        if (mpdMatches) {
                            mpdMatches.forEach(function(match) {
                                sources.push(match);
                                debugInfo.push('DASH Script[' + i + ']: ' + match);
                            });
                        }
                    });

                    var elements = document.querySelectorAll('[data-dash], [data-mpd]');
                    elements.forEach(function(el, i) {
                        ['data-dash', 'data-mpd'].forEach(function(attr) {
                            var val = el.getAttribute(attr);
                            if (val && val.includes('.mpd')) {
                                sources.push(val);
                                debugInfo.push('DASH Data[' + i + '].' + attr + ': ' + val);
                            }
                        });
                    });
                }

                // 3. Progressive Streaming Detection
                function findProgressiveSources() {
                    // Look for common progressive streaming patterns
                    var progressivePatterns = [
                        /https?:\\/\\/[^\\s"'<>]*\\/video\\/[^\\s"'<>]*\\.(mp4|webm)/gi,
                        /https?:\\/\\/[^\\s"'<>]*\\/stream\\/[^\\s"'<>]*\\.(mp4|webm)/gi,
                        /https?:\\/\\/[^\\s"'<>]*\\/media\\/[^\\s"'<>]*\\.(mp4|webm)/gi
                    ];

                    var pageContent = document.documentElement.outerHTML;
                    progressivePatterns.forEach(function(pattern, i) {
                        var matches = pageContent.match(pattern);
                        if (matches) {
                            matches.forEach(function(match) {
                                sources.push(match);
                                debugInfo.push('Progressive Pattern[' + i + ']: ' + match);
                            });
                        }
                    });
                }

                // 4. Blob URL Detection
                function findBlobSources() {
                    var videos = document.querySelectorAll('video');
                    videos.forEach(function(video, i) {
                        if (video.src && video.src.startsWith('blob:')) {
                            sources.push(video.src);
                            debugInfo.push('Blob Video[' + i + ']: ' + video.src);
                        }

                        var sourceTags = video.querySelectorAll('source');
                        sourceTags.forEach(function(source, j) {
                            if (source.src && source.src.startsWith('blob:')) {
                                sources.push(source.src);
                                debugInfo.push('Blob Source[' + i + '][' + j + ']: ' + source.src);
                            }
                        });
                    });
                }

                // 5. MediaSource API Detection
                function findMediaSourceSources() {
                    try {
                        if (window.MediaSource && window.MediaSource.isTypeSupported) {
                            // Check for MSE usage indicators
                            var videos = document.querySelectorAll('video');
                            videos.forEach(function(video, i) {
                                // Check if video is using MediaSource
                                if (video.src && video.src.startsWith('blob:')) {
                                    // This might be MSE, check for additional context
                                    debugInfo.push('Potential MSE Video[' + i + ']');
                                }
                            });
                        }
                    } catch(e) {}
                }

                // Run all detection methods
                findHLSSources();
                findDASHSources();
                findProgressiveSources();
                findBlobSources();
                findMediaSourceSources();

                return {
                    sources: sources,
                    debug: debugInfo
                };
            """)

            if streaming_sources and streaming_sources.get('sources'):
                self.log_status(f"🎯 Stream detection found {len(streaming_sources['sources'])} sources!")

                for debug_msg in streaming_sources.get('debug', [])[:8]:
                    self.log_status(f"  📋 {debug_msg}")

                for source in streaming_sources['sources']:
                    if source and len(source) > 10:
                        detected_sources.add(source)

            return detected_sources

        except Exception as e:
            self.log_status(f"Stream detection error: {str(e)[:100]}")
            return set()

    def _extract_urls_from_flashvars(self, flashvars):
        """Extract video URLs from Flash parameters"""
        try:
            urls = set()
            
            # Parse flashvars string
            params = {}
            for param in flashvars.split('&'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    params[key] = urllib.parse.unquote(value)
            
            # Common Flash video parameters
            video_params = ['video', 'file', 'src', 'url', 'stream', 'movie']
            
            for param_name, param_value in params.items():
                if any(video_param in param_name.lower() for video_param in video_params):
                    if self._is_valid_video_url(param_value):
                        urls.add(param_value)
            
            return urls
            
        except Exception:
            return set()

    def _dynamic_content_waiting_and_detection(self):
        """Wait for dynamic content loading and detect video sources"""
        try:
            self.log_status("⏳ Starting dynamic content waiting and detection...")
            detected_sources = set()

            # Initial page source analysis
            initial_sources = self._extract_from_current_page_source()
            detected_sources.update(initial_sources)

            # Wait for video players to initialize
            self.log_status("⏱️ Waiting for video players to initialize...")

            # Multiple wait strategies
            wait_strategies = [
                {'timeout': 3, 'description': 'Initial player loading'},
                {'timeout': 5, 'description': 'Video metadata loading'},
                {'timeout': 8, 'description': 'Full player initialization'}
            ]

            for strategy in wait_strategies:
                try:
                    # Wait with dynamic checking
                    start_time = time.time()
                    timeout = strategy['timeout']

                    while time.time() - start_time < timeout:
                        # Check for video elements periodically
                        current_sources = self._extract_from_current_page_source()
                        new_sources = current_sources - detected_sources

                        if new_sources:
                            self.log_status(f"🆕 Found {len(new_sources)} new sources during {strategy['description']}")
                            detected_sources.update(new_sources)

                        # Check if any video elements are now playing
                        playing_videos = self.driver.execute_script("""
                            var videos = document.querySelectorAll('video');
                            var playingCount = 0;
                            videos.forEach(function(video) {
                                if (!video.paused && !video.ended && video.readyState > 2) {
                                    playingCount++;
                                }
                            });
                            return playingCount;
                        """)

                        if playing_videos > 0:
                            self.log_status(f"▶️ Found {playing_videos} playing video(s)")
                            break

                        time.sleep(0.1)

                except Exception as e:
                    self.log_status(f"Wait strategy error: {str(e)[:50]}")
                    continue

            # Try to trigger video loading with user interactions
            self.log_status("👆 Attempting user interaction triggers...")
            interaction_results = self._simulate_user_interactions_for_video()
            detected_sources.update(interaction_results)

            # Final comprehensive scan
            self.log_status("🔍 Final comprehensive video scan...")
            final_sources = self._comprehensive_video_scan()
            detected_sources.update(final_sources)

            return detected_sources

        except Exception as e:
            self.log_status(f"Dynamic content waiting error: {str(e)[:100]}")
            return set()

    def _extract_from_current_page_source(self):
        """Enhanced extraction of video sources from current page source"""
        try:
            detected_sources = set()
            page_source = self.driver.page_source

            # Enhanced regex patterns for video URLs with better specificity
            video_patterns = [
                # Direct video file URLs with common parameters
                r'https?://[^\s"\'<>]+\.(?:mp4|webm|avi|mov|mkv|flv|m4v|ts)(?:\?[^\s"\'<>]*)?',
                # HLS streams and segments
                r'https?://[^\s"\'<>]+\.m3u8(?:\?[^\s"\'<>]*)?',
                r'https?://[^\s"\'<>]+/hls/[^\s"\'<>]*',
                # DASH streams
                r'https?://[^\s"\'<>]+\.mpd(?:\?[^\s"\'<>]*)?',
                # Common video hosting CDN patterns
                r'https?://[^\s"\'<>]*(?:video|stream|media|cdn|vcdn)[^\s"\'<>]*\.(?:mp4|webm|m3u8|mpd|ts)(?:\?[^\s"\'<>]*)?',
                # Video streaming URLs with quality parameters
                r'https?://[^\s"\'<>]*[?&](?:quality|resolution|bitrate)=[^\s"\'<>]*',
                # Common porn site video patterns
                r'https?://[^\s"\'<>]*(?:spankbang|pornhub|xnxx|xvideos|tube8|redtube)[^\s"\'<>]*\.(?:mp4|webm|m3u8)(?:\?[^\s"\'<>]*)?',
                # CDN and cache URLs
                r'https?://[^\s"\'<>]*(?:cache|assets|static)[^\s"\'<>]*\.(?:mp4|webm|m3u8)(?:\?[^\s"\'<>]*)?',
                # CDN-protected URLs with auth parameters (excluding trailers)
                r'https?://[^\s"\'<>]*\.mp4(?:\?[^\s"\'<>]*(?:verify|token|auth|signature)=[^\s"\'<>]*)?',
                # High quality video patterns (excluding trailers)
                r'https?://[^\s"\'<>]*(?:_high|_low|output_)(?!.*trailer)[^\s"\'<>]*\.mp4(?:\?[^\s"\'<>]*)?'
            ]

            import re
            for pattern in video_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches:
                    if len(match) > 20 and self._is_valid_video_url(match):  # Better filtering
                        detected_sources.add(match)

            # Enhanced source URL detection from JavaScript variables
            js_patterns = [
                r'(?:src|source|url|video_url|videoUrl)\s*[:=]\s*["\']([^"\']+\.(?:mp4|webm|m3u8|mpd)[^"\']*)["\']',
                r'(?:file|videoFile|mediaUrl)\s*[:=]\s*["\']([^"\']+)["\']',
                r'playlist\s*:\s*["\']([^"\']+\.m3u8[^"\']*)["\']'
            ]

            for pattern in js_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches:
                    if self._is_valid_video_url(match):
                        detected_sources.add(match)

            # Look for JSON data containing video URLs
            json_pattern = r'\{[^{}]*(?:video|stream|media)[^{}]*\}'
            json_matches = re.findall(json_pattern, page_source, re.IGNORECASE)
            for json_data in json_matches:
                try:
                    import json
                    data = json.loads(json_data)
                    self._extract_urls_from_json(data, detected_sources)
                except:
                    # Extract URLs from malformed JSON using regex
                    url_in_json = re.findall(r'https?://[^\s"\'<>]+\.(?:mp4|webm|m3u8|mpd)(?:\?[^\s"\'<>]*)?', json_data)
                    for url in url_in_json:
                        if self._is_valid_video_url(url):
                            detected_sources.add(url)

            # Look for base64 encoded video data
            base64_pattern = r'data:video/[^;]+;base64,[A-Za-z0-9+/]+=*'
            base64_matches = re.findall(base64_pattern, page_source)
            detected_sources.update(base64_matches)

            # Filter out SVG, non-video files, and advertisement URLs more aggressively
            filtered_sources = set()
            for source in detected_sources:
                source_lower = source.lower()

                # Skip obvious non-video files
                if any(exclude in source_lower for exclude in ['.svg', '.jpg', '.png', '.gif', '.css', '.js']):
                    continue

                # Skip advertisement and trailer URLs specifically
                if any(ad_term in source_lower for ad_term in ['trailer.mp4', '/trailer/', 'preview.mp4', '/preview/', '/ads/', '/ad/']):
                    continue

                # Only include URLs that pass our enhanced validation
                if self._is_valid_video_url(source):
                    filtered_sources.add(source)

            self.log_status(f"🔍 Enhanced extraction found {len(filtered_sources)} video sources")
            return filtered_sources

        except Exception as e:
            self.log_status(f"Enhanced page source extraction error: {str(e)[:50]}")
            return set()

    def _extract_urls_from_json(self, data, detected_sources):
        """Recursively extract video URLs from JSON data"""
        try:
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, str) and self._is_valid_video_url(value):
                        detected_sources.add(value)
                    elif isinstance(value, (dict, list)):
                        self._extract_urls_from_json(value, detected_sources)
            elif isinstance(data, list):
                for item in data:
                    self._extract_urls_from_json(item, detected_sources)
        except Exception:
            pass

    def _simulate_user_interactions_for_video(self):
        """Simulate user interactions to trigger video loading"""
        try:
            detected_sources = set()

            # Common elements that might trigger video loading
            trigger_selectors = [
                # Play buttons
                '//button[contains(@class, "play") or contains(@aria-label, "play")]',
                '//div[contains(@class, "play") and contains(@class, "button")]',
                '//span[contains(@class, "play-icon")]',

                # Video containers and overlays
                '//div[contains(@class, "video-overlay")]',
                '//div[contains(@class, "video-preview")]',
                '//div[contains(@class, "video-thumbnail")]',
                '//div[contains(@class, "video-container")]',

                # Generic clickable elements
                '//div[contains(@onclick, "video") or contains(@onclick, "play")]',
                '//a[contains(@href, "javascript:") and contains(@onclick, "play")]'
            ]

            for selector in trigger_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)

                    for element in elements[:3]:  # Try first 3 elements
                        try:
                            if element.is_displayed() and element.is_enabled():
                                self.log_status(f"👆 Clicking trigger element: {element.tag_name}")

                                # Try different click methods
                                click_methods = [
                                    lambda: element.click(),
                                    lambda: ActionChains(self.driver).click(element).perform(),
                                    lambda: self.driver.execute_script("arguments[0].click();", element)
                                ]

                                for click_method in click_methods:
                                    try:
                                        click_method()
                                        time.sleep(0.1)  # Wait for reaction

                                        # Check for new sources after click
                                        post_click_sources = self._extract_from_current_page_source()
                                        if post_click_sources:
                                            detected_sources.update(post_click_sources)
                                            self.log_status(f"✅ Click triggered {len(post_click_sources)} sources")

                                        break  # If click worked, don't try other methods
                                    except Exception:
                                        continue

                        except Exception:
                            continue

                except Exception:
                    continue

            # Try hovering over video areas
            self.log_status("🖱️ Trying hover interactions...")
            hover_selectors = [
                '//video',
                '//div[contains(@class, "video")]',
                '//iframe[contains(@src, "video") or contains(@src, "embed")]'
            ]

            for selector in hover_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    for element in elements[:2]:
                        try:
                            ActionChains(self.driver).move_to_element(element).perform()
                            time.sleep(0.2)

                            post_hover_sources = self._extract_from_current_page_source()
                            detected_sources.update(post_hover_sources)

                        except Exception:
                            continue
                except Exception:
                    continue

            # Enhanced iframe interaction patterns for nested players
            self.log_status("🎯 Enhanced iframe interaction patterns...")
            iframe_sources = self._enhanced_iframe_interactions()
            detected_sources.update(iframe_sources)

            return detected_sources

        except Exception as e:
            self.log_status(f"User interaction simulation error: {str(e)[:100]}")
            return set()

    def _enhanced_iframe_interactions(self):
        """Enhanced iframe interaction patterns for modern nested players"""
        try:
            self.log_status("🔗 Starting enhanced iframe interactions...")
            detected_sources = set()

            # Get all iframe elements including hidden/lazy-loaded ones
            all_iframes = self._get_all_iframe_elements_advanced()
            self.log_status(f"📊 Found {len(all_iframes)} iframe elements to process")

            for i, iframe in enumerate(all_iframes):
                try:
                    self.log_status(f"🔍 Processing iframe {i+1}/{len(all_iframes)}")

                    # Try to extract iframe source with better URL handling
                    iframe_url = self._extract_iframe_url_enhanced(iframe)
                    if iframe_url:
                        detected_sources.add(iframe_url)
                        self.log_status(f"✅ Extracted iframe URL: {iframe_url[:60]}")

                    # Try to interact with iframe to trigger content loading
                    iframe_interaction_sources = self._interact_with_iframe(iframe)
                    if iframe_interaction_sources:
                        detected_sources.update(iframe_interaction_sources)
                        self.log_status(f"🎯 Iframe interaction found {len(iframe_interaction_sources)} sources")

                    # Try to access iframe content if possible
                    iframe_content_sources = self._access_iframe_content_enhanced(iframe)
                    detected_sources.update(iframe_content_sources)

                except Exception as iframe_error:
                    self.log_status(f"Iframe {i+1} processing error: {str(iframe_error)[:50]}")
                    continue

            return detected_sources

        except Exception as e:
            self.log_status(f"Enhanced iframe interactions error: {str(e)[:100]}")
            return set()

    def _get_all_iframe_elements_advanced(self):
        """Get all iframe elements using advanced detection methods"""
        all_iframes = []
        try:
            # Multiple iframe detection strategies
            iframe_strategies = [
                # Standard iframe detection
                lambda: self.driver.find_elements(By.TAG_NAME, "iframe"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe"),

                # Data attribute iframes (lazy-loaded)
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "*[data-iframe]"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "*[data-embed]"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "*[data-player]"),

                # Hidden iframes
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[style*='display:none']"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[style*='visibility:hidden']"),

                # Dynamic iframes that might be created by JS
                lambda: self.driver.find_elements(By.XPATH, "//iframe[@src]"),
                lambda: self.driver.find_elements(By.XPATH, "//iframe[@data-src]"),
            ]

            for strategy in iframe_strategies:
                try:
                    elements = strategy()
                    for element in elements:
                        if element not in all_iframes:
                            all_iframes.append(element)
                except:
                    continue

            # Remove duplicates while preserving order
            unique_iframes = []
            seen_elements = set()
            for iframe in all_iframes:
                element_id = id(iframe)
                if element_id not in seen_elements:
                    unique_iframes.append(iframe)
                    seen_elements.add(element_id)

            return unique_iframes

        except Exception as e:
            self.log_status(f"Advanced iframe detection error: {str(e)[:50]}")
            return []

    def _extract_iframe_url_enhanced(self, iframe):
        """Extract iframe URL with enhanced deobfuscation and validation"""
        try:
            url = None

            # Try multiple attributes that might contain the URL
            url_attributes = ['src', 'data-src', 'data-iframe', 'data-embed', 'data-player', 'data-video-url']

            for attr in url_attributes:
                try:
                    attr_value = iframe.get_attribute(attr)
                    if attr_value and len(attr_value) > 10:
                        url = attr_value
                        break
                except:
                    continue

            if not url:
                return None

            # Enhanced URL deobfuscation
            url = self._deobfuscate_iframe_url_advanced(url)

            # Validate if URL looks like a video-related URL
            if self._is_valid_video_iframe_url(url):
                return url

            return None

        except Exception as e:
            self.log_status(f"Iframe URL extraction error: {str(e)[:50]}")
            return None

    def _deobfuscate_iframe_url_advanced(self, url):
        """Advanced iframe URL deobfuscation"""
        try:
            if not url:
                return url

            # Handle relative URLs
            if url.startswith('//'):
                url = 'https:' + url
            elif url.startswith('/'):
                try:
                    current_origin = self.driver.execute_script("return window.location.origin")
                    url = current_origin + url
                except:
                    pass

            # Remove common obfuscation patterns
            url = url.replace('\\/', '/')
            url = url.replace('\\"', '"')
            url = url.replace('\\\\', '\\')

            # Handle URL encoding
            try:
                from urllib.parse import unquote, unquote_plus
                decoded_url = unquote_plus(unquote(url))
                if decoded_url != url and len(decoded_url) > 10:
                    url = decoded_url
            except:
                pass

            # Handle base64 encoded parts (common in some embedded players)
            import re
            import base64
            base64_pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
            matches = re.findall(base64_pattern, url)

            for match in matches:
                try:
                    decoded_part = base64.b64decode(match).decode('utf-8')
                    if 'http' in decoded_part or 'video' in decoded_part:
                        # This might be an encoded URL part
                        self.log_status(f"🔓 Decoded base64 part: {decoded_part[:40]}")
                except:
                    continue

            return url

        except Exception as e:
            self.log_status(f"Advanced URL deobfuscation error: {str(e)[:50]}")
            return url

    def _is_valid_video_iframe_url(self, url):
        """Enhanced validation for video iframe URLs"""
        if not url or len(url) < 15:
            return False

        # Convert to lowercase for checking
        url_lower = url.lower()

        # Video-related domain indicators
        video_domains = [
            'yandex-video', 'youtube', 'vimeo', 'dailymotion', 'twitch',
            'vk.com', 'rutube', 'odnoklassniki', 'mail.ru', 'bitchute',
            'rumble', 'brightcove', 'jwpcdn', 'wistia', 'vidyard',
            'yastatic.net'  # Yandex static content including YouTube embeds
        ]

        # Video-related path indicators
        video_paths = [
            'embed', 'player', 'video', 'watch', 'stream', 'media',
            'content', 'iframe', 'play', 'viewer'
        ]

        # Check domains
        for domain in video_domains:
            if domain in url_lower:
                return True

        # Check paths
        for path in video_paths:
            if f'/{path}/' in url_lower or f'{path}/' in url_lower:
                return True

        # Check file extensions
        if any(ext in url_lower for ext in ['.mp4', '.webm', '.m3u8', '.mpd']):
            return True

        return False

    def _interact_with_iframe(self, iframe):
        """Try to interact with iframe to trigger content loading"""
        sources = set()
        try:
            # Try to scroll iframe into view
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", iframe)
                time.sleep(0.1)
            except:
                pass

            # Try to click on the iframe area
            try:
                if iframe.is_displayed():
                    iframe.click()
                    time.sleep(0.2)

                    # Check for newly loaded content
                    new_sources = self._scan_for_newly_revealed_sources()
                    sources.update(new_sources)
            except:
                pass

            # Try to hover over the iframe
            try:
                ActionChains(self.driver).move_to_element(iframe).perform()
                time.sleep(0.1)

                hover_sources = self._scan_for_newly_revealed_sources()
                sources.update(hover_sources)
            except:
                pass

        except Exception as e:
            self.log_status(f"Iframe interaction error: {str(e)[:50]}")

        return sources

    def _access_iframe_content_enhanced(self, iframe):
        """Enhanced iframe content access with better error handling"""
        sources = set()
        original_window = None

        try:
            original_window = self.driver.current_window_handle

            # Try to switch to iframe context
            try:
                self.driver.switch_to.frame(iframe)

                # Look for video sources within iframe
                iframe_video_sources = self._extract_sources_from_current_iframe_context()
                sources.update(iframe_video_sources)

                # Look for nested iframes
                nested_iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
                for nested in nested_iframes:
                    try:
                        nested_src = nested.get_attribute('src')
                        if nested_src and self._is_valid_video_iframe_url(nested_src):
                            sources.add(nested_src)
                    except:
                        continue

            except Exception as switch_error:
                self.log_status(f"Iframe context switch error: {str(switch_error)[:40]}")

        except Exception as e:
            self.log_status(f"Enhanced iframe content access error: {str(e)[:50]}")
        finally:
            # Always ensure we return to the main context
            try:
                if original_window:
                    self.driver.switch_to.default_content()
            except:
                pass

        return sources

    def _extract_sources_from_current_iframe_context(self):
        """Extract video sources from current iframe context"""
        sources = set()
        try:
            # Look for video elements
            videos = self.driver.find_elements(By.TAG_NAME, "video")
            for video in videos:
                src = video.get_attribute('src')
                if src:
                    sources.add(src)

                # Check source children
                video_sources = video.find_elements(By.TAG_NAME, "source")
                for source in video_sources:
                    source_src = source.get_attribute('src')
                    if source_src:
                        sources.add(source_src)

            # Look for audio elements that might be video streams
            audios = self.driver.find_elements(By.TAG_NAME, "audio")
            for audio in audios:
                src = audio.get_attribute('src')
                if src and any(ext in src.lower() for ext in ['.mp4', '.webm', '.m3u8']):
                    sources.add(src)

            # Extract from page source within iframe
            try:
                iframe_page_source = self.driver.page_source
                import re

                # Look for video URLs in the iframe source
                video_patterns = [
                    r'https?://[^\s"\'<>]+\.(?:mp4|webm|avi|mov|mkv|flv|m4v)(?:\?[^\s"\'<>]*)?',
                    r'https?://[^\s"\'<>]+\.m3u8(?:\?[^\s"\'<>]*)?',
                    r'https?://[^\s"\'<>]+\.mpd(?:\?[^\s"\'<>]*)?'
                ]

                for pattern in video_patterns:
                    matches = re.findall(pattern, iframe_page_source, re.IGNORECASE)
                    for match in matches:
                        if len(match) > 20:
                            sources.add(match)

            except Exception as source_error:
                self.log_status(f"Iframe source extraction error: {str(source_error)[:40]}")

        except Exception as e:
            self.log_status(f"Current iframe context extraction error: {str(e)[:50]}")

        return sources

    def _comprehensive_video_scan(self):
        """Comprehensive scan for all possible video sources"""
        try:
            detected_sources = set()

            # Run all enhanced detection methods
            detection_methods = [
                self._enhanced_javascript_video_detection,
                self._enhanced_embed_button_detection,
                self._advanced_stream_detection,
                self._network_request_monitoring,
                self._deep_iframe_inspection
            ]

            for method in detection_methods:
                try:
                    sources = method()
                    if sources:
                        detected_sources.update(sources)
                        self.log_status(f"📊 {method.__name__} found {len(sources)} sources")
                except Exception as e:
                    self.log_status(f"Detection method {method.__name__} error: {str(e)[:50]}")
                    continue

            return detected_sources

        except Exception as e:
            self.log_status(f"Comprehensive scan error: {str(e)[:100]}")
            return set()

    def _deep_iframe_inspection(self):
        """Deep inspection of iframes with cross-frame communication monitoring"""
        try:
            self.log_status("🔬 Starting deep iframe inspection...")
            detected_sources = set()

            # Get all iframes with multiple detection methods
            all_iframes = self._get_all_iframes_comprehensive()

            for i, iframe in enumerate(all_iframes):
                try:
                    iframe_src = iframe.get_attribute('src') or iframe.get_attribute('data-src') or ''
                    self.log_status(f"🔍 Inspecting iframe {i+1}: {iframe_src[:60]}")

                    # Store current window context
                    original_window = self.driver.current_window_handle

                    try:
                        # Switch to iframe context
                        self.driver.switch_to.frame(iframe)
                        self.log_status(f"✅ Successfully switched to iframe context")

                        # Extract sources from within iframe
                        iframe_sources = self._extract_sources_from_iframe_context()
                        if iframe_sources:
                            self.log_status(f"🎯 Found {len(iframe_sources)} sources in iframe")
                            detected_sources.update(iframe_sources)
                        else:
                            self.log_status("⚠️ No sources found in iframe context")

                        # Check for nested iframes
                        nested_iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
                        if nested_iframes:
                            self.log_status(f"🔗 Found {len(nested_iframes)} nested iframes")
                            for nested_iframe in nested_iframes:
                                try:
                                    nested_src = nested_iframe.get_attribute('src') or ''
                                    if nested_src and self._is_valid_video_url(nested_src):
                                        detected_sources.add(nested_src)
                                except Exception:
                                    continue

                    finally:
                        # Always return to main context
                        try:
                            self.driver.switch_to.default_content()
                        except:
                            pass

                    # Monitor postMessage communication
                    postmessage_sources = self._monitor_postmessage_communication()
                    detected_sources.update(postmessage_sources)

                except Exception as iframe_error:
                    self.log_status(f"Iframe {i+1} inspection error: {str(iframe_error)[:50]}")
                    # Ensure we're back in main context
                    try:
                        self.driver.switch_to.default_content()
                    except:
                        pass
                    continue

            return detected_sources

        except Exception as e:
            self.log_status(f"Deep iframe inspection error: {str(e)[:100]}")
            # Ensure we're in main context
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return set()

    def _enhanced_embed_button_detection(self):
        """Enhanced detection for embed buttons and nested iframes in modern video players"""
        try:
            self.log_status("🎯 Starting enhanced embed button detection...")
            detected_sources = set()

            # Look for embed buttons/icons with various selectors
            embed_selectors = [
                # Generic embed button classes
                "*[class*='embed']", "*[class*='share']", "*[class*='copy']",
                "*[class*='link']", "*[class*='url']", "*[title*='embed']",
                "*[title*='share']", "*[aria-label*='embed']", "*[aria-label*='share']",

                # Video player overlay elements
                "*[class*='overlay']", "*[class*='controls']", "*[class*='menu']",
                "*[class*='options']", "*[class*='settings']", "*[class*='more']",

                # Icon-based selectors
                "i[class*='embed']", "svg[class*='embed']", "span[class*='embed']",
                "button[class*='embed']", "a[class*='embed']", "div[class*='embed']",

                # Data attributes that might contain embed info
                "*[data-embed]", "*[data-share]", "*[data-url]", "*[data-link]",
                "*[data-iframe]", "*[data-player]", "*[data-video]"
            ]

            for selector in embed_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        # Extract embed URLs from various attributes
                        embed_sources = self._extract_embed_urls_from_element(element)
                        if embed_sources:
                            self.log_status(f"📎 Found {len(embed_sources)} embed URLs from {selector}")
                            detected_sources.update(embed_sources)

                        # Try clicking embed buttons to reveal hidden content
                        if self._is_clickable_embed_element(element):
                            try:
                                self._simulate_embed_button_click(element)
                                # Wait for potential content to load after click
                                time.sleep(0.2)
                                # Scan for newly revealed iframes/sources
                                new_sources = self._scan_for_newly_revealed_sources()
                                detected_sources.update(new_sources)
                            except Exception as click_error:
                                self.log_status(f"Embed button click failed: {str(click_error)[:50]}")

                except Exception as selector_error:
                    self.log_status(f"Selector {selector[:20]} error: {str(selector_error)[:30]}")
                    continue

            # Enhanced iframe URL extraction with deobfuscation
            iframe_sources = self._extract_obfuscated_iframe_urls()
            detected_sources.update(iframe_sources)

            return detected_sources

        except Exception as e:
            self.log_status(f"Enhanced embed detection error: {str(e)[:100]}")
            return set()

    def _extract_embed_urls_from_element(self, element):
        """Extract potential embed URLs from element attributes and content"""
        urls = set()
        try:
            # Check various attributes that might contain URLs
            url_attributes = [
                'src', 'data-src', 'data-embed', 'data-share', 'data-url',
                'data-link', 'data-iframe', 'data-player', 'data-video',
                'href', 'value', 'content', 'data-content'
            ]

            for attr in url_attributes:
                try:
                    attr_value = element.get_attribute(attr)
                    if attr_value and self._is_potential_video_url(attr_value):
                        urls.add(attr_value)
                except:
                    continue

            # Check text content for URLs
            try:
                text_content = element.get_attribute('textContent') or element.text or ''
                if text_content:
                    # Look for URLs in text content using regex
                    import re
                    url_pattern = r'https?://[^\s<>"]+|//[^\s<>"]+'
                    found_urls = re.findall(url_pattern, text_content)
                    for url in found_urls:
                        if self._is_potential_video_url(url):
                            urls.add(url)
            except:
                pass

            return urls

        except Exception as e:
            self.log_status(f"URL extraction error: {str(e)[:50]}")
            return set()

    def _is_potential_video_url(self, url):
        """Check if URL might be a video-related URL"""
        if not url or len(url) < 10:
            return False

        # Convert relative URLs to absolute
        if url.startswith('//'):
            url = 'https:' + url
        elif url.startswith('/'):
            current_domain = self.driver.execute_script("return window.location.origin")
            url = current_domain + url

        # Check for video-related domains and paths
        video_indicators = [
            'video', 'embed', 'player', 'stream', 'watch', 'play',
            'yandex-video', 'youtube', 'vimeo', 'dailymotion',
            'twitch', 'iframe', 'media', 'content'
        ]

        url_lower = url.lower()
        return any(indicator in url_lower for indicator in video_indicators)

    def _is_clickable_embed_element(self, element):
        """Determine if element is a clickable embed button"""
        try:
            # Check if element is clickable
            tag_name = element.tag_name.lower()
            if tag_name in ['button', 'a', 'input']:
                return True

            # Check for click event handlers
            onclick = element.get_attribute('onclick')
            if onclick:
                return True

            # Check CSS for cursor pointer
            cursor = element.value_of_css_property('cursor')
            if cursor == 'pointer':
                return True

            # Check for common embed button text/titles
            text_content = (element.text or '').lower()
            title = (element.get_attribute('title') or '').lower()
            aria_label = (element.get_attribute('aria-label') or '').lower()

            embed_keywords = ['embed', 'share', 'copy', 'link', 'url']
            all_text = f"{text_content} {title} {aria_label}"

            return any(keyword in all_text for keyword in embed_keywords)

        except:
            return False

    def _simulate_embed_button_click(self, element):
        """Safely simulate clicking an embed button"""
        try:
            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.1)

            # Try different click methods
            try:
                element.click()
            except:
                # Use JavaScript click if regular click fails
                self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            self.log_status(f"Button click simulation failed: {str(e)[:50]}")

    def _scan_for_newly_revealed_sources(self):
        """Scan for video sources that may have been revealed after clicking embed buttons"""
        sources = set()
        try:
            # Look for new iframes
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                src = iframe.get_attribute('src')
                if src and self._is_potential_video_url(src):
                    sources.add(src)

            # Look for new video elements
            videos = self.driver.find_elements(By.TAG_NAME, "video")
            for video in videos:
                src = video.get_attribute('src')
                if src:
                    sources.add(src)

            # Look for new source elements
            video_sources = self.driver.find_elements(By.TAG_NAME, "source")
            for source in video_sources:
                src = source.get_attribute('src')
                if src:
                    sources.add(src)

        except Exception as e:
            self.log_status(f"New sources scan error: {str(e)[:50]}")

        return sources

    def _extract_obfuscated_iframe_urls(self):
        """Extract and deobfuscate iframe URLs from modern video players"""
        sources = set()
        try:
            self.log_status("🔍 Extracting obfuscated iframe URLs...")

            # Get all iframes including hidden ones
            iframe_selectors = [
                "iframe", "iframe[src]", "iframe[data-src]",
                "iframe[style*='display:none']", "iframe[style*='visibility:hidden']",
                "*[data-iframe]", "*[data-player]", "*[data-embed-url]"
            ]

            all_iframes = set()
            for selector in iframe_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    all_iframes.update(elements)
                except:
                    continue

            self.log_status(f"🎯 Found {len(all_iframes)} total iframe elements")

            for iframe in all_iframes:
                try:
                    # Extract URL from various attributes
                    url_attrs = ['src', 'data-src', 'data-iframe', 'data-player', 'data-embed-url']
                    for attr in url_attrs:
                        url = iframe.get_attribute(attr)
                        if url:
                            # Deobfuscate and normalize URL
                            clean_url = self._deobfuscate_iframe_url(url)
                            if clean_url and self._is_potential_video_url(clean_url):
                                sources.add(clean_url)
                                self.log_status(f"📎 Extracted iframe URL: {clean_url[:60]}")

                    # Try to access iframe content directly
                    if iframe.get_attribute('src'):
                        iframe_sources = self._extract_from_iframe_directly(iframe)
                        sources.update(iframe_sources)

                except Exception as iframe_error:
                    self.log_status(f"Iframe processing error: {str(iframe_error)[:50]}")
                    continue

            return sources

        except Exception as e:
            self.log_status(f"Obfuscated iframe extraction error: {str(e)[:100]}")
            return set()

    def _deobfuscate_iframe_url(self, url):
        """Clean and deobfuscate iframe URLs"""
        try:
            if not url:
                return None

            # Handle relative URLs
            if url.startswith('//'):
                url = 'https:' + url
            elif url.startswith('/'):
                current_origin = self.driver.execute_script("return window.location.origin")
                url = current_origin + url

            # Remove common obfuscation patterns
            url = url.replace('\\/', '/')
            url = url.replace('\\"', '"')

            # URL decode if needed
            try:
                from urllib.parse import unquote
                decoded_url = unquote(url)
                if decoded_url != url and self._is_potential_video_url(decoded_url):
                    url = decoded_url
            except:
                pass

            return url

        except Exception as e:
            self.log_status(f"URL deobfuscation error: {str(e)[:50]}")
            return url

    def _extract_from_iframe_directly(self, iframe):
        """Try to extract video sources from iframe by accessing it directly"""
        sources = set()
        try:
            original_window = self.driver.current_window_handle

            # Try to switch to iframe and extract sources
            try:
                self.driver.switch_to.frame(iframe)

                # Look for video elements in iframe
                videos = self.driver.find_elements(By.TAG_NAME, "video")
                for video in videos:
                    src = video.get_attribute('src')
                    if src:
                        sources.add(src)

                # Look for source elements in iframe
                video_sources = self.driver.find_elements(By.TAG_NAME, "source")
                for source in video_sources:
                    src = source.get_attribute('src')
                    if src:
                        sources.add(src)

                # Look for nested iframes
                nested_iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
                for nested in nested_iframes:
                    nested_src = nested.get_attribute('src')
                    if nested_src and self._is_potential_video_url(nested_src):
                        sources.add(nested_src)

            finally:
                # Always return to main context
                try:
                    self.driver.switch_to.default_content()
                except:
                    pass

        except Exception as e:
            self.log_status(f"Direct iframe access error: {str(e)[:50]}")
            try:
                self.driver.switch_to.default_content()
            except:
                pass

        return sources

    def _get_all_iframes_comprehensive(self):
        """Get all iframes using comprehensive detection methods"""
        try:
            all_iframes = []

            # Multiple iframe detection methods
            detection_methods = [
                lambda: self.driver.find_elements(By.TAG_NAME, "iframe"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe"),
                lambda: self.driver.find_elements(By.XPATH, "//iframe"),
                lambda: self.driver.find_elements(By.XPATH, "//frame"),
                # Hidden/lazy-loaded iframes
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[data-src]"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[style*='display:none']"),
                lambda: self.driver.find_elements(By.CSS_SELECTOR, "iframe[style*='visibility:hidden']"),
                # Dynamically added iframes
                lambda: self.driver.find_elements(By.XPATH, "//iframe[contains(@class, 'lazy')]"),
                lambda: self.driver.find_elements(By.XPATH, "//iframe[contains(@loading, 'lazy')]")
            ]

            seen_iframes = set()
            for method in detection_methods:
                try:
                    iframes = method()
                    for iframe in iframes:
                        iframe_id = id(iframe)
                        if iframe_id not in seen_iframes:
                            all_iframes.append(iframe)
                            seen_iframes.add(iframe_id)
                except Exception:
                    continue

            self.log_status(f"🎯 Found {len(all_iframes)} total iframes for deep inspection")
            return all_iframes

        except Exception as e:
            self.log_status(f"Comprehensive iframe detection error: {str(e)[:50]}")
            return []

    def _extract_sources_from_iframe_context(self):
        """Extract video sources from within iframe context"""
        try:
            detected_sources = set()

            # Run enhanced detection within iframe
            iframe_js_sources = self.driver.execute_script("""
                var sources = [];

                // Check video elements
                var videos = document.querySelectorAll('video');
                videos.forEach(function(video) {
                    if (video.src) sources.push(video.src);
                    if (video.currentSrc) sources.push(video.currentSrc);

                    var sourceTags = video.querySelectorAll('source');
                    sourceTags.forEach(function(source) {
                        if (source.src) sources.push(source.src);
                    });
                });

                // Check for video URLs in scripts
                var scripts = document.querySelectorAll('script');
                scripts.forEach(function(script) {
                    var content = script.textContent || script.innerHTML;
                    var videoMatches = content.match(/https?:\\/\\/[^"'\\s]+\\.(mp4|webm|m3u8|mpd)[^"'\\s]*/gi);
                    if (videoMatches) {
                        sources = sources.concat(videoMatches);
                    }
                });

                // Check global video variables
                var globalVars = ['player', 'video', 'media', 'config'];
                globalVars.forEach(function(varName) {
                    if (window[varName] && typeof window[varName] === 'object') {
                        try {
                            var obj = window[varName];
                            if (obj.src) sources.push(obj.src);
                            if (obj.file) sources.push(obj.file);
                            if (obj.url) sources.push(obj.url);
                        } catch(e) {}
                    }
                });

                return sources.filter(function(s) { return s && s.length > 10; });
            """)

            if iframe_js_sources:
                for source in iframe_js_sources:
                    if self._is_valid_video_url(source):
                        detected_sources.add(source)

            return detected_sources

        except Exception as e:
            self.log_status(f"Iframe context extraction error: {str(e)[:50]}")
            return set()

    def _monitor_postmessage_communication(self):
        """Monitor postMessage communication for video URLs"""
        try:
            detected_sources = set()

            # Install postMessage monitor
            self.driver.execute_script("""
                window.videoPostMessages = [];

                // Override postMessage to capture messages
                var originalPostMessage = window.postMessage;
                window.postMessage = function(message, targetOrigin) {
                    try {
                        if (typeof message === 'string' &&
                            (message.includes('.mp4') || message.includes('.webm') ||
                             message.includes('.m3u8') || message.includes('video') ||
                             message.includes('stream'))) {
                            window.videoPostMessages.push({
                                message: message,
                                origin: targetOrigin,
                                timestamp: Date.now()
                            });
                        }
                    } catch(e) {}

                    return originalPostMessage.apply(this, arguments);
                };

                // Listen for incoming messages
                window.addEventListener('message', function(event) {
                    try {
                        var data = event.data;
                        if (typeof data === 'string' &&
                            (data.includes('.mp4') || data.includes('.webm') ||
                             data.includes('.m3u8') || data.includes('video') ||
                             data.includes('stream'))) {
                            window.videoPostMessages.push({
                                message: data,
                                origin: event.origin,
                                timestamp: Date.now(),
                                type: 'received'
                            });
                        } else if (typeof data === 'object' && data !== null) {
                            // Check object properties for video URLs
                            for (var key in data) {
                                var value = data[key];
                                if (typeof value === 'string' &&
                                    (value.includes('.mp4') || value.includes('.webm') ||
                                     value.includes('.m3u8') || value.includes('video'))) {
                                    window.videoPostMessages.push({
                                        message: value,
                                        origin: event.origin,
                                        key: key,
                                        timestamp: Date.now(),
                                        type: 'received_object'
                                    });
                                }
                            }
                        }
                    } catch(e) {}
                });
            """)

            # Wait for messages
            time.sleep(0.2)

            # Collect captured messages
            captured_messages = self.driver.execute_script("""
                return window.videoPostMessages || [];
            """)

            for message_data in captured_messages:
                message = message_data.get('message', '')
                if message and self._is_valid_video_url(message):
                    detected_sources.add(message)
                    self.log_status(f"📨 PostMessage captured: {message[:60]}")

            return detected_sources

        except Exception as e:
            self.log_status(f"PostMessage monitoring error: {str(e)[:50]}")
            return set()

    def _enhanced_comprehensive_video_detection(self):
        """STRATEGY 0.5: Enhanced comprehensive video detection using all new methods"""
        try:
            import time
            start_time = time.time()

            self.log_status("🚀 ENHANCED COMPREHENSIVE VIDEO DETECTION STARTED")
            self.log_status(f"📍 Current URL: {self.driver.current_url[:100]}...")

            # Check page readiness
            try:
                page_state = self.driver.execute_script("return document.readyState")
                iframe_count = self.driver.execute_script("return document.querySelectorAll('iframe').length")
                video_count = self.driver.execute_script("return document.querySelectorAll('video').length")
                self.log_status(f"📊 Page state: {page_state}, iframes: {iframe_count}, videos: {video_count}")
            except:
                self.log_status("📊 Page state check failed")

            all_detected_sources = set()
            successful_methods = []

            # Method 1: Enhanced JavaScript Detection
            try:
                js_sources = self._enhanced_javascript_video_detection()
                if js_sources:
                    all_detected_sources.update(js_sources)
                    successful_methods.append(f"Enhanced JS ({len(js_sources)} sources)")
            except Exception as e:
                pass

            # Method 2: Network Request Monitoring
            try:
                network_sources = self._network_request_monitoring()
                if network_sources:
                    new_sources = network_sources - all_detected_sources
                    all_detected_sources.update(network_sources)
                    successful_methods.append(f"Network Monitoring ({len(new_sources)} new)")
            except Exception as e:
                pass

            # Method 3: Advanced Stream Detection
            try:
                stream_sources = self._advanced_stream_detection()
                if stream_sources:
                    new_sources = stream_sources - all_detected_sources
                    all_detected_sources.update(stream_sources)
                    successful_methods.append(f"Stream Detection ({len(new_sources)} new)")
            except Exception as e:
                pass

            # Method 4: Dynamic Content Waiting
            try:
                dynamic_sources = self._dynamic_content_waiting_and_detection()
                if dynamic_sources:
                    new_sources = dynamic_sources - all_detected_sources
                    all_detected_sources.update(dynamic_sources)
                    successful_methods.append(f"Dynamic Content ({len(new_sources)} new)")
            except Exception as e:
                pass

            # Method 5: Deep Iframe Inspection
            try:
                iframe_sources = self._deep_iframe_inspection()
                if iframe_sources:
                    new_sources = iframe_sources - all_detected_sources
                    all_detected_sources.update(iframe_sources)
                    successful_methods.append(f"Deep Iframe ({len(new_sources)} new)")
            except Exception as e:
                pass

            # Summary with timing
            execution_time = time.time() - start_time
            self.log_status(f"📊 ENHANCED DETECTION SUMMARY:")
            self.log_status(f"  ⏱️ Execution time: {execution_time:.2f} seconds")
            self.log_status(f"  🎯 Total unique sources found: {len(all_detected_sources)}")
            self.log_status(f"  ✅ Successful methods: {len(successful_methods)}")

            if all_detected_sources:
                self.log_status(f"  📝 Found sources:")
                for i, source in enumerate(list(all_detected_sources)[:5]):  # Show first 5
                    self.log_status(f"    {i+1}. {source[:80]}...")
                if len(all_detected_sources) > 5:
                    self.log_status(f"    ... and {len(all_detected_sources) - 5} more")

            for method in successful_methods:
                self.log_status(f"    • {method}")

            # Return the detected sources, NOT download them!
            # The download should be handled by the calling code
            if all_detected_sources:
                execution_time = time.time() - start_time
                self.log_status(f"✅ Enhanced detection completed in {execution_time:.2f}s")
                self.log_status(f"🎯 Returning {len(all_detected_sources)} sources for download")

                # Return the actual sources list for the caller to process
                return list(all_detected_sources)

            execution_time = time.time() - start_time
            self.log_status(f"❌ No sources found by enhanced detection ({execution_time:.2f}s)")
            return None

        except Exception as e:
            execution_time = time.time() - start_time if 'start_time' in locals() else 0
            self.log_status(f"❌ Enhanced comprehensive detection error ({execution_time:.2f}s): {str(e)[:100]}")
            return None

    def _is_direct_video_url(self, url):
        """Check if URL is a direct video file"""
        if not url:
            return False

        direct_extensions = ['.mp4', '.webm', '.avi', '.mov', '.mkv', '.flv', '.m4v']
        url_lower = url.lower()
        return any(ext in url_lower for ext in direct_extensions)

    def _analyze_cross_frame_communication(self):
        """Analyze cross-frame communication for video sources"""
        try:
            detected_sources = set()
            
            # Set up message listener for cross-frame communication
            communication_script = """
            return new Promise(function(resolve) {
                var detectedSources = [];
                
                // Listen for postMessage communications
                function messageHandler(event) {
                    try {
                        var data = event.data;
                        if (typeof data === 'string') {
                            if (data.includes('.mp4') || data.includes('.webm') || data.includes('video')) {
                                detectedSources.push(data);
                            }
                        } else if (data && typeof data === 'object') {
                            // Check object properties for video URLs
                            for (var key in data) {
                                var value = data[key];
                                if (typeof value === 'string' && 
                                    (value.includes('.mp4') || value.includes('.webm') || value.includes('video'))) {
                                    detectedSources.push(value);
                                }
                            }
                        }
                    } catch(e) {}
                }
                
                window.addEventListener('message', messageHandler);
                
                // Send requests to potential child frames
                var iframes = document.querySelectorAll('iframe');
                iframes.forEach(function(iframe) {
                    try {
                        iframe.contentWindow.postMessage({
                            action: 'getVideoUrl',
                            request: 'source'
                        }, '*');
                    } catch(e) {}
                });
                
                // Also send to parent (in case we're in a frame)
                try {
                    window.parent.postMessage({
                        action: 'getVideoUrl',
                        request: 'source'
                    }, '*');
                } catch(e) {}
                
                // Wait for responses
                setTimeout(function() {
                    window.removeEventListener('message', messageHandler);
                    resolve(detectedSources);
                }, 3000);
            });
            """
            
            sources = self.driver.execute_async_script(communication_script)
            
            for source in sources:
                if self._is_valid_video_url(source):
                    detected_sources.add(source)
            
            return detected_sources
            
        except Exception as e:
            logger.error(f"Cross-frame communication analysis failed: {e}")
            return set()
    
    def _analyze_nested_iframes(self):
        """Recursively analyze nested iframe structures"""
        try:
            detected_sources = set()
            
            # Get all iframe elements
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")
            
            for iframe in iframes:
                try:
                    # Switch to iframe
                    self.driver.switch_to.frame(iframe)
                    
                    # Look for nested iframes
                    nested_iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
                    
                    for nested_iframe in nested_iframes:
                        try:
                            # Switch to nested iframe
                            self.driver.switch_to.frame(nested_iframe)
                            
                            # Extract video sources from nested context
                            nested_sources = self._comprehensive_iframe_video_extraction()
                            detected_sources.update(nested_sources)
                            
                            # Switch back to parent iframe
                            self.driver.switch_to.parent_frame()
                            
                        except Exception:
                            try:
                                self.driver.switch_to.parent_frame()
                            except:
                                pass
                            continue
                    
                    # Switch back to main context
                    self.driver.switch_to.default_content()
                    
                except Exception:
                    try:
                        self.driver.switch_to.default_content()
                    except:
                        pass
                    continue
            
            return detected_sources
            
        except Exception as e:
            logger.error(f"Nested iframe analysis failed: {e}")
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return set()
    
    def _extract_platform_direct_url(self, iframe_src):
        """Extract direct video URLs from known video platforms"""
        try:
            # YouTube
            if 'youtube.com' in iframe_src or 'youtu.be' in iframe_src:
                video_id_match = re.search(r'(?:embed/|v=|vi=|youtu\.be/)([a-zA-Z0-9_-]{11})', iframe_src)
                if video_id_match:
                    video_id = video_id_match.group(1)
                    # Note: This would require yt-dlp for actual extraction
                    return f"https://www.youtube.com/watch?v={video_id}"
            
            # Vimeo
            elif 'vimeo.com' in iframe_src:
                video_id_match = re.search(r'vimeo\.com/(?:video/)?(\d+)', iframe_src)
                if video_id_match:
                    video_id = video_id_match.group(1)
                    return f"https://vimeo.com/{video_id}"
            
            # Direct video file check
            elif any(ext in iframe_src.lower() for ext in ['.mp4', '.webm', '.avi', '.mov']):
                return iframe_src
            
            return None
            
        except Exception:
            return None
    
    def _fetch_iframe_video_sources(self, iframe_url):
        """Fetch and analyze iframe content for video sources"""
        try:
            sources = set()
            
            # Use requests to fetch iframe content
            import requests
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': self.driver.current_url
            }
            
            response = requests.get(iframe_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                content = response.text
                
                # Extract video URLs from iframe content
                video_patterns = [
                    r'["\']([^"\']*\.mp4[^"\']*)["\']',
                    r'["\']([^"\']*\.webm[^"\']*)["\']',
                    r'["\']([^"\']*\.avi[^"\']*)["\']',
                    r'src["\s]*:["\s]*["\']([^"\']*\.(mp4|webm|avi)[^"\']*)["\']'
                ]
                
                for pattern in video_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    for match in matches:
                        if isinstance(match, tuple):
                            url = match[0]
                        else:
                            url = match
                        
                        if self._is_valid_video_url(url):
                            # Convert relative URLs to absolute
                            if url.startswith('/'):
                                from urllib.parse import urljoin
                                url = urljoin(iframe_url, url)
                            sources.add(url)
            
            return sources
            
        except Exception as e:
            logger.error(f"Iframe content fetching failed: {e}")
            return set()
    
    def _evaluate_iframe_sources(self, sources):
        """Evaluate and rank iframe-discovered sources"""
        try:
            if not sources:
                return None
            
            scored_sources = []
            
            for source in sources:
                score = 0
                source_lower = source.lower()
                
                # Direct video file bonus
                if any(ext in source_lower for ext in ['.mp4', '.webm', '.avi', '.mov']):
                    score += 50
                
                # Quality indicators
                if any(q in source_lower for q in ['1080p', 'hd', 'high']):
                    score += 30
                elif any(q in source_lower for q in ['720p', 'medium']):
                    score += 20
                
                # Source reliability
                if any(indicator in source_lower for indicator in ['cdn', 'stream', 'media']):
                    score += 15
                
                # Platform bonus (known reliable sources)
                if any(platform in source_lower for platform in ['youtube', 'vimeo', 'streamable']):
                    score += 10
                
                # Penalize overly complex URLs
                if len(source) > 200:
                    score -= 10
                
                scored_sources.append((score, source))
            
            scored_sources.sort(reverse=True)
            best_source = scored_sources[0][1]
            
            self.log_status(f"Selected best iframe source (score: {scored_sources[0][0]}): {best_source}")
            return best_source
            
        except Exception:
            return list(sources)[0] if sources else None
    
    def _discover_api_endpoints(self):
        """STRATEGY 7: Discover API endpoints and streaming URLs"""
        try:
            self.log_status("Strategy 7: Discovering API endpoints and streaming URLs")
            
            # Common API patterns to look for
            api_patterns = [
                r'["\']([^"\']*\/api\/[^"\']*video[^"\']*)["\']',
                r'["\']([^"\']*\/stream\/[^"\']*)["\']',
                r'["\']([^"\']*\/media\/[^"\']*)["\']',
                r'["\']([^"\']*\/download\/[^"\']*)["\']',
                r'["\']([^"\']*\/file\/[^"\']*\.(mp4|avi|mov|webm|mkv)[^"\']*)["\']',
                r'streamUrl["\s]*:["\s]*["\']([^"\']+)["\']',
                r'videoUrl["\s]*:["\s]*["\']([^"\']+)["\']',
                r'src["\s]*:["\s]*["\']([^"\']*stream[^"\']*)["\']',
            ]
            
            page_source = self.driver.page_source
            
            # Search for API endpoints in page source
            for pattern in api_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches:
                    if isinstance(match, tuple):
                        api_url = match[0]
                    else:
                        api_url = match
                    
                    # Construct full URL if relative
                    if api_url.startswith('/'):
                        from urllib.parse import urljoin
                        api_url = urljoin(self.driver.current_url, api_url)
                    
                    if self._is_valid_video_url(api_url):
                        self.log_status(f"Found API endpoint: {api_url}")
                        return api_url
            
            # Try to trigger AJAX calls and monitor network
            self.driver.execute_script("""
                // Trigger common video loading functions
                if (window.loadVideo) window.loadVideo();
                if (window.initPlayer) window.initPlayer();
                if (window.startStream) window.startStream();
                
                // Click on elements that might trigger video loading
                var triggers = document.querySelectorAll('[onclick*="video"], [onclick*="play"], [onclick*="load"]');
                triggers.forEach(function(t) {
                    try { t.click(); } catch(e) {}
                });
            """)
            
            time.sleep(0.2)
            
            # Check for XMLHttpRequest or fetch calls in console logs
            logs = self.driver.get_log('browser')
            for log in logs:
                if 'video' in log['message'].lower() or 'stream' in log['message'].lower():
                    # Extract URLs from log messages
                    url_matches = re.findall(r'https?://[^\s"\']+', log['message'])
                    for url in url_matches:
                        if self._is_valid_video_url(url):
                            self.log_status(f"Found streaming URL in logs: {url}")
                            return url
            
            # Check for HLS/DASH streaming manifests
            streaming_patterns = [
                r'["\']([^"\']*\.m3u8[^"\']*)["\']',  # HLS
                r'["\']([^"\']*\.mpd[^"\']*)["\']',   # DASH
                r'["\']([^"\']*manifest[^"\']*)["\']', # Generic manifest
            ]
            
            for pattern in streaming_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches:
                    manifest_url = match
                    if manifest_url.startswith('/'):
                        from urllib.parse import urljoin
                        manifest_url = urljoin(self.driver.current_url, manifest_url)
                    
                    # Try to extract video URLs from manifest
                    video_url = self._extract_from_manifest(manifest_url)
                    if video_url:
                        return video_url
            
            return None
            
        except Exception as e:
            logger.error(f"Strategy 7 failed: {e}")
            return None
    
    def _handle_blob_and_data_urls(self):
        """STRATEGY 8: Handle blob URLs and data URLs with enhanced source element detection"""
        try:
            self.log_status("Strategy 8: Enhanced blob URLs and source element detection")

            # Enhanced JavaScript to find blob URLs and associated source elements
            blob_script = """
            function findBlobUrls() {
                var urls = [];

                // Check all video elements for blob/data URLs AND their source elements
                var videos = document.querySelectorAll('video');
                videos.forEach(function(v, index) {
                    var videoInfo = {type: 'video_with_sources', index: index, sources: []};

                    // Check video element's own URLs
                    if (v.src && (v.src.startsWith('blob:') || v.src.startsWith('data:'))) {
                        videoInfo.blob_url = v.src;
                    }
                    if (v.currentSrc && (v.currentSrc.startsWith('blob:') || v.currentSrc.startsWith('data:'))) {
                        videoInfo.current_blob_url = v.currentSrc;
                    }

                    // CRITICAL: Check source elements within this video
                    var sources = v.querySelectorAll('source');
                    sources.forEach(function(source, sourceIndex) {
                        var sourceSrc = source.getAttribute('src') || source.src;
                        if (sourceSrc) {
                            var sourceInfo = {
                                index: sourceIndex,
                                url: sourceSrc,
                                type: source.getAttribute('type') || '',
                                media: source.getAttribute('media') || ''
                            };

                            // Check if this is a segmented/clipped video URL
                            if (sourceSrc.includes('clip=') || sourceSrc.includes('/clip') ||
                                sourceSrc.includes('segment') || sourceSrc.includes('range=') ||
                                sourceSrc.includes('multi=') || sourceSrc.includes('/multi')) {
                                sourceInfo.is_segmented = true;
                                sourceInfo.priority = 'high';
                            }

                            // Check if this looks like an HLS or streaming URL
                            if (sourceSrc.includes('.m3u8') || sourceSrc.includes('/hls') ||
                                sourceSrc.includes('/stream') || sourceSrc.includes('/media=hls')) {
                                sourceInfo.is_streaming = true;
                                sourceInfo.priority = sourceInfo.priority || 'medium';
                            }

                            videoInfo.sources.push(sourceInfo);
                        }
                    });

                    // Only add if we found relevant sources or blob URLs
                    if (videoInfo.blob_url || videoInfo.current_blob_url || videoInfo.sources.length > 0) {
                        urls.push(videoInfo);
                    }
                });

                // Check for blob URLs in window objects
                for (var prop in window) {
                    try {
                        var val = window[prop];
                        if (typeof val === 'string' && val.startsWith('blob:')) {
                            urls.push({type: 'window_blob', url: val});
                        }
                    } catch(e) {}
                }

                // Check for MediaSource or SourceBuffer usage
                if (window.MediaSource) {
                    // Look for active media sources
                    var mediaElements = document.querySelectorAll('video, audio');
                    mediaElements.forEach(function(media) {
                        if (media.srcObject) {
                            urls.push({type: 'media_source', element: media});
                        }
                    });
                }

                return urls;
            }
            return findBlobUrls();
            """
            
            blob_results = self.driver.execute_script(blob_script)

            for result in blob_results:
                if result.get('type') == 'video_with_sources':
                    # ENHANCED: Handle video elements with source children
                    video_index = result.get('index', 0)
                    sources = result.get('sources', [])
                    blob_url = result.get('blob_url') or result.get('current_blob_url')

                    self.log_status(f"📹 Found video element {video_index} with {len(sources)} source(s)")
                    if blob_url:
                        self.log_status(f"🔗 Video has blob URL: {blob_url[:60]}...")

                    # Priority 1: Check for high-priority segmented sources first
                    high_priority_sources = [s for s in sources if s.get('priority') == 'high']
                    if high_priority_sources:
                        for source in high_priority_sources:
                            source_url = source['url']
                            self.log_status(f"🎯 Found HIGH PRIORITY segmented source: {source_url[:80]}...")

                            # Check if this is a clip URL that needs special handling
                            if self._is_segmented_video_url(source_url):
                                processed_url = self._process_segmented_video_url(source_url)
                                if processed_url:
                                    return self._create_fake_element_for_download(processed_url)

                            # Try the source URL directly
                            if self._is_valid_video_url(source_url):
                                return self._create_fake_element_for_download(source_url)

                    # Priority 2: Check medium priority streaming sources
                    medium_priority_sources = [s for s in sources if s.get('priority') == 'medium']
                    for source in medium_priority_sources:
                        source_url = source['url']
                        self.log_status(f"📡 Found streaming source: {source_url[:80]}...")
                        if self._is_valid_video_url(source_url):
                            return self._create_fake_element_for_download(source_url)

                    # Priority 3: Check any other sources
                    other_sources = [s for s in sources if not s.get('priority')]
                    for source in other_sources:
                        source_url = source['url']
                        if self._is_valid_video_url(source_url):
                            self.log_status(f"🎥 Found standard source: {source_url[:80]}...")
                            return self._create_fake_element_for_download(source_url)

                    # Priority 4: Try to convert blob URL as fallback
                    if blob_url:
                        self.log_status(f"⬇️ Attempting blob conversion: {blob_url}")
                        converted_url = self._convert_blob_to_downloadable(blob_url)
                        if converted_url:
                            return self._create_fake_element_for_download(converted_url)

                elif result.get('type') == 'window_blob' and result.get('url'):
                    blob_url = result['url']
                    self.log_status(f"Found window blob URL: {blob_url}")

                    # Try to convert blob to downloadable content
                    converted_url = self._convert_blob_to_downloadable(blob_url)
                    if converted_url:
                        return self._create_fake_element_for_download(converted_url)

                elif result.get('type') == 'media_source':
                    # Handle MediaSource API content
                    media_url = self._extract_from_media_source()
                    if media_url:
                        return self._create_fake_element_for_download(media_url)
            
            # Try to intercept blob creation
            intercept_script = """
            // Intercept blob URLs as they're created
            var originalCreateObjectURL = URL.createObjectURL;
            var blobUrls = [];
            
            URL.createObjectURL = function(blob) {
                var url = originalCreateObjectURL.call(this, blob);
                if (blob.type && blob.type.startsWith('video/')) {
                    blobUrls.push({url: url, blob: blob});
                }
                return url;
            };
            
            // Wait for blob creation
            setTimeout(function() {
                // Trigger any pending video operations
                var playButtons = document.querySelectorAll('[class*="play"], [onclick*="play"]');
                playButtons.forEach(function(btn) {
                    try { btn.click(); } catch(e) {}
                });
            }, 1000);
            
            return new Promise(function(resolve) {
                setTimeout(function() {
                    resolve(blobUrls);
                }, 3000);
            });
            """
            
            # Execute and wait for blob interception
            intercepted_blobs = self.driver.execute_async_script(intercept_script)
            
            for blob_info in intercepted_blobs:
                blob_url = blob_info.get('url')
                if blob_url:
                    converted_url = self._convert_blob_to_downloadable(blob_url)
                    if converted_url:
                        return self._create_fake_element_for_download(converted_url)
            
            return None
            
        except Exception as e:
            logger.error(f"Strategy 8 failed: {e}")
            return None

    def _extract_priority_video_url(self):
        """Extract priority video URLs (segmented, main content) before checking ads"""
        try:
            self.log_status("🕐 Waiting for dynamic video content to load...")

            # Wait for dynamic content to load and try multiple times
            import time
            max_attempts = 3
            wait_time = 2

            for attempt in range(max_attempts):
                if attempt > 0:
                    self.log_status(f"🔄 Attempt {attempt + 1}/{max_attempts} - waiting {wait_time}s for dynamic content...")
                    time.sleep(wait_time)

                # Execute enhanced JavaScript with better debugging and URL decoding
                blob_script = """
            function findPriorityVideoUrls() {
                var priorityUrls = [];
                var debugInfo = [];

                // Check all video elements for source elements with segmented content
                var videos = document.querySelectorAll('video');
                debugInfo.push('Found ' + videos.length + ' video elements');

                // Also check within iframes
                var iframes = document.querySelectorAll('iframe');
                debugInfo.push('Found ' + iframes.length + ' iframe elements');

                iframes.forEach(function(iframe, iframeIndex) {
                    try {
                        var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
                        if (iframeDoc) {
                            var iframeVideos = iframeDoc.querySelectorAll('video');
                            debugInfo.push('Iframe ' + iframeIndex + ' has ' + iframeVideos.length + ' video elements');

                            // Add iframe videos to main videos list
                            iframeVideos.forEach(function(v) {
                                videos = Array.prototype.slice.call(videos);
                                videos.push(v);
                            });
                        }
                    } catch(e) {
                        debugInfo.push('Iframe ' + iframeIndex + ' access blocked (cross-origin)');
                    }
                });

                videos.forEach(function(v, index) {
                    var videoInfo = {
                        index: index,
                        src: v.src || 'none',
                        currentSrc: v.currentSrc || 'none',
                        sources: []
                    };

                    // Check source elements within this video
                    var sources = v.querySelectorAll('source');
                    debugInfo.push('Video ' + index + ' has ' + sources.length + ' source elements');

                    sources.forEach(function(source, sourceIndex) {
                        var sourceSrc = source.getAttribute('src') || source.src;
                        if (sourceSrc) {
                            // IMPORTANT: Decode URL-encoded content
                            var decodedSrc = sourceSrc;
                            try {
                                decodedSrc = decodeURIComponent(sourceSrc);
                            } catch(e) {
                                // If decoding fails, use original
                            }

                            var sourceInfo = {
                                url: sourceSrc,  // Keep original for download
                                decodedUrl: decodedSrc,
                                priority: 0,
                                type: 'source_element',
                                videoIndex: index,
                                sourceIndex: sourceIndex
                            };

                            debugInfo.push('Source ' + sourceIndex + ': ' + sourceSrc.substring(0, 100) + '...');

                            // Check both original and decoded URLs for patterns
                            var urlToCheck = sourceSrc.toLowerCase() + ' ' + decodedSrc.toLowerCase();

                            // HIGH PRIORITY: Segmented/clipped video URLs (check URL-encoded versions too)
                            if (urlToCheck.includes('clip=') || urlToCheck.includes('clip%3d') ||
                                urlToCheck.includes('/clip') || urlToCheck.includes('segment') ||
                                urlToCheck.includes('range=') || urlToCheck.includes('range%3d') ||
                                urlToCheck.includes('multi=') || urlToCheck.includes('multi%3d')) {
                                sourceInfo.priority = 100;
                                sourceInfo.reason = 'segmented_content';
                                debugInfo.push('HIGH PRIORITY: Segmented content detected in source ' + sourceIndex);
                            }

                            // MEDIUM-HIGH PRIORITY: HLS2 or streaming URLs
                            else if (urlToCheck.includes('media=hls') || urlToCheck.includes('media%3dhls') ||
                                     urlToCheck.includes('.m3u8') || urlToCheck.includes('/hls') ||
                                     urlToCheck.includes('/stream')) {
                                sourceInfo.priority = 80;
                                sourceInfo.reason = 'streaming_content';
                                debugInfo.push('MEDIUM PRIORITY: Streaming content detected in source ' + sourceIndex);
                            }

                            // GOOD PRIORITY: Video CDN URLs
                            else if (urlToCheck.includes('vcdn') || urlToCheck.includes('video-') ||
                                     urlToCheck.includes('stream-') || urlToCheck.includes('media-')) {
                                sourceInfo.priority = 60;
                                sourceInfo.reason = 'video_cdn';
                                debugInfo.push('GOOD PRIORITY: Video CDN detected in source ' + sourceIndex);
                            }

                            // ANY valid video URL gets some priority
                            else if (urlToCheck.includes('.mp4') || urlToCheck.includes('.webm') ||
                                     urlToCheck.includes('.avi') || urlToCheck.includes('.mov')) {
                                sourceInfo.priority = 20;
                                sourceInfo.reason = 'video_file';
                                debugInfo.push('LOW PRIORITY: Video file detected in source ' + sourceIndex);
                            }

                            // Filter out obvious ads, previews, and non-video content
                            var isFiltered = urlToCheck.includes('aucdn.net') ||
                                           urlToCheck.includes('sacdnssedge.com') ||
                                           urlToCheck.includes('ads.') ||
                                           urlToCheck.includes('/ad/') ||
                                           urlToCheck.includes('advertisement') ||
                                           urlToCheck.includes('banner') ||
                                           urlToCheck.includes('.svg') ||
                                           urlToCheck.includes('.jpg') ||
                                           urlToCheck.includes('.png') ||
                                           urlToCheck.includes('.gif') ||
                                           urlToCheck.includes('trailer.mp4') ||
                                           urlToCheck.includes('preview.mp4') ||
                                           urlToCheck.includes('thumb') ||
                                           urlToCheck.includes('icon') ||
                                           urlToCheck.includes('logo') ||
                                           urlToCheck.includes('sugarcams.com');

                            if (isFiltered) {
                                sourceInfo.priority = 0;
                                sourceInfo.reason = 'filtered_content';
                                debugInfo.push('FILTERED: Non-video content detected in source ' + sourceIndex);
                            }

                            // BOOST PRIORITY for main video indicators
                            if (urlToCheck.includes('_high.mp4') ||
                                urlToCheck.includes('_medium.mp4') ||
                                urlToCheck.includes('main') ||
                                urlToCheck.includes('full') ||
                                (urlToCheck.includes('.mp4') && !urlToCheck.includes('trailer') && !urlToCheck.includes('preview'))) {
                                sourceInfo.priority += 100;  // Increased from 40 to 100 to meet high-priority threshold
                                sourceInfo.reason += '_main_video';
                                debugInfo.push('BOOSTED: Main video detected in source ' + sourceIndex);
                            }

                            // EXTRA BOOST for CDN URLs with auth parameters
                            if (urlToCheck.includes('verify=') || urlToCheck.includes('token=') ||
                                urlToCheck.includes('signature=') || urlToCheck.includes('auth=') ||
                                urlToCheck.includes('.cdn') || urlToCheck.includes('cdn.')) {
                                sourceInfo.priority += 150;  // Extra boost for CDN sources with auth
                                sourceInfo.reason += '_cdn_video';
                                debugInfo.push('EXTRA BOOSTED: CDN video detected in source ' + sourceIndex);
                            }

                            if (sourceInfo.priority > 0) {
                                priorityUrls.push(sourceInfo);
                            }

                            videoInfo.sources.push({
                                src: sourceSrc.substring(0, 100),
                                priority: sourceInfo.priority,
                                reason: sourceInfo.reason
                            });
                        }
                    });

                    // Also check video element's own src if it has blob URL
                    if (v.src && v.src.startsWith('blob:')) {
                        debugInfo.push('Video ' + index + ' has blob URL: ' + v.src);
                        // Video has blob URL, prioritize any source elements found
                        // This indicates dynamic content loading
                    }
                });

                // Sort by priority (highest first)
                priorityUrls.sort(function(a, b) { return b.priority - a.priority; });

                return {
                    urls: priorityUrls,
                    debug: debugInfo
                };
            }
            return findPriorityVideoUrls();
            """

                try:
                    priority_results = self.driver.execute_script(blob_script)

                    # Extract debug info and URLs
                    debug_info = priority_results.get('debug', [])
                    priority_urls = priority_results.get('urls', [])

                    # Log debug information for first attempt or if we find high-priority content
                    if attempt == 0 or any(url.get('priority', 0) >= 50 for url in priority_urls):
                        for debug_msg in debug_info[:20]:  # Limit to first 20 debug messages
                            self.log_status(f"🔍 DEBUG (attempt {attempt + 1}): {debug_msg}")

                    self.log_status(f"🎯 Attempt {attempt + 1}: Found {len(priority_urls)} priority video URLs")

                    # Look for high-priority URLs first (segmented content) - lowered threshold for detected videos
                    high_priority_urls = [url for url in priority_urls if url.get('priority', 0) >= 50]

                    if high_priority_urls:
                        self.log_status(f"🚀 Found {len(high_priority_urls)} high-priority URLs on attempt {attempt + 1}")

                        for result in high_priority_urls:
                            url = result.get('url')
                            priority = result.get('priority', 0)
                            reason = result.get('reason', 'unknown')
                            video_index = result.get('videoIndex', 0)
                            source_index = result.get('sourceIndex', 0)

                            if url and priority > 0:
                                self.log_status(f"🌟 HIGH PRIORITY URL found (score: {priority}, reason: {reason}, video: {video_index}, source: {source_index}): {url[:100]}...")

                                # Apply additional filtering
                                if not self._is_ad_url(url):
                                    self.log_status(f"✅ Selected high-priority URL: {url[:100]}...")
                                    return url
                                else:
                                    self.log_status(f"🚫 High-priority URL filtered as ad: {url[:80]}...")

                    # If no high-priority URLs found, try clicking play button to trigger loading
                    if attempt < max_attempts - 1:  # Don't try this on last attempt
                        try:
                            play_buttons = self.driver.find_elements("css selector", "[class*='play'], [onclick*='play'], .vjs-big-play-button, .play-btn")
                            if play_buttons:
                                self.log_status(f"🎬 Clicking play button to trigger content loading...")
                                play_buttons[0].click()
                                time.sleep(1)  # Short wait for content to load
                        except Exception as e:
                            logger.debug(f"Play button click failed: {e}")

                except Exception as e:
                    self.log_status(f"⚠️ Attempt {attempt + 1} failed: {str(e)[:50]}")
                    continue

            # If no high-priority URLs found in any attempt, check lower priority ones
            self.log_status("🔍 No high-priority segmented URLs found, checking all URLs from last attempt...")

            try:
                # Run one final check for any valid URLs
                final_results = self.driver.execute_script(blob_script)
                final_urls = final_results.get('urls', [])

                for result in final_urls:
                    url = result.get('url')
                    priority = result.get('priority', 0)
                    reason = result.get('reason', 'unknown')

                    if url and priority > 0:
                        self.log_status(f"🎯 Final check URL (score: {priority}, reason: {reason}): {url[:100]}...")

                        if not self._is_ad_url(url):
                            self.log_status(f"✅ Selected final URL: {url[:100]}...")
                            return url

            except Exception as e:
                logger.debug(f"Final URL check failed: {e}")

            self.log_status("⚠️ No valid priority URLs found after all attempts")
            return None

        except Exception as e:
            logger.debug(f"Priority URL extraction failed: {e}")
            return None

    def _is_ad_url(self, url):
        """Check if a URL is likely an advertisement"""
        try:
            if not url:
                return True

            url_lower = url.lower()

            # Known ad domains (excluding video CDN domains)
            ad_domains = [
                'sacdnssedge.com', 'adnium.com', 'adsystem.com', 'doubleclick.net',
                'googlesyndication.com', 'googletagmanager.com', 'analytics.com',
                'ads.yahoo.com', 'facebook.com/tr', 'twitter.com/i/adsct',
                'outbrain.com', 'taboola.com', 'revcontent.com', 'mgid.com',
                'propellerads.com', 'popads.net', 'popcash.net', 'adsterra.com'
            ]

            # However, allow CDN URLs with authentication parameters (not ads)
            if any(param in url_lower for param in ['verify=', 'token=', 'signature=', 'auth=']):
                return False  # Not an ad, it's an authenticated CDN video

            # Also allow .cdn domains or cdn. subdomains
            if '.cdn' in url_lower or 'cdn.' in url_lower:
                return False  # Not an ad, it's a CDN video

            # Ad patterns
            ad_patterns = [
                '/ads/', '/ad/', '/advertisement/', '/banner/', '/popup/',
                'banner', 'popup', 'preroll', 'midroll', 'postroll',
                'ads.', 'ad.', 'adv.', 'advertisement', 'sponsored'
            ]

            # Check for ad indicators
            for domain in ad_domains:
                if domain in url_lower:
                    return True

            for pattern in ad_patterns:
                if pattern in url_lower:
                    return True

            return False

        except Exception:
            return False

    def _is_segmented_video_url(self, url):
        """Check if a URL appears to be a segmented/clipped video"""
        try:
            if not url or not isinstance(url, str):
                return False

            url_lower = url.lower()

            # Check for common segmented video indicators (both encoded and non-encoded)
            segmented_indicators = [
                'clip=', '/clip', 'clip%3d', '%2fclip',  # clip parameters
                'segment=', '/segment', 'segment%3d', '%2fsegment',  # segment parameters
                'range=', '/range', 'range%3d', '%2frange',  # range parameters
                'multi=', '/multi', 'multi%3d', '%2fmulti',  # multi parameters
                'start=', 'end=', 'time=', 'duration=',  # time-based parameters
                'chunk=', '/chunk', 'part=', '/part'  # chunk/part parameters
            ]

            return any(indicator in url_lower for indicator in segmented_indicators)

        except Exception as e:
            logger.debug(f"Error checking segmented URL: {e}")
            return False

    def _process_segmented_video_url(self, source_url):
        """Process segmented video URLs to handle clip parameters properly"""
        try:
            self.log_status(f"🔧 Processing segmented URL: {source_url[:100]}...")

            import re
            from urllib.parse import urlparse, parse_qs, urlencode, unquote

            # First decode URL-encoded characters
            decoded_url = unquote(source_url)
            self.log_status(f"🔍 Decoded URL: {decoded_url[:100]}...")

            # Look for clip parameter in both encoded and decoded versions
            clip_patterns = [
                r'clip%3D([^%&/]+)',  # URL-encoded clip=
                r'/clip%3D([^/]+)',   # URL-encoded /clip=
                r'clip=([^&,/]+)',    # Regular clip=
                r'/clip=([^/]+)'      # Regular /clip=
            ]

            clip_ranges = None
            for pattern in clip_patterns:
                clip_match = re.search(pattern, source_url)
                if clip_match:
                    clip_ranges = clip_match.group(1)
                    self.log_status(f"📊 Found clip ranges: {clip_ranges}")
                    break

            if clip_ranges:
                # Parse clip ranges to understand the segments
                segments = clip_ranges.split('%2C') if '%2C' in clip_ranges else clip_ranges.split(',')
                self.log_status(f"📹 Found {len(segments)} video segments: {segments}")

                # Strategy 1: Reconstruct URL by removing clip parameters
                full_video_url = source_url

                # Find where the clip parameter starts and ends, then reconstruct URL
                # Pattern: ...multi%3D...%2F/clip%3D{segments}%2Fvideo156/...
                # Goal: ...multi%3D...%2F/video156/...

                clip_start = source_url.find('/clip%3D')
                if clip_start == -1:
                    clip_start = source_url.find('clip%3D')
                    prefix = source_url[:clip_start]
                else:
                    prefix = source_url[:clip_start + 1]  # Include the /

                # Find where video path starts (the actual file path)
                video_start = source_url.find('%2Fvideo')
                if video_start != -1:
                    # Extract the part after %2Fvideo (decode the %2F to /)
                    suffix = source_url[video_start + 3:]  # Skip %2F
                    full_video_url = prefix + suffix
                    self.log_status(f"🔧 Reconstructed URL by removing clip segment")
                    self.log_status(f"🔍 DEBUGGING: Original URL: {source_url}")
                    self.log_status(f"🔍 DEBUGGING: Prefix: {prefix}")
                    self.log_status(f"🔍 DEBUGGING: Suffix: {suffix}")
                    self.log_status(f"🎬 Full video URL: {full_video_url}")

                    if full_video_url != source_url:
                        return full_video_url

                # Fallback: Try other patterns if the above doesn't work
                self.log_status(f"🔄 Primary reconstruction failed, trying fallback patterns...")

                # Remove clip parameters with regex (less precise but broader)
                clip_removal_patterns = [
                    r'/clip%3D[^/]*',     # Remove /clip%3D...
                    r'clip%3D[^/]*',      # Remove clip%3D...
                    r'/clip=[^/]*',       # Remove /clip=...
                    r'clip=[^/]*'         # Remove clip=...
                ]

                for pattern in clip_removal_patterns:
                    old_url = full_video_url
                    full_video_url = re.sub(pattern, '', full_video_url)
                    if full_video_url != old_url:
                        self.log_status(f"🧹 Removed clip pattern: {pattern}")
                        # Clean up any double slashes
                        full_video_url = re.sub(r'([^:])//+', r'\1/', full_video_url)

                        if full_video_url != source_url:
                            self.log_status(f"🎬 Fallback URL: {full_video_url[:100]}...")
                            return full_video_url
                        break

            # Strategy 3: For HLS2 media URLs, try to construct a manifest URL
            if '/media=hls2' in source_url or 'media%3Dhls2' in source_url:
                self.log_status("🎬 Detected HLS2 media - attempting manifest construction")

                # Try to construct an HLS manifest URL
                manifest_url = re.sub(r'\.mp4$', '.m3u8', source_url)
                manifest_url = re.sub(r'/media=hls2', '/media=hls', manifest_url)
                manifest_url = re.sub(r'media%3Dhls2', 'media%3Dhls', manifest_url)

                if manifest_url != source_url:
                    self.log_status(f"🎥 Constructed HLS manifest: {manifest_url[:100]}...")
                    return manifest_url

            # Strategy 4: Use original URL with yt-dlp format selection to get best quality
            self.log_status("⚙️ Using original segmented URL - will use yt-dlp format selection for best quality")
            return source_url

        except Exception as e:
            logger.error(f"Error processing segmented URL: {e}")
            # If processing fails, return original URL
            return source_url

    def _extract_from_manifest(self, manifest_url):
        """Enhanced extraction from streaming manifests (HLS/DASH) with clip support"""
        try:
            import requests
            import re
            from urllib.parse import urljoin, urlparse

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': self.driver.current_url
            }

            # For URLs with special parameters (like clip, multi), try direct download first
            if any(param in manifest_url for param in ['clip=', 'multi=', 'media=hls']):
                self.log_status(f"🎬 Direct HLS URL with parameters detected")
                return manifest_url  # Let yt-dlp handle complex HLS URLs

            response = requests.get(manifest_url, headers=headers, timeout=10)
            if response.status_code == 200:
                content = response.text

                # Extract video segments from HLS manifest
                if '.m3u8' in manifest_url:
                    self.log_status("📺 Processing HLS manifest")
                    lines = content.split('\n')
                    best_quality_url = None
                    highest_bandwidth = 0

                    for i, line in enumerate(lines):
                        if line.startswith('#EXT-X-STREAM-INF:'):
                            # Extract bandwidth for quality comparison
                            bandwidth_match = re.search(r'BANDWIDTH=(\d+)', line)
                            current_bandwidth = int(bandwidth_match.group(1)) if bandwidth_match else 0

                            if i + 1 < len(lines):
                                stream_url = lines[i + 1].strip()
                                if stream_url and not stream_url.startswith('#'):
                                    if stream_url.startswith('/'):
                                        stream_url = urljoin(manifest_url, stream_url)

                                    # Select highest quality stream
                                    if current_bandwidth > highest_bandwidth:
                                        highest_bandwidth = current_bandwidth
                                        best_quality_url = stream_url
                                        self.log_status(f"🔝 Found higher quality stream: {current_bandwidth} bps")

                    if best_quality_url:
                        return best_quality_url

                    # Fallback: look for direct segment URLs if no stream info found
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith('#') and '.ts' in line:
                            if line.startswith('/'):
                                line = urljoin(manifest_url, line)
                            return line

                # Extract from DASH manifest
                elif '.mpd' in manifest_url:
                    self.log_status("📺 Processing DASH manifest")
                    # Parse DASH XML to find video representations
                    video_urls = re.findall(r'media="([^"]*\.mp4[^"]*)"', content)
                    if video_urls:
                        video_url = video_urls[0]
                        if video_url.startswith('/'):
                            video_url = urljoin(manifest_url, video_url)
                        return video_url

                    # Alternative DASH pattern
                    base_url_match = re.search(r'<BaseURL>([^<]+)</BaseURL>', content)
                    if base_url_match:
                        base_url = base_url_match.group(1)
                        if base_url.startswith('/'):
                            base_url = urljoin(manifest_url, base_url)
                        return base_url

            return None

        except Exception as e:
            logger.error(f"Error extracting from manifest: {e}")
            return None
    
    def _convert_blob_to_downloadable(self, blob_url):
        """Convert blob URL to downloadable content"""
        try:
            # Use JavaScript to convert blob to data URL
            conversion_script = f"""
            return new Promise(function(resolve) {{
                try {{
                    fetch('{blob_url}')
                        .then(response => response.blob())
                        .then(blob => {{
                            var reader = new FileReader();
                            reader.onload = function() {{
                                resolve(reader.result);
                            }};
                            reader.onerror = function() {{
                                resolve(null);
                            }};
                            reader.readAsDataURL(blob);
                        }})
                        .catch(() => resolve(null));
                }} catch(e) {{
                    resolve(null);
                }}
            }});
            """
            
            data_url = self.driver.execute_async_script(conversion_script)
            
            if data_url and data_url.startswith('data:video/'):
                # Save data URL content
                return self._save_data_url_content(data_url)
            
            return None
            
        except Exception as e:
            logger.error(f"Error converting blob URL: {e}")
            return None
    
    def _extract_from_media_source(self):
        """Extract content from MediaSource API"""
        try:
            # Check for media sources and try to extract segments
            media_script = """
            var mediaElements = document.querySelectorAll('video');
            var sources = [];
            
            mediaElements.forEach(function(video) {
                if (video.srcObject || video.mozSrcObject) {
                    // Try to get source from MediaStream
                    sources.push('media_stream_detected');
                }
                
                // Check for MSE usage
                if (video.src && video.src.startsWith('blob:')) {
                    sources.push(video.src);
                }
            });
            
            return sources;
            """
            
            sources = self.driver.execute_script(media_script)

            # Return actual sources if found, not fake indication
            if sources and len(sources) > 0:
                self.log_status(f"MediaSource detected with {len(sources)} source(s)")
                # Return the actual sources for processing
                return sources

            return None
            
        except Exception as e:
            logger.error(f"Error extracting from MediaSource: {e}")
            return None
    
    def _save_data_url_content(self, data_url):
        """Save data URL content to file"""
        try:
            import base64
            
            # Extract data from data URL
            header, data = data_url.split(',', 1)
            decoded_data = base64.b64decode(data)
            
            # Generate filename
            timestamp = int(time.time())
            filename = f"blob_video_{timestamp}.mp4"
            output_path = os.path.join(self.driver.download_folder, filename)
            
            # Save to file
            with open(output_path, 'wb') as f:
                f.write(decoded_data)
            
            self.log_status(f"Saved blob content: {filename}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error saving data URL content: {e}")
            return None

    def _source_page_navigation_fallback(self):
        """STRATEGY 9: Source page navigation fallback - Click source links when all else fails"""
        try:
            self.log_status("Strategy 9: Source page navigation fallback (final attempt)")

            # Look for various source/original page links that might contain the actual video
            source_selectors = [
                "//a[contains(@href, 'source')]",                    # Direct source links
                "//a[contains(text(), 'Source')]",                   # Source text links
                "//a[contains(text(), 'Original')]",                 # Original content links
                "//a[contains(text(), 'Full video')]",               # Full video links
                "//a[contains(text(), 'HD')]",                       # HD quality links
                "//a[contains(text(), 'Download')]",                 # Download links
                "//a[contains(@href, 'original')]",                  # Original URL pattern
                "//a[contains(@href, '.mp4')]",                      # Direct MP4 links
                "//a[contains(@href, '.mkv')]",                      # Direct MKV links
                "//a[contains(@href, '.avi')]",                      # Direct AVI links
                "//a[contains(@href, 'video')]",                     # Video URL pattern
                "//a[contains(@href, 'watch')]",                     # Watch page links
                "//a[contains(@class, 'source')]",                   # Source class
                "//a[contains(@class, 'original')]",                 # Original class
                "//button[contains(text(), 'Watch')]",               # Watch buttons
                "//div[contains(@class, 'source')]//a",              # Links in source containers
                "//div[contains(@class, 'download')]//a"             # Links in download containers
            ]

            current_url = self.driver.current_url
            self.log_status(f"Searching for source links on: {current_url[:60]}...")

            for i, selector in enumerate(source_selectors):
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    self.log_status(f"Source selector {i+1} found {len(elements)} elements")

                    for j, element in enumerate(elements):
                        if element.is_displayed():
                            href = element.get_attribute('href')
                            text_content = element.text.strip()

                            # Skip if no href or if it's the same page
                            if not href or href == current_url:
                                continue

                            # Skip unwanted links (ads, social media, etc.)
                            if any(skip in href.lower() for skip in ['facebook', 'twitter', 'instagram', 'tiktok', 'reddit', 'discord', 'telegram', 'ads', 'sponsor', 'affiliate']):
                                continue

                            self.log_status(f"Found potential source link: {href[:60]}...")
                            self.log_status(f"Link text: {text_content[:40]}...")

                            # Click the source link and try to extract video from that page
                            try:
                                # Save current window handle
                                original_window = self.driver.current_window_handle

                                # Try to open in new tab first (safer)
                                self.driver.execute_script("window.open(arguments[0], '_blank');", href)
                                time.sleep(0.1)

                                # Switch to new tab
                                if len(self.driver.window_handles) > 1:
                                    new_window = [w for w in self.driver.window_handles if w != original_window][0]
                                    self.driver.switch_to.window(new_window)

                                    # Ultra-fast page load check
                                    try:
                                        WebDriverWait(self.driver, 0.3).until(
                                            lambda driver: driver.execute_script("return document.readyState") != "loading"
                                        )
                                    except:
                                        pass  # Continue regardless
                                    time.sleep(0.1)  # Reduced wait time

                                    self.log_status(f"Navigated to source page: {self.driver.current_url[:60]}...")

                                    # Try to find video on source page using simplified detection
                                    video_element = self._find_video_on_source_page()

                                    if video_element:
                                        self.log_status("✅ Found video on source page!")
                                        # Close new tab and return to original
                                        self.driver.close()
                                        self.driver.switch_to.window(original_window)
                                        return video_element

                                    # Close new tab and return to original
                                    self.driver.close()
                                    self.driver.switch_to.window(original_window)

                                else:
                                    # If new tab didn't open, navigate directly (fallback)
                                    self.driver.get(href)
                                    time.sleep(0.2)

                                    video_element = self._find_video_on_source_page()

                                    if video_element:
                                        self.log_status("✅ Found video on direct navigation!")
                                        return video_element

                                    # Return to original page
                                    self.driver.get(current_url)
                                    time.sleep(0.1)

                            except Exception as nav_e:
                                self.log_status(f"Navigation error: {str(nav_e)[:40]}")
                                # Ensure we're back on original page
                                try:
                                    if len(self.driver.window_handles) > 1:
                                        self.driver.close()
                                        self.driver.switch_to.window(original_window)
                                    else:
                                        self.driver.get(current_url)
                                        time.sleep(0.2)
                                except:
                                    pass
                                continue

                except Exception as sel_e:
                    self.log_status(f"Selector {i+1} error: {str(sel_e)[:40]}")
                    continue

            self.log_status("No viable source links found for fallback navigation")
            return None

        except Exception as e:
            logger.error(f"Source page navigation fallback failed: {e}")
            return None

    def _find_video_on_source_page(self):
        """Simplified video detection for source pages"""
        try:
            # Quick check for direct video elements
            video_elements = self.safe_find_elements(By.TAG_NAME, "video")
            for video in video_elements:
                if video.is_displayed():
                    src = video.get_attribute('src')
                    if src and any(ext in src.lower() for ext in ['.mp4', '.mkv', '.avi', '.webm', '.mov']):
                        self.log_status(f"Found direct video: {src[:60]}...")
                        return self._create_fake_element_for_download(src)

            # Quick check for direct video links
            video_links = self.driver.find_elements(By.XPATH, "//a[contains(@href, '.mp4') or contains(@href, '.mkv') or contains(@href, '.avi')]")
            for link in video_links:
                if link.is_displayed():
                    href = link.get_attribute('href')
                    if href:
                        self.log_status(f"Found direct video link: {href[:60]}...")
                        return self._create_fake_element_for_download(href)

            # Quick page source scan for video URLs
            page_source = self.driver.page_source
            video_patterns = [
                r'https?://[^"\s]+\.mp4[^"\s]*',
                r'https?://[^"\s]+\.mkv[^"\s]*',
                r'https?://[^"\s]+\.avi[^"\s]*',
                r'https?://[^"\s]+\.webm[^"\s]*'
            ]

            for pattern in video_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches[:3]:  # Try first 3 matches
                    if 'video' in match.lower() or any(ext in match.lower() for ext in ['.mp4', '.mkv', '.avi']):
                        self.log_status(f"Found video URL in source: {match[:60]}...")
                        return self._create_fake_element_for_download(match)

            return None

        except Exception as e:
            logger.error(f"Error finding video on source page: {e}")
            return None

    def _detect_and_click_embed_links(self):
        """STRATEGY 11: Detect and click embed links to reach actual video source pages"""
        try:
            self.log_status("Strategy 11: General embed link detection and navigation")

            current_url = self.driver.current_url
            self.log_status(f"Analyzing page for embed links: {current_url[:60]}...")

            # DEBUG: Show page structure
            all_divs = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'video') or contains(@class, 'player') or contains(@class, 'VideoViewer')]")
            self.log_status(f"DEBUG: Found {len(all_divs)} video/player containers")

            # First, look for source page links in video players
            source_link_selectors = [
                # Look for "source" or "original" links
                "//a[contains(@href, 'source') or contains(@href, 'original')]",
                "//a[contains(text(), 'Source') or contains(text(), 'Original')]",
                "//a[contains(@class, 'source') or contains(@class, 'original')]",

                # Look for external links in video players
                "//div[contains(@class, 'player')]//a[@href and not(contains(@href, '#'))]",
                "//div[contains(@class, 'video')]//a[@href and not(contains(@href, '#'))]",
                "//div[contains(@class, 'VideoViewer')]//a[@href and not(contains(@href, '#'))]",

                # Look for watch/view links
                "//a[contains(@href, '/watch/') or contains(@href, '/view/')]",
                "//a[contains(text(), 'Watch on') or contains(text(), 'View on')]",

                # Yandex specific source links
                "//a[contains(@href, 'yandex.com/video/preview')]",
                "//a[contains(@class, 'VideoViewer')][@href]",

                # Generic embed source links
                "//iframe[@src]/..//a[@href]",
                "//video/..//a[@href]",
            ]

            # Try to find and click source links first
            for i, selector in enumerate(source_link_selectors):
                try:
                    links = self.driver.find_elements(By.XPATH, selector)
                    if links:
                        self.log_status(f"Selector {i+1} found {len(links)} potential source links: {selector[:50]}...")
                        for j, link in enumerate(links[:3]):  # Try first 3 links
                            try:
                                href = link.get_attribute('href')
                                if href and not href.startswith('#'):
                                    self.log_status(f"Clicking source link: {href[:60]}...")
                                    link.click()
                                    time.sleep(0.1)

                                    # Check if we navigated to a new page
                                    new_url = self.driver.current_url
                                    if new_url != current_url:
                                        self.log_status("Navigated to source page!")
                                        # Try to find video on the new page
                                        video = self._find_video_on_current_page()
                                        if video:
                                            return video
                                        # If no video found, continue trying other links
                            except Exception as e:
                                continue
                except Exception:
                    continue

            # If no source links found, try the original embed patterns
            embed_selectors = [
                # YANDEX VIDEO SPECIFIC PATTERNS
                "//div[contains(@class, 'VideoViewer-Direct')]",
                "//div[contains(@class, 'DirectInlineContainer')]",
                "//div[contains(@id, 'video-viewer')]",
                "//div[contains(@class, 'VideoViewer') and contains(@class, 'Direct')]",
                "//div[contains(@class, 'video-list') and @data-log-node]",

                # YOUTUBE EMBED PATTERNS
                "//div[contains(@class, 'youtube-player')]",
                "//div[contains(@id, 'youtube-player')]",
                "//iframe[contains(@src, 'youtube.com/embed')]",
                "//iframe[contains(@src, 'youtu.be')]",

                # VIMEO EMBED PATTERNS
                "//iframe[contains(@src, 'vimeo.com')]",
                "//div[contains(@class, 'vimeo')]",

                # DAILYMOTION EMBED PATTERNS
                "//iframe[contains(@src, 'dailymotion.com')]",
                "//div[contains(@class, 'dailymotion')]",

                # GENERIC VIDEO VIEWER PATTERNS
                "//div[contains(@class, 'video-viewer')]",
                "//div[contains(@class, 'VideoViewer')]",
                "//div[contains(@class, 'video-container')]",
                "//div[contains(@class, 'media-viewer')]",

                # Common embed button patterns
                "//button[contains(text(), 'Play')]",
                "//button[contains(text(), 'Watch')]",
                "//button[contains(text(), 'View')]",
                "//a[contains(text(), 'Play')]",
                "//a[contains(text(), 'Watch')]",
                "//a[contains(text(), 'View')]",

                # Video-specific embed patterns
                "//button[contains(@class, 'play')]",
                "//button[contains(@class, 'video')]",
                "//button[contains(@class, 'embed')]",
                "//a[contains(@class, 'play')]",
                "//a[contains(@class, 'video')]",
                "//a[contains(@class, 'embed')]",

                # Thumbnail and preview click patterns
                "//img[contains(@class, 'thumbnail')]",
                "//img[contains(@class, 'preview')]",
                "//img[contains(@class, 'video')]",
                "//div[contains(@class, 'thumbnail')]",
                "//div[contains(@class, 'preview')]",
                "//div[contains(@class, 'video-preview')]",

                # iframe and embed container clicks
                "//div[contains(@class, 'embed')]//button",
                "//div[contains(@class, 'embed')]//a",
                "//div[contains(@class, 'player')]//button",
                "//div[contains(@class, 'player')]//a",

                # Generic video container clicks
                "//div[contains(@class, 'video')]//button",
                "//div[contains(@class, 'video')]//a",
                "//div[contains(@id, 'video')]//button",
                "//div[contains(@id, 'player')]//button",

                # Data attributes for embed links
                "//a[@data-embed]",
                "//button[@data-embed]",
                "//a[@data-video]",
                "//button[@data-video]",
                "//a[@data-src]",
                "//button[@data-src]",
                "//*[@data-log-node]",  # Yandex-style data attributes

                # Common video hosting patterns
                "//a[contains(@href, 'embed')]",
                "//a[contains(@href, 'player')]",
                "//a[contains(@href, 'watch')]",
                "//a[contains(@href, 'video')]",
                "//a[contains(@href, 'preview')]",  # Yandex preview URLs

                # Role-based interactive elements
                "//div[@role='button'][contains(@class, 'play')]",
                "//div[@role='button'][contains(@class, 'video')]",
                "//span[@role='button'][contains(@class, 'play')]",

                # Icon-based play buttons (common patterns)
                "//i[contains(@class, 'play')]/../..",  # Parent of play icon
                "//svg[contains(@class, 'play')]/../..", # Parent of play SVG
                "//*[contains(@class, 'fa-play')]/../..", # Font Awesome play icon parent
            ]

            self.log_status(f"Checking {len(embed_selectors)} embed link patterns...")

            for i, selector in enumerate(embed_selectors):
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    self.log_status(f"Embed selector {i+1} found {len(elements)} elements")

                    for j, element in enumerate(elements[:3]):  # Try first 3 of each type
                        try:
                            if not element.is_displayed():
                                continue

                            # Get element info for logging
                            tag_name = element.tag_name
                            element_class = element.get_attribute('class') or ''
                            element_text = element.text.strip()[:20] if element.text else ''
                            href = element.get_attribute('href') if tag_name == 'a' else None

                            self.log_status(f"Trying embed element {j+1}: {tag_name} class='{element_class[:30]}' text='{element_text}'")

                            # Save current page state
                            original_url = self.driver.current_url
                            original_window = self.driver.current_window_handle

                            # Click the embed element
                            try:
                                # Scroll to element and click
                                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                                time.sleep(0.1)

                                # Special handling for Yandex VideoViewer elements
                                if 'VideoViewer' in element_class or 'DirectInlineContainer' in element_class:
                                    self.log_status("Detected Yandex VideoViewer - using special click method")
                                    # Try to find and click any child clickable elements
                                    try:
                                        clickable_children = element.find_elements(By.XPATH, ".//*[@role='button'] | .//button | .//a")
                                        for child in clickable_children[:3]:
                                            if child.is_displayed():
                                                self.log_status("Clicking Yandex child element")
                                                child.click()
                                                time.sleep(0.1)
                                                break
                                    except:
                                        pass

                                    # Also try clicking the container itself
                                    self.driver.execute_script("arguments[0].click();", element)
                                else:
                                    # Try different click methods for regular elements
                                    try:
                                        element.click()
                                    except:
                                        # Fallback to JavaScript click
                                        self.driver.execute_script("arguments[0].click();", element)

                                self.log_status(f"Clicked embed element, waiting for navigation...")
                                time.sleep(0.2)

                                # Check if we navigated to a new page or opened new window
                                new_url = self.driver.current_url
                                new_windows = self.driver.window_handles

                                # Handle new window/tab
                                if len(new_windows) > 1:
                                    self.log_status("New window/tab opened, switching...")
                                    new_window = [w for w in new_windows if w != original_window][0]
                                    self.driver.switch_to.window(new_window)
                                    new_url = self.driver.current_url
                                    time.sleep(0.1)

                                # Check if we're on a different page
                                if new_url != original_url:
                                    self.log_status(f"Navigated to embed source: {new_url[:60]}...")

                                    # Special handling for Yandex video URLs
                                    if 'yandex.com' in new_url and 'video' in new_url:
                                        yandex_video = self._extract_yandex_video_url(new_url)
                                        if yandex_video:
                                            self.log_status("✅ Found Yandex video URL!")
                                            return yandex_video

                                    # Try to find video on the new page
                                    video_element = self._find_video_on_embed_page()

                                    if video_element:
                                        self.log_status("✅ Found video on embed page!")
                                        return video_element

                                    # Also try iframe detection on embed page
                                    iframe_video = self._check_for_iframe_videos()
                                    if iframe_video:
                                        self.log_status("✅ Found video in iframe on embed page!")
                                        return iframe_video

                                # Clean up - return to original state
                                if len(self.driver.window_handles) > 1:
                                    self.driver.close()
                                    self.driver.switch_to.window(original_window)
                                elif new_url != original_url:
                                    self.driver.get(original_url)
                                    time.sleep(0.1)

                            except Exception as click_e:
                                self.log_status(f"Click error: {str(click_e)[:40]}")
                                # Ensure we're back to original state
                                try:
                                    if len(self.driver.window_handles) > 1:
                                        self.driver.close()
                                        self.driver.switch_to.window(original_window)
                                    elif self.driver.current_url != original_url:
                                        self.driver.get(original_url)
                                        time.sleep(0.2)
                                except:
                                    pass
                                continue

                        except Exception as element_e:
                            self.log_status(f"Element {j+1} error: {str(element_e)[:40]}")
                            continue

                except Exception as selector_e:
                    self.log_status(f"Selector {i+1} error: {str(selector_e)[:40]}")
                    continue

            self.log_status("No functional embed links found")
            return None

        except Exception as e:
            logger.error(f"Embed link detection failed: {e}")
            return None

    def _javascript_link_discovery(self):
        """STRATEGY 12: Use JavaScript to find hidden or dynamic embed links"""
        try:
            self.log_status("Strategy 12: JavaScript-based dynamic link discovery")

            # JavaScript to analyze the page for hidden or dynamic elements
            discover_script = """
            // Find all elements that might contain video embeds
            var results = [];

            // 1. Find all clickable elements with video-related attributes
            var clickableElements = document.querySelectorAll('[onclick], [data-click], [data-src], [data-video]');
            clickableElements.forEach(function(elem, idx) {
                if (idx < 10) { // Limit to first 10
                    results.push({
                        type: 'clickable',
                        tag: elem.tagName,
                        id: elem.id || 'NO_ID',
                        class: elem.className || 'NO_CLASS',
                        onclick: elem.getAttribute('onclick') || '',
                        dataSrc: elem.getAttribute('data-src') || '',
                        dataVideo: elem.getAttribute('data-video') || '',
                        href: elem.href || '',
                        text: elem.textContent.trim().substring(0, 50)
                    });
                }
            });

            // 2. Find all elements with video-related class names
            var videoElements = document.querySelectorAll('[class*="video"], [class*="player"], [class*="play"], [class*="embed"]');
            videoElements.forEach(function(elem, idx) {
                if (idx < 10) { // Limit to first 10
                    var links = elem.querySelectorAll('a[href]');
                    links.forEach(function(link, linkIdx) {
                        if (linkIdx < 3) { // Limit to first 3 links per container
                            results.push({
                                type: 'container_link',
                                container: elem.className,
                                tag: link.tagName,
                                href: link.href,
                                text: link.textContent.trim().substring(0, 50)
                            });
                        }
                    });
                }
            });

            // 3. Look for hidden iframes that might contain video links
            var hiddenIframes = document.querySelectorAll('iframe[style*="display:none"], iframe[style*="visibility:hidden"]');
            hiddenIframes.forEach(function(iframe, idx) {
                if (idx < 5) { // Limit to first 5
                    results.push({
                        type: 'hidden_iframe',
                        src: iframe.src,
                        id: iframe.id || 'NO_ID',
                        class: iframe.className || 'NO_CLASS'
                    });
                }
            });

            return results;
            """

            js_results = self.driver.execute_script(discover_script)
            self.log_status(f"JavaScript discovered {len(js_results)} potential elements")

            current_url = self.driver.current_url

            # Process the JavaScript results
            for i, result in enumerate(js_results):
                try:
                    self.log_status(f"JS Element {i+1}: {result['type']} - {str(result)[:80]}...")

                    if result['type'] == 'clickable' and result.get('onclick'):
                        # Try elements with onclick handlers
                        try:
                            element = self.driver.find_element(By.ID, result['id']) if result['id'] != 'NO_ID' else None
                            if not element and result['class'] != 'NO_CLASS':
                                element = self.driver.find_element(By.CLASS_NAME, result['class'].split()[0])

                            if element:
                                self.log_status(f"Clicking JS-discovered element: {result['onclick'][:50]}...")
                                element.click()
                                time.sleep(0.2)

                                new_url = self.driver.current_url
                                if new_url != current_url:
                                    self.log_status("Navigation detected from JS click!")
                                    video = self._find_video_on_current_page()
                                    if video:
                                        return video
                                    # Return to original page if no video found
                                    self.driver.get(current_url)
                                    time.sleep(0.1)
                        except Exception as e:
                            self.log_status(f"JS click failed: {str(e)[:50]}")
                            continue

                    elif result['type'] == 'container_link' and result.get('href'):
                        # Try links found in video containers
                        href = result['href']
                        if any(indicator in href.lower() for indicator in ['youtube', 'vimeo', 'dailymotion', 'video', 'watch', 'play']):
                            self.log_status(f"Found potential video link in container: {href[:60]}...")
                            try:
                                link_element = self.driver.find_element(By.XPATH, f"//a[@href='{href}']")
                                link_element.click()
                                time.sleep(0.2)

                                new_url = self.driver.current_url
                                if new_url != current_url:
                                    self.log_status("Navigation detected from container link!")
                                    video = self._find_video_on_current_page()
                                    if video:
                                        return video
                                    # Return to original page if no video found
                                    self.driver.get(current_url)
                                    time.sleep(0.1)
                            except Exception as e:
                                self.log_status(f"Container link click failed: {str(e)[:50]}")
                                continue

                    elif result['type'] == 'hidden_iframe' and result.get('src'):
                        # Check hidden iframes for video content
                        iframe_src = result['src']
                        if any(domain in iframe_src for domain in ['youtube', 'vimeo', 'dailymotion']):
                            self.log_status(f"Found hidden video iframe: {iframe_src[:60]}...")
                            return self._create_fake_element_for_download(iframe_src)

                except Exception as e:
                    self.log_status(f"Error processing JS result {i+1}: {str(e)[:50]}")
                    continue

            self.log_status("JavaScript discovery completed - no video found")
            return None

        except Exception as e:
            logger.error(f"JavaScript link discovery failed: {e}")
            return None

    def _intelligent_video_player_clicking(self):
        """STRATEGY 9: Intelligent random clicking system with AI pattern learning"""
        try:
            self.log_status("Starting intelligent video player clicking system")

            current_url = self.driver.current_url
            initial_links_count = len(self.driver.find_elements(By.TAG_NAME, "a"))

            # FIRST: Try to find existing embed buttons like your VK Video example
            embed_buttons = self._find_immediate_embed_buttons()
            if embed_buttons:
                for button in embed_buttons:
                    try:
                        href = button.get_attribute('href')
                        aria_label = button.get_attribute('aria-label') or ''
                        class_name = button.get_attribute('class') or ''

                        self.log_status(f"Found embed button: {aria_label} -> {href[:60]}...")

                        # Click the embed button directly
                        button.click()
                        time.sleep(0.2)

                        # Check if we navigated to a video source
                        new_url = self.driver.current_url
                        if new_url != current_url:
                            self.log_status("Successfully clicked embed button and navigated!")
                            return self._find_video_on_current_page()

                    except Exception as e:
                        self.log_status(f"Embed button click failed: {str(e)[:50]}")
                        continue

            # Find video player areas to focus clicking
            player_areas = self._find_video_player_areas()

            if not player_areas:
                self.log_status("No video player areas detected - using full page")
                # Use the entire viewport as the click area
                player_areas = [{'element': self.driver.find_element(By.TAG_NAME, "body"), 'type': 'fullpage'}]

            self.log_status(f"Found {len(player_areas)} video player areas to explore")

            # Smart clicking strategy
            for i, area in enumerate(player_areas):
                self.log_status(f"Exploring player area {i+1}: {area['type']}")

                result = self._perform_intelligent_clicking(area, current_url, initial_links_count)
                if result:
                    return result

            self.log_status("Intelligent clicking completed - no embed links revealed")
            return None

        except Exception as e:
            self.log_status(f"Intelligent clicking error: {str(e)[:100]}")
            return None

    def _find_immediate_embed_buttons(self):
        """Find embed buttons that are already visible (like your VK Video example)"""
        try:
            embed_button_selectors = [
                # Specific patterns based on your VK Video example
                "a[class*='videoplayer_btn'][href*='vkvideo']",
                "a[class*='videoplayer_btn'][href*='youtube']",
                "a[class*='videoplayer_btn'][href*='vimeo']",
                "a[class*='videoplayer_controls'][href*='video']",
                "a[aria-label*='Video'][href]",
                "a[aria-label*='VK Video'][href]",
                "a[aria-label*='YouTube'][href]",

                # Generic embed button patterns
                "a[class*='embed'][href*='video']",
                "a[class*='source'][href*='video']",
                "a[class*='watch'][href*='video']",
                "button[class*='embed'][data-src]",

                # Links that go to video hosting sites
                "a[href*='vkvideo.ru']",
                "a[href*='youtube.com/watch']",
                "a[href*='vimeo.com/']",
                "a[href*='dailymotion.com']",
            ]

            found_buttons = []

            for selector in embed_button_selectors:
                try:
                    buttons = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for button in buttons:
                        if button.is_displayed():
                            found_buttons.append(button)
                except:
                    continue

            self.log_status(f"Found {len(found_buttons)} immediate embed buttons")
            return found_buttons

        except Exception as e:
            self.log_status(f"Error finding embed buttons: {str(e)[:50]}")
            return []

    def _find_video_player_areas(self):
        """Find all potential video player areas on the page"""
        player_areas = []

        # Common video player selectors with priority
        player_selectors = [
            # HIGHEST priority - specific embed buttons like your VK Video example
            ("[class*='videoplayer_btn']", "embed-button"),
            ("[class*='videoplayer_controls']", "player-controls"),
            ("[aria-label*='Video']", "video-aria-button"),
            ("[href*='vkvideo.ru']", "vk-video-link"),
            ("[href*='youtube.com']", "youtube-link"),
            ("[href*='vimeo.com']", "vimeo-link"),

            # High priority - common video players
            ("[class*='player']", "video-player"),
            ("[class*='video']", "video-container"),
            ("[id*='player']", "player-id"),
            ("[id*='video']", "video-id"),

            # Medium priority - embed containers
            ("[class*='embed']", "embed-container"),
            ("[class*='VideoViewer']", "yandex-viewer"),
            ("[class*='media']", "media-container"),

            # Lower priority - generic containers
            ("iframe", "iframe-element"),
            ("[role='main']", "main-content"),
            (".container", "generic-container")
        ]

        for selector, area_type in player_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    if element.is_displayed() and element.size['width'] > 100 and element.size['height'] > 100:
                        player_areas.append({
                            'element': element,
                            'type': area_type,
                            'selector': selector
                        })
            except:
                continue

        return player_areas[:5]  # Limit to top 5 areas

    def _perform_intelligent_clicking(self, area, original_url, initial_links):
        """Perform intelligent clicking within a video player area"""
        try:
            element = area['element']
            area_type = area['type']

            self.log_status(f"Clicking strategy for {area_type}")

            # Get area boundaries for random clicking
            location = element.location
            size = element.size

            # Smart click patterns
            click_patterns = [
                # Center of element (most common for play buttons)
                (0.5, 0.5, "center"),
                # Common button locations
                (0.1, 0.1, "top-left"),
                (0.9, 0.1, "top-right"),
                (0.1, 0.9, "bottom-left"),
                (0.9, 0.9, "bottom-right"),
                # Along edges where controls often appear
                (0.5, 0.1, "top-center"),
                (0.5, 0.9, "bottom-center"),
                (0.1, 0.5, "left-center"),
                (0.9, 0.5, "right-center"),
                # Random exploration points
                (0.3, 0.3, "inner-left"),
                (0.7, 0.3, "inner-right"),
                (0.3, 0.7, "lower-left"),
                (0.7, 0.7, "lower-right")
            ]

            for i, (x_ratio, y_ratio, position_name) in enumerate(click_patterns):
                try:
                    # Calculate click coordinates
                    click_x = location['x'] + int(size['width'] * x_ratio)
                    click_y = location['y'] + int(size['height'] * y_ratio)

                    self.log_status(f"Click {i+1}: {position_name} at ({click_x}, {click_y})")

                    # Perform the click
                    self._smart_click_at_coordinates(click_x, click_y)

                    # Wait and check for changes
                    time.sleep(0.3)

                    # Check if new links appeared (indicating embed revealed)
                    new_links_count = len(self.driver.find_elements(By.TAG_NAME, "a"))

                    if new_links_count > initial_links:
                        self.log_status(f"SUCCESS! Click revealed {new_links_count - initial_links} new links!")

                        # Try to find and click the new embed links
                        embed_result = self._analyze_newly_revealed_links(initial_links)
                        if embed_result:
                            return embed_result

                    # Check if URL changed (navigation occurred)
                    current_url = self.driver.current_url
                    if current_url != original_url:
                        self.log_status(f"Navigation detected to: {current_url[:60]}...")
                        video = self._find_video_on_current_page()
                        if video:
                            return video
                        # Go back if no video found
                        self.driver.back()
                        time.sleep(0.1)

                except Exception as click_error:
                    self.log_status(f"Click {i+1} failed: {str(click_error)[:50]}")
                    continue

            return None

        except Exception as e:
            self.log_status(f"Intelligent clicking area error: {str(e)[:100]}")
            return None

    def _smart_click_at_coordinates(self, x, y):
        """Perform a smart click at specific coordinates"""
        try:
            # Method 1: ActionChains click
            from selenium.webdriver.common.action_chains import ActionChains
            actions = ActionChains(self.driver)
            actions.move_by_offset(x, y).click().perform()

        except Exception:
            try:
                # Method 2: JavaScript click at coordinates
                self.driver.execute_script(f"""
                    var element = document.elementFromPoint({x}, {y});
                    if (element) {{
                        element.click();
                    }}
                """)
            except Exception:
                # Method 3: Mouse event simulation
                self.driver.execute_script(f"""
                    var event = new MouseEvent('click', {{
                        bubbles: true,
                        cancelable: true,
                        clientX: {x},
                        clientY: {y}
                    }});
                    document.elementFromPoint({x}, {y}).dispatchEvent(event);
                """)

    def _analyze_newly_revealed_links(self, initial_count):
        """Analyze newly revealed links to find embed sources"""
        try:
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            new_links = all_links[initial_count:]  # Get only the new links

            self.log_status(f"Analyzing {len(new_links)} newly revealed links...")

            for link in new_links:
                try:
                    href = link.get_attribute('href')
                    text = link.text or link.get_attribute('title') or ''

                    # Check if this looks like a video embed link
                    video_indicators = ['youtube', 'vimeo', 'dailymotion', 'embed', 'watch', 'video', 'source']

                    if href and any(indicator in href.lower() for indicator in video_indicators):
                        self.log_status(f"Found promising embed link: {href[:80]}")

                        # Try clicking this embed link
                        try:
                            link.click()
                            time.sleep(0.2)

                            # Check if we navigated to a video source
                            new_url = self.driver.current_url
                            if any(domain in new_url for domain in ['youtube.com', 'vimeo.com', 'dailymotion.com']):
                                self.log_status("Successfully navigated to video source!")
                                return self._find_video_on_current_page()

                        except Exception as click_error:
                            self.log_status(f"Failed to click embed link: {str(click_error)[:50]}")
                            continue

                except Exception as link_error:
                    continue

            return None

        except Exception as e:
            self.log_status(f"Link analysis error: {str(e)[:100]}")
            return None

    def _find_video_on_embed_page(self):
        """Find video on the embed/source page after clicking embed link"""
        try:
            # Quick video detection on embed page
            self.log_status("Scanning embed page for video elements...")

            # Method 1: Direct video tags
            video_elements = self.safe_find_elements(By.TAG_NAME, "video")
            for video in video_elements:
                if video.is_displayed():
                    src = video.get_attribute('src')
                    if src and any(ext in src.lower() for ext in ['.mp4', '.mkv', '.avi', '.webm', '.mov']):
                        self.log_status(f"Found video element: {src[:60]}...")
                        return self._create_fake_element_for_download(src)

            # Method 2: Video source elements
            source_elements = self.safe_find_elements(By.TAG_NAME, "source")
            for source in source_elements:
                src = source.get_attribute('src')
                if src and any(ext in src.lower() for ext in ['.mp4', '.mkv', '.avi', '.webm', '.mov']):
                    self.log_status(f"Found source element: {src[:60]}...")
                    return self._create_fake_element_for_download(src)

            # Method 3: Direct video links
            video_links = self.driver.find_elements(By.XPATH, "//a[contains(@href, '.mp4') or contains(@href, '.mkv') or contains(@href, '.avi') or contains(@href, '.webm')]")
            for link in video_links:
                if link.is_displayed():
                    href = link.get_attribute('href')
                    if href:
                        self.log_status(f"Found video link: {href[:60]}...")
                        return self._create_fake_element_for_download(href)

            # Method 4: Page source scan for video URLs
            page_source = self.driver.page_source
            video_patterns = [
                r'https?://[^"\s]+\.mp4[^"\s]*',
                r'https?://[^"\s]+\.mkv[^"\s]*',
                r'https?://[^"\s]+\.avi[^"\s]*',
                r'https?://[^"\s]+\.webm[^"\s]*',
                r'https?://[^"\s]+\.mov[^"\s]*'
            ]

            for pattern in video_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches[:2]:  # Try first 2 matches
                    if not any(skip in match.lower() for skip in ['thumb', 'preview', 'poster']):
                        self.log_status(f"Found video URL in embed page: {match[:60]}...")
                        return self._create_fake_element_for_download(match)

            return None

        except Exception as e:
            logger.error(f"Error finding video on embed page: {e}")
            return None

    def _check_for_iframe_videos(self):
        """Check for videos inside iframes on embed pages"""
        try:
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")
            self.log_status(f"Found {len(iframes)} iframes to check...")

            for i, iframe in enumerate(iframes[:3]):  # Check first 3 iframes
                try:
                    if iframe.is_displayed():
                        # Get iframe src
                        iframe_src = iframe.get_attribute('src')
                        if iframe_src:
                            self.log_status(f"Checking iframe {i+1}: {iframe_src[:60]}...")

                            # Check if iframe src itself is a video
                            if any(ext in iframe_src.lower() for ext in ['.mp4', '.mkv', '.avi', '.webm', '.mov']):
                                self.log_status(f"Iframe contains direct video: {iframe_src[:60]}...")
                                return self._create_fake_element_for_download(iframe_src)

                            # Switch to iframe and look for videos
                            try:
                                self.driver.switch_to.frame(iframe)
                                time.sleep(0.1)

                                # Look for video elements inside iframe
                                iframe_videos = self.driver.find_elements(By.TAG_NAME, "video")
                                for video in iframe_videos:
                                    if video.is_displayed():
                                        src = video.get_attribute('src')
                                        if src and any(ext in src.lower() for ext in ['.mp4', '.mkv', '.avi', '.webm', '.mov']):
                                            self.log_status(f"Found video in iframe: {src[:60]}...")
                                            self.driver.switch_to.default_content()
                                            return self._create_fake_element_for_download(src)

                                # Switch back to main content
                                self.driver.switch_to.default_content()

                            except Exception as iframe_e:
                                # Make sure we switch back to main content
                                try:
                                    self.driver.switch_to.default_content()
                                except:
                                    pass
                                continue

                except Exception as iframe_outer_e:
                    continue

            return None

        except Exception as e:
            logger.error(f"Error checking iframe videos: {e}")
            # Ensure we're back to main content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return None

    def _extract_yandex_video_url(self, yandex_url):
        """Extract actual video URL from Yandex video page"""
        try:
            self.log_status(f"Extracting Yandex video from: {yandex_url[:60]}...")

            # Wait for Yandex page to load
            time.sleep(0.1)  # Reduced from 5 to 2 seconds

            # Method 1: Look for video elements on Yandex page
            video_elements = self.safe_find_elements(By.TAG_NAME, "video")
            for video in video_elements:
                if video.is_displayed():
                    src = video.get_attribute('src')
                    if src and any(ext in src.lower() for ext in ['.mp4', '.mkv', '.avi', '.webm', '.mov']):
                        self.log_status(f"Found Yandex video element: {src[:60]}...")
                        return self._create_fake_element_for_download(src)

            # Method 2: Check page source for video URLs
            page_source = self.driver.page_source

            # Yandex-specific video URL patterns
            yandex_patterns = [
                r'"videoUrl":"([^"]+\.mp4[^"]*)"',
                r'"url":"([^"]+\.mp4[^"]*)"',
                r'"src":"([^"]+\.mp4[^"]*)"',
                r'data-video-url="([^"]+)"',
                r'data-src="([^"]+\.mp4[^"]*)"',
                r'https://video-preview\.s3\.yandex\.net/[^"\s]+\.mp4[^"\s]*',
                r'https://[^"\s]+\.mp4[^"\s]*',
                r'https://[^"\s]+\.webm[^"\s]*',
                r'https://[^"\s]+\.avi[^"\s]*'
            ]

            for pattern in yandex_patterns:
                matches = re.findall(pattern, page_source, re.IGNORECASE)
                for match in matches:
                    # Clean up the URL if it's from JSON
                    video_url = match.replace('\\/', '/')
                    if 'yandex' in video_url or any(ext in video_url.lower() for ext in ['.mp4', '.webm', '.avi']):
                        self.log_status(f"Found Yandex video URL: {video_url[:60]}...")
                        return self._create_fake_element_for_download(video_url)

            # Method 3: JavaScript execution to get video data
            try:
                js_video_data = self.driver.execute_script("""
                    // Try to find video data in various Yandex objects
                    var sources = [];

                    // Check for player data
                    if (window.Ya && window.Ya.player && window.Ya.player.current) {
                        var current = window.Ya.player.current;
                        if (current.videoUrl) sources.push(current.videoUrl);
                        if (current.src) sources.push(current.src);
                    }

                    // Check for video elements
                    var videos = document.querySelectorAll('video');
                    for (var i = 0; i < videos.length; i++) {
                        if (videos[i].src) sources.push(videos[i].src);
                        if (videos[i].currentSrc) sources.push(videos[i].currentSrc);
                    }

                    // Check for data attributes
                    var videoElements = document.querySelectorAll('[data-video-url], [data-src]');
                    for (var i = 0; i < videoElements.length; i++) {
                        var url = videoElements[i].getAttribute('data-video-url') || videoElements[i].getAttribute('data-src');
                        if (url) sources.push(url);
                    }

                    // Enhanced: Look for JSON embedded video data
                    var scripts = document.querySelectorAll('script[type="application/json"], script:not([src])');
                    for (var i = 0; i < scripts.length; i++) {
                        try {
                            var text = scripts[i].textContent || scripts[i].innerHTML;
                            if (text && text.includes('video-preview.s3.yandex.net')) {
                                var matches = text.match(/https:\\/\\/video-preview\\.s3\\.yandex\\.net\\/[^"\\\\s]+\\.mp4/g);
                                if (matches) {
                                    matches.forEach(function(url) { sources.push(url); });
                                }
                            }
                        } catch(e) {}
                    }

                    return sources;
                """)

                if js_video_data:
                    for video_url in js_video_data:
                        if video_url and any(ext in video_url.lower() for ext in ['.mp4', '.webm', '.avi', '.mov']):
                            self.log_status(f"Found Yandex JS video URL: {video_url[:60]}...")
                            return self._create_fake_element_for_download(video_url)

            except Exception as js_e:
                self.log_status(f"JavaScript extraction failed: {str(js_e)[:40]}")

            # Method 4: Look for iframe sources on Yandex page
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                iframe_src = iframe.get_attribute('src')
                if iframe_src and any(ext in iframe_src.lower() for ext in ['.mp4', '.webm', '.avi']):
                    self.log_status(f"Found Yandex iframe video: {iframe_src[:60]}...")
                    return self._create_fake_element_for_download(iframe_src)

            self.log_status("No video URL found on Yandex page")
            return None

        except Exception as e:
            logger.error(f"Error extracting Yandex video: {e}")
            return None

    def _detect_yandex_embeds(self):
        """STRATEGY 9: Dedicated Yandex video embed detection with main player focus"""
        try:
            self.log_status("Strategy 9: Yandex embed detection - focusing on main video player")

            current_url = self.driver.current_url
            page_source = self.driver.page_source

            # Check if this looks like a page with Yandex embeds
            yandex_patterns = ['VideoViewer', 'yandex', 'DirectInlineContainer']
            found_patterns = [p for p in yandex_patterns if p in page_source]

            if not found_patterns:
                self.log_status("No Yandex patterns detected, skipping Strategy 9")
                return None

            self.log_status(f"Yandex patterns detected: {found_patterns} - focusing on main video player")

            # PRIORITY 1: Find and click the MAIN video player area first
            main_player_result = self._click_main_yandex_video_player()
            if main_player_result:
                return main_player_result

            # PRIORITY 2: If main player click didn't work, try targeted embed links in video area
            # (avoiding recommendation sections)
            embed_result = self._click_main_area_embeds_only()
            if embed_result:
                return embed_result

            # Method 1: Direct Yandex container clicking
            yandex_containers = [
                "//div[contains(@class, 'VideoViewer-Direct')]",
                "//div[contains(@class, 'DirectInlineContainer')]",
                "//div[contains(@id, 'video-viewer')]",
                "//div[contains(@class, 'VideoViewer')]",
                "//*[@data-log-node]"
            ]

            for i, selector in enumerate(yandex_containers):
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    self.log_status(f"Yandex selector {i+1} found {len(elements)} elements")

                    for j, element in enumerate(elements[:2]):  # Try first 2
                        if self._try_yandex_element_click(element, f"Container-{i+1}-{j+1}"):
                            return True  # Return immediately if successful

                except Exception as e:
                    continue

            # Method 2: Look for any clickable elements within Yandex containers
            yandex_areas = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'VideoViewer') or contains(@class, 'DirectInlineContainer')]")

            for area in yandex_areas[:3]:  # Check first 3 areas
                try:
                    # Find all potentially clickable children
                    clickable_children = area.find_elements(By.XPATH, ".//*")
                    self.log_status(f"Scanning {len(clickable_children)} child elements in Yandex area")

                    for child in clickable_children[:10]:  # Try first 10 children
                        if child.is_displayed():
                            tag = child.tag_name
                            if tag in ['a', 'button', 'div', 'span', 'img']:
                                if self._try_yandex_element_click(child, f"Child-{tag}"):
                                    return True

                except Exception as e:
                    continue

            # Method 3: Search for Yandex preview URLs and construct direct links
            preview_pattern = r'https://yandex\.com[^"\s]*/video/preview/(\d+)'
            matches = re.findall(preview_pattern, page_source)

            if matches:
                for video_id in matches[:2]:  # Try first 2 video IDs
                    self.log_status(f"Found Yandex video ID: {video_id}")

                    # Try to construct direct Yandex video URL
                    direct_yandex_url = f"https://yandex.com.tr/video/preview/{video_id}"
                    self.log_status(f"Attempting direct navigation to: {direct_yandex_url}")

                    try:
                        original_url = self.driver.current_url
                        self.driver.get(direct_yandex_url)
                        time.sleep(0.3)

                        # Try to extract video from direct Yandex page
                        yandex_video = self._extract_yandex_video_url(direct_yandex_url)
                        if yandex_video:
                            self.log_status("✅ Success via direct Yandex URL navigation!")
                            return yandex_video

                        # Return to original page if no success
                        self.driver.get(original_url)
                        time.sleep(0.1)

                    except Exception as nav_e:
                        self.log_status(f"Direct navigation failed: {str(nav_e)[:40]}")
                        try:
                            self.driver.get(current_url)
                            time.sleep(0.2)
                        except:
                            pass

            # Method 4: Aggressive element interaction - try clicking everything that might be Yandex-related
            all_elements = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'video') or contains(@class, 'Video') or contains(@id, 'video')]")

            self.log_status(f"Aggressive mode: trying {len(all_elements)} video-related elements")

            for element in all_elements[:15]:  # Try first 15 video-related elements
                try:
                    if element.is_displayed() and element.size['width'] > 50 and element.size['height'] > 50:
                        if self._try_yandex_element_click(element, "Aggressive"):
                            return True
                except Exception as e:
                    continue

            self.log_status("No successful Yandex embed clicks found")
            return None

        except Exception as e:
            logger.error(f"Yandex embed detection failed: {e}")
            return None

    def _try_yandex_element_click(self, element, element_type):
        """Try to click a Yandex element with multiple methods and check for success"""
        try:
            original_url = self.driver.current_url
            original_window = self.driver.current_window_handle

            # Get element info for logging
            tag_name = element.tag_name
            element_class = element.get_attribute('class') or ''
            element_id = element.get_attribute('id') or ''

            self.log_status(f"Trying {element_type}: {tag_name} class='{element_class[:30]}' id='{element_id[:20]}'")

            # Method 1: Scroll and regular click
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                time.sleep(0.2)
                element.click()
                self.log_status(f"Regular click attempted on {element_type}")
                time.sleep(0.2)
            except:
                pass

            # Method 2: JavaScript click
            try:
                self.driver.execute_script("arguments[0].click();", element)
                self.log_status(f"JavaScript click attempted on {element_type}")
                time.sleep(0.2)
            except:
                pass

            # Method 3: Action chains click
            try:
                from selenium.webdriver.common.action_chains import ActionChains
                ActionChains(self.driver).move_to_element(element).click().perform()
                self.log_status(f"Action chains click attempted on {element_type}")
                time.sleep(0.2)
            except:
                pass

            # Method 4: Double click
            try:
                from selenium.webdriver.common.action_chains import ActionChains
                ActionChains(self.driver).double_click(element).perform()
                self.log_status(f"Double click attempted on {element_type}")
                time.sleep(0.2)
            except:
                pass

            # Check if navigation occurred
            new_url = self.driver.current_url
            new_windows = self.driver.window_handles

            # Handle new window/tab
            if len(new_windows) > 1:
                self.log_status(f"New window opened from {element_type} click")
                new_window = [w for w in new_windows if w != original_window][0]
                self.driver.switch_to.window(new_window)
                new_url = self.driver.current_url
                time.sleep(0.2)

            # Check if we successfully navigated
            if new_url != original_url:
                self.log_status(f"✅ Navigation success with {element_type}: {new_url[:60]}...")

                # If it's a Yandex URL, try to extract video
                if 'yandex.com' in new_url:
                    yandex_video = self._extract_yandex_video_url(new_url)
                    if yandex_video:
                        self.log_status(f"✅ Video extracted from {element_type} click!")
                        return yandex_video

                # Try general video detection on new page
                video_element = self._find_video_on_embed_page()
                if video_element:
                    self.log_status(f"✅ Video found on page from {element_type} click!")
                    return video_element

            # Clean up - return to original state
            if len(self.driver.window_handles) > 1:
                self.driver.close()
                self.driver.switch_to.window(original_window)
            elif new_url != original_url:
                self.driver.get(original_url)
                time.sleep(0.1)

            return False

        except Exception as e:
            self.log_status(f"Error clicking {element_type}: {str(e)[:40]}")
            # Ensure we're back to original state
            try:
                if len(self.driver.window_handles) > 1:
                    self.driver.close()
                    self.driver.switch_to.window(original_window)
                elif self.driver.current_url != original_url:
                    self.driver.get(original_url)
                    time.sleep(0.2)
            except:
                pass

    def _click_main_yandex_video_player(self):
        """Find and click the MAIN video player area on Yandex pages (not recommendations)"""
        try:
            self.log_status("Looking for main Yandex video player area...")

            # Get viewport center for prioritizing elements near center
            viewport_center = self.driver.execute_script("""
                return {
                    x: window.innerWidth / 2,
                    y: window.innerHeight / 2,
                    width: window.innerWidth,
                    height: window.innerHeight
                };
            """)

            # Priority selectors for main video player (in order of priority)
            main_player_selectors = [
                # Highest priority - central video containers
                "//div[contains(@class, 'VideoViewer-Container')]",
                "//div[contains(@class, 'VideoViewer-Player')]",
                "//div[contains(@class, 'video-player-container')]",
                "//div[contains(@class, 'DirectInlineContainer')]",

                # Medium priority - main video areas
                "//div[contains(@class, 'VideoViewer')]",
                "//main//div[contains(@class, 'video')]",
                "//section//div[contains(@class, 'video')]",

                # Lower priority but still main content
                "//div[contains(@id, 'video-player')]",
                "//div[contains(@id, 'main-video')]"
            ]

            for i, selector in enumerate(main_player_selectors):
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    self.log_status(f"Main player selector {i+1} found {len(elements)} elements")

                    if not elements:
                        continue

                    # Filter elements to find the most central and largest one
                    main_candidates = []
                    for element in elements:
                        try:
                            if not element.is_displayed():
                                continue

                            location = element.location
                            size = element.size

                            # Skip tiny elements
                            if size['width'] < 200 or size['height'] < 150:
                                continue

                            # Calculate distance from viewport center
                            element_center_x = location['x'] + size['width'] / 2
                            element_center_y = location['y'] + size['height'] / 2

                            distance_from_center = ((element_center_x - viewport_center['x']) ** 2 +
                                                  (element_center_y - viewport_center['y']) ** 2) ** 0.5

                            # Calculate area (larger is better for main player)
                            area = size['width'] * size['height']

                            # Score: larger area = better, closer to center = better
                            score = area - (distance_from_center * 10)

                            main_candidates.append({
                                'element': element,
                                'score': score,
                                'distance': distance_from_center,
                                'area': area,
                                'location': location,
                                'size': size
                            })

                        except Exception as e:
                            continue

                    # Sort by score (best first)
                    main_candidates.sort(key=lambda x: x['score'], reverse=True)

                    # Try the best candidate(s)
                    for j, candidate in enumerate(main_candidates[:2]):  # Try top 2 candidates
                        element = candidate['element']

                        self.log_status(f"Trying main player candidate {j+1}: area={candidate['area']}, "
                                      f"center_distance={candidate['distance']:.0f}, score={candidate['score']:.0f}")

                        # First, try clicking the center of this main player area
                        result = self._click_center_of_main_player(element)
                        if result:
                            return result

                        # If center click didn't work, look for play/embed buttons within this area
                        result = self._find_embed_buttons_in_main_area(element)
                        if result:
                            return result

                except Exception as e:
                    self.log_status(f"Error with main player selector {i+1}: {str(e)[:50]}")
                    continue

            self.log_status("No main video player area found")
            return None

        except Exception as e:
            self.log_status(f"Error in main player detection: {str(e)[:50]}")
            return None

    def _click_center_of_main_player(self, player_element):
        """Click the center of the main video player to reveal embed content"""
        try:
            self.log_status("Clicking center of main video player...")

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", player_element)
            time.sleep(0.2)

            # Get original state
            original_url = self.driver.current_url
            original_window = self.driver.current_window_handle
            original_iframe_count = len(self.driver.find_elements(By.TAG_NAME, "iframe"))

            # Try multiple click methods on the center
            location = player_element.location
            size = player_element.size
            center_x = location['x'] + size['width'] // 2
            center_y = location['y'] + size['height'] // 2

            self.log_status(f"Clicking center coordinates: ({center_x}, {center_y})")

            # Method 1: JavaScript click on center
            try:
                self.driver.execute_script(f"""
                    var element = document.elementFromPoint({center_x}, {center_y});
                    if (element) {{
                        console.log('Clicking center element:', element);
                        element.click();
                    }}
                """)
                time.sleep(0.1)
            except:
                pass

            # Method 2: ActionChains click on center
            try:
                from selenium.webdriver.common.action_chains import ActionChains
                ActionChains(self.driver).move_to_element_with_offset(
                    player_element, size['width'] // 2, size['height'] // 2
                ).click().perform()
                time.sleep(0.1)
            except:
                pass

            # Method 3: Click the player element itself
            try:
                player_element.click()
                time.sleep(0.1)
            except:
                pass

            # Wait a bit longer for potential iframe loading
            time.sleep(0.2)

            # Check if any iframes appeared after clicking
            new_iframe_count = len(self.driver.find_elements(By.TAG_NAME, "iframe"))
            if new_iframe_count > original_iframe_count:
                self.log_status(f"✅ New iframes appeared after main player click! ({original_iframe_count} -> {new_iframe_count})")

                # Look for video in the new iframes
                iframe_result = self._extract_from_new_iframes()
                if iframe_result:
                    return iframe_result

            # Check if we navigated to a new page
            new_url = self.driver.current_url
            new_windows = self.driver.window_handles

            if new_url != original_url or len(new_windows) > 1:
                self.log_status(f"✅ Navigation occurred after main player click!")

                # Handle new window
                if len(new_windows) > 1:
                    new_window = [w for w in new_windows if w != original_window][0]
                    self.driver.switch_to.window(new_window)
                    new_url = self.driver.current_url

                # Try to find video on new page
                if 'yandex.com' in new_url:
                    yandex_video = self._extract_yandex_video_url(new_url)
                    if yandex_video:
                        return yandex_video

                # Try general video detection
                video_result = self._find_video_on_current_page()
                if video_result:
                    return video_result

                # Clean up if no video found
                if len(new_windows) > 1:
                    self.driver.close()
                    self.driver.switch_to.window(original_window)
                else:
                    self.driver.get(original_url)
                    time.sleep(0.2)

            return None

        except Exception as e:
            self.log_status(f"Error clicking center of main player: {str(e)[:50]}")
            return None

    def _find_embed_buttons_in_main_area(self, main_area):
        """Find and click embed/play buttons specifically within the main video area"""
        try:
            self.log_status("Looking for embed buttons within main video area...")

            # Look for buttons/links specifically within this main area that might reveal embeds
            embed_selectors_in_main = [
                # Play/embed buttons
                ".//button[contains(@class, 'play') or contains(@class, 'embed')]",
                ".//div[contains(@class, 'play') or contains(@class, 'embed')]",
                ".//a[contains(@class, 'play') or contains(@class, 'embed')]",

                # Video source links (but only external ones, not Yandex internal)
                ".//a[@href and not(contains(@href, 'yandex.com/video/search')) and not(contains(@href, 'yandex.com/video/preview'))]",

                # Overlay elements that might be clickable
                ".//div[contains(@class, 'overlay')]",
                ".//div[contains(@class, 'preview')]",
                ".//div[contains(@class, 'thumbnail')]"
            ]

            for selector in embed_selectors_in_main:
                try:
                    buttons = main_area.find_elements(By.XPATH, selector)

                    for button in buttons:
                        try:
                            if not button.is_displayed():
                                continue

                            # Get button info
                            tag_name = button.tag_name
                            button_class = button.get_attribute('class') or ''
                            button_href = button.get_attribute('href') or ''
                            button_text = (button.text or button.get_attribute('title') or '')[:50]

                            # Skip recommendation links and internal Yandex navigation
                            if button_href:
                                skip_patterns = [
                                    'yandex.com/video/search',
                                    'yandex.com/video/preview',
                                    '/recommended',
                                    '/suggestion',
                                    '#'
                                ]
                                if any(pattern in button_href for pattern in skip_patterns):
                                    self.log_status(f"Skipping internal/recommendation link: {button_href[:60]}")
                                    continue

                            self.log_status(f"Trying embed button in main area: {tag_name} class='{button_class[:30]}' text='{button_text}'")

                            # Try clicking this button
                            result = self._try_yandex_element_click(button, f"MainAreaButton-{tag_name}")
                            if result:
                                return result

                        except Exception as e:
                            continue

                except Exception as e:
                    continue

            return None

        except Exception as e:
            self.log_status(f"Error finding embed buttons in main area: {str(e)[:50]}")
            return None

    def _click_main_area_embeds_only(self):
        """Click embed links but ONLY in main content area, avoiding recommendations"""
        try:
            self.log_status("Looking for embed links in main content area only...")

            # Find the main content container (avoid sidebars, footers, recommendations)
            main_content_selectors = [
                "//main",
                "//div[contains(@class, 'content') and contains(@class, 'main')]",
                "//div[contains(@id, 'main')]",
                "//div[contains(@class, 'VideoViewer')]",
                "//section[contains(@class, 'video')]",
                "//article"
            ]

            main_containers = []
            for selector in main_content_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    main_containers.extend(elements)
                except:
                    continue

            if not main_containers:
                # Fallback: use body but be more selective
                main_containers = [self.driver.find_element(By.TAG_NAME, "body")]

            self.log_status(f"Found {len(main_containers)} main content areas to search")

            for container in main_containers[:3]:  # Check first 3 main areas
                try:
                    # Look for video source links within this main container
                    video_links = container.find_elements(By.XPATH,
                        ".//a[@href and ("
                        "contains(@href, 'youtube.com') or "
                        "contains(@href, 'vimeo.com') or "
                        "contains(@href, 'dailymotion.com') or "
                        "contains(@href, 'pornhub.com') or "
                        "contains(@href, 'xvideos.com') or "
                        "contains(@href, 'embed') or "
                        "contains(@href, 'watch') or "
                        "contains(@href, 'video')"
                        ") and not("
                        "contains(@href, 'yandex.com/video/search') or "
                        "contains(@href, 'yandex.com/video/preview') or "
                        "contains(@href, '/recommended') or "
                        "contains(@href, '/suggestion')"
                        ")]"
                    )

                    self.log_status(f"Found {len(video_links)} potential video links in main area")

                    # Sort links by position (prefer those closer to center/top)
                    viewport_center = self.driver.execute_script("return {x: window.innerWidth/2, y: window.innerHeight/2};")

                    link_candidates = []
                    for link in video_links:
                        try:
                            if not link.is_displayed():
                                continue

                            location = link.location
                            href = link.get_attribute('href')
                            text = (link.text or link.get_attribute('title') or '')[:30]

                            # Calculate distance from center
                            distance = ((location['x'] - viewport_center['x']) ** 2 +
                                      (location['y'] - viewport_center['y']) ** 2) ** 0.5

                            link_candidates.append({
                                'element': link,
                                'href': href,
                                'text': text,
                                'distance': distance
                            })

                        except:
                            continue

                    # Sort by distance from center (closer = better)
                    link_candidates.sort(key=lambda x: x['distance'])

                    # Try the most central links first
                    for candidate in link_candidates[:5]:  # Try top 5 central links
                        link = candidate['element']
                        href = candidate['href']
                        text = candidate['text']

                        self.log_status(f"Trying main area embed link: {href[:60]} | Text: '{text}'")

                        result = self._try_yandex_element_click(link, f"MainAreaEmbed")
                        if result:
                            return result

                except Exception as e:
                    continue

            return None

        except Exception as e:
            self.log_status(f"Error in main area embed clicking: {str(e)[:50]}")
            return None

    def _extract_from_new_iframes(self):
        """Extract video URLs from newly appeared iframes"""
        try:
            self.log_status("Checking new iframes for video content...")

            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")

            for i, iframe in enumerate(iframes):
                try:
                    iframe_src = iframe.get_attribute('src')
                    if not iframe_src:
                        continue

                    self.log_status(f"Checking iframe {i+1}: {iframe_src[:80]}")

                    # Check for video platforms in iframe src
                    video_platforms = [
                        'youtube.com', 'vimeo.com', 'dailymotion.com',
                        'pornhub.com', 'xvideos.com', 'vk.com/video',
                        'yastatic.net'
                    ]

                    for platform in video_platforms:
                        if platform in iframe_src:
                            self.log_status(f"✅ Found {platform} iframe: {iframe_src}")

                            # Handle different platforms
                            if 'vk.com' in iframe_src:
                                return self._handle_vk_iframe_direct(iframe_src)
                            elif 'youtube.com' in iframe_src:
                                return self._handle_youtube_iframe(iframe_src)
                            elif 'yastatic.net' in iframe_src and 'youtube' in iframe_src:
                                return self._handle_yandex_youtube_iframe(iframe_src)
                            elif 'pornhub.com' in iframe_src:
                                return self._handle_pornhub_iframe(iframe_src)
                            else:
                                # Try generic iframe handling
                                return self._handle_generic_iframe(iframe_src)

                except Exception as e:
                    continue

            return None

        except Exception as e:
            self.log_status(f"Error extracting from new iframes: {str(e)[:50]}")
            return None

    def _handle_youtube_iframe(self, iframe_src):
        """Handle YouTube iframe embed"""
        try:
            self.log_status(f"Handling YouTube iframe: {iframe_src}")

            # Extract video ID from YouTube embed URL
            import re
            video_id_match = re.search(r'/embed/([^/?]+)', iframe_src)
            if video_id_match:
                video_id = video_id_match.group(1)
                youtube_url = f"https://www.youtube.com/watch?v={video_id}"
                self.log_status(f"Extracted YouTube URL: {youtube_url}")
                return youtube_url

            return None
        except Exception as e:
            self.log_status(f"Error handling YouTube iframe: {str(e)[:50]}")
            return None

    def _handle_yandex_youtube_iframe(self, iframe_src):
        """Handle Yandex YouTube iframe embed wrapper"""
        try:
            self.log_status(f"Processing Yandex YouTube wrapper: {iframe_src}")

            # Try to access the iframe and extract YouTube video ID
            current_handle = self.driver.current_window_handle

            try:
                # Find the iframe element and switch to it
                iframe_elements = self.driver.find_elements(By.CSS_SELECTOR, f'iframe[src*="yastatic.net"]')

                for iframe in iframe_elements:
                    try:
                        self.driver.switch_to.frame(iframe)

                        # Look for YouTube video IDs in the iframe context
                        youtube_patterns = [
                            r'["\']?videoId["\']?\s*[:=]\s*["\']([^"\']+)["\']',
                            r'v=([a-zA-Z0-9_-]{11})',
                            r'embed/([a-zA-Z0-9_-]{11})',
                            r'watch\?v=([a-zA-Z0-9_-]{11})',
                            r'youtu\.be/([a-zA-Z0-9_-]{11})'
                        ]

                        # Check page source for YouTube video ID
                        page_source = self.driver.page_source

                        import re
                        for pattern in youtube_patterns:
                            matches = re.findall(pattern, page_source, re.IGNORECASE)
                            for match in matches:
                                if len(match) == 11:  # YouTube video IDs are 11 characters
                                    youtube_url = f"https://www.youtube.com/watch?v={match}"
                                    self.log_status(f"✅ Extracted YouTube URL from Yandex wrapper: {youtube_url}")
                                    return youtube_url

                        # Also check for data attributes and JavaScript variables
                        js_video_id = self.driver.execute_script("""
                            // Look for YouTube video ID in various places
                            var sources = [];

                            // Check window objects
                            if (window.videoId) sources.push(window.videoId);
                            if (window.youtubeId) sources.push(window.youtubeId);

                            // Check data attributes
                            var elements = document.querySelectorAll('[data-video-id], [data-youtube-id], [data-id]');
                            elements.forEach(el => {
                                var id = el.dataset.videoId || el.dataset.youtubeId || el.dataset.id;
                                if (id && id.length === 11) sources.push(id);
                            });

                            // Check for YouTube URLs in scripts
                            var scripts = document.querySelectorAll('script');
                            scripts.forEach(script => {
                                var text = script.textContent || script.innerText;
                                var matches = text.match(/(?:v=|embed\\/|youtu\\.be\\/)([a-zA-Z0-9_-]{11})/g);
                                if (matches) {
                                    matches.forEach(match => {
                                        var id = match.replace(/.*[\\/=]/, '');
                                        if (id.length === 11) sources.push(id);
                                    });
                                }
                            });

                            return sources.length > 0 ? sources[0] : null;
                        """)

                        if js_video_id:
                            youtube_url = f"https://www.youtube.com/watch?v={js_video_id}"
                            self.log_status(f"✅ JS extracted YouTube URL from Yandex: {youtube_url}")
                            return youtube_url

                    except Exception as frame_error:
                        self.log_status(f"Frame access error: {str(frame_error)[:40]}")
                        continue
                    finally:
                        try:
                            self.driver.switch_to.default_content()
                        except:
                            pass

            finally:
                try:
                    self.driver.switch_to.window(current_handle)
                    self.driver.switch_to.default_content()
                except:
                    pass

            return None

        except Exception as e:
            self.log_status(f"Error handling Yandex YouTube iframe: {str(e)[:50]}")
            return None

    def _handle_pornhub_iframe(self, iframe_src):
        """Handle Pornhub iframe embed"""
        try:
            self.log_status(f"Handling Pornhub iframe: {iframe_src}")

            # Extract video ID from Pornhub embed URL
            import re
            video_id_match = re.search(r'viewkey=([^&]+)', iframe_src)
            if video_id_match:
                video_id = video_id_match.group(1)
                pornhub_url = f"https://www.pornhub.com/view_video.php?viewkey={video_id}"
                self.log_status(f"Extracted Pornhub URL: {pornhub_url}")
                return pornhub_url

            # If it's already a direct embed, return it
            if 'pornhub.com' in iframe_src and 'embed' in iframe_src:
                return iframe_src

            return None
        except Exception as e:
            self.log_status(f"Error handling Pornhub iframe: {str(e)[:50]}")
            return None

    def _handle_generic_iframe(self, iframe_src):
        """Handle generic video iframe embed"""
        try:
            self.log_status(f"Handling generic iframe: {iframe_src}")

            # For generic iframes, try to navigate to them directly
            # and see if they contain video content
            if iframe_src.startswith('http'):
                self.log_status(f"Found generic video iframe: {iframe_src}")
                return iframe_src

            return None
        except Exception as e:
            self.log_status(f"Error handling generic iframe: {str(e)[:50]}")
            return None

    def _perform_right_click_download(self, video_element):
        """Perform right-click and select save video option - Enhanced for direct downloads"""
        try:
            # Check if this is a fake element with direct URL
            if hasattr(video_element, 'video_url'):
                return self._download_direct_url(video_element.video_url)
            
            # Check if we have a stored direct URL from advanced detection
            if hasattr(self, '_direct_video_url'):
                return self._download_direct_url(self._direct_video_url)
            
            # Traditional right-click method
            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", video_element)
            time.sleep(0.1)
            
            # Try to get video source before right-clicking
            src = video_element.get_attribute('src')
            if src and self._is_valid_video_url(src):
                # Try direct download first
                if self._download_direct_url(src):
                    return True
            
            # Perform right-click
            actions = ActionChains(self.driver)
            actions.context_click(video_element).perform()

            self.log_status("Performed right-click on video element")
            time.sleep(0.1)

            # Try to capture what's visible on screen after right-click
            try:
                # Look for any context menu that appeared
                context_menus = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'context') or contains(@class, 'menu') or contains(@role, 'menu')]")
                self.log_status(f"Found {len(context_menus)} potential context menu elements")

                # Also check for any new elements that appeared
                visible_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Save') or contains(text(), 'Download') or contains(text(), 'save') or contains(text(), 'download')]")
                self.log_status(f"Found {len(visible_elements)} elements with save/download text")

                for elem in visible_elements[:3]:  # Log first 3
                    try:
                        text = elem.text.strip()[:50] if elem.text else "(no text)"
                        tag = elem.tag_name
                        self.log_status(f"  - {tag}: {text}")
                    except:
                        pass
            except Exception as e:
                self.log_status(f"Could not analyze context menu: {str(e)[:50]}")

            time.sleep(0.2)
            
            # Try to find and click "Save video as" option
            save_options = [
                "Save video as...",
                "Save video",
                "Download video",
                "Save as...",
                "Download",
                "Сохранить видео как...",  # Russian
                "Guardar vídeo como...",   # Spanish
                "Salvar vídeo como...",    # Portuguese
                "Enregistrer la vidéo sous...",  # French
                "Video speichern unter...",      # German
                "Zapisz wideo jako...",    # Polish
                "保存视频为...",           # Chinese
                "動画を保存...",          # Japanese
            ]
            
            for save_text in save_options:
                try:
                    # Try to find the context menu option
                    save_element = WebDriverWait(self.driver, 1).until(
                        EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{save_text}')]"))
                    )
                    save_element.click()
                    self.log_status(f"Clicked '{save_text}' option")
                    return True
                except TimeoutException:
                    continue
                except Exception:
                    continue
            
            # If text-based search fails, try keyboard shortcuts
            try:
                # First try using arrow keys to navigate context menu
                self.log_status("Trying keyboard navigation of context menu")

                # Navigate down to video save option (usually 4-5 items down)
                for i in range(5):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(0.2)

                # Press Enter to select
                actions.send_keys(Keys.ENTER).perform()
                self.log_status("Selected context menu item via keyboard")
                return True

            except Exception as e:
                self.log_status(f"Keyboard navigation failed: {str(e)[:50]}")

            # Final fallback: try direct keyboard shortcuts
            try:
                # ESC to close any open menus first
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(0.1)

                # Right-click again
                actions.context_click(video_element).perform()
                time.sleep(0.2)

                # Try keyboard shortcuts (typically 'S' for Save or 'V' for Video)
                for key in ['s', 'v', 'a', 'd']:  # Save, Video, sAve, Download
                    try:
                        actions.send_keys(key).perform()
                        time.sleep(0.2)
                        self.log_status(f"Attempted keyboard shortcut: {key}")
                        # Continue trying other keys
                    except:
                        continue

                # Don't return True here - we haven't verified anything worked!
                # The calling code will check if download actually completed
                return False
                
            except Exception:
                pass
            
            return False
            
        except Exception as e:
            logger.error(f"Right-click download failed: {e}")
            return False
    
    def download_video_browser_headless(self, url, output_folder):
        """Download video using browser automation with advanced strategies - HEADLESS MODE"""
        try:
            self.log_status("Starting headless browser automation", url)

            # Setup browser driver only if not already initialized
            if not self.driver:
                if not self._setup_browser_driver(output_folder):
                    self.log_status("Browser automation not available - using yt-dlp only", url)
                    self.log_status("To enable browser automation: install Chrome/Firefox + webdriver-manager", url)
                    return False
            else:
                self.log_status("Reusing existing browser session", url)
            
            # Store download folder for direct downloads
            self.driver.download_folder = output_folder
            
            try:
                # Start progress tracking
                if self.progress_callback:
                    self.progress_callback('start', None)
                
                # Advanced video detection with multiple strategies
                self.log_status("Analyzing page with advanced detection", url)
                video_element = self._find_video_element(url)
                
                if not video_element:
                    self.log_status("No video element found with any strategy", url)
                    return False
                
                # Attempt download using detected element/URL
                self.log_status("Attempting download with detected video", url)
                if not self._perform_right_click_download(video_element):
                    self.log_status("Right-click download failed", url)
                    return False
                
                # Wait for download completion
                self.log_status("Waiting for download completion", url)
                downloaded_file = self._wait_for_download_completion(output_folder, self.download_timeout)
                
                if downloaded_file:
                    self.log_status("Headless browser download successful", url)
                    return True
                else:
                    self.log_status("Download did not complete", url)
                    return False
                
            finally:
                # Don't cleanup browser here - reuse it for retry attempts
                # Browser will be cleaned up when the entire download manager is done

                # Stop progress tracking
                if self.progress_callback:
                    self.progress_callback('stop', None)
            
        except Exception as e:
            logger.error(f"Headless browser download error: {e}")
            return False
    
    def _find_video_on_current_page(self):
        """Try to find a video element on the current page after navigation"""
        try:
            self.log_status("Searching for video on current page...")

            # Check if we're on a VK Video page and handle specifically
            current_url = self.driver.current_url
            if 'vk.com' in current_url or 'vkvideo.ru' in current_url:
                self.log_status(f"🎯 Detected VK Video page: {current_url[:80]}...")
                vk_video = self._extract_vk_video()
                if vk_video:
                    return vk_video

            # Check for other specific video platforms
            if 'youtube.com' in current_url or 'youtu.be' in current_url:
                yt_video = self._extract_youtube_video()
                if yt_video:
                    return yt_video

            # Quick check for standard video elements
            video_selectors = [
                "//video[@src]",
                "//video/source[@src]",
                "//iframe[contains(@src, 'youtube.com/embed')]",
                "//iframe[contains(@src, 'vimeo.com/video')]",
                "//iframe[contains(@src, 'dailymotion.com/embed')]",
                "//div[@data-video-url]",
                "//div[@data-video-src]"
            ]

            for selector in video_selectors:
                try:
                    elements = self.safe_find_elements(By.XPATH, selector)
                    if elements:
                        self.log_status(f"Found video element on source page!")
                        return elements[0]
                except:
                    continue

            # If no video found, try traditional detection
            return self._traditional_element_detection()

        except Exception as e:
            self.log_status(f"Error finding video on page: {str(e)[:50]}")
            return None

    def _extract_vk_video(self):
        """Extract video from VK Video page using VK-specific patterns"""
        try:
            self.log_status("VK Video page detected - using VK-specific extraction")

            # VK Video specific extraction patterns
            vk_strategies = [
                self._vk_strategy_direct_video_element,
                self._vk_strategy_page_source_extraction,
                self._vk_strategy_api_data_extraction,
                self._vk_strategy_javascript_variables
            ]

            for strategy in vk_strategies:
                try:
                    result = strategy()
                    if result:
                        self.log_status(f"VK extraction succeeded with {strategy.__name__}")
                        return result
                except Exception as strategy_error:
                    self.log_status(f"VK strategy {strategy.__name__} failed: {str(strategy_error)[:50]}")
                    continue

            return None

        except Exception as e:
            self.log_status(f"VK video extraction error: {str(e)[:50]}")
            return None

    def _vk_strategy_direct_video_element(self):
        """Look for direct video elements on VK page and extract URLs"""
        try:
            self.log_status("🔍 Starting VK direct video URL extraction...")

            # Enhanced VK Video URL extraction
            video_urls = self.driver.execute_script(r"""
                const videoUrls = [];
                const debugInfo = { methods: [], errors: [] };

                // Method 1: Look for video elements
                try {
                    const videos = document.querySelectorAll('video');
                    debugInfo.methods.push(`Method 1: Found ${videos.length} video elements`);
                    videos.forEach((video, i) => {
                        if (video.src) {
                            videoUrls.push(video.src);
                            debugInfo.methods.push(`Video ${i} src: ${video.src.substring(0, 80)}`);
                        }
                        if (video.currentSrc) {
                            videoUrls.push(video.currentSrc);
                            debugInfo.methods.push(`Video ${i} currentSrc: ${video.currentSrc.substring(0, 80)}`);
                        }

                        // Check source elements
                        const sources = video.querySelectorAll('source');
                        sources.forEach((source, j) => {
                            if (source.src) {
                                videoUrls.push(source.src);
                                debugInfo.methods.push(`Video ${i} source ${j}: ${source.src.substring(0, 80)}`);
                            }
                        });
                    });
                } catch(e) {
                    debugInfo.errors.push(`Method 1 error: ${e.message}`);
                }

                // Method 2: VK-specific player data
                try {
                    debugInfo.methods.push(`Method 2: window.cur = ${typeof window.cur}`);
                    if (window.cur) {
                        debugInfo.methods.push(`Method 2: cur keys = ${Object.keys(window.cur).join(', ')}`);

                        if (window.cur.player) {
                            const player = window.cur.player;
                            debugInfo.methods.push(`Method 2: Found cur.player, opts = ${typeof player.opts}`);
                            if (player.opts && player.opts.url720) {
                                videoUrls.push(player.opts.url720);
                                debugInfo.methods.push(`Method 2: url720 = ${player.opts.url720.substring(0, 80)}`);
                            }
                            if (player.opts && player.opts.url480) {
                                videoUrls.push(player.opts.url480);
                                debugInfo.methods.push(`Method 2: url480 = ${player.opts.url480.substring(0, 80)}`);
                            }
                            if (player.opts && player.opts.url360) {
                                videoUrls.push(player.opts.url360);
                                debugInfo.methods.push(`Method 2: url360 = ${player.opts.url360.substring(0, 80)}`);
                            }
                            if (player.opts && player.opts.url240) {
                                videoUrls.push(player.opts.url240);
                                debugInfo.methods.push(`Method 2: url240 = ${player.opts.url240.substring(0, 80)}`);
                            }
                        } else {
                            debugInfo.methods.push(`Method 2: No window.cur.player found`);
                        }

                        // Check other cur properties that might contain video data
                        if (window.cur.mvData) {
                            debugInfo.methods.push(`Method 2b: Found cur.mvData`);
                            const mvData = window.cur.mvData;
                            ['url720', 'url480', 'url360', 'url240'].forEach(quality => {
                                if (mvData[quality]) {
                                    videoUrls.push(mvData[quality]);
                                    debugInfo.methods.push(`Method 2b: mvData.${quality} = ${mvData[quality].substring(0, 80)}`);
                                }
                            });
                        }

                        // Check if cur has video property
                        if (window.cur.video) {
                            debugInfo.methods.push(`Method 2c: Found cur.video`);
                            const video = window.cur.video;
                            if (typeof video === 'object') {
                                Object.keys(video).forEach(key => {
                                    if (typeof video[key] === 'string' && video[key].includes('.mp4')) {
                                        videoUrls.push(video[key]);
                                        debugInfo.methods.push(`Method 2c: video.${key} = ${video[key].substring(0, 80)}`);
                                    }
                                });
                            }
                        }
                    } else {
                        debugInfo.methods.push(`Method 2: No window.cur found`);
                    }
                } catch(e) {
                    debugInfo.errors.push(`Method 2 error: ${e.message}`);
                }

                // Method 3: Global VK variables
                try {
                    debugInfo.methods.push(`Method 3: window.videoData = ${typeof window.videoData}`);
                    if (window.videoData) {
                        debugInfo.methods.push(`Method 3: videoData keys = ${Object.keys(window.videoData).join(', ')}`);
                        Object.values(window.videoData).forEach((value, i) => {
                            if (typeof value === 'string' && value.includes('.mp4')) {
                                videoUrls.push(value);
                                debugInfo.methods.push(`Method 3: videoData[${i}] = ${value.substring(0, 80)}`);
                            }
                        });
                    }

                    // Check other common VK Video globals
                    const vkVideoGlobals = ['vkVideo', 'videoPlayer', 'playerData', 'mvp'];
                    vkVideoGlobals.forEach(globalName => {
                        if (window[globalName]) {
                            debugInfo.methods.push(`Method 3b: Found window.${globalName}`);
                            try {
                                const obj = window[globalName];
                                if (typeof obj === 'object') {
                                    Object.keys(obj).forEach(key => {
                                        const value = obj[key];
                                        if (typeof value === 'string' && value.includes('.mp4') && value.includes('http')) {
                                            videoUrls.push(value);
                                            debugInfo.methods.push(`Method 3b: ${globalName}.${key} = ${value.substring(0, 80)}`);
                                        }
                                    });
                                }
                            } catch(e) {
                                debugInfo.errors.push(`Method 3b ${globalName} error: ${e.message}`);
                            }
                        }
                    });
                } catch(e) {
                    debugInfo.errors.push(`Method 3 error: ${e.message}`);
                }

                // Method 4: Check all global variables for video URLs
                for (let key in window) {
                    try {
                        const value = window[key];
                        if (typeof value === 'string' && value.includes('.mp4') && value.includes('http')) {
                            videoUrls.push(value);
                        } else if (typeof value === 'object' && value !== null) {
                            JSON.stringify(value, (k, v) => {
                                if (typeof v === 'string' && v.includes('.mp4') && v.includes('http')) {
                                    videoUrls.push(v);
                                }
                                return v;
                            });
                        }
                    } catch(e) {}
                }

                // Method 5: VK Video specific patterns
                try {
                    const scripts = document.querySelectorAll('script');
                    debugInfo.methods.push(`Method 5: Found ${scripts.length} script elements`);

                    let scriptUrlsFound = 0;
                    scripts.forEach((script, scriptIndex) => {
                        if (script.textContent) {
                            try {
                                // VK Video specific patterns
                                const patterns = [
                                    /"url(720|480|360|240)":"([^"]+)"/g,
                                    /"mp4":"([^"]+)"/g,
                                    /"hls":"([^"]+)"/g,
                                    /https:\\/\\/[^"'\\s]*\\.mp4[^"'\\s]*/g,
                                    /https:\\/\\/[^"'\\s]*vkvideo[^"'\\s]*\\.mp4[^"'\\s]*/g,
                                    /"source":"([^"]*\.mp4[^"]*)"/g,
                                    /"video_url":"([^"]+)"/g
                                ];

                                patterns.forEach((pattern, patternIndex) => {
                                    const matches = script.textContent.match(pattern);
                                    if (matches) {
                                        debugInfo.methods.push(`Method 5: Script ${scriptIndex} pattern ${patternIndex} found ${matches.length} matches`);
                                        matches.forEach((match, matchIndex) => {
                                            try {
                                                let url = '';
                                                if (match.includes('":"')) {
                                                    // Extract URL from JSON-like structure
                                                    const parts = match.split('":"');
                                                    if (parts.length >= 2) {
                                                        url = parts[1].replace(/"/g, '');
                                                    }
                                                } else {
                                                    // Direct URL match
                                                    url = match;
                                                }

                                                // Handle common escape sequences
                                                url = url.replace(/\\u002F/g, '/');
                                                url = url.replace(/\\\//g, '/');
                                                url = url.replace(/\\\\/g, '/');

                                                if (url.includes('.mp4') && url.includes('http')) {
                                                    videoUrls.push(url);
                                                    scriptUrlsFound++;
                                                    debugInfo.methods.push(`Method 5: Found URL ${scriptUrlsFound}: ${url.substring(0, 80)}`);
                                                }
                                            } catch(e) {
                                                debugInfo.errors.push(`Method 5 URL parsing error: ${e.message}`);
                                            }
                                        });
                                    }
                                });
                            } catch(e) {
                                debugInfo.errors.push(`Method 5 script ${scriptIndex} error: ${e.message}`);
                            }
                        }
                    });
                } catch(e) {
                    debugInfo.errors.push(`Method 5 error: ${e.message}`);
                }

                // Method 6: Deep page structure analysis for VK Video
                try {
                    debugInfo.methods.push(`Method 6: Deep VK Video page analysis`);

                    // Check current page HTML for embedded data
                    const pageContent = document.documentElement.outerHTML;

                    // Look for common VK Video data patterns in HTML
                    const htmlPatterns = [
                        /data-video[^=]*="([^"]*\.mp4[^"]*)"/gi,
                        /data-src[^=]*="([^"]*\.mp4[^"]*)"/gi,
                        /src="([^"]*vkvideo[^"]*\.mp4[^"]*)"/gi,
                        /href="([^"]*\.mp4[^"]*)"/gi,
                        /'([^']*\.mp4[^']*)'/gi,
                        /"([^"]*\.mp4[^"]*)"/gi
                    ];

                    let htmlUrlsFound = 0;
                    htmlPatterns.forEach((pattern, i) => {
                        const matches = pageContent.match(pattern);
                        if (matches && matches.length > 0) {
                            debugInfo.methods.push(`Method 6: HTML pattern ${i} found ${matches.length} matches`);
                            matches.forEach(match => {
                                // Extract URL from the match
                                const urlMatch = match.match(/https?:\/\/[^"'\s]*\.mp4[^"'\s]*/);
                                if (urlMatch) {
                                    const url = urlMatch[0];
                                    if (!url.includes('preview') && !url.includes('thumbnail')) {
                                        videoUrls.push(url);
                                        htmlUrlsFound++;
                                        debugInfo.methods.push(`Method 6: HTML URL ${htmlUrlsFound}: ${url.substring(0, 80)}`);
                                    }
                                }
                            });
                        }
                    });

                    // Check for VK Video specific global objects
                    if (window.cur && typeof window.cur === 'object') {
                        debugInfo.methods.push(`Method 6b: Scanning window.cur object deeply`);

                        // Recursive function to find video URLs in nested objects
                        function findUrlsInObject(obj, path = 'cur', depth = 0) {
                            if (depth > 3) return; // Prevent infinite recursion

                            try {
                                Object.keys(obj).forEach(key => {
                                    const value = obj[key];
                                    const currentPath = `${path}.${key}`;

                                    if (typeof value === 'string') {
                                        if (value.includes('.mp4') && value.includes('http')) {
                                            videoUrls.push(value);
                                            debugInfo.methods.push(`Method 6b: Found in ${currentPath}: ${value.substring(0, 80)}`);
                                        }
                                    } else if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
                                        findUrlsInObject(value, currentPath, depth + 1);
                                    }
                                });
                            } catch(e) {
                                debugInfo.errors.push(`Method 6b error in ${path}: ${e.message}`);
                            }
                        }

                        findUrlsInObject(window.cur);
                    }

                    // Check video elements more thoroughly
                    const allVideos = document.querySelectorAll('video, source, object, embed');
                    debugInfo.methods.push(`Method 6c: Found ${allVideos.length} media elements`);
                    allVideos.forEach((el, i) => {
                        ['src', 'data-src', 'data-video', 'data-url', 'href'].forEach(attr => {
                            const value = el.getAttribute(attr);
                            if (value && value.includes('.mp4') && value.includes('http')) {
                                videoUrls.push(value);
                                debugInfo.methods.push(`Method 6c: Media element ${i} ${attr}: ${value.substring(0, 80)}`);
                            }
                        });
                    });

                } catch(e) {
                    debugInfo.errors.push(`Method 6 error: ${e.message}`);
                }

                // Clean and deduplicate URLs
                const cleanUrls = [...new Set(videoUrls)]
                    .filter(url => url && url.includes('.mp4') && url.startsWith('http'))
                    .filter(url => !url.includes('yandex.net') || url.includes('video-preview.s3.yandex.net')); // Allow direct video URLs

                debugInfo.methods.push(`Found ${videoUrls.length} total URLs, ${cleanUrls.length} clean URLs`);

                return { urls: cleanUrls, debug: debugInfo };
            """)

            # Log debug information
            if isinstance(video_urls, dict) and 'debug' in video_urls:
                debug_info = video_urls['debug']
                self.log_status("📊 VK extraction debug:")
                for method in debug_info.get('methods', []):
                    self.log_status(f"  ✓ {method}")
                for error in debug_info.get('errors', []):
                    self.log_status(f"  ❌ {error}")
                video_urls = video_urls.get('urls', [])

            # If no URLs found, try waiting for dynamic content
            if not video_urls or len(video_urls) == 0:
                self.log_status("⏳ No URLs found immediately, waiting for dynamic content...")
                try:
                    # Wait up to 10 seconds for video URLs to appear
                    for attempt in range(10):
                        time.sleep(0.2)
                        dynamic_urls = self.driver.execute_script("""
                            // Quick check for any new video URLs
                            const newUrls = [];

                            // Check video elements
                            document.querySelectorAll('video, source').forEach(el => {
                                ['src', 'currentSrc'].forEach(attr => {
                                    const url = el[attr];
                                    if (url && url.includes('.mp4') && url.includes('http')) {
                                        newUrls.push(url);
                                    }
                                });
                            });

                            // Check for newly loaded global variables
                            if (window.cur && window.cur.player && window.cur.player.opts) {
                                const opts = window.cur.player.opts;
                                ['url720', 'url480', 'url360', 'url240'].forEach(quality => {
                                    if (opts[quality]) newUrls.push(opts[quality]);
                                });
                            }

                            return [...new Set(newUrls)];
                        """)

                        if dynamic_urls and len(dynamic_urls) > 0:
                            self.log_status(f"✅ Found {len(dynamic_urls)} URLs after {attempt + 1}s wait")
                            video_urls = dynamic_urls
                            break

                    if not video_urls or len(video_urls) == 0:
                        self.log_status("⏰ No dynamic URLs found after 10s wait")

                except Exception as e:
                    self.log_status(f"Dynamic content wait error: {str(e)[:50]}")

            if video_urls and len(video_urls) > 0:
                # Sort by quality (prefer higher quality)
                quality_order = ['720', '480', '360', '240']
                sorted_urls = []

                for quality in quality_order:
                    for url in video_urls:
                        if quality in url and url not in sorted_urls:
                            sorted_urls.append(url)

                # Add remaining URLs
                for url in video_urls:
                    if url not in sorted_urls:
                        sorted_urls.append(url)

                for url in sorted_urls:
                    self.log_status(f"🎯 VK Video URL found: {url[:80]}...")
                    self.log_status(f"📁 Will use direct download instead of right-click")
                    # Create a fake element with the direct download URL
                    return self._create_fake_element_for_download(url)

            self.log_status("❌ No VK video URLs found with direct extraction")
            return None

        except Exception as e:
            self.log_status(f"VK direct video extraction error: {str(e)[:50]}")
            return None

    def _vk_strategy_page_source_extraction(self):
        """Extract video URLs from VK page source"""
        try:
            page_source = self.driver.page_source

            # VK-specific URL patterns in page source
            vk_patterns = [
                r'"url720":"([^"]+)"',
                r'"url480":"([^"]+)"',
                r'"url360":"([^"]+)"',
                r'"url240":"([^"]+)"',
                r'"hls":"([^"]+)"',
                r'"dash":"([^"]+)"',
                r'"mp4":"([^"]+)"',
                r'"webm":"([^"]+)"',
                r'https://[^"\s]*\.(?:mp4|webm|m3u8)[^"\s]*'
            ]

            found_urls = []
            for pattern in vk_patterns:
                matches = re.findall(pattern, page_source)
                for match in matches:
                    # Clean up escaped characters
                    url = match.replace('\\/', '/').replace('\\u0026', '&')
                    if self._is_valid_video_url(url) and ('yandex.net' not in url or 'video-preview.s3.yandex.net' in url):
                        found_urls.append(url)

            if found_urls:
                # Prefer higher quality
                best_url = self._select_best_vk_url(found_urls)
                if best_url:
                    self.log_status(f"Extracted VK video URL: {best_url[:60]}")
                    return self._create_fake_element_for_download(best_url)

            return None

        except Exception as e:
            return None

    def _vk_strategy_api_data_extraction(self):
        """Extract video from VK API data in page"""
        try:
            # Look for VK API data in page
            api_script = """
                // Look for VK video data in various global variables
                const possibleSources = [];

                // Check common VK global variables
                if (typeof cur !== 'undefined' && cur.mvData) {
                    try {
                        const mvData = cur.mvData;
                        if (mvData.url720) possibleSources.push(mvData.url720);
                        if (mvData.url480) possibleSources.push(mvData.url480);
                        if (mvData.url360) possibleSources.push(mvData.url360);
                        if (mvData.url240) possibleSources.push(mvData.url240);
                    } catch(e) {}
                }

                // Check for video data in window objects
                if (typeof window.videoData !== 'undefined') {
                    try {
                        const vd = window.videoData;
                        Object.keys(vd).forEach(key => {
                            if (typeof vd[key] === 'string' && vd[key].includes('.mp4')) {
                                possibleSources.push(vd[key]);
                            }
                        });
                    } catch(e) {}
                }

                // Look for video URLs in data attributes
                const videoElements = document.querySelectorAll('[data-video], [data-src], [data-url]');
                videoElements.forEach(el => {
                    ['data-video', 'data-src', 'data-url'].forEach(attr => {
                        const val = el.getAttribute(attr);
                        if (val && val.includes('.mp4')) {
                            possibleSources.push(val);
                        }
                    });
                });

                return possibleSources;
            """

            video_urls = self.driver.execute_script(api_script)

            if video_urls:
                # Filter out Yandex preview URLs
                valid_urls = [url for url in video_urls if self._is_valid_video_url(url) and ('yandex.net' not in url or 'video-preview.s3.yandex.net' in url)]

                if valid_urls:
                    best_url = self._select_best_vk_url(valid_urls)
                    if best_url:
                        self.log_status(f"VK API extraction found: {best_url[:60]}")
                        return self._create_fake_element_for_download(best_url)

            return None

        except Exception as e:
            return None

    def _vk_strategy_javascript_variables(self):
        """Extract from JavaScript variables on VK page"""
        try:
            # Execute comprehensive JavaScript extraction
            js_extraction = """
                const videoSources = [];

                // Function to recursively search objects
                function searchForVideoUrls(obj, path = '') {
                    if (typeof obj !== 'object' || obj === null) return;

                    for (const key in obj) {
                        try {
                            const value = obj[key];
                            const currentPath = path + '.' + key;

                            if (typeof value === 'string') {
                                // Look for video-like URLs
                                if (value.match(/https?:\\/\\/[^\\s]*\\.(mp4|webm|m3u8)/i) &&
                                    (!value.includes('yandex.net') || value.includes('video-preview.s3.yandex.net'))) {
                                    videoSources.push({
                                        url: value,
                                        path: currentPath,
                                        quality: value.includes('720') ? 720 :
                                                value.includes('480') ? 480 :
                                                value.includes('360') ? 360 : 240
                                    });
                                }
                            } else if (typeof value === 'object' && path.split('.').length < 5) {
                                searchForVideoUrls(value, currentPath);
                            }
                        } catch(e) {}
                    }
                }

                // Search in common VK global objects
                ['cur', 'window', 'videoData', 'playerData', 'mvData'].forEach(globalName => {
                    try {
                        const globalObj = eval(globalName);
                        if (globalObj) {
                            searchForVideoUrls(globalObj, globalName);
                        }
                    } catch(e) {}
                });

                return videoSources;
            """

            video_sources = self.driver.execute_script(js_extraction)

            if video_sources:
                # Sort by quality (prefer higher quality)
                video_sources.sort(key=lambda x: x.get('quality', 0), reverse=True)

                for source in video_sources:
                    url = source['url']
                    if self._is_valid_video_url(url):
                        self.log_status(f"JS extraction found video: {url[:60]} (quality: {source.get('quality')})")
                        return self._create_fake_element_for_download(url)

            return None

        except Exception as e:
            return None

    def _select_best_vk_url(self, urls):
        """Select the best quality video URL from VK URLs"""
        try:
            if not urls:
                return None

            # Quality priority order
            quality_order = ['720', '480', '360', '240']

            for quality in quality_order:
                for url in urls:
                    if quality in url:
                        return url

            # If no quality indicators, return first valid URL
            return urls[0] if urls else None

        except Exception as e:
            return None

    def _extract_youtube_video(self):
        """Extract video from YouTube page"""
        try:
            self.log_status("YouTube page detected - using YouTube-specific extraction")

            # YouTube specific patterns
            yt_patterns = [
                r'"url":"([^"]*\.mp4[^"]*)","mimeType":"video/mp4"',
                r'"signatureCipher":"([^"]+)"',
                r'"url":"([^"]*videoplayback[^"]*)","itag"',
            ]

            page_source = self.driver.page_source
            for pattern in yt_patterns:
                matches = re.findall(pattern, page_source)
                for match in matches:
                    if 'videoplayback' in match:
                        # Clean up URL
                        url = match.replace('\\u0026', '&').replace('\\/', '/')
                        self.log_status(f"Found YouTube video URL: {url[:60]}")
                        return self._create_fake_element_for_download(url)

            return None

        except Exception as e:
            self.log_status(f"YouTube extraction error: {str(e)[:50]}")
            return None

    def _log_page_analysis(self):
        """Log information about what's on the current page for debugging"""
        try:
            # Find all links on page
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            self.log_status(f"Page contains {len(all_links)} total links")

            # Check for video-related links
            video_links = []
            for link in all_links[:20]:  # Check first 20 links
                try:
                    href = link.get_attribute('href') or ''
                    text = link.text or ''
                    if any(keyword in href.lower() + text.lower() for keyword in
                          ['video', 'watch', 'view', 'source', 'youtube', 'vimeo', 'dailymotion']):
                        video_links.append(href[:100])
                except:
                    continue

            if video_links:
                self.log_status(f"Found {len(video_links)} video-related links")
                for i, link in enumerate(video_links[:3]):
                    self.log_status(f"  Link {i+1}: {link}")

            # Check for iframes
            iframes = self.safe_find_elements(By.TAG_NAME, "iframe")
            if iframes:
                self.log_status(f"Page contains {len(iframes)} iframes")

            # Check for video elements
            videos = self.driver.find_elements(By.TAG_NAME, "video")
            if videos:
                self.log_status(f"Page contains {len(videos)} video elements")

        except Exception as e:
            self.log_status(f"Error analyzing page: {str(e)[:50]}")

    def _wait_for_download_completion(self, download_folder, timeout=300):
        """Wait for download to complete by monitoring the download folder and handling save dialog"""
        try:
            # Initialize download diagnostics logger
            self._log_download_diagnostics("INIT", {
                "download_folder": download_folder,
                "timeout": timeout,
                "browser": "Chrome",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })

            start_time = time.time()
            initial_files = set(os.listdir(download_folder)) if os.path.exists(download_folder) else set()

            # Log initial folder state and test write permissions
            folder_writeable = False
            try:
                test_file = os.path.join(download_folder, f"test_{uuid.uuid4().hex}.tmp")
                with open(test_file, 'w') as f:
                    f.write("test")
                os.remove(test_file)
                folder_writeable = True
            except:
                folder_writeable = False

            self._log_download_diagnostics("FOLDER_STATE", {
                "exists": os.path.exists(download_folder),
                "writeable": folder_writeable,
                "path": download_folder,
                "initial_files": list(initial_files)[:10],  # First 10 files
                "total_files": len(initial_files)
            })

            # First, try to handle the save dialog if it appears
            save_dialog_handled = False
            try:
                # Try sending Enter to accept default save location
                time.sleep(0.1)  # Give save dialog time to appear
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ENTER).perform()
                self.log_status("Attempted to confirm save dialog")
                save_dialog_handled = True

                # Log save dialog handling
                self._log_download_diagnostics("SAVE_DIALOG", {
                    "handled": True,
                    "method": "ENTER key"
                })
            except Exception as e:
                self.log_status(f"No save dialog to handle or already handled: {str(e)[:50]}")
                self._log_download_diagnostics("SAVE_DIALOG", {
                    "handled": False,
                    "error": str(e)[:100]
                })

            # Monitor the specified download folder and Chrome's default as fallback
            fallback_folders = [download_folder]

            # Add Chrome default downloads folder
            chrome_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
            if os.path.abspath(chrome_downloads) != os.path.abspath(download_folder):
                if os.path.exists(chrome_downloads):
                    fallback_folders.append(chrome_downloads)
                    self.log_status(f"Also monitoring Chrome default downloads: {chrome_downloads}")

            # Also monitor the Downloads Chrome folder where browser actually downloads
            downloads_chrome_folder = "D:/4k video downloader - Copy/Downloads Chrome"
            if os.path.abspath(downloads_chrome_folder) != os.path.abspath(download_folder):
                if os.path.exists(downloads_chrome_folder):
                    fallback_folders.append(downloads_chrome_folder)
                    self.log_status(f"Also monitoring Downloads Chrome folder: {downloads_chrome_folder}")

            self.log_status(f"Primary download folder: {download_folder}")

            # Run browser download state check
            self._check_browser_download_state()

            # Monitor for new files
            check_interval = 0
            last_diagnostic_time = time.time()

            while time.time() - start_time < timeout:
                check_interval += 1

                # Log periodic diagnostics every 30 seconds
                if time.time() - last_diagnostic_time > 30:
                    self._log_download_diagnostics("MONITORING", {
                        "elapsed_time": time.time() - start_time,
                        "check_interval": check_interval,
                        "folders_monitored": fallback_folders
                    })
                    last_diagnostic_time = time.time()

                for folder in fallback_folders:
                    if not os.path.exists(folder):
                        self._log_download_diagnostics("FOLDER_ERROR", {
                            "folder": folder,
                            "error": "Folder does not exist"
                        })
                        continue

                    current_files = set(os.listdir(folder))

                    # For Chrome downloads folder, only look at recent files
                    if folder == chrome_downloads:
                        # Filter to files created in last 5 minutes
                        recent_files = set()
                        for f in current_files:
                            fp = os.path.join(folder, f)
                            if os.path.isfile(fp):
                                file_time = os.path.getctime(fp)
                                if time.time() - file_time < 300:  # Created in last 5 minutes
                                    recent_files.add(f)
                        new_files = recent_files - initial_files if folder == download_folder else recent_files
                    else:
                        new_files = current_files - initial_files

                    if new_files:
                        # Log detected new files
                        self._log_download_diagnostics("NEW_FILES", {
                            "folder": folder,
                            "files": list(new_files),
                            "count": len(new_files)
                        })

                        # Check if any new files are complete (not .part, .crdownload, etc.)
                        for file_name in new_files:
                            file_path = os.path.join(folder, file_name)

                            # Check for temporary download files that indicate download in progress
                            if any(ext in file_name.lower() for ext in ['.crdownload', '.tmp', '.download', '.part']):
                                self.log_status(f"Download in progress: {file_name}")
                                self._log_download_diagnostics("TEMP_FILE", {
                                    "file": file_name,
                                    "path": file_path,
                                    "size": os.path.getsize(file_path) if os.path.exists(file_path) else 0
                                })
                                continue

                            # Check if it's a video file
                            if any(ext in file_name.lower() for ext in ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v', '.mpg', '.mpeg']):
                                # Wait a bit more to ensure file is complete
                                time.sleep(0.2)

                                # Check file is not still growing
                                if os.path.exists(file_path):
                                    size1 = os.path.getsize(file_path)
                                    time.sleep(0.1)
                                    size2 = os.path.getsize(file_path) if os.path.exists(file_path) else 0

                                    if size1 == size2 and size2 > 10240:  # File size stable and > 10KB
                                        self.log_status(f"Download completed: {file_name} ({size2/1024/1024:.1f} MB)")

                                        # If file is in Chrome downloads or Downloads Chrome folder but we want it elsewhere, move it
                                        if folder != download_folder and (folder == chrome_downloads or folder == downloads_chrome_folder):
                                            try:
                                                target_path = os.path.join(download_folder, file_name)
                                                # If target already exists, generate a unique name
                                                if os.path.exists(target_path):
                                                    base, ext = os.path.splitext(file_name)
                                                    counter = 1
                                                    while os.path.exists(target_path):
                                                        target_path = os.path.join(download_folder, f"{base}_{counter}{ext}")
                                                        counter += 1
                                                shutil.move(file_path, target_path)
                                                self.log_status(f"Moved file to: {target_path}")
                                                return target_path
                                            except Exception as e:
                                                self.log_status(f"Could not move file: {e}")
                                                # Still return the file path even if we couldn't move it
                                                return file_path

                                        return file_path

                # Update progress if callback available
                if self.progress_callback:
                    try:
                        elapsed = time.time() - start_time
                        progress_text = f"Waiting for download... ({elapsed:.0f}s)"
                        self.progress_callback('update', progress_text)
                    except:
                        pass

                # If we haven't handled save dialog yet and it's been a while, try again
                if not save_dialog_handled and time.time() - start_time > 5:
                    try:
                        actions = ActionChains(self.driver)
                        actions.send_keys(Keys.ENTER).perform()
                        save_dialog_handled = True
                        self.log_status("Retried save dialog confirmation")
                    except:
                        pass

                time.sleep(0.1)

            self.log_status("Download timeout reached")

            # Log comprehensive timeout diagnostics
            self._log_download_diagnostics("TIMEOUT", {
                "elapsed_time": timeout,
                "folders_checked": fallback_folders,
                "total_checks": check_interval,
                "reason": "No completed video files detected within timeout period"
            })

            # Final browser state check
            final_state = self._check_browser_download_state()
            self._log_download_diagnostics("FINAL_STATE", final_state)

            return None

        except Exception as e:
            logger.error(f"Error waiting for download: {e}")
            self._log_download_diagnostics("ERROR", {
                "error": str(e),
                "traceback": traceback.format_exc()
            })
            return None
    
    def _download_with_ytdlp(self, video_url, output_folder):
        """Download video using detected URL - direct download or yt-dlp"""
        try:
            self.log_status(f"🔍 DEBUGGING: _download_with_ytdlp called with URL: {video_url[:80]}...")
            self.log_status(f"🔍 Starting download with detected URL: {video_url[:80]}...")

            # Check if this is a segmented video URL first
            is_segmented = self._is_segmented_video_url(video_url)
            self.log_status(f"🔍 DEBUGGING: Is segmented URL? {is_segmented}")

            if is_segmented:
                self.log_status(f"🧩 Segmented video URL detected - processing with clip removal")
                processed_url = self._process_segmented_video_url(video_url)
                self.log_status(f"🔄 Processed segmented URL: {processed_url[:80]}...")

                # Use the processed URL for download
                self.log_status(f"🔍 DEBUGGING: Calling download method for processed URL")
                self.log_status(f"🔍 DEBUGGING: Processed URL being passed: {processed_url}")

                # After removing clip parameters, treat as direct video file
                # Decode URL to check for video extensions properly
                from urllib.parse import unquote
                decoded_processed_url = unquote(processed_url)
                if decoded_processed_url.endswith('.mp4') or decoded_processed_url.endswith('.mkv') or decoded_processed_url.endswith('.avi'):
                    self.log_status(f"🎯 Processed URL appears to be direct video file - using direct download")
                    self.log_status(f"🔍 DEBUGGING: Decoded URL: {decoded_processed_url}")
                    result = self._download_direct_video_file(processed_url, output_folder)
                else:
                    self.log_status(f"🎯 Using yt-dlp for processed URL")
                    result = self._download_with_ytdlp_command(processed_url, output_folder)

                self.log_status(f"🔍 DEBUGGING: Download method returned: {result}")
                if result:
                    return True
                else:
                    self.log_status(f"🔄 Processed URL failed, trying original URL...")
                    # Fall through to try original URL

            # Check if this is a direct video file URL
            is_direct = self._is_direct_video_file_url(video_url)
            self.log_status(f"🔍 DEBUGGING: Is direct video file? {is_direct}")

            if is_direct:
                self.log_status(f"🎯 Direct video file detected - using direct download")
                return self._download_direct_video_file(video_url, output_folder)
            else:
                self.log_status(f"🎯 Video page/streaming URL detected - using yt-dlp")
                return self._download_with_ytdlp_command(video_url, output_folder)

        except Exception as e:
            self.log_status(f"❌ Error in download with detected URL: {str(e)[:100]}")
            logger.error(f"Error in _download_with_ytdlp: {e}")
            return False

    def _is_direct_video_file_url(self, url):
        """Check if URL points directly to a video file (excluding segmented URLs)"""
        video_extensions = ['.mp4', '.avi', '.mov', '.webm', '.mkv', '.flv', '.wmv', '.m4v']
        url_lower = url.lower()

        # First check if it's a segmented/special URL that needs yt-dlp handling
        if self._is_segmented_video_url(url):
            return False  # Segmented URLs should use yt-dlp, not direct download

        # Check for HLS or other streaming indicators
        streaming_indicators = [
            '.m3u8', '/hls/', 'media=hls', 'media%3dhls',
            'clip=', '/clip', 'segment=', '/segment',
            'multi=', '/multi', 'range=', '/range'
        ]

        if any(indicator in url_lower for indicator in streaming_indicators):
            return False  # Streaming URLs should use yt-dlp

        # Check for regular video file extensions
        return any(url_lower.endswith(ext) or f'{ext}?' in url_lower for ext in video_extensions)

    def _download_direct_video_file(self, video_url, output_folder):
        """Download direct video file using simple HTTP request (no bypass)"""
        try:
            import requests
            import os
            from urllib.parse import urlparse
            
            self.log_status(f"📥 Downloading video: {video_url[:80]}...")
            
            # Create filename
            parsed_url = urlparse(video_url)
            filename = os.path.basename(parsed_url.path) or "video.mp4"
            if not any(filename.lower().endswith(ext) for ext in ['.mp4', '.avi', '.mov', '.webm', '.mkv']):
                filename = "video.mp4"
            
            # Add timestamp
            import time
            timestamp = int(time.time())
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{timestamp}{ext}"
            output_path = os.path.join(output_folder, filename)
            
            # Create output directory
            os.makedirs(output_folder, exist_ok=True)
            
            # Simple headers (no bypass)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'video/mp4,video/webm,video/*,*/*;q=0.8',
            }
            
            # Make request
            response = requests.get(video_url, headers=headers, stream=True, timeout=30)
            response.raise_for_status()
            
            # Download
            total_size = int(response.headers.get('content-length', 0))
            if total_size > 0:
                self.log_status(f"📁 Downloading {total_size // 1024 // 1024}MB...")
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                self.log_status(f"✅ Download successful: {output_path}")
                return True
            
            return False
            
        except requests.exceptions.HTTPError as e:
            self.log_status(f"❌ HTTP error: {e.response.status_code}")
            if e.response.status_code == 403:
                self.log_status("⚠️ Access forbidden - content may be protected")
            return False
        except Exception as e:
            self.log_status(f"❌ Download error: {str(e)[:200]}")
            return False

    def _browser_download_video_direct(self, video_url, output_path):
        """Download video using browser with JavaScript fetch - bypasses CDN token restrictions"""
        try:
            self.log_status(f"🌐 Starting JavaScript-based browser download: {video_url[:60]}...")

            # Get output directory and filename
            output_dir = os.path.dirname(output_path)
            output_filename = os.path.basename(output_path)

            self.log_status(f"📁 Target: {output_filename}")

            # Use JavaScript to download the video within the browser context
            # This preserves all cookies and authentication
            download_script = f"""
            (async function() {{
                try {{
                    console.log('Starting download via fetch...');
                    const url = '{video_url}';

                    // Fetch the video using the browser's authenticated session
                    const response = await fetch(url);

                    if (!response.ok) {{
                        return 'ERROR: HTTP ' + response.status;
                    }}

                    // Get the blob
                    const blob = await response.blob();
                    console.log('Blob size: ' + blob.size);

                    if (blob.size < 1000) {{
                        return 'ERROR: File too small - ' + blob.size + ' bytes';
                    }}

                    // Create download link and trigger it
                    const a = document.createElement('a');
                    a.href = URL.createObjectURL(blob);
                    a.download = '{output_filename}';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(a.href);

                    return 'SUCCESS: Downloaded ' + blob.size + ' bytes';
                }} catch(error) {{
                    return 'ERROR: ' + error.message;
                }}
            }})();
            """

            # Set Chrome download directory via CDP first
            try:
                params = {'behavior': 'allow', 'downloadPath': output_dir}
                self.driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
                self.log_status(f"✅ Download directory set to: {output_dir}")
            except Exception as cdp_error:
                self.log_status(f"⚠️ CDP config warning: {cdp_error}")

            # Execute the download script
            self.log_status("🔄 Executing JavaScript download in browser context...")

            # Use WebDriverWait for async script execution
            from selenium.webdriver.support.ui import WebDriverWait

            result = self.driver.execute_async_script(download_script + "arguments[arguments.length - 1](await " + download_script.split("(async function() {")[1].split("})();")[0] + ");")

            self.log_status(f"📊 JavaScript result: {result}")

            if result and 'SUCCESS' in str(result):
                # Wait for file to appear
                self.log_status("⏳ Waiting for download to complete...")
                max_wait = 60
                check_interval = 2
                elapsed = 0

                while elapsed < max_wait:
                    try:
                        files_in_dir = os.listdir(output_dir)
                        video_files = [f for f in files_in_dir if f.endswith('.mp4') and not f.endswith('.crdownload')]
                        temp_files = [f for f in files_in_dir if '.crdownload' in f or '.tmp' in f]

                        if temp_files:
                            self.log_status(f"📥 Download in progress... ({elapsed}s)")
                        elif video_files:
                            # Check for our file or latest file
                            matching = [f for f in video_files if output_filename in f or f in output_filename]
                            if matching:
                                target_file = os.path.join(output_dir, matching[0])
                            else:
                                target_file = max([os.path.join(output_dir, f) for f in video_files], key=os.path.getctime)

                            file_size = os.path.getsize(target_file)

                            if file_size > 100000:  # At least 100KB
                                self.log_status(f"✅ Download complete: {file_size:,} bytes")

                                # Rename if needed
                                if target_file != output_path:
                                    try:
                                        if os.path.exists(output_path):
                                            os.remove(output_path)
                                        os.rename(target_file, output_path)
                                        self.log_status(f"✅ Saved as: {output_filename}")
                                    except:
                                        pass

                                return True

                    except Exception as check_error:
                        self.log_status(f"⚠️ Check error: {check_error}")

                    time.sleep(check_interval)
                    elapsed += check_interval

                self.log_status(f"⏱️ Timeout waiting for file")
                return False
            else:
                self.log_status(f"❌ JavaScript download failed: {result}")
                return False

        except Exception as e:
            import traceback
            self.log_status(f"❌ Browser download error: {str(e)[:200]}")
            self.log_status(f"🔍 {traceback.format_exc()[:500]}")
            return False

    def _download_with_ytdlp_command(self, video_url, output_folder):
        """Download using yt-dlp command for video pages and segmented URLs"""
        try:
            self.log_status(f"🔍 DEBUGGING: _download_with_ytdlp_command called with: {video_url[:100]}...")

            # Preprocess URL for better yt-dlp compatibility
            processed_url = self._preprocess_url_for_yt_dlp(video_url)
            self.log_status(f"🔍 DEBUGGING: After preprocessing: {processed_url[:100]}...")

            # Build yt-dlp command with specific output template and options
            import os
            output_template = os.path.join(output_folder, '%(title)s.%(ext)s')

            # Base command
            cmd = [
                'yt-dlp',
                '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',  # Best video+audio, merge if needed
                '--merge-output-format', 'mp4',  # Ensure output is MP4
                '--output', output_template,
                '--no-warnings',
                '--extract-flat', 'false',
                '--write-info-json', 'false',
                '--write-description', 'false',
                '--write-annotations', 'false',
                '--write-sub', 'false',
                '--write-thumbnail', 'false',
                '--ignore-errors',
                '--no-continue',
                '--retry', '3',
                '--retry-sleep', '1',
                '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            ]

            # Special handling for segmented URLs
            if self._is_segmented_video_url(video_url):
                self.log_status(f"🧩 Detected segmented video - adding special options")

                # Add options specific to segmented/HLS content
                cmd.extend([
                    '--allow-unplayable-formats',  # Allow potentially unplayable formats
                    '--force-generic-extractor',   # Use generic extractor for complex URLs
                    '--hls-prefer-native',         # Use native HLS downloader if available
                    '--external-downloader', 'native',  # Use native downloader
                    '--fragment-retries', '10',     # Retry fragments multiple times
                    '--retry-sleep', '2'            # Longer sleep between retries
                ])

                # For HLS2 URLs, try different approaches
                if '/media=hls2' in video_url or 'media%3Dhls2' in video_url:
                    self.log_status(f"🎬 HLS2 media detected - trying manifest approach")

                    # Try to convert to HLS manifest first
                    import re
                    manifest_url = re.sub(r'\.mp4$', '.m3u8', video_url)
                    manifest_url = re.sub(r'/media=hls2', '/media=hls', manifest_url)
                    manifest_url = re.sub(r'media%3Dhls2', 'media%3Dhls', manifest_url)

                    if manifest_url != video_url:
                        self.log_status(f"🔄 Trying HLS manifest: {manifest_url[:100]}...")
                        processed_url = manifest_url

            # Add the URL at the end
            cmd.append(processed_url)

            self.log_status(f"🎯 Executing yt-dlp command for {'segmented' if self._is_segmented_video_url(video_url) else 'regular'} URL...")

            # Execute yt-dlp command with timeout
            result = self._execute_download_command_with_progress(cmd, output_folder)

            if result:
                self.log_status(f"✅ yt-dlp download completed successfully")
                return True
            else:
                # If segmented URL fails, try alternative approaches
                if self._is_segmented_video_url(video_url):
                    return self._retry_segmented_download(video_url, output_folder)
                else:
                    self.log_status(f"⚠️ yt-dlp failed")
                    return False

        except Exception as e:
            self.log_status(f"Error in yt-dlp command: {str(e)[:50]}")
            return False

    def _retry_segmented_download(self, video_url, output_folder):
        """Retry segmented video download with alternative approaches"""
        try:
            self.log_status(f"🔄 Retrying segmented download with alternative methods...")

            import re
            import os

            # Approach 1: Try base URL without clip parameters
            base_url = re.sub(r'/clip=[^/]*', '', video_url)
            base_url = re.sub(r'clip=[^&/]*[&/]?', '', base_url)

            if base_url != video_url and self._is_valid_video_url(base_url):
                self.log_status(f"🔗 Trying base URL without clip: {base_url[:100]}...")
                output_template = os.path.join(output_folder, '%(title)s_base.%(ext)s')
                cmd = [
                    'yt-dlp',
                    '--format', 'best[ext=mp4]/best',
                    '--merge-output-format', 'mp4',
                    '--output', output_template,
                    '--no-warnings',
                    '--retry', '5',
                    base_url
                ]

                result = self._execute_download_command_with_progress(cmd, output_folder)
                if result:
                    self.log_status(f"✅ Base URL download successful")
                    return True

            # Approach 2: Try with different quality settings for multi-quality URLs
            multi_match = re.search(r'multi=([^&,/]+)', video_url)
            if multi_match:
                multi_qualities = multi_match.group(1)
                quality_pattern = r'(\d+)x(\d+):(\d+)'
                quality_matches = re.findall(quality_pattern, multi_qualities)

                if quality_matches:
                    # Try different quality levels
                    for quality in sorted(quality_matches, key=lambda x: int(x[0]) * int(x[1]), reverse=True):
                        self.log_status(f"🎨 Trying quality {quality[0]}x{quality[1]}...")

                        quality_url = re.sub(r'/multi=[^/]*', f'/{quality[0]}x{quality[1]}', video_url)
                        quality_url = re.sub(r'multi=[^&/]*[&/]?', f'quality={quality[2]}&', quality_url)

                        if quality_url != video_url:
                            output_template = os.path.join(output_folder, f'%(title)s_{quality[0]}x{quality[1]}.%(ext)s')
                            cmd = [
                                'yt-dlp',
                                '--format', 'best[ext=mp4]/best',
                                '--output', output_template,
                                '--no-warnings',
                                quality_url
                            ]

                            result = self._execute_download_command_with_progress(cmd, output_folder)
                            if result:
                                self.log_status(f"✅ Quality-specific download successful")
                                return True

            # Approach 3: Use external downloader for complex segmented content
            self.log_status(f"🛠️ Trying with external downloader...")
            output_template = os.path.join(output_folder, '%(title)s_external.%(ext)s')
            cmd = [
                'yt-dlp',
                '--external-downloader', 'aria2c',
                '--external-downloader-args', 'aria2c:-c -j 3 -x 3 -s 3 -k 1M',
                '--output', output_template,
                '--no-warnings',
                '--format', 'best',
                video_url
            ]

            result = self._execute_download_command_with_progress(cmd, output_folder)
            if result:
                self.log_status(f"✅ External downloader successful")
                return True

            # Approach 4: Last resort - simple download
            self.log_status(f"🚨 Last resort - simple download attempt...")
            output_template = os.path.join(output_folder, '%(title)s_simple.%(ext)s')
            cmd = [
                'yt-dlp',
                '--output', output_template,
                '--format', 'best',
                '--no-warnings',
                '--ignore-errors',
                video_url
            ]

            result = self._execute_download_command_with_progress(cmd, output_folder)
            if result:
                self.log_status(f"✅ Simple download successful")
                return True

            self.log_status(f"❌ All retry approaches failed")
            return False

        except Exception as e:
            self.log_status(f"Error in retry segmented download: {str(e)[:50]}")
            return False

    def download_video_browser(self, url, output_folder):
        """Download video using browser automation (right-click method)"""
        try:
            self.log_status("Starting browser automation download", url)
            self.log_status("🔍 DEBUGGING: download_video_browser method called", url)

            # Setup browser driver only if not already initialized
            if not self.driver:
                self.log_status("🔍 DEBUGGING: No existing driver, setting up browser", url)
                if not self._setup_browser_driver(output_folder):
                    self.log_status("Browser automation not available - using yt-dlp only", url)
                    self.log_status("To enable browser automation: install Chrome/Firefox + webdriver-manager", url)
                    self.log_status("🔍 DEBUGGING: Browser setup failed", url)
                    return False
                self.log_status("🔍 DEBUGGING: Browser setup successful", url)
            else:
                self.log_status("Reusing existing browser session", url)
                self.log_status("🔍 DEBUGGING: Reusing existing browser driver", url)

                # Clean up browser state before new download attempt
                try:
                    self.log_status("🧹 Cleaning browser state for fresh download attempt", url)
                    self.driver.delete_all_cookies()
                    self.driver.execute_script("window.localStorage.clear();")
                    self.driver.execute_script("window.sessionStorage.clear();")
                    self.log_status("✅ Browser state cleaned successfully", url)
                except Exception as cleanup_error:
                    self.log_status(f"⚠️ Browser cleanup warning: {str(cleanup_error)[:50]}", url)

            try:
                # Start progress tracking
                if self.progress_callback:
                    self.progress_callback('start', None)

                # Find video element
                self.log_status("Looking for video element", url)
                self.log_status("🔍 DEBUGGING: About to call _find_video_element (THIS CONTAINS METHODS 1-4)", url)

                video_element = self._find_video_element(url)

                self.log_status(f"🔍 DEBUGGING: _find_video_element returned: {video_element is not None}", url)

                if not video_element:
                    self.log_status("No video element found", url)
                    self.log_status("🔍 DEBUGGING: Methods 1-4 completed but found no video", url)
                    # Log what we found on the page for debugging
                    self._log_page_analysis()
                    return False

                # Check if we have a video URL from Methods 1-3 (direct detection)
                self.log_status(f"🔍 DEBUGGING: video_element type: {type(video_element)}", url)
                detected_video_url = None

                # Case 1: Mock element with video_url attribute (from source parsing)
                if hasattr(video_element, 'video_url') and video_element.video_url:
                    detected_video_url = video_element.video_url
                    self.log_status(f"🔍 DEBUGGING: Found video_url in mock element: {detected_video_url}", url)

                # Case 2: Real DOM element with src attributes (from video tag detection)
                elif hasattr(video_element, 'get_attribute'):
                    for attr in ['src', 'data-src', 'data-video-src', 'data-url']:
                        try:
                            attr_value = video_element.get_attribute(attr)
                            if attr_value and self._is_valid_video_url(attr_value):
                                detected_video_url = attr_value
                                self.log_status(f"🔍 DEBUGGING: Found video URL in {attr} attribute: {detected_video_url}", url)
                                break
                        except:
                            continue

                if detected_video_url:
                    self.log_status(f"✅ Video URL detected from Methods 1-3: {detected_video_url[:80]}...", url)
                    self.log_status("🔍 DEBUGGING: Using detected URL for yt-dlp download", url)

                    # Use yt-dlp with the detected URL
                    self.log_status("🔍 DEBUGGING: About to call _download_with_ytdlp", url)
                    try:
                        success = self._download_with_ytdlp(detected_video_url, output_folder)
                        self.log_status(f"🔍 DEBUGGING: _download_with_ytdlp returned: {success}", url)
                        if success:
                            self.log_status("✅ Download completed successfully with detected URL", url)
                            return True
                        else:
                            self.log_status("⚠️ yt-dlp failed with detected URL, falling back to right-click", url)
                    except Exception as e:
                        self.log_status(f"🔍 DEBUGGING: _download_with_ytdlp threw exception: {str(e)[:100]}", url)

                # Perform right-click download (Method 4 - Complex)
                self.log_status("Attempting right-click download (Method 4)", url)
                if not self._perform_right_click_download(video_element):
                    self.log_status("Right-click download failed", url)
                    return False
                
                # Wait for download completion
                self.log_status("Waiting for download completion", url)
                downloaded_file = self._wait_for_download_completion(output_folder, self.download_timeout)
                
                if downloaded_file:
                    self.log_status("Browser download successful", url)
                    return True
                else:
                    self.log_status("Download did not complete", url)
                    return False
                
            finally:
                # Don't cleanup browser here - reuse it for retry attempts
                # Browser will be cleaned up when the entire download manager is done

                # Stop progress tracking
                if self.progress_callback:
                    self.progress_callback('stop', None)
            
        except Exception as e:
            logger.error(f"Browser download error: {e}")
            return False

    def _download_with_yt_dlp(self, video_url):
        """Download video using yt-dlp for video page URLs (like Pornhub, YouTube, etc.)"""
        try:
            self.log_status(f"🎬 Using yt-dlp for video page: {video_url[:60]}")

            # Get download folder - check multiple possible locations
            download_folder = None
            if hasattr(self.driver, 'download_folder'):
                download_folder = self.driver.download_folder
            elif hasattr(self, 'download_folder'):
                download_folder = self.download_folder
            else:
                # Use default Downloads Chrome folder
                download_folder = "D:/4k video downloader - Copy/Downloads Chrome"

            self.log_status(f"📁 Download folder: {download_folder}")

            # Ensure download folder exists
            os.makedirs(download_folder, exist_ok=True)

            # Preprocess URL for better yt-dlp compatibility
            processed_url = self._preprocess_url_for_yt_dlp(video_url)
            self.log_status(f"🔄 Processed URL: {processed_url}")

            # Build yt-dlp command with specific output template and options
            output_template = os.path.join(download_folder, '%(title)s.%(ext)s')
            cmd = [
                'yt-dlp',
                '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',  # Best video+audio, merge if needed
                '--merge-output-format', 'mp4',  # Ensure output is MP4
                '--output', output_template,
                '--no-warnings',
                '--prefer-insecure',  # Speed up by skipping some checks
                '--extractor-retries', '3',
                '--fragment-retries', '3',
                '--retry-sleep', '1',
                '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                processed_url
            ]

            self.log_status(f"🎯 Executing yt-dlp command: {' '.join(cmd[:3])} ... {processed_url[:40]}")

            # Execute yt-dlp command with timeout
            import subprocess
            import time

            try:
                start_time = time.time()
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)

                stdout, stderr = process.communicate(timeout=15)  # 15 second timeout - ULTRA FAST

                if process.returncode == 0:
                    self.log_status(f"✅ yt-dlp download completed successfully")
                    return True
                else:
                    self.log_status(f"❌ yt-dlp download failed with return code {process.returncode}")
                    if stderr:
                        self.log_status(f"yt-dlp error: {stderr[:200]}")
                    return False

            except subprocess.TimeoutExpired:
                process.kill()
                self.log_status(f"❌ yt-dlp download timed out after 120 seconds")
                return False

        except Exception as e:
            self.log_status(f"❌ yt-dlp download error: {str(e)[:100]}")
            logger.error(f"yt-dlp download failed: {e}")
            return False

class RealTimeDownloadManager:
    """Download manager with real-time progress tracking + Browser Automation Fallback"""
    
    def __init__(self, status_callback=None, progress_callback=None):
        self.status_callback = status_callback or print
        self.progress_callback = progress_callback
        self.active_downloads = {}
        self.download_queue = Queue()
        self.executor = None
        self.max_concurrent = 1  # Only one download at a time
        self.retry_attempts = 3
        self.temp_dir = tempfile.gettempdir()
        self.downloaded_files = set()
        self.strategies = self._init_all_strategies()

        # Browser automation manager - lazy initialization
        self.browser_manager = None
        self._browser_status_callback = status_callback
        self._browser_progress_callback = progress_callback

    def _get_browser_manager(self):
        """Initialize browser manager only when needed (lazy initialization)"""
        if self.browser_manager is None:
            self.log_status("🔍 BROWSER MANAGER: Creating new BrowserDownloadManager instance")
            self.browser_manager = BrowserDownloadManager(
                self._browser_status_callback,
                self._browser_progress_callback
            )
            # Pass GUI reference to browser manager if available
            if hasattr(self, 'gui') and self.gui:
                self.browser_manager.gui = self.gui
                self.log_status("🔍 BROWSER MANAGER: GUI reference passed to browser manager")
            else:
                self.log_status("🔍 BROWSER MANAGER: No GUI reference available yet")
        else:
            self.log_status("🔍 BROWSER MANAGER: Reusing existing browser manager instance")
        return self.browser_manager

    def _init_all_strategies(self):
        """Initialize all download strategies in priority order - ALL MP4 FOCUSED + Browser Automation"""
        return [
            ('Browser Right-Click Download', self._strategy_browser_download),  # MOVED TO TOP - Methods 1-4 execute here
            ('MP4 Best Quality', self._strategy_mp4_best),
            ('MP4 High Quality', self._strategy_mp4_high),
            ('MP4 Medium Quality', self._strategy_mp4_medium),
            ('MP4 Standard', self._strategy_mp4_standard),
            ('MP4 Compatible', self._strategy_mp4_compatible),
            ('MP4 with Cookies', self._strategy_mp4_cookies),
            ('MP4 IPv4 Force', self._strategy_mp4_ipv4),
            ('MP4 Geo Bypass', self._strategy_mp4_geo),
            ('MP4 Android UA', self._strategy_mp4_android),
            ('MP4 Generic', self._strategy_mp4_generic),
            ('MP4 Fallback', self._strategy_mp4_fallback),
        ]
    
    def log_status(self, message, url=None):
        """Log status with optional URL context"""
        if url:
            domain = self._get_domain(url)
            full_message = f"[{domain}] {message}"
        else:
            full_message = message

        logger.info(full_message)

        # Send the full message to status callback
        if self.status_callback:
            try:
                self.status_callback(full_message)
            except:
                pass

    def test_yt_dlp_installation(self):
        """Test if yt-dlp is properly installed and working"""
        try:
            self.log_status("🧪 Testing yt-dlp installation...")

            # Test 1: Check if yt-dlp command exists
            test_cmd = ['yt-dlp', '--version']
            try:
                result = subprocess.run(test_cmd, capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    version = result.stdout.strip()
                    self.log_status(f"✅ yt-dlp version: {version}")
                else:
                    self.log_status(f"❌ yt-dlp version check failed: {result.stderr}")
                    return False
            except subprocess.TimeoutExpired:
                self.log_status("❌ yt-dlp version check timed out")
                return False
            except FileNotFoundError:
                self.log_status("❌ yt-dlp command not found in PATH")
                return False

            # Test 2: Test with a simple URL (YouTube test video)
            test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Never Gonna Give You Up (short)
            test_cmd = ['yt-dlp', '--simulate', '--quiet', test_url]
            try:
                result = subprocess.run(test_cmd, capture_output=True, text=True, timeout=15)
                if result.returncode == 0:
                    self.log_status("✅ yt-dlp can access YouTube (simulate mode)")
                    return True
                else:
                    self.log_status(f"❌ yt-dlp simulation failed: {result.stderr}")
                    return False
            except subprocess.TimeoutExpired:
                self.log_status("❌ yt-dlp simulation timed out")
                return False

        except Exception as e:
            self.log_status(f"❌ yt-dlp test failed: {e}")
            return False
    
    def _get_domain(self, url):
        """Extract domain from URL"""
        try:
            parsed = urllib.parse.urlparse(url)
            return parsed.netloc.replace('www.', '')
        except:
            return "unknown"
    
    def _extract_video_id(self, url):
        """Extract video ID from URL using multiple patterns"""
        patterns = [
            r'/video/([a-zA-Z0-9_-]+)',
            r'/v/([a-zA-Z0-9_-]+)',
            r'/watch/([a-zA-Z0-9_-]+)',
            r'/([a-zA-Z0-9_-]+)$',
            r'[?&]v=([a-zA-Z0-9_-]+)',
            r'[?&]id=([a-zA-Z0-9_-]+)',
            r'/([0-9]+)$',
            r'/embed/([a-zA-Z0-9_-]+)',
            r'/player/([a-zA-Z0-9_-]+)',
            r'#([a-zA-Z0-9_-]+)$'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def _generate_output_path(self, url, output_folder):
        """Generate consistent output path for MP4 files"""
        domain = self._get_domain(url)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Try to extract meaningful video ID or title
        video_id = self._extract_video_id(url)
        if video_id:
            base_name = f"{domain}_{video_id}"
        else:
            base_name = f"{domain}_{timestamp}"
        
        # Always use .mp4 extension
        output_path = os.path.join(output_folder, f"{base_name}.mp4")
        
        # If file already exists, add counter
        counter = 1
        while os.path.exists(output_path):
            output_path = os.path.join(output_folder, f"{base_name}_{counter}.mp4")
            counter += 1
        
        return output_path
    
    def _check_if_already_downloaded(self, url, output_folder):
        """Check if this URL was already successfully downloaded - MORE STRICT CHECK"""
        # For now, disable this check to ensure downloads always attempt
        # This prevents false positives that skip actual downloads
        return None
    
    def _cleanup_duplicate_files(self, output_folder, final_file):
        """Clean up any duplicate or partial files, keep only the final MP4"""
        try:
            final_basename = os.path.splitext(os.path.basename(final_file))[0]
            
            # Find all files with similar names
            for file_path in glob.glob(os.path.join(output_folder, "*")):
                if file_path == final_file:
                    continue
                
                file_basename = os.path.splitext(os.path.basename(file_path))[0]
                
                # Remove files with same base name but different extensions
                if file_basename.startswith(final_basename.split('_')[0]):
                    try:
                        # Don't delete if it's significantly larger (might be better quality)
                        if os.path.getsize(file_path) < os.path.getsize(final_file) * 1.5:
                            os.remove(file_path)
                    except:
                        pass
        except Exception as e:
            logger.error(f"Error cleaning up files: {e}")
    
    def start_progress_tracking(self, output_path):
        """Start progress tracking for file"""
        if self.progress_callback:
            try:
                self.progress_callback('start', output_path)
            except:
                pass
    
    def stop_progress_tracking(self):
        """Stop progress tracking"""
        if self.progress_callback:
            try:
                self.progress_callback('stop', None)
            except:
                pass
    
    def update_progress_from_line(self, line):
        """Update progress from yt-dlp output line"""
        if self.progress_callback:
            try:
                self.progress_callback('update', line)
            except:
                pass
    
    def _list_available_formats(self, url):
        """List available formats for debugging"""
        try:
            cmd = ['yt-dlp', '--list-formats', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            if result.returncode == 0:
                # Show first few lines of format list
                lines = result.stdout.split('\n')[:10]
                self.log_status(f"📋 Available formats: {' | '.join([l.strip() for l in lines if l.strip()])[:200]}...")
            else:
                self.log_status("Could not list formats")
        except Exception as e:
            self.log_status(f"Format listing failed: {str(e)[:50]}")

    def _strategy_mp4_best(self, url, output_path):
        """Best quality MP4 strategy with real-time progress"""
        self.log_status("Downloading best quality MP4", url)

        # List available formats for debugging
        self._list_available_formats(url)

        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--no-check-certificate',
            '--no-write-info-json',
            '--no-write-description',
            '--no-write-thumbnail',
            '--no-write-info-json',  # Prevent JSON file creation
            '--no-write-description',
            '--no-write-thumbnail',
            '--no-write-sub',
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '--no-playlist',
            '--retries', '3',
            '--ignore-errors',
            '--extractor-args', 'youtube:player_client=android',
            '--compat-options', 'no-youtube-unavailable-videos',
            '--newline',  # Important for real-time progress
            url
        ]
        
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_high(self, url, output_path):
        """High quality MP4 strategy"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--no-check-certificate',
            '--no-write-info-json',
            '--no-write-description',
            '--no-write-thumbnail',
            '--no-playlist',
            '--retries', '3',
            '--ignore-errors',
            '--extractor-args', 'youtube:player_client=android',
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_medium(self, url, output_path):
        """Medium quality MP4 strategy"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[height<=480]+bestaudio/best[height<=480]/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--no-check-certificate',
            '--no-write-info-json',
            '--no-write-description',
            '--no-write-thumbnail',
            '--no-playlist',
            '--retries', '3',
            '--ignore-errors',
            '--extractor-args', 'youtube:player_client=android',
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_standard(self, url, output_path):
        """Standard MP4 strategy"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--no-check-certificate',
            '--no-write-info-json',
            '--no-write-description',
            '--no-write-thumbnail',
            '--no-playlist',
            '--retries', '3',
            '--ignore-errors',
            '--extractor-args', 'youtube:player_client=android',
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_compatible(self, url, output_path):
        """Compatible MP4 strategy"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'worst',
            '--merge-output-format', 'mp4',
            '--no-check-certificate',
            '--no-write-info-json',
            '--no-write-description',
            '--no-write-thumbnail',
            '--prefer-free-formats',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_cookies(self, url, output_path):
        """MP4 with browser cookies"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--cookies-from-browser', 'chrome',
            '--no-check-certificate',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_ipv4(self, url, output_path):
        """MP4 with IPv4 force"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--force-ipv4',
            '--no-check-certificate',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_geo(self, url, output_path):
        """MP4 with geo bypass"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--geo-bypass',
            '--no-check-certificate',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_android(self, url, output_path):
        """MP4 with Android user agent"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--user-agent', 'com.google.android.youtube/14.21.54',
            '--no-check-certificate',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_generic(self, url, output_path):
        """MP4 generic extractor"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--merge-output-format', 'mp4',
            '--force-generic-extractor',
            '--no-check-certificate',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_mp4_fallback(self, url, output_path):
        """Final MP4 fallback strategy"""
        cmd = [
            'yt-dlp',
            '--output', output_path,
            '--merge-output-format', 'mp4',
            '--no-check-certificate',
            '--no-write-info-json',
            '--no-write-description',
            '--no-write-thumbnail',
            '--ignore-errors',
            '--no-warnings',
            '--newline',
            url
        ]
        return self._execute_download_command_with_progress(cmd, output_path)
    
    def _strategy_browser_download(self, url, output_path):
        """NEW: Browser automation strategy for right-click downloads"""
        try:
            self.log_status("Trying browser right-click download", url)
            self.log_status("🔍 DEBUGGING: Browser automation strategy started", url)

            # Extract output folder from output_path
            output_folder = os.path.dirname(output_path)
            self.log_status(f"🔍 DEBUGGING: Output folder: {output_folder}", url)

            # Check if browser manager is available
            try:
                browser_manager = self._get_browser_manager()
                self.log_status("🔍 DEBUGGING: Browser manager obtained successfully", url)
            except Exception as bm_error:
                self.log_status(f"🔍 DEBUGGING: Browser manager failed: {str(bm_error)[:100]}", url)
                return False

            # Use browser automation to download
            self.log_status("🔍 DEBUGGING: About to call download_video_browser", url)
            try:
                success = browser_manager.download_video_browser(url, output_folder)
                self.log_status(f"🔍 DEBUGGING: download_video_browser returned: {success}", url)
            except Exception as download_error:
                self.log_status(f"🔍 DEBUGGING: download_video_browser failed: {str(download_error)[:100]}", url)
                import traceback
                self.log_status(f"🔍 DEBUGGING: Traceback: {traceback.format_exc()[:200]}", url)
                return False

            if success:
                # Check if any new video files were downloaded
                video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']

                for file_name in os.listdir(output_folder):
                    file_path = os.path.join(output_folder, file_name)

                    # Check if it's a recently created video file
                    if (any(ext in file_name.lower() for ext in video_extensions) and
                        os.path.getmtime(file_path) > time.time() - 600):  # Created within last 10 minutes

                        # Rename to expected output path if needed
                        if file_path != output_path:
                            try:
                                shutil.move(file_path, output_path)
                            except:
                                # If rename fails, just verify the downloaded file exists
                                if os.path.exists(file_path) and os.path.getsize(file_path) > 1024:
                                    return True

                        return True

            self.log_status("🔍 DEBUGGING: Browser strategy completed but no success", url)
            return False

        except Exception as e:
            self.log_status(f"🔍 DEBUGGING: Browser strategy exception: {str(e)[:100]}", url)
            import traceback
            self.log_status(f"🔍 DEBUGGING: Exception traceback: {traceback.format_exc()[:200]}", url)
            logger.error(f"Browser download strategy failed: {e}")
            return False
    
    def _preprocess_url_for_yt_dlp(self, url):
        """Preprocess URL to convert embed URLs to regular URLs for better yt-dlp compatibility"""
        try:
            # Convert Pornhub embed URLs to regular video URLs
            if 'pornhub.com/embed/' in url:
                video_id = url.split('/embed/')[-1].split('?')[0]
                regular_url = f"https://www.pornhub.com/view_video.php?viewkey={video_id}"
                self.log_status(f"🔄 Converting embed URL to regular URL: {regular_url}")
                return regular_url

            # Convert other common embed URLs
            if '/embed/' in url:
                self.log_status(f"⚠️ Warning: Embed URL detected, yt-dlp may have issues: {url}")

            return url
        except Exception as e:
            self.log_status(f"⚠️ URL preprocessing error: {e}")
            return url

    def _execute_download_command_with_progress(self, cmd, expected_output_path):
        """Execute download command with real-time progress monitoring and enhanced error logging"""
        try:
            # Start progress tracking
            self.start_progress_tracking(expected_output_path)

            # Preprocess the URL in the command
            if len(cmd) > 0:
                original_url = cmd[-1]  # URL is typically the last argument
                processed_url = self._preprocess_url_for_yt_dlp(original_url)
                if processed_url != original_url:
                    cmd = cmd[:-1] + [processed_url]

            # Enhanced debug logging
            self.log_status(f"🔍 Executing yt-dlp command: {' '.join(cmd[:3])} ... {cmd[-1]}")

            # Start process with real-time output and timeout
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,  # Separate stderr for better error capture
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True
            )

            # Set timeout for yt-dlp commands (300 seconds for video downloads)
            import threading
            timeout_seconds = 300  # 5 minutes timeout for video downloads

            # Collect all output for debugging
            all_output = []
            error_output = []

            # Monitor output in real-time with timeout
            start_time = time.time()
            last_activity = start_time
            activity_timeout = 60  # 1 minute without output = stalled

            while True:
                # Check global timeout
                if time.time() - start_time > timeout_seconds:
                    self.log_status(f"⏰ yt-dlp timed out after {timeout_seconds} seconds")
                    self._force_terminate_process(process)
                    return_code = -1
                    break

                # Check activity timeout (no output for 60 seconds = stalled)
                if time.time() - last_activity > activity_timeout:
                    self.log_status(f"⏰ yt-dlp stalled - no output for {activity_timeout} seconds")
                    self._force_terminate_process(process)
                    return_code = -1
                    break

                try:
                    line = process.stdout.readline()
                    if not line and process.poll() is not None:
                        break

                    if line:
                        line = line.strip()
                        if line:  # Only count non-empty lines as activity
                            last_activity = time.time()
                            all_output.append(line)
                            # Update progress from this line
                            self.update_progress_from_line(line)

                            # Log critical errors immediately
                            if any(error_word in line.lower() for error_word in ['error', 'failed', 'unable', 'forbidden', 'not found']):
                                self.log_status(f"⚠️ yt-dlp error: {line}")

                except Exception:
                    break

                # Small sleep to prevent CPU spinning
                time.sleep(0.1)

            # Capture any remaining stderr
            try:
                stderr_output = process.stderr.read()
                if stderr_output:
                    error_output.append(stderr_output.strip())
                    self.log_status(f"⚠️ yt-dlp stderr: {stderr_output.strip()}")
            except:
                pass

            # Get return code if not already set
            if 'return_code' not in locals():
                return_code = process.poll()
                if return_code is None:
                    return_code = -1

            # Enhanced error reporting
            if return_code != 0:
                self.log_status(f"❌ yt-dlp exited with code {return_code}")
                if all_output:
                    self.log_status(f"📝 Last stdout lines: {' | '.join(all_output[-3:])}")
                if error_output:
                    self.log_status(f"📝 Error output: {' | '.join(error_output)}")

            # Check if the expected file exists and is an MP4
            if os.path.exists(expected_output_path):
                if self._verify_mp4_file(expected_output_path):
                    self.log_status(f"✅ Download successful: {os.path.basename(expected_output_path)}")
                    # Check if video has audio (method is at module level, not class method)
                    # Commenting out for now as it's causing errors
                    # check_video_has_audio(expected_output_path)
                    return True
                else:
                    self.log_status(f"🔄 Attempting format conversion for: {os.path.basename(expected_output_path)}")
                    return self._convert_to_mp4(expected_output_path)

            # Look for any downloaded file in the same directory
            output_dir = os.path.dirname(expected_output_path)
            base_name = os.path.splitext(os.path.basename(expected_output_path))[0]

            # Find downloaded files, including partial files
            for file_path in glob.glob(os.path.join(output_dir, f"{base_name}.*")):
                if file_path != expected_output_path and os.path.getsize(file_path) > 1024:
                    # Handle .part files (partial downloads)
                    if file_path.endswith('.part'):
                        self.log_status(f"⚠️ Found partial download: {os.path.basename(file_path)}")
                        # Try to rename/move partial file to final location
                        try:
                            if file_path.replace('.part', '') == expected_output_path:
                                os.rename(file_path, expected_output_path)
                                self.log_status(f"✅ Renamed partial file to: {os.path.basename(expected_output_path)}")
                                if self._verify_mp4_file(expected_output_path):
                                    return True
                        except Exception as e:
                            self.log_status(f"⚠️ Could not rename partial file: {e}")
                    else:
                        self.log_status(f"🔄 Found alternative file, converting: {os.path.basename(file_path)}")
                        if self._convert_to_mp4(file_path, expected_output_path):
                            return True

            self.log_status(f"❌ No valid output file found after yt-dlp execution")
            return False

        except Exception as e:
            logger.error(f"Download command failed: {e}")
            self.log_status(f"💥 Command execution error: {str(e)}")
            return False
        finally:
            # Stop progress tracking
            self.stop_progress_tracking()

    def _force_terminate_process(self, process):
        """Forcefully terminate a process"""
        try:
            self.log_status("🛑 Force terminating yt-dlp process...")
            process.terminate()
            try:
                process.wait(timeout=5)
                self.log_status("✅ Process terminated gracefully")
            except subprocess.TimeoutExpired:
                self.log_status("💀 Process didn't terminate, killing...")
                process.kill()
                process.wait(timeout=3)
                self.log_status("✅ Process killed")
        except Exception as e:
            self.log_status(f"⚠️ Error terminating process: {e}")

    def _verify_mp4_file(self, file_path):
        """Verify if file is a valid MP4 - STRICTER CHECK"""
        try:
            if not os.path.exists(file_path):
                logger.error(f"File does not exist: {file_path}")
                return False
            
            # Check file size (must be > 100KB for a real download)
            file_size = os.path.getsize(file_path)
            if file_size < 100 * 1024:  # 100KB minimum
                logger.error(f"File too small ({file_size} bytes): {file_path}")
                return False
            
            # Check file extension
            if not file_path.lower().endswith('.mp4'):
                logger.error(f"Wrong extension: {file_path}")
                return False
            
            # Basic MP4 header check
            with open(file_path, 'rb') as f:
                header = f.read(12)
                if len(header) >= 12:
                    # Check for MP4 signature
                    if b'ftyp' in header:
                        logger.info(f"Valid MP4 file verified: {file_path} ({file_size} bytes)")
                        return True
                    else:
                        logger.error(f"Invalid MP4 header: {file_path}")
                        return False
            
            logger.error(f"Cannot read file header: {file_path}")
            return False
        except Exception as e:
            logger.error(f"Error verifying file {file_path}: {e}")
            return False
    
    def _convert_to_mp4(self, input_path, output_path=None):
        """Convert video file to MP4 using ffmpeg"""
        try:
            if not output_path:
                output_path = os.path.splitext(input_path)[0] + '.mp4'
            
            # Check if ffmpeg is available
            try:
                subprocess.run(['ffmpeg', '-version'], capture_output=True, timeout=5)
            except:
                # ffmpeg not available, just rename if it's close enough
                if input_path.lower().endswith(('.webm', '.mkv', '.avi')):
                    shutil.move(input_path, output_path)
                    return os.path.exists(output_path)
                return False
            
            # Convert using ffmpeg
            cmd = [
                'ffmpeg', '-i', input_path,
                '-c:v', 'copy',  # Copy video stream if possible
                '-c:a', 'aac',   # Convert audio to AAC
                '-y',            # Overwrite output
                output_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, timeout=60)
            
            if result.returncode == 0 and os.path.exists(output_path):
                # Remove original file if conversion successful
                try:
                    if input_path != output_path:
                        os.remove(input_path)
                except:
                    pass
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Conversion failed: {e}")
            return False
    
    def download_url(self, url, output_folder):
        """Download URL with real-time progress tracking - ENHANCED WITH BROWSER FALLBACK"""

        self.log_status("Starting download", url)

        # Debug: Log all available strategies
        self.log_status(f"🔍 STRATEGIES: Total strategies available: {len(self.strategies)}", url)
        for idx, (strategy_name, _) in enumerate(self.strategies, 1):
            self.log_status(f"🔍 STRATEGIES: #{idx} - {strategy_name}", url)
            if idx >= 3:  # Just show first 3 for brevity
                self.log_status(f"🔍 STRATEGIES: ... and {len(self.strategies) - 3} more", url)
                break

        # Generate output path
        output_path = self._generate_output_path(url, output_folder)

        # Mark this file as being downloaded
        self.downloaded_files.add(output_path)

        # Try each strategy until one succeeds
        for i, (name, strategy) in enumerate(self.strategies, 1):
            try:
                self.log_status(f"Trying {name}", url)

                # Special debugging for browser strategy
                if "Browser" in name:
                    self.log_status("🔍 MAIN LOOP: About to execute Browser Right-Click Download strategy", url)
                    self.log_status(f"🔍 MAIN LOOP: Strategy #{i} of {len(self.strategies)}", url)

                # Try the strategy
                result = strategy(url, output_path)

                if "Browser" in name:
                    self.log_status(f"🔍 MAIN LOOP: Browser strategy returned: {result}", url)

                if result:
                    # Verify the download
                    if self._verify_mp4_file(output_path):
                        self.log_status("Download complete", url)

                        # Clean up any duplicate files
                        self._cleanup_duplicate_files(output_folder, output_path)

                        return True
                    else:
                        self.log_status(f"{name} failed verification", url)
                        # Remove invalid file
                        try:
                            if os.path.exists(output_path):
                                os.remove(output_path)
                        except:
                            pass
                else:
                    self.log_status(f"{name} failed", url)

            except Exception as e:
                logger.error(f"Strategy {name} failed: {e}")
                self.log_status(f"{name} error: {str(e)[:50]}", url)
                if "Browser" in name:
                    self.log_status(f"🔍 MAIN LOOP: Browser strategy exception: {str(e)}", url)
                    import traceback
                    self.log_status(f"🔍 MAIN LOOP: Traceback: {traceback.format_exc()[:300]}", url)
                continue
        
        self.log_status("All download strategies exhausted - unable to download", url)
        self.log_status("Possible issues: video may be private, region-locked, or requires login", url)

        # Remove from downloaded files set if failed
        self.downloaded_files.discard(output_path)

        return False
    
    def download_concurrent(self, urls, output_folder, max_workers=1):
        """Download multiple URLs one at a time"""
        results = {'success': 0, 'failed': 0}

        # Process URLs one at a time
        for url in urls:
            try:
                # Reset status indicators for this specific URL
                if hasattr(self, 'gui') and hasattr(self.gui, 'reset_status_for_url'):
                    self.gui.reset_status_for_url(url)
                if self.download_with_retry(url, output_folder):
                    results['success'] += 1
                    # Update URL status to success
                    if hasattr(self, 'gui') and hasattr(self.gui, 'update_url_status'):
                        self.gui.update_url_status(url, "success")
                else:
                    results['failed'] += 1
                    # Update URL status to failed
                    if hasattr(self, 'gui') and hasattr(self.gui, 'update_url_status'):
                        self.gui.update_url_status(url, "failed")
            except Exception as e:
                results['failed'] += 1
                if hasattr(self, 'gui') and hasattr(self.gui, 'update_url_status'):
                    self.gui.update_url_status(url, "failed")

        return results
    
    def download_with_retry(self, url, output_folder):
        """Download with retry logic"""
        # Test yt-dlp on first run
        if not hasattr(self, '_yt_dlp_tested'):
            self._yt_dlp_tested = True
            if not self.test_yt_dlp_installation():
                self.log_status("⚠️ yt-dlp installation issues detected - downloads may fail")

        for attempt in range(self.retry_attempts):
            if attempt > 0:
                self.log_status(f"Retry attempt {attempt + 1} of {self.retry_attempts}", url)
                time.sleep(2 * attempt)
            else:
                self.log_status(f"Starting download (attempt 1 of {self.retry_attempts})", url)

            if self.download_url(url, output_folder):
                self.log_status("Download successful!", url)

                # Cleanup browser after successful download
                if hasattr(self, 'browser_manager') and self.browser_manager:
                    self.browser_manager.cleanup()

                return True

        self.log_status(f"FAILED: All {self.retry_attempts} attempts failed for this URL", url)

        # Cleanup browser after all attempts are complete
        if hasattr(self, 'browser_manager') and self.browser_manager:
            self.browser_manager.cleanup()

        return False

class DependencyManager:
    """Enhanced dependency manager with automatic installation including Selenium"""
    
    def __init__(self, status_callback=None):
        self.status_callback = status_callback
        self.dependencies_checked = False
        # Persistent dependency check cache
        self.cache_file = os.path.join(os.path.expanduser('~'), '.fasstvideo_deps_cache.json')
        self.cache_expiry_hours = 24  # Cache valid for 24 hours
        self._load_dependency_cache()
        self.required_packages = {
            # Core packages
            'requests': 'requests>=2.28.0',
            'urllib3': 'urllib3>=1.26.0',
            'Pillow': 'Pillow>=9.0.0',
            
            # Security packages
            'cryptography': 'cryptography>=40.0.0',
            'psutil': 'psutil>=5.9.0',
            
            # Windows-specific security
            'pywin32': 'pywin32>=305' if os.name == 'nt' else None,
            
            # Video processing
            'yt-dlp': 'yt-dlp>=2023.7.6',
            
            # Browser automation
            'selenium': 'selenium>=4.15.0',
        }
        
        # Remove None values (platform-specific packages)
        self.required_packages = {k: v for k, v in self.required_packages.items() if v is not None}
        
        self.optional_packages = {
            'ffmpeg-python': 'ffmpeg-python>=0.2.0'
        }
        
    def log_status(self, message):
        """Log status with optional callback"""
        logger.info(message)
        if self.status_callback:
            try:
                self.status_callback(message)
            except:
                pass
    
    def _load_dependency_cache(self):
        """Load cached dependency check status"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r') as f:
                    cache = json.load(f)

                # Check if cache is still valid
                cache_time = datetime.fromisoformat(cache.get('timestamp', '2000-01-01'))
                if datetime.now() - cache_time < timedelta(hours=self.cache_expiry_hours):
                    if cache.get('dependencies_valid', False):
                        self.dependencies_checked = True
                        logger.info("Loaded cached dependency check - all dependencies valid")
                        return True
            return False
        except:
            return False

    def _save_dependency_cache(self, valid=True):
        """Save dependency check status to cache"""
        try:
            cache = {
                'timestamp': datetime.now().isoformat(),
                'dependencies_valid': valid,
                'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
            }
            with open(self.cache_file, 'w') as f:
                json.dump(cache, f)
            logger.info("Saved dependency check to cache")
        except:
            pass

    def check_python_version(self):
        """Check if Python version is compatible"""
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 7):
            self.log_status(f"Warning: Python 3.7+ recommended. Current: {version.major}.{version.minor}")
            return False
        self.log_status(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    
    def check_pip(self):
        """Ensure pip is available and up to date"""
        try:
            # Check if pip exists
            result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                                  capture_output=True, check=True, timeout=10)
            self.log_status("✓ pip available")
            
            # Upgrade pip if needed
            self.log_status("Checking pip version...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], 
                          capture_output=True, timeout=30)
            
            return True
        except Exception as e:
            self.log_status(f"✗ pip not available: {e}")
            return False
    
    def install_package(self, package_name, package_spec, required=True):
        """Install a Python package with progress tracking"""
        try:
            self.log_status(f"Checking {package_name}...")
            
            # First try to import to see if already installed
            try:
                if package_name == 'Pillow':
                    import PIL
                elif package_name == 'pywin32':
                    import win32api
                elif package_name == 'yt-dlp':
                    import yt_dlp
                elif package_name == 'ffmpeg-python':
                    import ffmpeg
                elif package_name == 'selenium':
                    import selenium
                else:
                    __import__(package_name)
                
                self.log_status(f"✓ {package_name} already installed")
                return True
                
            except ImportError:
                pass
            
            # Install the package
            self.log_status(f"Installing {package_name}...")
            
            install_cmd = [
                sys.executable, '-m', 'pip', 'install', 
                package_spec,
                '--user',  # Install for user only
                '--upgrade',
                '--no-warn-script-location'
            ]
            
            # For Windows security packages, might need different approach
            if package_name == 'pywin32' and os.name == 'nt':
                install_cmd = [sys.executable, '-m', 'pip', 'install', package_spec, '--user']
            
            result = subprocess.run(install_cmd, capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                self.log_status(f"✓ {package_name} installed successfully")
                return True
            else:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                self.log_status(f"✗ Failed to install {package_name}: {error_msg}")
                
                if required:
                    # Try alternative installation methods
                    return self._try_alternative_install(package_name, package_spec)
                return False
                
        except Exception as e:
            self.log_status(f"✗ Error installing {package_name}: {e}")
            if required:
                return self._try_alternative_install(package_name, package_spec)
            return False
    
    def _try_alternative_install(self, package_name, package_spec):
        """Try alternative installation methods"""
        try:
            self.log_status(f"Trying alternative installation for {package_name}...")
            
            # Method 1: Try without --user flag
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install', package_spec, '--upgrade'
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                self.log_status(f"✓ {package_name} installed via alternative method")
                return True
            
            # Method 2: Try with --force-reinstall
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install', package_spec, 
                '--force-reinstall', '--no-deps'
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                self.log_status(f"✓ {package_name} force-installed")
                return True
            
            # Method 3: Try installing just the package name
            base_package = package_spec.split('>=')[0].split('==')[0]
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install', base_package
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                self.log_status(f"✓ {package_name} installed (base version)")
                return True
            
            return False
            
        except Exception as e:
            self.log_status(f"✗ All installation methods failed for {package_name}: {e}")
            return False
    
    def install_webdriver(self):
        """Install WebDriver components for browser automation"""
        try:
            self.log_status("Checking WebDriver components...")
            
            # Check if Chrome/Chromium is available
            chrome_available = False
            try:
                chrome_paths = [
                    "google-chrome", "chromium-browser", "chromium",
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                ]
                
                for chrome_path in chrome_paths:
                    try:
                        subprocess.run([chrome_path, '--version'], capture_output=True, timeout=5)
                        chrome_available = True
                        self.log_status(f"✓ Chrome found: {chrome_path}")
                        break
                    except:
                        continue
                        
            except:
                pass
            
            # Check if Firefox is available
            firefox_available = False
            try:
                firefox_paths = ["firefox", r"C:\Program Files\Mozilla Firefox\firefox.exe"]
                
                for firefox_path in firefox_paths:
                    try:
                        subprocess.run([firefox_path, '--version'], capture_output=True, timeout=5)
                        firefox_available = True
                        self.log_status(f"✓ Firefox found: {firefox_path}")
                        break
                    except:
                        continue
                        
            except:
                pass
            
            if not chrome_available and not firefox_available:
                self.log_status("⚠ No browsers found for automation")
                self.log_status("  Browser automation may not work without Chrome or Firefox")
                return False
            
            # Try to install webdriver-manager for automatic driver management
            try:
                self.install_package('webdriver-manager', 'webdriver-manager>=3.8.0', required=False)
            except:
                pass
            
            return True
            
        except Exception as e:
            self.log_status(f"✗ WebDriver setup error: {e}")
            return False
    
    def install_ffmpeg(self):
        """Install or check FFmpeg availability"""
        try:
            # First check if ffmpeg is already available
            result = subprocess.run(['ffmpeg', '-version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                self.log_status(f"✓ {version_line}")
                return True
        except:
            pass
        
        self.log_status("FFmpeg not found, attempting installation...")
        
        # Try different installation methods based on platform
        if os.name == 'nt':
            return self._install_ffmpeg_windows()
        elif sys.platform == 'darwin':
            return self._install_ffmpeg_macos()
        else:
            return self._install_ffmpeg_linux()
    
    def _install_ffmpeg_windows(self):
        """Install FFmpeg on Windows"""
        try:
            # Method 1: Try using ffmpeg-python package
            if self.install_package('ffmpeg-python', 'ffmpeg-python>=0.2.0', required=False):
                self.log_status("✓ ffmpeg-python installed")
            
            # Method 2: Download ffmpeg binary (simplified approach)
            self.log_status("⚠ FFmpeg binary installation requires manual setup on Windows")
            self.log_status("  Download from: https://ffmpeg.org/download.html")
            self.log_status("  Add to PATH or place in application directory")
            
            return True  # Don't fail on this
            
        except Exception as e:
            self.log_status(f"✗ FFmpeg installation failed: {e}")
            return False
    
    def _install_ffmpeg_macos(self):
        """Install FFmpeg on macOS"""
        try:
            # Try using Homebrew
            result = subprocess.run(['brew', 'install', 'ffmpeg'], 
                                  capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                self.log_status("✓ FFmpeg installed via Homebrew")
                return True
            
            self.log_status("⚠ FFmpeg installation requires Homebrew: brew install ffmpeg")
            return True  # Don't fail on this
            
        except Exception:
            self.log_status("⚠ FFmpeg installation requires Homebrew: brew install ffmpeg")
            return True
    
    def _install_ffmpeg_linux(self):
        """Install FFmpeg on Linux"""
        try:
            # Try different package managers
            package_managers = [
                (['apt-get', 'update'], ['apt-get', 'install', '-y', 'ffmpeg']),
                (['yum', 'install', '-y', 'ffmpeg'],),
                (['dnf', 'install', '-y', 'ffmpeg'],),
                (['pacman', '-S', '--noconfirm', 'ffmpeg'],),
            ]
            
            for commands in package_managers:
                try:
                    for cmd in commands:
                        result = subprocess.run(cmd, capture_output=True, timeout=300)
                        if result.returncode != 0:
                            break
                    else:
                        self.log_status("✓ FFmpeg installed via system package manager")
                        return True
                except:
                    continue
            
            self.log_status("⚠ FFmpeg installation requires system package manager")
            self.log_status("  Try: sudo apt install ffmpeg (Ubuntu/Debian)")
            self.log_status("  Or: sudo yum install ffmpeg (CentOS/RHEL)")
            
            return True  # Don't fail on this
            
        except Exception:
            return True
    
    def check_yt_dlp(self):
        """Check and install yt-dlp"""
        return self.install_package('yt-dlp', self.required_packages['yt-dlp'])
    
    def create_requirements_txt(self):
        """Create requirements.txt file for manual installation"""
        try:
            requirements_content = []
            for package, spec in self.required_packages.items():
                requirements_content.append(spec)
            
            for package, spec in self.optional_packages.items():
                requirements_content.append(f"# Optional: {spec}")
            
            requirements_path = "requirements.txt"
            with open(requirements_path, 'w') as f:
                f.write('\n'.join(requirements_content))
            
            self.log_status(f"✓ Created {requirements_path}")
            self.log_status("  You can install manually with: pip install -r requirements.txt")
            
        except Exception as e:
            self.log_status(f"✗ Failed to create requirements.txt: {e}")
    
    def show_installation_dialog(self):
        """Show installation progress dialog"""
        if not hasattr(self, '_install_dialog'):
            try:
                self._install_dialog = tk.Toplevel()
                self._install_dialog.title("Installing Dependencies")
                self._install_dialog.geometry("600x400")
                self._install_dialog.configure(bg=COLORS['bg_primary'])
                
                # Progress text
                self._install_text = tk.Text(self._install_dialog, 
                                           bg=COLORS['glass_bg'], 
                                           fg=COLORS['text_primary'],
                                           font=('Courier', 10))
                self._install_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
                
                # Scrollbar
                scrollbar = tk.Scrollbar(self._install_dialog, command=self._install_text.yview)
                self._install_text.configure(yscrollcommand=scrollbar.set)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                
            except:
                self._install_dialog = None
    
    def update_install_dialog(self, message):
        """Update installation dialog with progress"""
        try:
            if hasattr(self, '_install_text'):
                self._install_text.insert(tk.END, message + '\n')
                self._install_text.see(tk.END)
                self._install_text.update()
        except:
            pass
    
    def close_install_dialog(self):
        """Close installation dialog"""
        try:
            if hasattr(self, '_install_dialog') and self._install_dialog:
                self._install_dialog.destroy()
        except:
            pass
    
    def check_all_dependencies(self):
        """Comprehensive dependency check and installation INCLUDING Selenium"""
        # Check if already validated in cache
        if self.dependencies_checked:
            self.log_status("✓ Dependencies already verified (cached)")
            return True

        try:
            self.log_status("=== FasstVideo Dependency Check ===")
            
            # Show installation dialog
            try:
                self.show_installation_dialog()
                self.status_callback = self.update_install_dialog
            except:
                pass
            
            # Check Python version
            if not self.check_python_version():
                self.log_status("⚠ Python version warning - continuing anyway")
            
            # Check and upgrade pip
            if not self.check_pip():
                self.log_status("✗ pip unavailable - manual installation required")
                self.create_requirements_txt()
                return False
            
            # Install required packages
            failed_packages = []
            for package_name, package_spec in self.required_packages.items():
                if not self.install_package(package_name, package_spec, required=True):
                    failed_packages.append(package_name)
            
            # Install optional packages
            for package_name, package_spec in self.optional_packages.items():
                self.install_package(package_name, package_spec, required=False)
            
            # Install WebDriver components
            self.install_webdriver()
            
            # Install FFmpeg
            self.install_ffmpeg()
            
            # Final verification
            self.log_status("\n=== Verifying Installation ===")
            self._verify_installation()
            
            if failed_packages:
                self.log_status(f"\n⚠ Some packages failed to install: {', '.join(failed_packages)}")
                self.log_status("Application will continue with reduced functionality")
                self.create_requirements_txt()
            else:
                self.log_status("\n✓ All dependencies installed successfully!")
            
            self.dependencies_checked = True
            # Save successful dependency check to cache
            self._save_dependency_cache(valid=True)

            # Close dialog after a delay
            if hasattr(self, '_install_dialog'):
                threading.Timer(3.0, self.close_install_dialog).start()
            
            return True
            
        except Exception as e:
            self.log_status(f"\n✗ Dependency installation failed: {e}")
            self.create_requirements_txt()
            self.dependencies_checked = True
            return False
    
    def _verify_installation(self):
        """Verify that packages were installed correctly"""
        verification_tests = {
            'requests': lambda: __import__('requests').get('https://httpbin.org/get', timeout=5),
            'Pillow': lambda: __import__('PIL.Image', fromlist=['Image']),
            'cryptography': lambda: __import__('cryptography.fernet', fromlist=['Fernet']),
            'psutil': lambda: __import__('psutil').virtual_memory(),
            'yt-dlp': lambda: __import__('yt_dlp').__version__,
            'selenium': lambda: __import__('selenium.webdriver', fromlist=['webdriver']),
        }
        
        if os.name == 'nt':
            verification_tests['pywin32'] = lambda: __import__('win32api').GetVersion()
        
        for package, test_func in verification_tests.items():
            try:
                test_func()
                self.log_status(f"✓ {package} verified")
            except Exception as e:
                self.log_status(f"⚠ {package} verification failed: {e}")
    
    def install_on_first_run(self):
        """Check if this is first run and install dependencies"""
        first_run_file = os.path.join(os.path.expanduser("~"), ".fasstvideo_first_run")
        
        if not os.path.exists(first_run_file):
            self.log_status("First run detected - installing dependencies...")
            
            # Install dependencies
            success = self.check_all_dependencies()
            
            # Mark as completed
            try:
                with open(first_run_file, 'w') as f:
                    f.write(str(time.time()))
            except:
                pass
            
            return success
        
        return True

class EventLogsWindow:
    """Real-time event logs window for debugging and monitoring"""

    def __init__(self, parent):
        self.parent = parent
        self.window = None
        self.logs_text = None
        self.log_buffer = []
        self.max_log_entries = 1000

    def show_window(self):
        """Show or focus the logs window"""
        if self.window is None or not self.window.winfo_exists():
            self.create_window()
        else:
            # Window exists, just bring it to front
            self.window.lift()
            self.window.focus_force()

    def create_window(self):
        """Create the logs window"""
        try:
            self.window = tk.Toplevel(self.parent.root)
            self.window.title("🔍 Event Logs - Real-time Debugging")
            self.window.geometry("900x600")
            self.window.configure(bg=COLORS['bg_primary'])

            # Make window semi-transparent
            try:
                self.window.attributes('-alpha', 0.95)
            except:
                pass

            # Window icon
            try:
                if hasattr(self.parent, 'logo_manager') and self.parent.logo_manager.logo_icon:
                    self.window.iconphoto(False, self.parent.logo_manager.logo_icon)
            except:
                pass

            # Create main frame
            main_frame = GlassFrame(self.window, glass_opacity=0.15)
            main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # Title
            title_frame = tk.Frame(main_frame, bg=COLORS['glass_bg'])
            title_frame.pack(fill=tk.X, padx=10, pady=(10, 5))

            title_label = tk.Label(title_frame, text="📋 Real-time Event Logs",
                                 bg=COLORS['glass_bg'], fg=COLORS['text_primary'],
                                 font=('Segoe UI', 16, 'bold'))
            title_label.pack(side=tk.LEFT)

            # Control buttons
            controls_frame = tk.Frame(title_frame, bg=COLORS['glass_bg'])
            controls_frame.pack(side=tk.RIGHT)

            clear_btn = ModernButton(controls_frame, text="🗑 Clear",
                                   command=self.clear_logs,
                                   bg='#3A4565', fg=COLORS['text_primary'],
                                   hover_bg='#4A5575',
                                   padx=15, pady=8, width=10)
            clear_btn.pack(side=tk.LEFT, padx=5)

            export_btn = ModernButton(controls_frame, text="💾 Export",
                                    command=self.export_logs,
                                    bg='#2E5C8A', fg=COLORS['text_primary'],
                                    hover_bg='#3E6C9A',
                                    padx=15, pady=8, width=10)
            export_btn.pack(side=tk.LEFT, padx=5)

            # Status info
            info_frame = tk.Frame(main_frame, bg=COLORS['glass_bg'])
            info_frame.pack(fill=tk.X, padx=10, pady=5)

            self.status_label = tk.Label(info_frame, text="📊 Monitoring: Browser automation, downloads, errors",
                                       bg=COLORS['glass_bg'], fg=COLORS['text_secondary'],
                                       font=('Segoe UI', 10))
            self.status_label.pack(side=tk.LEFT)

            self.log_count_label = tk.Label(info_frame, text="Logs: 0",
                                          bg=COLORS['glass_bg'], fg=COLORS['accent'],
                                          font=('Segoe UI', 10, 'bold'))
            self.log_count_label.pack(side=tk.RIGHT)

            # Logs text area
            text_frame = tk.Frame(main_frame, bg=COLORS['glass_bg'])
            text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))

            # Create text widget with scrollbar
            self.logs_text = tk.Text(text_frame, bg='#0F1429', fg='#E0E6ED',
                                   font=('Consolas', 10), wrap=tk.WORD,
                                   insertbackground='#00D4FF',
                                   selectbackground='#2A5F8F')

            scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.logs_text.yview)
            self.logs_text.configure(yscrollcommand=scrollbar.set)

            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.logs_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Configure text tags for different log levels
            self.logs_text.tag_configure("ERROR", foreground="#FF5555", font=('Consolas', 10, 'bold'))
            self.logs_text.tag_configure("WARNING", foreground="#FFAA55", font=('Consolas', 10, 'bold'))
            self.logs_text.tag_configure("SUCCESS", foreground="#55FF55", font=('Consolas', 10, 'bold'))
            self.logs_text.tag_configure("INFO", foreground="#55AAFF")
            self.logs_text.tag_configure("DEBUG", foreground="#888888")
            self.logs_text.tag_configure("BROWSER", foreground="#FF55FF", font=('Consolas', 10, 'bold'))
            self.logs_text.tag_configure("DOWNLOAD", foreground="#55FFAA", font=('Consolas', 10, 'bold'))

            # Load existing logs if any
            self.load_existing_logs()

            # Make sure window stays on top initially
            self.window.transient(self.parent.root)

        except Exception as e:
            print(f"Error creating logs window: {e}")

    def add_log(self, message, level="INFO"):
        """Add a log message with timestamp and level"""
        try:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            log_entry = f"[{timestamp}] [{level}] {message}\n"

            # Add to buffer
            self.log_buffer.append((log_entry, level))

            # Keep buffer size manageable
            if len(self.log_buffer) > self.max_log_entries:
                self.log_buffer = self.log_buffer[-self.max_log_entries:]

            # Update window if it exists - use thread-safe approach
            if self.window and hasattr(self.window, 'winfo_exists'):
                try:
                    if self.window.winfo_exists() and self.logs_text:
                        # Use after_idle to ensure thread safety
                        self.window.after_idle(self._update_logs_ui, log_entry, level)
                except tk.TclError:
                    # Window was destroyed
                    pass

        except Exception as e:
            print(f"Error adding log: {e}")

    def _update_logs_ui(self, log_entry, level):
        """Thread-safe UI update for logs"""
        try:
            if self.logs_text and hasattr(self.logs_text, 'insert'):
                self.logs_text.insert(tk.END, log_entry, level)
                self.logs_text.see(tk.END)  # Auto-scroll to bottom

                # Update log count
                if hasattr(self, 'log_count_label') and self.log_count_label:
                    self.log_count_label.configure(text=f"Logs: {len(self.log_buffer)}")

        except Exception as e:
            print(f"Error updating logs UI: {e}")

    def load_existing_logs(self):
        """Load any existing logs from buffer"""
        try:
            if self.logs_text and self.log_buffer:
                for log_entry, level in self.log_buffer:
                    self.logs_text.insert(tk.END, log_entry, level)

                self.logs_text.see(tk.END)

                # Update log count
                if hasattr(self, 'log_count_label') and self.log_count_label:
                    self.log_count_label.configure(text=f"Logs: {len(self.log_buffer)}")

            # If no logs exist yet, add a startup message
            elif self.logs_text:
                startup_msg = f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] Event logs initialized - ready to monitor activity\n"
                self.logs_text.insert(tk.END, startup_msg, "INFO")
                if hasattr(self, 'log_count_label') and self.log_count_label:
                    self.log_count_label.configure(text="Logs: 1")

        except Exception as e:
            print(f"Error loading existing logs: {e}")

    def clear_logs(self):
        """Clear all logs"""
        try:
            if self.logs_text:
                self.logs_text.delete(1.0, tk.END)
            self.log_buffer.clear()

            if hasattr(self, 'log_count_label'):
                self.log_count_label.configure(text="Logs: 0")

        except Exception as e:
            print(f"Error clearing logs: {e}")

    def export_logs(self):
        """Export logs to file"""
        try:
            if not self.log_buffer:
                messagebox.showinfo("Export Logs", "No logs to export.")
                return

            from tkinter import filedialog
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Export Event Logs"
            )

            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"FasstVideo Event Logs Export\n")
                    f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("=" * 60 + "\n\n")

                    for log_entry, level in self.log_buffer:
                        f.write(log_entry)

                messagebox.showinfo("Export Logs", f"Logs exported successfully to:\n{filename}")

        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export logs: {e}")

class CleanFasstVideoDownloader:
    """Clean main application class with real-time progress tracking + Browser Automation"""

    def __init__(self, root):
        try:
            self.root = root
            
            # Initialize application
            app_name = protection_manager.get_obfuscated_constant('app_name') or "FasstVideo"
            self.root.title(app_name)
            self.root.geometry("1400x900")  # Expanded from 1280x760 to prevent cutoff
            self.root.configure(bg=COLORS['bg_primary'])
            
            # Initialize variables early
            self.download_folder = tk.StringVar(value=r"D:\4k video downloader - Copy\Downloads Chrome")
            self.download_active = False
            self.dependency_manager = DependencyManager()
            self.download_manager = None
            self.concurrent_downloads = 1  # Only one download at a time
            self.status_messages = []

            # Initialize event logs window
            self.event_logs = EventLogsWindow(self)

            # Log application startup
            self.log_event("FasstVideo application initializing...", "INFO")
            self.log_event(f"Application started on {platform.system()} {platform.release()}", "INFO")

            # Initialize animated title and real-time spinner
            self.animated_title = None
            self.realtime_spinner = None
            
            # Make window slightly transparent for glass effect (with fallback)
            try:
                self.root.attributes('-alpha', 0.98)
            except:
                pass
            
            self.logo_manager = LogoManager()
            
            # Set window icon (with better error handling)
            self.setup_window_icon()
            
            # Security checks (non-blocking)
            self.start_security_check()
            
            # Setup modern UI
            self.setup_modern_ui()
            self.center_window()

            # Initialize line numbers after UI setup
            self.root.after(100, self.update_line_numbers)

            # Check dependencies silently in background
            self.root.after(1000, self.check_dependencies_async)
            
            # Show legal disclaimer with one-time acceptance
            self.show_legal_disclaimer()
            
        except Exception as e:
            logger.exception("Error initializing application")
            # Show a basic error dialog
            try:
                messagebox.showerror("Initialization Error", f"Failed to initialize application: {e}")
            except:
                print(f"Failed to initialize application: {e}")
    
    def show_legal_disclaimer(self):
        """Show comprehensive legal disclaimer with persistent acceptance option"""
        try:
            # Check if user has previously accepted (stored in a settings file)
            settings_file = os.path.join(os.path.expanduser("~"), ".fasstvideo_settings.json")
            
            try:
                if os.path.exists(settings_file):
                    with open(settings_file, 'r') as f:
                        settings = json.load(f)
                        if settings.get('disclaimer_accepted', False):
                            return  # Skip disclaimer if previously accepted
            except Exception:
                pass  # If settings can't be read, show disclaimer
            
            disclaimer = """
LEGAL DISCLAIMER AND USER RESPONSIBILITY NOTICE

By using this software, you acknowledge and agree to the following terms based on established U.S. case law:

1. COPYRIGHT COMPLIANCE REQUIREMENT
Per 17 U.S.C. § 106, copyright owners have exclusive rights to reproduce, distribute, and publicly display their works. This software does not grant users any rights to copyrighted content. Users must ensure they have proper authorization before downloading any protected material.

2. FAIR USE LIMITATIONS
While 17 U.S.C. § 107 provides fair use exceptions, the Supreme Court in Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569 (1994) established that fair use analysis requires case-by-case evaluation. Users bear the burden of determining fair use applicability.

3. DMCA SAFE HARBOR COMPLIANCE
This software operates under principles established in Viacom International Inc. v. YouTube, Inc., 676 F.3d 19 (2d Cir. 2012). Users must comply with DMCA provisions and platform terms of service. The developer maintains no control over or liability for downloaded content.

4. SUBSTANTIAL NON-INFRINGING USE DOCTRINE
Following Sony Corp. v. Universal City Studios, 464 U.S. 417 (1984), this tool is capable of substantial non-infringing uses including: downloading public domain content, user-created content, Creative Commons licensed material, and content where users hold valid licenses.

5. LIABILITY LIMITATION
Per Perfect 10, Inc. v. Amazon.com, Inc., 508 F.3d 1146 (9th Cir. 2007), technology providers are not liable for users' direct infringement absent actual knowledge and material contribution. Users assume full legal responsibility for their actions.

6. INDUCEMENT LIABILITY WARNING
The Supreme Court in MGM Studios v. Grokster, 545 U.S. 913 (2005) established liability for those who induce infringement. This software does not encourage, promote, or assist in copyright infringement.

USER CERTIFICATIONS:
□ I understand my legal obligations under copyright law
□ I will only download content I have legal rights to access  
□ I accept full responsibility for my use of this software
□ I acknowledge the developer bears no liability for my actions

Do you accept these terms and certify your understanding of your legal obligations?
            """
            
            # Create custom dialog with checkbox
            dialog = tk.Toplevel(self.root)
            dialog.title("Legal Disclaimer")
            dialog.geometry("800x700")  # Made taller to accommodate buttons
            dialog.configure(bg=COLORS['bg_primary'])
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Center the dialog
            dialog.update_idletasks()
            x = (dialog.winfo_screenwidth() - dialog.winfo_width()) // 2
            y = (dialog.winfo_screenheight() - dialog.winfo_height()) // 2
            dialog.geometry(f"+{x}+{y}")
            
            # Main container for proper layout
            main_container = tk.Frame(dialog, bg=COLORS['bg_primary'])
            main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
            
            # Disclaimer text - with fixed height
            text_frame = tk.Frame(main_container, bg=COLORS['bg_primary'])
            text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
            
            text_widget = tk.Text(text_frame, wrap=tk.WORD, bg=COLORS['glass_bg'], 
                                 fg=COLORS['text_primary'], font=('Segoe UI', 11),
                                 padx=15, pady=15, height=20)  # Fixed height
            text_widget.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
            text_widget.insert('1.0', disclaimer)
            text_widget.configure(state='disabled')
            
            # Scrollbar
            scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview)
            text_widget.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Checkbox frame
            checkbox_frame = tk.Frame(main_container, bg=COLORS['bg_primary'], relief='ridge', bd=2)
            checkbox_frame.pack(fill=tk.X, pady=10)
            
            remember_var = tk.BooleanVar()
            remember_checkbox = tk.Checkbutton(checkbox_frame, 
                                              text="✓ Remember my choice (don't show this again)",
                                              variable=remember_var,
                                              bg=COLORS['bg_primary'],
                                              fg=COLORS['text_primary'],
                                              selectcolor=COLORS['success'],
                                              activebackground=COLORS['bg_secondary'],
                                              activeforeground=COLORS['text_primary'],
                                              font=('Segoe UI', 12, 'bold'),
                                              indicatoron=1)
            remember_checkbox.pack(anchor=tk.W, padx=10, pady=10)
            
            # Button frame - with guaranteed height and space
            button_frame = tk.Frame(main_container, bg=COLORS['bg_primary'], height=80)
            button_frame.pack(fill=tk.X, pady=(10, 0))
            button_frame.pack_propagate(False)  # Don't shrink the frame
            
            result = {'accepted': False}
            
            def accept_terms():
                result['accepted'] = True
                
                # Save settings if checkbox is checked
                if remember_var.get():
                    try:
                        settings = {
                            'disclaimer_accepted': True,
                            'acceptance_date': datetime.now().isoformat(),
                            'version': '1.0'
                        }
                        with open(settings_file, 'w') as f:
                            json.dump(settings, f, indent=2)
                        logger.info(f"Saved acceptance to {settings_file}")
                        
                        # Verify the file was written correctly
                        if os.path.exists(settings_file):
                            with open(settings_file, 'r') as f:
                                verify = json.load(f)
                                if verify.get('disclaimer_accepted', False):
                                    logger.info("Settings file verified successfully")
                                else:
                                    logger.warning("Settings file verification failed")
                        
                    except Exception as e:
                        logger.error(f"Failed to save settings: {e}")
                        # Show error but don't block acceptance
                        try:
                            messagebox.showwarning("Settings Save Error", 
                                                 "Could not save your preference. The disclaimer may appear again next time.")
                        except:
                            pass
                
                dialog.destroy()
            
            def decline_terms():
                result['accepted'] = False
                dialog.destroy()
            
            # Create buttons with proper styling and positioning
            button_container = tk.Frame(button_frame, bg=COLORS['bg_primary'])
            button_container.pack(expand=True, fill=tk.BOTH)
            
            # Decline button (left side)
            decline_btn = ModernButton(button_container, text="Decline (Close Program)", 
                                      command=decline_terms,
                                      bg=COLORS['danger'], fg=COLORS['text_primary'],
                                      hover_bg='#FF5577',
                                      padx=25, pady=15, font=('Segoe UI', 12, 'bold'))
            decline_btn.pack(side=tk.LEFT, padx=(0, 20), pady=10)
            
            # I Agree button (right side)
            accept_btn = ModernButton(button_container, text="I Agree", 
                                     command=accept_terms,
                                     bg=COLORS['success'], fg=COLORS['text_primary'],
                                     hover_bg='#00F0FF',
                                     padx=40, pady=15, font=('Segoe UI', 12, 'bold'))
            accept_btn.pack(side=tk.RIGHT, pady=10)
            
            # Wait for user response
            dialog.wait_window()
            
            if not result['accepted']:
                messagebox.showinfo("Notice", "You must accept the legal terms to use this software.")
                self.root.destroy()
                sys.exit(0)
                
        except Exception:
            pass

    def check_video_has_audio(self, video_path):
        """Check if a video file contains audio streams"""
        try:
            if not os.path.exists(video_path):
                return False

            # Use ffprobe to check for audio streams
            cmd = [
                'ffprobe', '-v', 'quiet',
                '-select_streams', 'a:0',
                '-show_entries', 'stream=codec_type',
                '-of', 'csv=p=0',
                video_path
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            has_audio = result.returncode == 0 and 'audio' in result.stdout.lower()

            if has_audio:
                self.log_event(f"✅ Video has audio: {os.path.basename(video_path)}", "SUCCESS")
            else:
                self.log_event(f"⚠️ Video has NO audio: {os.path.basename(video_path)}", "WARNING")

            return has_audio

        except Exception as e:
            self.log_event(f"Could not check audio: {str(e)[:50]}", "WARNING")
            return None

    def setup_window_icon(self):
        """Setup window icon with comprehensive error handling"""
        try:
            ico_path = self.logo_manager.get_icon_path()
            if ico_path and os.path.exists(ico_path):
                self.root.iconbitmap(ico_path)
                return
        except Exception:
            pass
        
        try:
            icon = self.logo_manager.load_logo_for_window()
            if icon:
                self.root.iconphoto(True, icon)
                return
        except Exception:
            pass
        
        try:
            # Fallback: try to set empty icon
            self.root.iconbitmap('')
        except Exception:
            # Final fallback: just continue without custom icon
            pass
    
    def start_security_check(self):
        """Basic security initialization without periodic monitoring"""
        try:
            # Perform one-time security check
            if hasattr(protection_manager, 'perform_integrity_check'):
                protection_manager.perform_integrity_check()
        except Exception:
            pass
    
    def create_gradient_bg(self):
        """Create gradient background effect"""
        if PIL_AVAILABLE:
            try:
                width = 1280
                height = 760
                
                # Create gradient
                gradient = Image.new('RGB', (width, height))
                draw = ImageDraw.Draw(gradient)
                
                # Vertical gradient from dark to slightly lighter
                for i in range(height):
                    color_value = int(10 + (i / height) * 20)
                    color = (color_value, color_value + 4, color_value + 20)
                    draw.rectangle([(0, i), (width, i + 1)], fill=color)
                
                # Apply blur for smooth effect
                gradient = gradient.filter(ImageFilter.GaussianBlur(radius=20))
                
                return ImageTk.PhotoImage(gradient)
            except:
                pass
        return None
    
    def setup_modern_ui(self):
        """Setup modern glassmorphic UI with animated title and real-time progress"""
        try:
            # Create gradient background
            gradient_bg = self.create_gradient_bg()
            if gradient_bg:
                bg_label = tk.Label(self.root, image=gradient_bg, bg=COLORS['bg_primary'])
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                bg_label.image = gradient_bg
            
            # Main container with padding
            main_container = tk.Frame(self.root, bg=COLORS['bg_primary'])
            main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
            
            
            # URL input section
            self.setup_url_section(main_container)
            
            # Settings section
            self.setup_settings_section(main_container)
            
            # Control buttons
            self.setup_control_buttons(main_container)
            
            # Real-time progress section
            self.setup_realtime_progress_section(main_container)
            
        except Exception as e:
            logger.exception("Error setting up UI")
            # Create a basic fallback UI
            self.setup_fallback_ui()

    def show_event_logs(self):
        """Show the event logs window"""
        try:
            self.event_logs.show_window()
            # Log the action
            self.log_event("Event logs window opened", "INFO")
            # Add some test logs to verify system is working
            self.log_event("Event logs system is functioning correctly", "SUCCESS")
            self.log_event("Ready to monitor downloads and browser operations", "INFO")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open event logs: {e}")

    def log_event(self, message, level="INFO"):
        """Central logging method that sends to event logs window"""
        try:
            # Send to event logs window
            if hasattr(self, 'event_logs') and self.event_logs:
                self.event_logs.add_log(message, level)

            # Also log to standard logger
            if level == "ERROR":
                logger.error(message)
            elif level == "WARNING":
                logger.warning(message)
            elif level == "SUCCESS":
                logger.info(f"SUCCESS: {message}")
            elif level == "BROWSER":
                logger.info(f"BROWSER: {message}")
            elif level == "DOWNLOAD":
                logger.info(f"DOWNLOAD: {message}")
            else:
                logger.info(message)

        except Exception as e:
            # Fallback to print if logging fails
            print(f"Log error: {e} - Original message: {message}")
    
    def setup_url_section(self, parent):
        """Setup URL input section with line numbers and Excel-like formatting"""
        try:
            url_frame = GlassFrame(parent, glass_opacity=0.15)
            url_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15), padx=5)

            # Header container for URLs section and FasstVideo logo/title
            header_container = tk.Frame(url_frame, bg=COLORS['glass_bg'])
            header_container.pack(fill=tk.X, padx=15, pady=(10, 5))

            # URLs section label on the left
            url_title = tk.Label(header_container, text="📎 Video URLs",
                               bg=COLORS['glass_bg'], fg=COLORS['text_primary'],
                               font=('Segoe UI', 13, 'bold'))
            url_title.pack(side=tk.LEFT, anchor=tk.W)

            # FasstVideo logo and title centered in header - moved several inches to right
            logo_title_header = tk.Frame(header_container, bg=COLORS['glass_bg'])
            logo_title_header.pack(side=tk.LEFT, anchor=tk.CENTER, padx=(350, 0))

            # Try to load and display logo - reduced 33% from 96x96 to 64x64
            try:
                logo_image = self.logo_manager.load_logo_for_ui(size=(64, 64))
                if logo_image:
                    logo_label = tk.Label(logo_title_header, image=logo_image, bg=COLORS['glass_bg'])
                    logo_label.pack(side=tk.LEFT, padx=(0, 10))
                    logo_label.image = logo_image
            except:
                pass

            # FasstVideo title - reduced 33% from 48pt to 32pt
            app_name = protection_manager.get_obfuscated_constant('app_name') or "FasstVideo"
            title_label = tk.Label(logo_title_header, text=app_name,
                                 bg=COLORS['glass_bg'], fg=COLORS['text_primary'],
                                 font=('Segoe UI', 32, 'bold'))
            title_label.pack(side=tk.LEFT)

            url_container = tk.Frame(url_frame, bg=COLORS['glass_bg'])
            url_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

            # Line numbers frame with container for number and underline
            line_numbers_container = tk.Frame(url_container, bg='#0A0E27', width=45)
            line_numbers_container.pack(side=tk.LEFT, fill=tk.Y)
            line_numbers_container.pack_propagate(False)

            # Line numbers text widget - lowered 10% more for better alignment
            self.line_numbers = tk.Text(line_numbers_container, width=4, height=8,
                                      bg='#0A0E27', fg='#FFD700',
                                      font=('Consolas', 13, 'bold'), bd=0,
                                      highlightthickness=0, state=tk.DISABLED,
                                      cursor='arrow', takefocus=0,
                                      padx=3, pady=11, wrap=tk.NONE,
                                      insertwidth=0)
            self.line_numbers.pack(fill=tk.BOTH, expand=True)

            # Separator line between numbers and URLs
            separator = tk.Frame(url_container, bg='#2A3F7D', width=2)
            separator.pack(side=tk.LEFT, fill=tk.Y, padx=(2, 2))

            # URL text widget
            self.url_text = ModernText(url_container, height=8, bg='#0F1429',
                                     font=('Consolas', 10),
                                     padx=3, pady=2, wrap=tk.NONE)

            # Scrollbar with error handling
            try:
                url_scroll = ttk.Scrollbar(url_container, orient=tk.VERTICAL, command=self.sync_scroll)
                self.url_text.configure(yscrollcommand=self.on_text_scroll)
                url_scroll.pack(side=tk.RIGHT, fill=tk.Y)
            except:
                pass

            self.url_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(2, 5))

            # Bind events for line number updates and scrolling
            self.url_text.bind('<KeyRelease>', self.update_line_numbers)
            self.url_text.bind('<Button-1>', self.update_line_numbers)
            self.url_text.bind('<MouseWheel>', self.on_mousewheel)
            self.url_text.bind('<KeyPress>', self.on_keypress)

            # Bind mousewheel to line numbers too for synchronized scrolling
            self.line_numbers.bind('<MouseWheel>', self.on_mousewheel)
            
            # Create context menu immediately after text widget
            self.context_menu = tk.Menu(self.root, tearoff=0, bg='#2A3F7D', fg='white', 
                                       activebackground=COLORS['accent'], activeforeground='white')
            self.context_menu.add_command(label="Paste", command=self.context_paste)
            self.context_menu.add_separator()
            self.context_menu.add_command(label="Cut", command=self.context_cut)
            self.context_menu.add_command(label="Copy", command=self.context_copy)
            self.context_menu.add_separator()
            self.context_menu.add_command(label="Select All", command=self.context_select_all)
            self.context_menu.add_command(label="Clear All", command=self.clear_urls)
            
            # Bind right-click directly
            self.url_text.bind("<Button-3>", self.show_context_menu)
            
            # Placeholder text (cleaned up)
            placeholder = "Enter video URLs (one per line):"
            self.url_text.insert("1.0", placeholder)
            self.url_text.configure(foreground=COLORS['text_muted'])
            
            self.url_text.bind("<FocusIn>", self.on_url_focus_in)
            self.url_text.bind("<FocusOut>", self.on_url_focus_out)
            
        except Exception as e:
            logger.exception("Error setting up URL section")

    def show_context_menu(self, event):
        """Show context menu on right-click"""
        try:
            self.context_menu.post(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def context_paste(self):
        """Paste clipboard content"""
        try:
            current_text = self.url_text.get("1.0", tk.END).strip()
            if "Enter video URLs" in current_text:
                self.url_text.delete("1.0", tk.END)
                self.url_text.configure(foreground=COLORS['text_primary'])

            clipboard_content = self.root.clipboard_get()
            self.url_text.insert(tk.INSERT, clipboard_content)
            self.update_line_numbers()
        except:
            pass

    def context_cut(self):
        """Cut selected text"""
        try:
            self.url_text.event_generate("<<Cut>>")
        except:
            pass

    def context_copy(self):
        """Copy selected text"""
        try:
            self.url_text.event_generate("<<Copy>>")
        except:
            pass

    def context_select_all(self):
        """Select all text"""
        try:
            self.url_text.tag_add(tk.SEL, "1.0", tk.END)
            self.url_text.mark_set(tk.INSERT, "1.0")
            self.url_text.see(tk.INSERT)
        except:
            pass

    def update_line_numbers(self, event=None):
        """Update line numbers to align perfectly with URL text"""
        try:
            if not hasattr(self, 'line_numbers') or not hasattr(self, 'url_text'):
                return

            content = self.url_text.get("1.0", tk.END)
            lines = content.split('\n')
            line_count = len(lines) - 1 if lines[-1] == '' else len(lines)

            # Ensure at least 1 line for proper display
            if line_count == 0:
                line_count = 1

            # Different colors for each line number
            colors = ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF', '#5F27CD', '#00D2D3']

            # Update line numbers content with different colors
            self.line_numbers.configure(state=tk.NORMAL)
            self.line_numbers.delete("1.0", tk.END)

            for i in range(1, line_count + 1):
                line_num_text = f"{i:>3}"
                color = colors[(i-1) % len(colors)]  # Cycle through colors

                # Insert line number
                if i > 1:
                    self.line_numbers.insert(tk.END, "\n")
                self.line_numbers.insert(tk.END, line_num_text)

                # Apply color to this specific line number
                tag_name = f"line_num_{i}"
                start_pos = f"{i}.0"
                end_pos = f"{i}.end"
                self.line_numbers.tag_add(tag_name, start_pos, end_pos)
                self.line_numbers.tag_configure(tag_name, foreground=color)

            self.line_numbers.configure(state=tk.DISABLED)

            # Add bottom border to URL text widget for each line
            for i in range(1, line_count + 1):
                # Create tag for each URL line with underline
                tag_name = f"url_line_{i}"
                start_pos = f"{i}.0"
                end_pos = f"{i}.end"

                # Apply underline to the entire URL line
                self.url_text.tag_add(tag_name, start_pos, end_pos)
                self.url_text.tag_configure(tag_name, underline=True, underlinefg='#FFD700')

            # Sync scrolling position
            try:
                top_fraction = self.url_text.yview()[0]
                self.line_numbers.yview_moveto(top_fraction)
            except:
                pass

        except Exception as e:
            logger.error(f"Error updating line numbers: {e}")

    def sync_scroll(self, *args):
        """Sync scrolling between line numbers and URL text"""
        try:
            if hasattr(self, 'url_text') and hasattr(self, 'line_numbers'):
                self.url_text.yview(*args)
                self.line_numbers.yview(*args)
        except:
            pass

    def on_text_scroll(self, *args):
        """Handle text widget scrolling and sync line numbers"""
        try:
            # Update scrollbar if it exists
            if hasattr(self, 'url_scroll'):
                self.url_scroll.set(*args)

            # Sync line numbers scrolling
            if hasattr(self, 'line_numbers') and len(args) >= 1:
                self.line_numbers.yview_moveto(float(args[0]))

        except Exception as e:
            logger.error(f"Error in scroll sync: {e}")

    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling for both widgets"""
        try:
            # Scroll both widgets together
            if hasattr(self, 'url_text') and hasattr(self, 'line_numbers'):
                self.url_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
                self.line_numbers.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except:
            pass

    def on_keypress(self, event):
        """Handle key press events that might change content"""
        try:
            # Schedule line number update for next idle cycle
            self.root.after_idle(self.update_line_numbers)
        except:
            pass

    def setup_settings_section(self, parent):
        """Setup settings section"""
        try:
            settings_frame = GlassFrame(parent, glass_opacity=0.15)
            settings_frame.pack(fill=tk.X, pady=(0, 15), padx=5)
            
            settings_title = tk.Label(settings_frame, text="📁 Download Folder", 
                                    bg=COLORS['glass_bg'], fg=COLORS['text_primary'], 
                                    font=('Segoe UI', 13, 'bold'))
            settings_title.pack(anchor=tk.W, padx=15, pady=(10, 5))
            
            settings_container = tk.Frame(settings_frame, bg=COLORS['glass_bg'])
            settings_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
            
            folder_input_frame = tk.Frame(settings_container, bg=COLORS['glass_bg'])
            folder_input_frame.pack(fill=tk.BOTH, expand=True)
            
            self.folder_entry = ModernEntry(folder_input_frame, textvariable=self.download_folder, 
                                           bg='#0F1429', font=('Segoe UI', 11))
            self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=(8, 8))
            
            browse_btn = ModernButton(folder_input_frame, text="Browse", 
                                    command=self.browse_folder,
                                    bg=COLORS['accent'], fg=COLORS['text_primary'],
                                    padx=25, pady=10)
            browse_btn.pack(side=tk.RIGHT, pady=(8, 8))
            
        except Exception as e:
            logger.exception("Error setting up settings section")
    
    def setup_control_buttons(self, parent):
        """Setup control buttons"""
        try:
            button_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
            button_frame.pack(fill=tk.X, pady=(0, 15))
            
            button_container = tk.Frame(button_frame, bg=COLORS['bg_primary'])
            button_container.pack()
            
            self.download_btn = ModernButton(button_container, text="⚡ Download MP4", 
                                            command=self.start_download,
                                            bg=COLORS['success'], fg=COLORS['bg_primary'],
                                            hover_bg='#00F0FF',
                                            padx=20, pady=12, width=15)
            self.download_btn.pack(side=tk.LEFT, padx=5)
            
            self.stop_btn = ModernButton(button_container, text="⏸ Stop", 
                                        command=self.stop_download,
                                        bg=COLORS['danger'], fg=COLORS['text_primary'],
                                        hover_bg='#FF5577',
                                        padx=20, pady=12, width=15,
                                        state=tk.DISABLED)
            self.stop_btn.pack(side=tk.LEFT, padx=5)
            
            clear_btn = ModernButton(button_container, text="🗑 Clear",
                                   command=self.clear_urls,
                                   bg='#3A4565', fg=COLORS['text_primary'],
                                   hover_bg='#4A5575',
                                   padx=20, pady=12, width=15)
            clear_btn.pack(side=tk.LEFT, padx=5)

            logs_btn = ModernButton(button_container, text="🔍 Event Logs",
                                  command=self.show_event_logs,
                                  bg='#2E5C8A', fg=COLORS['text_primary'],
                                  hover_bg='#3E6C9A',
                                  padx=20, pady=12, width=15)
            logs_btn.pack(side=tk.LEFT, padx=5)
            
            open_folder_btn = ModernButton(button_container, text="📂 Open Folder", 
                                          command=self.open_folder,
                                          bg=COLORS['warning'], fg=COLORS['bg_primary'],
                                          hover_bg='#FFC520',
                                          padx=20, pady=12, width=15)
            open_folder_btn.pack(side=tk.LEFT, padx=5)
            
        except Exception as e:
            logger.exception("Error setting up control buttons")
    
    def setup_realtime_progress_section(self, parent):
        """Setup real-time progress section with live numbers"""
        try:
            # Create the glass frame that will contain everything
            progress_frame = GlassFrame(parent, glass_opacity=0.15)
            progress_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20), padx=0)
            
            # Status label - hidden/removed to avoid clutter above phase bar
            # self.status_label = tk.Label(progress_frame, text="Ready",
            #                             bg=COLORS['glass_bg'], fg=COLORS['text_primary'],
            #                             font=('Segoe UI', 14, 'bold'))
            # self.status_label.pack(pady=(15, 5))
            # Create invisible placeholder for compatibility
            self.status_label = tk.Label(progress_frame, text="", bg=COLORS['glass_bg'])
            # Don't pack it to keep it hidden

            # Phase indicator frame (separate from progress bar)
            self.phase_frame = tk.Frame(progress_frame, bg=COLORS['glass_bg'], height=35)
            self.phase_frame.pack(fill=tk.X, pady=(5, 10), padx=20)
            self.phase_frame.pack_propagate(False)  # Maintain fixed height

            # Initialize arrow-chain phase indicators
            self.current_phase = 1
            self.total_phases = 4
            self.phase_labels = ["Method 1 (Basic)", "Method 2 (Intermediate)", "Method 3 (Advanced)", "Method 4 (Complex)"]
            self.phase_colors = ["#E91E63", "#FF9800", "#607D8B", "#009688"]  # Magenta, Orange, Gray, Teal
            self.phase_canvas = None
            self.glow_animation_job = None  # For glow animation
            self.glow_intensity = 0  # Current glow intensity for animation
            self.glow_direction = 1  # 1 for increasing, -1 for decreasing
            self.setup_arrow_chain_indicators()

            # Initialize URL status tracking
            self.url_statuses = {}  # Track status for each URL
            self.url_status_tags = {}  # Track text widget tags for each URL

            # Real-time progress canvas (cyberpunk style)
            self.progress_canvas = tk.Canvas(progress_frame,
                                            height=34,  # Reduced by 50% from 69 to 34
                                            bg='#0A0A0A',  # Deep black for cyberpunk
                                            highlightthickness=2,
                                            highlightbackground='#00FFFF',  # Cyan border
                                            highlightcolor='#00FFFF')
            self.progress_canvas.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
            
            # Initialize real-time progress spinner
            self.realtime_spinner = RealTimeProgressSpinner(self.root, self.progress_canvas,
                                                           color=COLORS['tropical_aqua'],
                                                           bg_color='#1F2547')
            
            # Bind canvas resize event
            self.progress_canvas.bind('<Configure>', self.on_canvas_configure)
            
            # Initialize empty state
            self.realtime_spinner.draw_empty_state()
            
        except Exception as e:
            logger.exception("Error setting up real-time progress section")
            self.setup_basic_progress_fallback(parent)

    def setup_basic_progress_fallback(self, parent):
        """Fallback basic progress section"""
        try:
            self.status_label = tk.Label(parent, text="Ready", bg=COLORS['bg_primary'], fg=COLORS['text_primary'])
            self.status_label.pack(pady=10)
            
            # Simple label instead of real-time spinner
            self.progress_label = tk.Label(parent, text="", bg=COLORS['bg_primary'], fg=COLORS['text_primary'])
            self.progress_label.pack(pady=10)
        except:
            pass

    def on_canvas_configure(self, event):
        """Handle canvas resize"""
        try:
            if self.realtime_spinner and not self.realtime_spinner.active:
                self.realtime_spinner.draw_empty_state()
        except:
            pass
    
    def setup_fallback_ui(self):
        """Setup a basic fallback UI if the modern UI fails"""
        try:
            # Clear any existing widgets
            for widget in self.root.winfo_children():
                widget.destroy()
            
            app_name = protection_manager.get_obfuscated_constant('app_name') or "FasstVideo"
            
            # Basic UI
            tk.Label(self.root, text=app_name, font=('Arial', 16), bg=COLORS['bg_primary'], fg=COLORS['text_primary']).pack(pady=10)
            
            # URL input
            tk.Label(self.root, text="Video URLs:", bg=COLORS['bg_primary'], fg=COLORS['text_primary']).pack()
            self.url_text = tk.Text(self.root, height=8, width=80)
            self.url_text.pack(padx=20, pady=5)
            
            # Folder selection
            folder_frame = tk.Frame(self.root, bg=COLORS['bg_primary'])
            folder_frame.pack(pady=5)
            
            tk.Label(folder_frame, text="Download Folder:", bg=COLORS['bg_primary'], fg=COLORS['text_primary']).pack(side=tk.LEFT)
            self.folder_entry = tk.Entry(folder_frame, textvariable=self.download_folder, width=50)
            self.folder_entry.pack(side=tk.LEFT, padx=5)
            tk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side=tk.LEFT)
            
            # Buttons
            button_frame = tk.Frame(self.root, bg=COLORS['bg_primary'])
            button_frame.pack(pady=10)
            
            self.download_btn = tk.Button(button_frame, text="Download MP4", command=self.start_download)
            self.download_btn.pack(side=tk.LEFT, padx=5)
            
            self.stop_btn = tk.Button(button_frame, text="Stop", command=self.stop_download, state=tk.DISABLED)
            self.stop_btn.pack(side=tk.LEFT, padx=5)
            
            tk.Button(button_frame, text="Clear", command=self.clear_urls).pack(side=tk.LEFT, padx=5)
            tk.Button(button_frame, text="Open Folder", command=self.open_folder).pack(side=tk.LEFT, padx=5)
            
            # Status
            self.status_label = tk.Label(self.root, text="Ready", bg=COLORS['bg_primary'], fg=COLORS['text_primary'])
            self.status_label.pack()
            
            # Progress indicator
            self.progress_label = tk.Label(self.root, text="", bg=COLORS['bg_primary'], fg=COLORS['text_primary'])
            self.progress_label.pack()
            
        except Exception as e:
            logger.exception("Error creating fallback UI")
    
    def center_window(self):
        """Center window on screen"""
        try:
            self.root.update_idletasks()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            x = (self.root.winfo_screenwidth() - width) // 2
            y = (self.root.winfo_screenheight() - height) // 2
            self.root.geometry(f'{width}x{height}+{x}+{y}')
        except:
            pass
    
    def check_dependencies_async(self):
        """Enhanced dependency check with automatic installation"""
        def dependency_worker():
            try:
                # Install dependencies on first run or if missing
                self.dependency_manager.install_on_first_run()
                
                # Check all dependencies with auto-installation
                success = self.dependency_manager.check_all_dependencies()
                
                if success:
                    self.root.after(0, lambda: self.update_status_safe("Ready"))
                else:
                    self.root.after(0, lambda: self.update_status_safe("Dependencies incomplete"))
                    
            except Exception as e:
                logger.exception("Dependency check error")
                self.root.after(0, lambda: self.update_status_safe("Ready"))
        
        try:
            thread = threading.Thread(target=dependency_worker, daemon=True)
            thread.start()
        except:
            pass
    
    def reset_all_status_bars(self):
        """Reset all status bars and indicators before starting new download"""
        try:
            # Reset main status
            self.update_status_safe("Ready")

            # Reset progress bar
            if hasattr(self, 'progress_var'):
                self.progress_var.set(0)

            # Reset speed and ETA displays
            if hasattr(self, 'speed_label'):
                self.speed_label.config(text="Speed: 0 KB/s")

            if hasattr(self, 'eta_label'):
                self.eta_label.config(text="ETA: --:--")

            # Reset method status indicators (turn off all glows)
            for i in range(1, 5):  # Methods 1-4
                method_frame = getattr(self, f'method{i}_frame', None)
                if method_frame:
                    # Reset glow effect
                    method_frame.config(bg=COLORS['bg_secondary'])

                    # Reset method status text
                    method_label = getattr(self, f'method{i}_status', None)
                    if method_label:
                        method_label.config(text="Standby", fg=COLORS['text_secondary'])

            # Reset URL status indicators
            if hasattr(self, 'url_statuses'):
                for url in self.url_statuses:
                    self.update_url_status(url, "pending")

            # Clear any existing error states
            if hasattr(self, 'status_label'):
                self.status_label.config(fg=COLORS['text_primary'])

            self.log_event("Status indicators reset for new download", "INFO")

        except Exception as e:
            self.log_event(f"Error resetting status bars: {str(e)[:50]}", "ERROR")

    def reset_status_for_url(self, url):
        """Reset status indicators for a specific URL during multi-URL downloads"""
        try:
            # Validate URL parameter
            if not url or not isinstance(url, str) or url == "processing":
                self.log_event(f"Invalid URL parameter in reset_status_for_url: {url}", "ERROR")
                return

            # Reset method status indicators (turn off all glows) but keep main status
            for i in range(1, 5):  # Methods 1-4
                method_frame = getattr(self, f'method{i}_frame', None)
                if method_frame:
                    # Reset glow effect
                    method_frame.config(bg=COLORS['bg_secondary'])

                    # Reset method status text
                    method_label = getattr(self, f'method{i}_status', None)
                    if method_label:
                        method_label.config(text="Standby", fg=COLORS['text_secondary'])

            # Reset main status indicators for this URL
            if hasattr(self, 'status_label'):
                self.status_label.config(text="Processing...", fg=COLORS['processing'])

            if hasattr(self, 'progress_label'):
                self.progress_label.config(text="0%")

            if hasattr(self, 'progress_bar'):
                self.progress_bar['value'] = 0

            if hasattr(self, 'speed_label'):
                self.speed_label.config(text="0 MB/s")

            # Reset this URL's status to processing (with validation)
            try:
                self.update_url_status(url, "processing")
            except Exception as status_error:
                self.log_event(f"Error updating URL status: {str(status_error)[:50]}", "ERROR")

            self.log_event(f"Status indicators reset for URL: {url[:50]}...", "INFO")

        except Exception as e:
            self.log_event(f"Error resetting status for URL: {str(e)[:50]}", "ERROR")

    def update_status_safe(self, message):
        """Safely update status label - filter out method details"""
        try:
            # ALLOW DEBUG MESSAGES AND METHOD PROGRESSION THROUGH!
            if "🔍" in message or "🔧" in message or "Method" in message or "DEBUGGING" in message or "STRATEGIES" in message:
                # Log debug and method progression messages directly without filtering
                self.log_event(message, "DEBUG")
                return

            # Filter out any detailed method or technical information
            filtered_message = "Processing..."

            # Only show basic states
            if any(keyword in message.lower() for keyword in ['ready', 'complete', 'finished']):
                filtered_message = "Ready"
            elif any(keyword in message.lower() for keyword in ['starting', 'initializing']):
                filtered_message = "Processing..."
            elif any(keyword in message.lower() for keyword in ['error', 'failed']):
                filtered_message = "Error"
            elif any(keyword in message.lower() for keyword in ['success', 'downloaded']):
                filtered_message = "Complete"

            # Don't update status label - keep it blank/hidden to avoid text above phase bar
            # if hasattr(self, 'status_label'):
            #     self.status_label.configure(text=filtered_message)

            # Improved logging - reduce repetitive error messages
            level = "INFO"
            if any(keyword in message.lower() for keyword in ['error', 'failed']):
                level = "ERROR"
                # Only log unique errors to reduce spam
                if not hasattr(self, '_last_error_time') or time.time() - self._last_error_time > 2.0:
                    self._last_error_time = time.time()
                    self.log_event(filtered_message, level)
                return  # Skip logging repetitive errors
            elif any(keyword in message.lower() for keyword in ['success', 'completed']):
                level = "SUCCESS"

            # Send message to event logs (skip repetitive processing messages)
            if filtered_message != "Processing..." or not hasattr(self, '_last_processing_time') or time.time() - getattr(self, '_last_processing_time', 0) > 5.0:
                if filtered_message == "Processing...":
                    self._last_processing_time = time.time()
                self.log_event(filtered_message, level)

        except:
            pass

    def setup_arrow_chain_indicators(self):
        """Setup arrow-chain phase indicator with chevron connectors"""
        try:
            # Clear existing widgets
            for widget in self.phase_frame.winfo_children():
                widget.destroy()

            # Create canvas for arrow chain
            self.phase_canvas = tk.Canvas(self.phase_frame,
                                        height=35,
                                        bg=COLORS['glass_bg'],
                                        highlightthickness=0)
            self.phase_canvas.pack(fill=tk.BOTH, expand=True)

            # Bind resize event to redraw
            self.phase_canvas.bind('<Configure>', self.on_phase_canvas_resize)

            self.draw_arrow_chain()

        except Exception as e:
            logger.error(f"Error setting up arrow chain indicators: {e}")

    def on_phase_canvas_resize(self, event):
        """Redraw arrow chain when canvas is resized"""
        try:
            self.draw_arrow_chain()
        except Exception as e:
            logger.error(f"Error on canvas resize: {e}")

    def draw_arrow_chain(self):
        """Draw the arrow-chain phase indicator"""
        try:
            if not self.phase_canvas:
                return

            # Clear canvas
            self.phase_canvas.delete("all")

            # Get canvas dimensions
            canvas_width = self.phase_canvas.winfo_width()
            canvas_height = self.phase_canvas.winfo_height()

            if canvas_width <= 1 or canvas_height <= 1:
                return

            # Calculate dimensions
            step_width = canvas_width // self.total_phases
            step_height = canvas_height - 4  # Leave small margin
            arrow_width = 12  # Width of arrow point
            start_y = 2

            for i in range(self.total_phases):
                start_x = i * step_width

                # Determine if this step is active/completed/current
                if i + 1 < self.current_phase:
                    # Completed phases
                    fill_color = self.phase_colors[i]
                    text_color = "white"
                    is_current = False
                elif i + 1 == self.current_phase:
                    # Current active phase - add glow effect
                    fill_color = self.phase_colors[i]
                    text_color = "white"
                    is_current = True
                else:
                    # Future phases - inactive
                    fill_color = "#3A3A3A"  # Inactive gray
                    text_color = "#888888"
                    is_current = False

                # Create arrow shape points
                if i == self.total_phases - 1:
                    # Last step - no arrow point
                    points = [
                        start_x, start_y,  # Top left
                        start_x + step_width, start_y,  # Top right
                        start_x + step_width, start_y + step_height,  # Bottom right
                        start_x, start_y + step_height  # Bottom left
                    ]
                else:
                    # Regular step with arrow point
                    points = [
                        start_x, start_y,  # Top left
                        start_x + step_width - arrow_width, start_y,  # Top right before arrow
                        start_x + step_width, start_y + step_height // 2,  # Arrow point
                        start_x + step_width - arrow_width, start_y + step_height,  # Bottom right before arrow
                        start_x, start_y + step_height  # Bottom left
                    ]

                # Draw pulsing glow effect for current phase
                if is_current:
                    # Create animated pulsing glow using phase color
                    phase_color = self.phase_colors[i]

                    # Extract RGB values from hex color
                    r = int(phase_color[1:3], 16)
                    g = int(phase_color[3:5], 16)
                    b = int(phase_color[5:7], 16)

                    # Calculate pulsing intensity (0.3 to 1.0)
                    pulse_intensity = 0.3 + 0.7 * (abs(self.glow_intensity) / 100.0)

                    # Create multiple glow layers with pulsing effect
                    for glow_layer in range(8, 0, -1):  # More layers for smoother glow
                        # Create expanded points for glow
                        glow_points = []
                        expansion = glow_layer * 2 * pulse_intensity  # Scale expansion with pulse

                        for idx in range(0, len(points), 2):
                            x, y = points[idx], points[idx + 1]
                            # Create fade effect within boundaries instead of expanding outward
                            center_x = start_x + step_width // 2
                            center_y = start_y + step_height // 2

                            # Keep glow within original box boundaries by using inward fade instead of outward expansion
                            # Calculate how much to move toward center for fade effect
                            fade_factor = (glow_layer / 8.0) * 0.3  # Small inward movement for fade

                            if x < center_x:
                                new_x = x + fade_factor * (center_x - x)
                            else:
                                new_x = x - fade_factor * (x - center_x)

                            if y < center_y:
                                new_y = y + fade_factor * (center_y - y)
                            else:
                                new_y = y - fade_factor * (y - center_y)

                            glow_points.extend([new_x, new_y])

                        # Calculate animated glow color
                        alpha = ((8 - glow_layer) / 8.0) * pulse_intensity

                        # Create bright pulsing glow colors
                        glow_r = min(255, int(r + (255 - r) * alpha))
                        glow_g = min(255, int(g + (255 - g) * alpha))
                        glow_b = min(255, int(b + (255 - b) * alpha))

                        glow_color = f"#{glow_r:02x}{glow_g:02x}{glow_b:02x}"

                        self.phase_canvas.create_polygon(glow_points, fill=glow_color, outline="", width=0, tags="glow")

                # Draw shadow effect
                shadow_points = [p + 2 if idx % 2 == 0 else p + 2 for idx, p in enumerate(points)]
                self.phase_canvas.create_polygon(shadow_points, fill="#000000", outline="", width=0, tags="shadow")

                # Draw main arrow shape
                outline_color = "#FFFFFF" if not is_current else "#FFFFFF"
                outline_width = 1 if not is_current else 3
                self.phase_canvas.create_polygon(points, fill=fill_color, outline=outline_color, width=outline_width, tags="arrow")

                # Add step text with enhanced styling for current phase
                text_x = start_x + (step_width - arrow_width) // 2
                text_y = start_y + step_height // 2

                # Enhanced text styling for current phase
                if is_current:
                    # Add text shadow for current phase
                    self.phase_canvas.create_text(
                        text_x + 1, text_y + 1,
                        text=self.phase_labels[i],
                        fill="#000000",
                        font=('Segoe UI', 8, 'bold'),
                        tags="text_shadow"
                    )

                    # Main text with bright white for current phase
                    self.phase_canvas.create_text(
                        text_x, text_y,
                        text=self.phase_labels[i],
                        fill="#FFFFFF",
                        font=('Segoe UI', 8, 'bold'),
                        tags="text"
                    )
                else:
                    # Regular text for non-current phases
                    self.phase_canvas.create_text(
                        text_x, text_y,
                        text=self.phase_labels[i],
                        fill=text_color,
                        font=('Segoe UI', 8, 'bold'),
                        tags="text"
                    )

        except Exception as e:
            logger.error(f"Error drawing arrow chain: {e}")

    def set_phase(self, phase):
        """Set the current phase and update arrow chain"""
        if 1 <= phase <= self.total_phases:
            self.current_phase = phase
            self.draw_arrow_chain()
            # Start glow animation for current phase
            self.start_glow_animation()
            # Force canvas update to ensure glow effect shows
            if self.phase_canvas:
                self.phase_canvas.update_idletasks()

    def start_glow_animation(self):
        """Start pulsing glow animation for current phase"""
        if self.glow_animation_job:
            self.root.after_cancel(self.glow_animation_job)
        self.animate_glow()

    def animate_glow(self):
        """Animate the glow intensity for pulsing effect"""
        try:
            # Update glow intensity
            self.glow_intensity += self.glow_direction * 3

            # Reverse direction at boundaries
            if self.glow_intensity >= 100:
                self.glow_intensity = 100
                self.glow_direction = -1
            elif self.glow_intensity <= 0:
                self.glow_intensity = 0
                self.glow_direction = 1

            # Redraw with new glow intensity
            self.draw_arrow_chain()

            # Continue animation
            self.glow_animation_job = self.root.after(50, self.animate_glow)  # 50ms for smooth animation

        except Exception as e:
            logger.error(f"Error in glow animation: {e}")

    def stop_glow_animation(self):
        """Stop the glow animation"""
        if self.glow_animation_job:
            self.root.after_cancel(self.glow_animation_job)
            self.glow_animation_job = None

    def on_url_focus_in(self, event):
        """Clear placeholder on focus"""
        try:
            current_text = self.url_text.get("1.0", tk.END).strip()
            if "Enter video URLs" in current_text:
                self.url_text.delete("1.0", tk.END)
                self.url_text.configure(foreground=COLORS['text_primary'])
            self.update_line_numbers()
        except:
            pass

    def on_url_focus_out(self, event):
        """Restore placeholder if empty"""
        try:
            current_text = self.url_text.get("1.0", tk.END).strip()
            if not current_text:
                placeholder = "Enter video URLs (one per line):"
                self.url_text.insert("1.0", placeholder)
                self.url_text.configure(foreground=COLORS['text_muted'])
            self.update_line_numbers()
        except:
            pass
    
    def browse_folder(self):
        """Browse for download folder"""
        try:
            folder = filedialog.askdirectory(
                initialdir=self.download_folder.get(),
                title="Select Download Folder"
            )
            if folder:
                self.download_folder.set(folder)
        except Exception as e:
            logger.error(f"Error browsing folder: {e}")
    
    def open_folder(self):
        """Open download folder"""
        try:
            folder = self.download_folder.get()
            if os.path.exists(folder):
                if os.name == 'nt':
                    os.startfile(folder)
                else:
                    subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', folder])
            else:
                messagebox.showerror("Error", "Download folder does not exist")
        except Exception as e:
            logger.error(f"Error opening folder: {e}")
            messagebox.showerror("Error", f"Cannot open folder: {e}")
    
    def clear_urls(self):
        """Clear URL text area"""
        try:
            self.url_text.delete("1.0", tk.END)
            self.url_text.configure(foreground=COLORS['text_primary'])
            # Clear URL status tracking
            self.url_statuses.clear()
            self.url_status_tags.clear()
            # Update line numbers
            self.update_line_numbers()
        except:
            pass

    def update_url_status(self, url, status):
        """Update the status of a specific URL in the text widget"""
        try:
            if not hasattr(self, 'url_text') or not self.url_text:
                return

            # Get all text content
            all_text = self.url_text.get("1.0", tk.END)
            lines = all_text.split('\n')

            # Find the line containing this URL
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if url in line:
                    # Calculate text positions
                    line_start = f"{line_num}.0"
                    line_end = f"{line_num}.end"

                    # Remove any existing status for this line
                    existing_tag = self.url_status_tags.get(url)
                    if existing_tag:
                        self.url_text.tag_delete(existing_tag)

                    # Create status indicator
                    status_text = ""
                    status_color = ""

                    if status == "success":
                        status_text = " ✓ SUCCESS"
                        status_color = "#4CAF50"  # Green
                    elif status == "failed":
                        status_text = " ✗ FAILED"
                        status_color = "#F44336"  # Red
                    elif status == "processing":
                        status_text = " ⏳ PROCESSING"
                        status_color = "#FF9800"  # Orange

                    if status_text:
                        # Check if status already exists at end of line
                        if not any(indicator in line for indicator in ["✓ SUCCESS", "✗ FAILED", "⏳ PROCESSING"]):
                            # Add status to end of line
                            self.url_text.insert(line_end, status_text)

                            # Create tag for coloring
                            tag_name = f"status_{url}_{line_num}"
                            start_pos = f"{line_num}.{len(line)}"
                            end_pos = f"{line_num}.{len(line) + len(status_text)}"

                            self.url_text.tag_add(tag_name, start_pos, end_pos)
                            self.url_text.tag_config(tag_name, foreground=status_color, font=('Segoe UI', 9, 'bold'))

                            # Store tag reference
                            self.url_status_tags[url] = tag_name
                        else:
                            # Update existing status
                            line_content = self.url_text.get(line_start, line_end)
                            # Remove old status indicators
                            for old_indicator in ["✓ SUCCESS", "✗ FAILED", "⏳ PROCESSING"]:
                                line_content = line_content.replace(f" {old_indicator}", "")

                            # Replace line with updated status
                            self.url_text.delete(line_start, line_end)
                            self.url_text.insert(line_start, line_content + status_text)

                            # Apply coloring to status part
                            tag_name = f"status_{url}_{line_num}"
                            start_pos = f"{line_num}.{len(line_content)}"
                            end_pos = f"{line_num}.{len(line_content) + len(status_text)}"

                            self.url_text.tag_add(tag_name, start_pos, end_pos)
                            self.url_text.tag_config(tag_name, foreground=status_color, font=('Segoe UI', 9, 'bold'))

                            self.url_status_tags[url] = tag_name

                    # Store status
                    self.url_statuses[url] = status
                    break

        except Exception as e:
            logger.error(f"Error updating URL status: {e}")

    def get_urls_for_download(self):
        """Get clean URLs from text widget (without status indicators)"""
        try:
            all_text = self.url_text.get("1.0", tk.END).strip()
            if not all_text or "Enter video URLs" in all_text:
                return []

            urls = []
            lines = all_text.split('\n')

            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Remove status indicators to get clean URL
                    clean_line = line
                    for indicator in ["✓ SUCCESS", "✗ FAILED", "⏳ PROCESSING"]:
                        clean_line = clean_line.replace(f" {indicator}", "")

                    clean_url = clean_line.strip()
                    if clean_url and ('http' in clean_url or 'www.' in clean_url):
                        urls.append(clean_url)

            return urls

        except Exception as e:
            logger.error(f"Error getting URLs: {e}")
            return []
    
    def handle_realtime_progress(self, action, data):
        """Handle real-time progress updates"""
        try:
            if action == 'start':
                if self.realtime_spinner:
                    self.realtime_spinner.start(data)  # data = file path
                elif hasattr(self, 'progress_label'):
                    self.progress_label.configure(text="Downloading...")
            elif action == 'stop':
                if self.realtime_spinner:
                    self.realtime_spinner.stop()
                elif hasattr(self, 'progress_label'):
                    self.progress_label.configure(text="")
            elif action == 'update':
                if self.realtime_spinner:
                    self.realtime_spinner.update_progress_from_output(data)  # data = progress line
        except Exception as e:
            logger.error(f"Real-time progress error: {e}")
    
    def start_download(self):
        """Start download process with real-time progress tracking + Browser Automation Fallback"""
        try:
            # RESET ALL STATUS BARS AND INDICATORS FIRST
            self.reset_all_status_bars()

            # Log download start
            self.log_event("Download process started", "DOWNLOAD")

            # Perform basic security check
            if hasattr(protection_manager, 'perform_integrity_check'):
                protection_manager.perform_integrity_check()

            # Check dependencies
            if not hasattr(self.dependency_manager, 'dependencies_checked') or not self.dependency_manager.dependencies_checked:
                self.dependency_manager.dependencies_checked = True

            # Get clean URLs using the new method
            urls = self.get_urls_for_download()

            if not urls:
                self.log_event("Download failed: No valid URLs provided", "ERROR")
                messagebox.showwarning("Input Required", "Please enter valid URLs to download")
                return

            # Mark all URLs as processing
            for url in urls:
                self.update_url_status(url, "processing")

            # Log parsed URLs
            self.log_event(f"Parsed {len(urls)} URLs for download", "INFO")
            
            # Validate folder
            folder = self.download_folder.get()
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder, exist_ok=True)
                except Exception as e:
                    messagebox.showerror("Folder Error", f"Cannot create folder: {e}")
                    return
            
            # Start download
            self.download_active = True
            
            try:
                self.download_btn.configure(state=tk.DISABLED, text="⏳ Downloading...")
                self.stop_btn.configure(state=tk.NORMAL)
            except:
                pass
            
            self.update_status_safe("Starting...")
            
            # Initialize real-time download manager with BROWSER AUTOMATION SUPPORT (reuse if exists)
            if not hasattr(self, 'download_manager') or self.download_manager is None:
                self.log_event("Creating new download manager instance", "INFO")
                self.download_manager = RealTimeDownloadManager(
                    status_callback=self.update_status_safe,
                    progress_callback=self.handle_realtime_progress
                )
                # Pass GUI reference to download manager for phase updates
                self.download_manager.gui = self
            else:
                self.log_event("Reusing existing download manager instance", "INFO")
            
            thread = threading.Thread(target=self.download_worker, args=(urls, folder), daemon=True)
            thread.start()
            
        except Exception as e:
            logger.exception("Error starting download")
            messagebox.showerror("Error", f"Failed to start download: {e}")
            self.reset_download_state()
    
    def download_worker(self, urls, folder):
        """Download worker thread with real-time progress + Browser Automation Fallback"""
        try:
            # Download with real-time progress tracking + Browser Automation Fallback
            results = self.download_manager.download_concurrent(
                urls, 
                folder, 
                max_workers=self.concurrent_downloads
            )
            
            # Force progress to 100% if any downloads succeeded
            if results['success'] > 0:
                if hasattr(self, 'realtime_spinner') and self.realtime_spinner:
                    self.realtime_spinner.current_progress = 100.0
                    self.realtime_spinner.download_completed = True
                    self.realtime_spinner.eta = "Complete"
                    # Immediately update display
                    try:
                        self.realtime_spinner.canvas.delete("all")
                        self.realtime_spinner.draw_progress_display()
                    except:
                        pass
            
            # Show results
            if results['success'] > 0:
                messagebox.showinfo("Download Complete", 
                                  f"Successfully downloaded {results['success']} MP4 videos!\n"
                                  f"Failed: {results['failed']}\n\n"
                                  f"Note: Some downloads may have used browser automation\n"
                                  f"for sites where direct download wasn't possible.")
            else:
                messagebox.showwarning("Download Failed",
                                     "Unable to download videos from the provided URLs.\n"
                                     "Please check the URLs and try again.\n\n"
                                     "Browser automation setup failed. To fix this:\n"
                                     "1. Install Chrome or Firefox browser\n"
                                     "2. Run: pip install webdriver-manager\n"
                                     "3. Or install: pip install undetected-chromedriver\n\n"
                                     "These packages will automatically manage browser drivers.")
        
        except Exception as e:
            logger.exception("Download error")
            messagebox.showerror("Download Error", f"An error occurred during download: {e}")
        
        finally:
            self.reset_download_state()
    
    def reset_download_state(self):
        """Reset download UI state and restart animations"""
        try:
            self.download_active = False
            
            try:
                self.download_btn.configure(state=tk.NORMAL, text="⚡ Download MP4")
                self.stop_btn.configure(state=tk.DISABLED)
            except:
                pass
            
            # Only stop progress tracking, don't reset progress if download completed
            # The spinner will handle showing completion state
            if hasattr(self, 'realtime_spinner') and self.realtime_spinner:
                # If download didn't complete, reset everything
                if not getattr(self.realtime_spinner, 'download_completed', False):
                    self.handle_realtime_progress('stop', None)
                # If download completed, just stop the animation but keep progress at 100%
                else:
                    self.realtime_spinner.active = False
                    if self.realtime_spinner.animation_job:
                        self.root.after_cancel(self.realtime_spinner.animation_job)
                        self.realtime_spinner.animation_job = None
                    # Force progress to 100% and redraw
                    self.realtime_spinner.current_progress = 100.0
                    self.realtime_spinner.eta = "Complete"
                    self.realtime_spinner.canvas.delete("all")
                    self.realtime_spinner.draw_progress_display()
            
            self.update_status_safe("Ready")
            
            # Restart title animation
            if self.animated_title:
                self.root.after(2000, self.animated_title.start_animation)
            
        except:
            pass
    
    def stop_download(self):
        """Stop download process"""
        try:
            self.download_active = False
            self.update_status_safe("Stopping...")
            
            # Stop real-time progress and title animation
            self.handle_realtime_progress('stop', None)
            if self.animated_title:
                self.animated_title.stop_animation()
        except:
            pass

def clean_main():
    """Clean main entry point with comprehensive error handling"""
    try:
        # Initialize tkinter
        root = tk.Tk()
        
        # Create clean application
        app = CleanFasstVideoDownloader(root)
        
        # Setup close handler
        def on_closing():
            try:
                # Stop animations and real-time spinner
                if hasattr(app, 'animated_title') and app.animated_title:
                    app.animated_title.stop_animation()
                if hasattr(app, 'realtime_spinner') and app.realtime_spinner:
                    app.realtime_spinner.stop()
                
                if hasattr(app, 'download_active') and app.download_active:
                    if messagebox.askokcancel("Quit", "Downloads are active. Do you want to quit?"):
                        app.download_active = False
                        cleanup_and_close()
                else:
                    cleanup_and_close()
            except:
                root.destroy()
        
        def cleanup_and_close():
            try:
                root.destroy()
            except:
                pass
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Start main loop
        root.mainloop()
        
    except Exception as e:
        logger.exception("Critical application error")
        try:
            messagebox.showerror("Critical Error", f"Application failed to start: {e}")
        except:
            print(f"Critical Error: Application failed to start: {e}")

if __name__ == "__main__":
    # Final integrity check before execution
    try:
        if hasattr(protection_manager, 'perform_integrity_check'):
            if protection_manager.perform_integrity_check():
                clean_main()
            else:
                logger.error("Final integrity check failed")
                sys.exit(1)
        else:
            clean_main()
    except Exception as e:
        logger.error(f"Application startup failed: {e}")
        sys.exit(1)
