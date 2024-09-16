import os
import sys
from pathlib import Path

# Extensions
EXTENSION_ROOT = Path('_ext')
sys.path.extend([str(path.resolve()) for path in EXTENSION_ROOT.glob('*')])

# General configuration
project = 'Test RST Documentation'

extensions = [
    'sphinxcontrib.jquery',
    'sphinxcontrib.plantuml',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx.ext.graphviz',
    'vartext'
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

git_url = "https://some.weird.place"
if 'GITHUB_SERVER_URL' in os.environ and 'GITHUB_REPOSITORY' in os.environ:
    git_url = os.environ['GITHUB_SERVER_URL'] + '/' + os.environ['GITHUB_REPOSITORY']

vartext_replacements = {
    "{GITURL}" : git_url
}
