# REDACTED Save Editor
BC Editor (outdated/no longer in use)  
THIS CODE DOES NOT WORK ANYMORE  
A professional command-line tool for editing REDACTED save data via transfer codes.

## Features

- ✨ Edit Cat Food (CF) amounts
- 📈 Edit Experience Points (XP)
- 🔒 Secure save file checksum patching
- 🌐 Direct integration with game servers
- 🎨 Colorful, user-friendly CLI interface

## Architecture

The project follows a modular, object-oriented design

### Key Components

- **Config**: Centralized configuration management for paths, URLs, and constants
- **NetworkHandler**: Handles all API interactions (download/upload saves, server checks)
- **SaveEditor**: Binary file manipulation with context manager support
- **UIHandler**: Clean separation of presentation logic with colored output
- **BCEditor**: Main orchestrator class coordinating all components

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the editor:
```bash
python main.py
```

Follow the on-screen prompts to:
1. Enter your transfer code and confirmation code
2. Edit CF and/or XP values
3. Receive new transfer codes to use in-game

## Requirements

- Python 3.7+
- Internet connection
- Valid REDACTED transfer codes

## Technical Highlights

- **Type Hints**: Full type annotations for better code clarity
- **Context Managers**: Proper resource management with `__enter__`/`__exit__`
- **Error Handling**: Comprehensive exception handling throughout
- **Separation of Concerns**: Each module has a single, well-defined responsibility
- **PEP 8 Compliance**: Follows Python style guidelines
- **Docstrings**: Complete documentation for all classes and methods

## Security Notes

- SSL certificate verification is disabled for certain API calls (required for game server compatibility)
- Transfer codes are never stored permanently
- All network operations use timeouts to prevent hanging

## Credits

Created by: Me and JulietCat  
Inspired by: csehydrogen and beeven

## License

This is a free tool. If you paid for it, you were scammed.

## Disclaimer

This tool is for educational purposes. Use at your own risk. The authors are not responsible for any account issues that may result from use of this tool.
