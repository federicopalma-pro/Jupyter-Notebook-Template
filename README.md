# Python Project with UV and Jupyter Notebook

This is a Python project template configured to use UV as package manager and support Jupyter Notebook with VS Code.

> **Note**: This is a generic template. After cloning, `uv.lock` will be generated locally when you run `uv sync`.

## Requirements

- Python 3.9+
- UV (package manager)
- VS Code

## UV Installation

If you haven't installed UV yet, you can do it with:

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Project Setup

1. **Clone or download the project**
2. **Open terminal in the project folder**
3. **Run the setup script:**

```bash
# Run the setup script to initialize the project (REQUIRED)
python scripts.py setup
```

This setup script will:
- Check if UV is installed.
- Create a virtual environment (in the `.venv` folder) and install all dependencies from `pyproject.toml` using `uv sync`.
- Install a Jupyter kernel named `notebook-project` for use within your notebooks.
- Create an example notebook in the `notebooks/` directory (`notebooks/example.ipynb`).

4. **Alternatively, for manual setup without the script:**

```bash
# Create virtual environment and install dependencies manually
uv sync

# To install development dependencies too
uv sync --all-extras

# Or install specific groups
uv sync --extra dev
uv sync --extra ml
uv sync --extra viz
```

**Note**: This project uses `pyproject.toml` for dependency management (modern standard). No `requirements.txt` needed with UV!

## Starting Jupyter

```bash
# Activate virtual environment & start Jupyter Lab
uv run jupyter lab

# Or start the classic Jupyter Notebook
uv run jupyter notebook

# To start Jupyter Lab from a specific folder
uv run jupyter lab notebooks/

# To start Jupyter Notebook from a specific folder
uv run jupyter notebook notebooks/
```

## Using with VS Code

1. **Open the project folder in VS Code**
2. **Install recommended extensions** (VS Code will ask automatically)
3. **Select Python interpreter:** 
   - Cmd/Ctrl + Shift + P
   - Search "Python: Select Interpreter"
   - Select the interpreter in `.venv/Scripts/python.exe` (Windows) or `.venv/bin/python` (macOS/Linux)

## Dependency Management

This project uses **UV** with `pyproject.toml` for modern Python dependency management:

- **`pyproject.toml`** - Main configuration file (dependencies, project metadata)
- **`uv.lock`** - Auto-generated lock file with exact versions (created after `uv sync`)
- **No `requirements.txt`** - UV handles everything through pyproject.toml

### Why UV + pyproject.toml?
- ✅ **Faster** than pip
- ✅ **Modern standard** (PEP 621, PEP 631) 
- ✅ **Built-in virtual environment** management
- ✅ **Optional dependency groups** (`dev`, `ml`, `viz`)
- ✅ **Automatic lock files** for reproducible builds
- ✅ **Single source of truth** for project configuration

## Useful UV Commands

```bash
# Add a new dependency
uv add pandas numpy matplotlib

# Add development dependency
uv add --dev pytest black

# Remove dependency
uv remove package-name

# Update dependencies
uv sync --upgrade

# Run Python script
uv run python script.py

# Run command in virtual environment
uv run command

# Show installed dependencies
uv pip list
```

## Project Scripts (`scripts.py`)

This project includes a `scripts.py` file for automating common tasks. You've already used `python scripts.py setup` during the project setup. Here are other available commands:

```bash
# Start Jupyter Lab
python scripts.py jupyter
# (For the classic Jupyter Notebook, use 'uv run jupyter notebook')

# Run project tests (you may need to configure tests first)
python scripts.py test

# Format code using Black and isort
python scripts.py format

# Lint code using Flake8
python scripts.py lint
```

You can see all available actions by running `python scripts.py` without any arguments.
