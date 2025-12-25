# Architecture Overview

## Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                          main.py                            │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │             REDACTEDEditor (Main Class)               │ │
│  │                                                       │ │
│  │  - Orchestrates entire workflow                      │ │
│  │  - Manages application state                         │ │
│  │  - Coordinates all components                        │ │
│  └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
         │              │              │              │
         │              │              │              │
         ▼              ▼              ▼              ▼
    ┌────────┐    ┌──────────┐   ┌────────────┐  ┌──────┐
    │ ui.py  │    │network.py│   │save_editor │  │utils │
    │        │    │          │   │    .py     │  │ .py  │
    └────────┘    └──────────┘   └────────────┘  └──────┘
         │              │              │              │
         │              │              │              │
         └──────────────┴──────────────┴──────────────┘
                        │
                        ▼
                  ┌──────────┐
                  │config.py │
                  │          │
                  └──────────┘
```

## Module Responsibilities

### 1. **config.py**
- Stores all constants (URLs, file names, limits)
- Provides path resolution methods
- Central configuration source
- No dependencies on other modules

### 2. **utils.py**
- Console title management
- File operations (hash, exists, delete)
- Platform-specific utilities
- Minimal dependencies

### 3. **network.py** (NetworkHandler class)
- API communication with game servers
- Download save files via transfer codes
- Upload modified saves
- Server status checks
- Dependencies: config.py, requests

### 4. **save_editor.py** (SaveEditor class)
- Binary file manipulation
- Cat Food editing (3-byte little-endian at offset 7)
- XP editing (4-byte little-endian at offset 76)
- Checksum calculation and patching
- Context manager for safe file handling
- Dependencies: config.py

### 5. **ui.py** (UIHandler class)
- All user interaction (input/output)
- Colored console output
- Progress bar animations
- Error/success/info messages
- Menu display
- No dependencies on other custom modules

### 6. **main.py** (BattleCatsEditor class)
- Application entry point
- Workflow orchestration
- Component initialization
- Error handling at application level
- Dependencies: All other modules

## Data Flow

```
1. User Start
   └─> main.py initializes REDACTEDEditor
       
2. Welcome & Server Check
   └─> UIHandler.show_welcome()
   └─> NetworkHandler.check_server_status()
       
3. Download Save
   └─> UIHandler.get_transfer_codes()
   └─> NetworkHandler.download_save()
   └─> SaveEditor.save_to_file()
       
4. Edit Loop
   └─> UIHandler.show_main_menu()
   └─> SaveEditor.set_cat_food() or set_xp()
   └─> Repeat until user chooses to finish
       
5. Finalize
   └─> SaveEditor.patch_checksum()
   └─> SaveEditor.load_from_file()
   └─> NetworkHandler.upload_save()
   └─> UIHandler.show_transfer_info()
```

## Design Patterns Used

1. **Separation of Concerns**: Each module handles one aspect
2. **Dependency Injection**: Components passed to main class
3. **Context Manager**: SaveEditor uses `with` statement
4. **Static Methods**: Config and SaveEditor utility methods
5. **Class-based Organization**: Related functionality grouped
6. **Single Responsibility**: Each class has one clear purpose

## Benefits of This Architecture

✅ **Testability**: Each component can be tested independently  
✅ **Maintainability**: Changes isolated to specific modules  
✅ **Readability**: Clear structure and naming conventions  
✅ **Extensibility**: Easy to add new features  
✅ **Reusability**: Components can be used in other projects  
✅ **Professional**: Follows industry best practices  

## Example Usage in Code

```python
# Original monolithic approach
def mainmenu():
    # 200 lines of mixed logic...

# Refactored modular approach
class REDACTEDEditor:
    def _edit_save(self):
        with SaveEditor(self.save_path) as editor:
            choice = self.ui.show_main_menu()
            if choice == '1':
                self._edit_cat_food(editor)
```

The refactored code is:
- More readable
- Easier to debug
- Better for collaboration
- Professional for portfolio
