import os
import sys

sys.path.insert(0, os.path.abspath('../../bababel'))  # Adjust to your project structure

# Project Information
project = 'Bababel'
copyright = '2025, Gustavo Delai Onzi Da Silva'
author = 'Gustavo Delai Onzi Da Silva'
release = '0.2.0'  # Change as needed

# Enable required extensions
extensions = [
    'sphinx.ext.autodoc',        # Auto-generates documentation from docstrings
    'sphinx.ext.napoleon',       # Supports Google-style docstrings
    'sphinx.ext.viewcode',       # Adds links to source code
    'sphinx.ext.autosummary',    # Auto-generates module summaries
]

# Ensure Napoleon uses Google-style docstrings
napoleon_google_docstring = True
