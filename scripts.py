#!/usr/bin/env python3
"""
Setup and automation script for UV + Jupyter project.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command: str, description: str = None):
    """Execute a command and handle errors."""
    if description:
        print(f"[*] {description}...")

    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        if description:
            print(f"[OK] {description} completed")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error during: {description or command}")
        print(f"Error: {e.stderr}")
        sys.exit(1)


def create_example_notebook():
    """Create example notebook if it doesn't exist."""
    import json

    notebook_path = Path("notebooks/example.ipynb")

    if notebook_path.exists():
        print("[OK] Example notebook already exists")
        return

    # Create notebooks directory if it doesn't exist
    notebook_path.parent.mkdir(exist_ok=True)

    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Example Notebook\\n",
                    "\\n",
                    "This is an example notebook to test the project setup with UV and Jupyter.",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Import base libraries\\n",
                    "import pandas as pd\\n",
                    "import numpy as np\\n",
                    "import matplotlib.pyplot as plt\\n",
                    "import seaborn as sns\\n",
                    "\\n",
                    "print('Setup completed successfully!')\\n",
                    "print(f'Pandas version: {pd.__version__}')\\n",
                    "print(f'NumPy version: {np.__version__}')",
                ],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "notebook-project",
                "language": "python",
                "name": "notebook-project",
            },
            "language_info": {"name": "python", "version": "3.12.9"},
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    try:
        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(notebook_content, f, indent=1)
        print("[OK] Example notebook created: notebooks/example.ipynb")
    except Exception as e:
        print(f"[WARNING] Could not create example notebook: {e}")


def create_status_report():
    """Create a status report after successful setup."""
    import datetime

    status_content = f"""# ✅ PROJECT STATUS VERIFICATION

## Setup Completed: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Current Project Structure:
```
C:\\Users\\fpclo\\Desktop\\Notebook\\
├── .venv/                    # ✅ Virtual environment (active)
├── .vscode/                  # ✅ VS Code configuration
├── notebooks/                # ✅ Jupyter notebooks folder
│   └── example.ipynb        # ✅ Example notebook
├── src/                      # ✅ Python source code
├── .gitignore               # ✅ Git ignore file
├── pyproject.toml           # ✅ UV configuration & dependencies
├── uv.lock                  # ✅ Dependencies lock file
├── scripts.py               # ✅ Automation scripts
└── README.md                # ✅ Documentation
```

## ✅ Status: PROJECT READY FOR USE! 🎉

### Dependency Management:
- **UV Package Manager**: ✅ Active and configured
- **pyproject.toml**: ✅ Main dependency configuration
- **uv.lock**: ✅ Exact versions locked
- **NO requirements.txt**: ✅ Clean modern setup

## 🚀 Ready to Use Commands:

```bash
# Start Jupyter Lab
uv run jupyter lab

# Test dependencies
uv run python -c "import pandas, numpy, matplotlib, seaborn; print('All OK!')"

# Add new dependencies
uv add package-name

# Use automation script
python scripts.py jupyter
```

## 📋 Next Steps:
1. Open VS Code in this folder
2. Install recommended extensions when prompted
3. Select `.venv\\Scripts\\python.exe` as Python interpreter
4. Open `notebooks/example.ipynb` and test it
5. Start developing your notebooks!
"""

    try:
        with open("PROJECT_STATUS.md", "w", encoding="utf-8") as f:
            f.write(status_content)
        print("[OK] Status report created: PROJECT_STATUS.md")
    except Exception as e:
        print(f"[WARNING] Could not create status report: {e}")


def setup_project():
    """Initial project setup."""
    print("UV + Jupyter project setup\n")

    # Check if UV is installed
    try:
        subprocess.run(["uv", "--version"], check=True, capture_output=True)
        print("[OK] UV is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ERROR] UV is not installed. Install it with:")
        print(
            '   PowerShell: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"'
        )
        print("   macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh")
        sys.exit(1)

    # Sync dependencies
    run_command("uv sync", "Installing dependencies")

    # Install Jupyter kernel
    run_command(
        "uv run python -m ipykernel install --user --name=notebook-project",
        "Installing Jupyter kernel",
    )

    # Create example notebook if it doesn't exist
    create_example_notebook()

    # Create status report (commented out for generic template)
    # create_status_report()

    print("\n[OK] Setup completed!")
    print("\nNext steps:")
    print("1. Open VS Code in this folder")
    print("2. Install recommended extensions")
    print("3. Select Python interpreter: .venv/Scripts/python.exe")
    print("4. Start Jupyter with: uv run jupyter lab")


def start_jupyter():
    """Start Jupyter Lab."""
    print("Starting Jupyter Lab...")
    os.system("uv run jupyter lab")


def run_tests():
    """Run project tests."""
    if not Path("tests").exists():
        print("Creating tests folder...")
        Path("tests").mkdir()
        Path("tests/__init__.py").touch()

    run_command("uv run pytest", "Running tests")


def format_code():
    """Format code with black and isort."""
    run_command("uv run black .", "Formatting code with black")
    run_command("uv run isort .", "Sorting imports with isort")


def lint_code():
    """Check code with flake8."""
    run_command("uv run flake8 .", "Checking code with flake8")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python scripts.py <command>")
        print("\nAvailable commands:")
        print("  setup     - Initial project setup")
        print("  jupyter   - Start Jupyter Lab")
        print("  test      - Run tests")
        print("  format    - Format code")
        print("  lint      - Check code")
        sys.exit(1)

    command = sys.argv[1]

    commands = {
        "setup": setup_project,
        "jupyter": start_jupyter,
        "test": run_tests,
        "format": format_code,
        "lint": lint_code,
    }

    if command in commands:
        commands[command]()
    else:
        print(f"[ERROR] Command '{command}' not recognized")
        sys.exit(1)


if __name__ == "__main__":
    main()
