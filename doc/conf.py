import os
import sys
from pathlib import Path

# General configuration
project = 'Test RST Documentation'

extensions = [
    'sphinxcontrib.jquery',
    'sphinxcontrib.plantuml',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx.ext.graphviz'
]

# Specify main page and which files have to be excluded
master_doc = 'doc/index'

include_patterns = [
    'dir1/**/doc/**',
    'dirA/**/doc/**',
    'doc/**'
]
exclude_patterns = [
]
