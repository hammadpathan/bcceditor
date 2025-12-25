"""
Main entry point for Battle Cats Save Editor.
Orchestrates the entire save editing workflow.
"""
import sys

from config import Config
from network import NetworkHandler
from save_editor import SaveEditor
from ui import UIHandler
from utils import set_console_title, delete_file


class BattleCatsEditor:
    """Main application class for the Battle Cats Save Editor."""
    
    def __init__(self):
        """Initialize the editor with necessary components."""
        self.ui = UIHandler()
        self.network = NetworkHandler()
        self.cat_food_limit = 40000  # Default limit
        self.save_path = Config.get_save_path()
    
    def run(self) -> int:
        """
        Run the main editor workflow.
        
        Returns:
            Exit code (0 for success, 1 for error)
        """
        try:
            # Set console title
            set_console_title(Config.APP_NAME)
            
            # Show welcome screen
            self.ui.show_welcome()
            
            # Check server status
            if not self._check_server():
                return 1
            
            # Get save data from server
            if not self._download_save():
                return 1
            
            # Edit save file
            self._edit_save()
            
            # Patch and upload
            if not self._finalize_save():
                return 1
            
            self.ui.pause("Press ENTER to exit")
            return 0
            
        except KeyboardInterrupt:
            self.ui.show_info("\nOperation cancelled by user.")
            return 1
        except Exception as e:
            self.ui.show_error(f"An unexpected error occurred: {str(e)}")
            return 1
        finally:
            # Cleanup: optionally delete the save file
            # Uncomment if you want to auto-delete after processing
            # delete_file(self.save_path)
            pass
    
    def _check_server(self) -> bool:
        """
        Check server status and get configuration.
        
        Returns:
            True if server is available, False otherwise
        """
        success, cat_food_limit, message = self.network.check_server_status()
        
        if not success:
            self.ui.show_error(message)
            self.ui.pause()
            return False
        
        if cat_food_limit:
            self.cat_food_limit = cat_food_limit
        
        self.ui.show_backup_warning()
        return True
    
    def _download_save(self) -> bool:
        """
        Download save data from the server.
        
        Returns:
            True if successful, False otherwise
        """
        max_attempts = 3
        attempt = 0
        
        while attempt < max_attempts:
            # Get transfer codes from user
            transfer_code, confirmation_code = self.ui.get_transfer_codes()
            
            # Attempt download
            success, save_data, message = self.network.download_save(
                transfer_code, confirmation_code
            )
            
            if success and save_data:
                SaveEditor.save_to_file(self.save_path, save_data)
                self.ui.show_success("Save data downloaded successfully!")
                return True
            
            # Show error and retry
            self.ui.clear_screen()
            self.ui.show_error(message if message else "Failed to download save data.")
            attempt += 1
        
        self.ui.show_error("Maximum attempts reached. Exiting...")
        return False
    
    def _edit_save(self) -> None:
        """Handle the save editing menu loop."""
        with SaveEditor(self.save_path) as editor:
            while True:
                choice = self.ui.show_main_menu()
                
                if choice == '1':
                    self._edit_cat_food(editor)
                elif choice == '2':
                    self._edit_xp(editor)
                elif choice == '3':
                    break
                else:
                    self.ui.clear_screen()
                    self.ui.show_error("Please enter a number from the list!")
    
    def _edit_cat_food(self, editor: SaveEditor) -> None:
        """
        Handle cat food editing.
        
        Args:
            editor: The SaveEditor instance
        """
        amount = self.ui.get_cat_food_amount(self.cat_food_limit)
        
        if amount is None:
            return
        
        while amount is not None and amount > self.cat_food_limit:
            self.ui.clear_screen()
            amount = self.ui.get_cat_food_amount(self.cat_food_limit)
        
        if amount is not None:
            editor.set_cat_food(amount)
            self.ui.show_progress_bar(1.0)
            self.ui.show_success("Done")
    
    def _edit_xp(self, editor: SaveEditor) -> None:
        """
        Handle XP editing.
        
        Args:
            editor: The SaveEditor instance
        """
        amount = self.ui.get_xp_amount(Config.MAX_XP)
        
        if amount is None:
            return
        
        while amount is not None and amount > Config.MAX_XP:
            self.ui.clear_screen()
            amount = self.ui.get_xp_amount(Config.MAX_XP)
        
        if amount is not None:
            editor.set_xp(amount)
            self.ui.show_progress_bar(1.0)
            self.ui.show_success("Done")
    
    def _finalize_save(self) -> bool:
        """
        Patch checksum and upload the modified save.
        
        Returns:
            True if successful, False otherwise
        """
        # Patch the save file
        print('\033[1m\nStarting patcher...')
        was_patched = SaveEditor.patch_checksum(self.save_path)
        
        if was_patched:
            self.ui.show_error('SAVE_DATA not patched, patching now...')
            self.ui.show_success('SAVE_DATA patched successfully.')
        else:
            self.ui.show_success('SAVE_DATA already patched.')
        
        self.ui.pause('\nPress Enter to get your transfer codes')
        
        # Upload the save
        save_data = SaveEditor.load_from_file(self.save_path)
        success, transfer_info, message = self.network.upload_save(save_data)
        
        if success and transfer_info:
            self.ui.show_transfer_info(
                transfer_info['transfer_code'],
                transfer_info['confirmation_code']
            )
            return True
        else:
            self.ui.show_error(message if message else 
                             "Something went wrong! Your save was not uploaded.")
            self.ui.show_info("Your save is still in your game. "
                            "Please make another transfer and try again.")
            return False


def main():
    """Main entry point for the application."""
    editor = BattleCatsEditor()
    sys.exit(editor.run())


if __name__ == "__main__":
    main()
