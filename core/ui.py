"""
User interface module for Battle Cats Save Editor.
Handles all console output and user input.
"""
import sys
import time
from typing import Optional, Tuple

import colorama
from termcolor import colored


class UIHandler:
    """Handles all user interface operations."""
    
    def __init__(self):
        """Initialize colorama for colored terminal output."""
        colorama.init()
    
    @staticmethod
    def clear_screen() -> None:
        """Clear the console screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def show_welcome() -> None:
        """Display the welcome screen."""
        universal_editor = colored("Editor EN", 'magenta', attrs=['bold'])
        names = colored("Lethal / 1plus1equalswindow_", 'cyan', attrs=['bold'])
        names2 = colored("JulietCat", 'yellow', attrs=['bold'])
        names3 = colored("csehydrogen", 'blue', attrs=['bold'])
        names4 = colored("beeven", 'green', attrs=['bold'])
        nott = colored("not", 'red', attrs=['bold'])
        rootjailbreak = colored("root/jailbreak", 'green', attrs=['bold'])
        free = colored("free", 'green', attrs=['bold'])
        
        print('\033[1mWelcome to ' + universal_editor + ' \033[1mmade by:\n'
              + names + ' \033[1mand ' + names2 + '\033[1m; inspired by '
              + names3 + ' \033[1mand ' + names4 
              + '\n\033[1mThis editor does ' + nott + ' \033[1mrequire a '
              + rootjailbreak + '.\n\033[1mIt only requires your Transfer Code '
              'and Confirmation code.\n\n\nIf you paid for this Editor, you were '
              'ripped off. This Editor is available for ' + free 
              + '\033[1m.\n\nGet your codes ready and press enter...\n')
        input()
    
    @staticmethod
    def show_backup_warning() -> None:
        """Display backup warning message."""
        print(colored("PLEASE USE THE BACKUPMANAGER TO BACKUP YOUR SAVES "
                     "BEFORE USING THIS EDITOR!!\n", 'red', attrs=['bold']))
    
    @staticmethod
    def show_error(message: str) -> None:
        """Display an error message."""
        print(colored(f"\n{message}\n", 'red', attrs=['bold']))
    
    @staticmethod
    def show_success(message: str) -> None:
        """Display a success message."""
        print(colored(f"\n{message}\n", 'green', attrs=['bold']))
    
    @staticmethod
    def show_info(message: str) -> None:
        """Display an info message."""
        print(colored(f"\n{message}\n", 'cyan', attrs=['bold']))
    
    @staticmethod
    def get_transfer_codes() -> Tuple[str, str]:
        """
        Prompt user for transfer and confirmation codes.
        
        Returns:
            Tuple of (transfer_code, confirmation_code)
        """
        print('\033[1m\nPlease type only your transfer code:')
        transfer_code = input().strip()
        
        print('\033[1m\nPlease type only your confirmation code:')
        confirmation_code = input().strip()
        
        return transfer_code, confirmation_code
    
    @staticmethod
    def show_main_menu() -> str:
        """
        Display the main menu and get user choice.
        
        Returns:
            User's menu choice as a string
        """
        print(colored("\nWhat would you like to do with your save? Type a number:",
                     'cyan', attrs=['bold']))
        print('\033[1m\n1 = Edit amount of CF')
        print('2 = Edit amount of XP')
        print('3 = Finish, and Get your Transfer Codes!\n')
        return input().strip()
    
    @staticmethod
    def get_cat_food_amount(max_amount: int) -> Optional[int]:
        """
        Prompt user for cat food amount.
        
        Args:
            max_amount: Maximum allowed cat food amount
            
        Returns:
            The amount entered by user, or None if invalid
        """
        print(f"\033[1m\nHow much CF do you want? MAX: {max_amount}")
        try:
            amount = int(input().strip())
            if amount < 0 or amount > max_amount:
                UIHandler.show_error(f"You cannot put more than {max_amount} CF! "
                                   f"Enter {max_amount} or lower!")
                return None
            return amount
        except ValueError:
            UIHandler.show_error("Going back to the main menu because you didn't "
                               "type a PROPER NUMBER")
            return None
    
    @staticmethod
    def get_xp_amount(max_amount: int = 99999999) -> Optional[int]:
        """
        Prompt user for XP amount.
        
        Args:
            max_amount: Maximum allowed XP amount
            
        Returns:
            The amount entered by user, or None if invalid
        """
        print(f"\033[1m\nHow much XP do you want? MAX: {max_amount}")
        try:
            amount = int(input().strip())
            if amount < 0 or amount > max_amount:
                UIHandler.show_error(f"You cannot add more than {max_amount} XP! "
                                   f"Enter {max_amount} or lower!")
                return None
            return amount
        except ValueError:
            UIHandler.show_error("Going back to the main menu because you didn't "
                               "type a PROPER NUMBER")
            return None
    
    @staticmethod
    def show_progress_bar(duration: float = 1.0) -> None:
        """
        Display a progress bar animation.
        
        Args:
            duration: Duration of the progress bar in seconds
        """
        for i in range(101):
            time.sleep(duration / 100)
            sys.stdout.write(f"\r{i}%")
            sys.stdout.flush()
        print('\n')
    
    @staticmethod
    def show_transfer_info(transfer_code: str, confirmation_code: str) -> None:
        """
        Display the new transfer codes.
        
        Args:
            transfer_code: The transfer code
            confirmation_code: The confirmation code
        """
        print(colored('\nTransfer Code: ', 'blue', attrs=['bold']) 
              + colored(transfer_code, 'cyan', attrs=['bold']))
        print(colored('Confirmation Code: ', 'blue', attrs=['bold']) 
              + colored(confirmation_code, 'cyan', attrs=['bold']))
        print('\nThose are your codes, put them back in the game.\n')
    
    @staticmethod
    def pause(message: str = "Press ENTER to continue...") -> None:
        """Pause and wait for user input."""
        input(message)
