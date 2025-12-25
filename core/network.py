"""
Network operations module for REDACTED Save Editor.
Handles all API interactions with the game servers.
"""
import hashlib
import json
import os
import random
import time
from typing import Dict, Tuple, Optional

import requests
from requests import Session

from core.config import Config


class NetworkHandler:
    """Handles all network operations for the save editor."""
    
    def __init__(self):
        """Initialize the network handler with a configured session."""
        self.session = Session()
        cert_path = Config.get_cert_path()
        if os.path.exists(cert_path):
            self.session.verify = cert_path
        else:
            self.session.verify = False
    
    @staticmethod
    def _generate_nonce() -> str:
        """Generate a random nonce hash for API requests."""
        nonce_num = random.randint(0, 1 << 6)
        return hashlib.md5(str(nonce_num).encode()).hexdigest()
    
    def check_server_status(self) -> Tuple[bool, Optional[int], str]:
        """
        Check server status and retrieve configuration.
        
        Returns:
            Tuple of (success, cat_food_limit, status_message)
        """
        try:
            response = requests.get(Config.URL_VERSION_CHECK, timeout=10)
            data = json.loads(response.text)
            
            check_status = data.get('newcheckEN2020', '0')
            cat_food_limit = data.get('catfoodlimit', '40000')
            
            if check_status == '1':
                return False, None, "The Editor is under maintenance! Please try again later."
            elif check_status == '2':
                return False, None, "Your Editor is OUTDATED! Please UPDATE!"
            
            return True, int(cat_food_limit), ""
            
        except Exception as e:
            return False, None, f"Failed to check server status: {str(e)}"
    
    def download_save(self, transfer_code: str, confirmation_code: str) -> Tuple[bool, Optional[bytes], str]:
        """
        Download save data from the server.
        
        Args:
            transfer_code: The transfer code from the game
            confirmation_code: The confirmation code from the game
            
        Returns:
            Tuple of (success, save_data, error_message)
        """
        try:
            url = Config.URL_TRANSFER_RECEPTION.format(transfer_code)
            nonce = self._generate_nonce()
            
            payload = {
                **Config.CLIENT_INFO,
                "nonce": nonce,
                "pin": str(confirmation_code)
            }
            
            headers = {'content-type': 'application/json'}
            
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                verify=False,
                timeout=30
            )
            
            if response.status_code == 200:
                return True, response.content, ""
            else:
                return False, None, "Invalid transfer codes. Please verify and try again."
                
        except requests.RequestException as e:
            return False, None, f"Network error: {str(e)}"
    
    def upload_save(self, save_data: bytes) -> Tuple[bool, Optional[Dict[str, str]], str]:
        """
        Upload modified save data to the server.
        
        Args:
            save_data: The modified save data to upload
            
        Returns:
            Tuple of (success, transfer_info_dict, error_message)
        """
        try:
            r_num = random.randint(0, 1 << 32)
            ct = int(time.time() * 1000)
            boundary = f'__-----------------------{r_num}{ct}'
            
            # Construct multipart form data
            msg = f'--{boundary}\r\n'
            msg += ('Content-Disposition: attachment; name="saveData";'
                   'filename="data.sav"\r\nContent-Type: application/octet'
                   '-stream\r\n\r\n')
            msg += save_data.decode('ISO-8859-1') + '\r\n'
            msg += f'--{boundary}--'
            
            headers = {
                'Connection': 'Keep-Alive',
                'Charset': 'UTF-8',
                'Content-Type': f'multipart/form-data;boundary={boundary}',
            }
            
            response = requests.post(
                Config.URL_STORE,
                data=msg,
                headers=headers,
                verify=False,
                timeout=30
            )
            
            if response.status_code == 200:
                result = json.loads(response.text)
                transfer_info = {
                    'transfer_code': result.get('accountId', ''),
                    'confirmation_code': result.get('pin', '')
                }
                return True, transfer_info, ""
            else:
                return False, None, "Failed to upload save data. Please try again."
                
        except Exception as e:
            return False, None, f"Upload error: {str(e)}"
