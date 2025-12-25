"""
Quick verification script to ensure all modules import correctly.
Run this to validate the refactored code structure.
"""

def test_imports():
    """Test that all modules can be imported without errors."""
    print("Testing imports...")
    
    try:
        import config
        print("✓ config.py imported successfully")
        
        import utils
        print("✓ utils.py imported successfully")
        
        import network
        print("✓ network.py imported successfully")
        
        import save_editor
        print("✓ save_editor.py imported successfully")
        
        import ui
        print("✓ ui.py imported successfully")
        
        import main
        print("✓ main.py imported successfully")
        
        print("\n✅ All modules imported successfully!")
        print("\nYou can now run: python main.py")
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("\nMake sure you've installed dependencies:")
        print("pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


def check_dependencies():
    """Check if required dependencies are installed."""
    print("\nChecking dependencies...")
    dependencies = ['requests', 'termcolor', 'colorama']
    all_installed = True
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} is installed")
        except ImportError:
            print(f"✗ {dep} is NOT installed")
            all_installed = False
    
    if not all_installed:
        print("\nInstall missing dependencies with:")
        print("pip install -r requirements.txt")
    
    return all_installed


if __name__ == "__main__":
    print("=" * 60)
    print("Battle Cats Save Editor - Module Verification")
    print("=" * 60)
    print()
    
    deps_ok = check_dependencies()
    print()
    
    if deps_ok:
        imports_ok = test_imports()
        if imports_ok:
            print("\n" + "=" * 60)
            print("✅ All checks passed! The refactored code is ready to use.")
            print("=" * 60)
    else:
        print("\n⚠️  Please install dependencies first.")
