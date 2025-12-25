# Quick Reference Guide

## File Overview

| File | Lines | Purpose | Key Classes/Functions |
|------|-------|---------|----------------------|
| **config.py** | 66 | Configuration & constants | `Config` class |
| **utils.py** | 72 | Utility functions | `set_console_title()`, `calculate_file_hash()` |
| **network.py** | 145 | API interactions | `NetworkHandler` class |
| **save_editor.py** | 226 | Save file manipulation | `SaveEditor` class |
| **ui.py** | 156 | User interface | `UIHandler` class |
| **main.py** | 189 | Application entry point | `BattleCatsEditor` class |

## Module Dependencies

```
main.py
├── config.py
├── network.py (depends on config.py)
├── save_editor.py (depends on config.py)
├── ui.py (no dependencies)
└── utils.py (no dependencies)
```

## Quick Commands

```bash
# Verify setup
python verify_setup.py

# Run the application
python main.py

# Install dependencies
pip install -r requirements.txt
```

## API Reference

### Config Class
```python
from config import Config

# Get paths
save_path = Config.get_save_path()
dir_path = Config.get_dir_path()

# Access constants
max_xp = Config.MAX_XP
app_name = Config.APP_NAME
```

### NetworkHandler Class
```python
from network import NetworkHandler

handler = NetworkHandler()

# Check server status
success, cf_limit, message = handler.check_server_status()

# Download save
success, data, error = handler.download_save("transfer_code", "confirm_code")

# Upload save
success, info, error = handler.upload_save(save_data)
```

### SaveEditor Class
```python
from save_editor import SaveEditor

# Use with context manager
with SaveEditor(save_path) as editor:
    editor.set_cat_food(10000)
    editor.set_xp(9999999)

# Patch checksum
was_patched = SaveEditor.patch_checksum(save_path)
```

### UIHandler Class
```python
from ui import UIHandler

ui = UIHandler()

# Display messages
ui.show_welcome()
ui.show_error("Error message")
ui.show_success("Success!")

# Get user input
transfer, confirm = ui.get_transfer_codes()
amount = ui.get_cat_food_amount(max_amount=40000)

# Show progress
ui.show_progress_bar(duration=1.0)
```

### Utils Module
```python
from utils import set_console_title, calculate_file_hash

# Set window title
set_console_title("My App")

# Calculate file hash
hash_value = calculate_file_hash("path/to/file")
```

## Common Tasks

### Adding a New Feature
1. Determine which module should handle it
2. Add method to appropriate class
3. Update main.py workflow if needed
4. Add UI elements to ui.py if required

### Testing Individual Components
```python
# Test network operations
from network import NetworkHandler
handler = NetworkHandler()
success, limit, msg = handler.check_server_status()
print(f"Server OK: {success}, CF Limit: {limit}")

# Test save editor
from save_editor import SaveEditor
with SaveEditor("test_save") as editor:
    editor.set_cat_food(5000)
```

### Error Handling Pattern
```python
try:
    success, data, error = some_operation()
    if not success:
        ui.show_error(error)
        return False
    # Process data...
except Exception as e:
    ui.show_error(f"Unexpected error: {e}")
    return False
```

## Design Patterns Used

1. **Singleton-like Config**: Centralized configuration
2. **Context Manager**: SaveEditor for resource cleanup
3. **Facade Pattern**: BattleCatsEditor simplifies complex workflow
4. **Separation of Concerns**: Each module has single responsibility
5. **Dependency Injection**: Components passed to main class

## Code Style Guidelines

- **Type hints**: Use for all function parameters and returns
- **Docstrings**: Google-style for all public methods
- **Naming**: 
  - Classes: `PascalCase`
  - Functions/methods: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
- **Line length**: Max 88 characters (Black formatter standard)
- **Imports**: Grouped (stdlib, third-party, local)

## Testing Checklist

- [ ] All modules import without errors
- [ ] Dependencies installed (requests, termcolor, colorama)
- [ ] Config paths resolve correctly
- [ ] UI displays colored output
- [ ] Network handler can reach server
- [ ] Save editor can read/write files
- [ ] Main workflow executes completely

## Troubleshooting

### Import Errors
```bash
pip install -r requirements.txt
```

### SSL/Certificate Errors
- Ensure charlescert.pem is in the same directory
- Network handler disables verification for game servers

### Save File Errors
- Check SAVE_DATA(transfer) file exists
- Verify file permissions
- Ensure not corrupted

## Performance Notes

- File operations use binary mode for speed
- Context managers ensure proper cleanup
- Progress bars provide user feedback
- Network timeouts prevent hanging

## Future Improvements

Potential enhancements:
1. Add unit tests for each module
2. Implement logging system
3. Add configuration file support (JSON/YAML)
4. Create GUI version using same backend
5. Add more save editing features
6. Implement backup/restore functionality
