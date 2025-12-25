"""
Save file editing module for Battle Cats Save Editor.
Handles reading, modifying, and patching save data.
"""
import binascii
import hashlib
import os
from typing import Optional

from config import Config


class SaveEditor:
    """Handles save file operations and modifications."""
    
    def __init__(self, save_path: str):
        """
        Initialize the save editor.
        
        Args:
            save_path: Path to the save file
        """
        self.save_path = save_path
        self._file_handle: Optional[object] = None
    
    def __enter__(self):
        """Context manager entry - opens the save file."""
        self._file_handle = open(self.save_path, 'r+b')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - closes the save file."""
        if self._file_handle:
            self._file_handle.close()
    
    def set_cat_food(self, amount: int) -> None:
        """
        Set the cat food amount in the save file.
        
        Args:
            amount: The amount of cat food to set (up to 3 bytes)
        """
        if not self._file_handle:
            raise RuntimeError("Save file is not open")
        
        # Convert to hex and handle endianness
        hex_value = hex(amount)[2:]
        length = len(hex_value)
        padding = bytes.fromhex("00")
        
        # Write bytes in little-endian format at offset 7
        if length == 1:
            self._file_handle.seek(7)
            self._file_handle.write(bytes.fromhex("0" + hex_value))
            self._file_handle.seek(8)
            self._file_handle.write(padding)
            self._file_handle.seek(9)
            self._file_handle.write(padding)
            
        elif length == 2:
            self._file_handle.seek(7)
            self._file_handle.write(bytes.fromhex(hex_value))
            self._file_handle.seek(8)
            self._file_handle.write(padding)
            self._file_handle.seek(9)
            self._file_handle.write(padding)
            
        elif length == 3:
            byte1 = bytes.fromhex("0" + hex_value[:1])
            byte2 = bytes.fromhex(hex_value[1:])
            self._file_handle.seek(7)
            self._file_handle.write(byte2)
            self._file_handle.seek(8)
            self._file_handle.write(byte1)
            self._file_handle.seek(9)
            self._file_handle.write(padding)
            
        elif length == 4:
            byte1 = bytes.fromhex(hex_value[-4:-2])
            byte2 = bytes.fromhex(hex_value[-2:])
            self._file_handle.seek(7)
            self._file_handle.write(byte2)
            self._file_handle.seek(8)
            self._file_handle.write(byte1)
            self._file_handle.seek(9)
            self._file_handle.write(padding)
    
    def set_xp(self, amount: int) -> None:
        """
        Set the XP amount in the save file.
        
        Args:
            amount: The amount of XP to set (up to 4 bytes)
        """
        if not self._file_handle:
            raise RuntimeError("Save file is not open")
        
        hex_value = hex(amount)[2:]
        length = len(hex_value)
        padding = bytes.fromhex("00")
        
        # Write bytes in little-endian format at offset 76
        if length == 1:
            self._file_handle.seek(76)
            self._file_handle.write(bytes.fromhex("0" + hex_value))
            for i in range(77, 80):
                self._file_handle.seek(i)
                self._file_handle.write(padding)
                
        elif length == 2:
            self._file_handle.seek(76)
            self._file_handle.write(bytes.fromhex(hex_value))
            for i in range(77, 80):
                self._file_handle.seek(i)
                self._file_handle.write(padding)
                
        elif length == 3:
            byte1 = bytes.fromhex("0" + hex_value[:1])
            byte2 = bytes.fromhex(hex_value[1:])
            self._file_handle.seek(76)
            self._file_handle.write(byte2)
            self._file_handle.seek(77)
            self._file_handle.write(byte1)
            for i in range(78, 80):
                self._file_handle.seek(i)
                self._file_handle.write(padding)
                
        elif length == 4:
            byte1 = bytes.fromhex(hex_value[-4:-2])
            byte2 = bytes.fromhex(hex_value[-2:])
            self._file_handle.seek(76)
            self._file_handle.write(byte2)
            self._file_handle.seek(77)
            self._file_handle.write(byte1)
            for i in range(78, 80):
                self._file_handle.seek(i)
                self._file_handle.write(padding)
                
        elif length == 5:
            byte1 = bytes.fromhex("0" + hex_value[:1])
            byte2 = bytes.fromhex(hex_value[1:3])
            byte3 = bytes.fromhex(hex_value[3:])
            self._file_handle.seek(76)
            self._file_handle.write(byte3)
            self._file_handle.seek(77)
            self._file_handle.write(byte2)
            self._file_handle.seek(78)
            self._file_handle.write(byte1)
            self._file_handle.seek(79)
            self._file_handle.write(padding)
                
        elif length == 6:
            byte1 = bytes.fromhex(hex_value[4:])
            byte2 = bytes.fromhex(hex_value[2:4])
            byte3 = bytes.fromhex(hex_value[:2])
            self._file_handle.seek(76)
            self._file_handle.write(byte1)
            self._file_handle.seek(77)
            self._file_handle.write(byte2)
            self._file_handle.seek(78)
            self._file_handle.write(byte3)
            self._file_handle.seek(79)
            self._file_handle.write(padding)
                
        elif length == 7:
            byte1 = bytes.fromhex(hex_value[5:])
            byte2 = bytes.fromhex(hex_value[3:5])
            byte3 = bytes.fromhex(hex_value[1:3])
            byte4 = bytes.fromhex("0" + hex_value[:1])
            self._file_handle.seek(76)
            self._file_handle.write(byte1)
            self._file_handle.seek(77)
            self._file_handle.write(byte2)
            self._file_handle.seek(78)
            self._file_handle.write(byte3)
            self._file_handle.seek(79)
            self._file_handle.write(byte4)
    
    @staticmethod
    def patch_checksum(save_path: str) -> bool:
        """
        Patch the checksum of the save file.
        
        Args:
            save_path: Path to the save file
            
        Returns:
            True if patching was needed, False if already valid
        """
        with open(save_path, 'r+b') as f:
            raw_data = f.read()
            data, checksum = raw_data[:-32], raw_data[-32:]
            
            # Calculate new checksum
            new_checksum = hashlib.md5(Config.CHECKSUM_SALT + data).hexdigest()
            
            # Check if patching is needed
            if new_checksum != checksum.decode():
                f.seek(-32, os.SEEK_END)
                f.write(binascii.hexlify(bytes.fromhex(new_checksum)))
                return True
            
            return False
    
    @staticmethod
    def save_to_file(save_path: str, data: bytes) -> None:
        """
        Save raw data to a file.
        
        Args:
            save_path: Path where to save the file
            data: Raw bytes data to save
        """
        with open(save_path, 'wb') as f:
            f.write(data)
    
    @staticmethod
    def load_from_file(save_path: str) -> bytes:
        """
        Load raw data from a file.
        
        Args:
            save_path: Path to the file to load
            
        Returns:
            Raw bytes data from the file
        """
        with open(save_path, 'rb') as f:
            return f.read()
