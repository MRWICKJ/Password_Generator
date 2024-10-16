# app/__init__.py

"""
Password Generator Package

This package provides a command-line interface (CLI) and a graphical user interface (GUI) 
for generating secure passwords with customizable options.

Modules:
- cli: Command-line interface for generating passwords
- gui: Graphical user interface for generating passwords
"""

from .cli import generate_password_cli
from .gui import run_gui

__version__ = "1.0.0"
__author__ = "Shubhendu Halder"
__description__ = "A simple password generator with CLI and GUI options."

# Optional: Expose the main functions for easier access
__all__ = ['generate_password_cli', 'run_gui']
