"""
Configuration module for Battle Cats Save Editor.
Contains all constants, paths, and configuration settings.
"""
import os
import sys


class Config:
    """Central configuration class for the editor."""
    
    # Application metadata
    APP_NAME = "Editor EN"
    VERSION = "1.0.0"
    
    # API endpoints
    URL_TRANSFER_RECEPTION = "https://nyanko-save.ponosgames.com/v1/transfers/{}/reception"
    URL_BACKUP_DELETE = "https://nyanko-backups.ponosgames.com/?action=delete&accountId=transfer&pin=confirmation&country=en"
    URL_STORE = "https://nyanko.ponosgames.com/?action=store&country=en"
    URL_VERSION_CHECK = "http://1plus1equalswindow.pythonanywhere.com/"
    
    # Client information for API requests
    CLIENT_INFO = {
        "clientInfo": {
            "client": {
                "countryCode": "en",
                "version": "100400"
            },
            "device": {
                "model": "iPhone12,1"
            },
            "os": {
                "type": "ios",
                "version": "14.400000"
            }
        }
    }
    
    # Game constraints
    MAX_XP = 99999999
    
    # File names
    SAVE_FILE = "SAVE_DATA(transfer)"
    BACKUP_FILE = "BackupSave(use_backupmanager_to_restore)"
    EXE_FILE = "EditorEN.exe"
    CERT_FILE = "charlescert.pem"
    
    # Checksum salt
    CHECKSUM_SALT = b'battlecatsen'
    
    @classmethod
    def get_dir_path(cls):
        """Get the directory path of the running script."""
        return os.path.dirname(os.path.realpath(sys.argv[0]))
    
    @classmethod
    def get_save_path(cls):
        """Get the full path to the save file."""
        return os.path.join(cls.get_dir_path(), cls.SAVE_FILE)
    
    @classmethod
    def get_backup_path(cls):
        """Get the full path to the backup file."""
        return os.path.join(cls.get_dir_path(), cls.BACKUP_FILE)
    
    @classmethod
    def get_exe_path(cls):
        """Get the full path to the executable."""
        return os.path.join(cls.get_dir_path(), cls.EXE_FILE)
    
    @classmethod
    def get_cert_path(cls):
        """Get the full path to the certificate file."""
        return os.path.join(cls.get_dir_path(), cls.CERT_FILE)
