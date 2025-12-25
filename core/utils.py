"""
Utility functions for REDACTED Save Editor.
Contains helper functions for various operations.
"""
import ctypes
import hashlib
import os
import sys
from typing import Optional


def set_console_title(title: str) -> None:
    """
    Set the console window title (Windows only).
    
    Args:
        title: The title to set for the console window
    """
    try:
        if sys.platform == 'win32':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception:
        # Silently fail if not on Windows or if it doesn't work
        pass


def calculate_file_hash(file_path: str) -> Optional[str]:
    """
    Calculate MD5 hash of a file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        MD5 hash as hexadecimal string, or None if file doesn't exist
    """
    if not os.path.exists(file_path):
        return None
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            return hashlib.md5(data).hexdigest()
    except IOError:
        return None


def file_exists(file_path: str) -> bool:
    """
    Check if a file exists.
    
    Args:
        file_path: Path to the file
        
    Returns:
        True if file exists, False otherwise
    """
    return os.path.exists(file_path)


def delete_file(file_path: str) -> bool:
    """
    Delete a file if it exists.
    
    Args:
        file_path: Path to the file to delete
        
    Returns:
        True if deleted successfully, False otherwise
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except OSError:
        return False
