# A small Python project created to practice Git, GitHub, virtual environments, environments variables and basic project configuration
## Features
- Loads configuration from '.env' file
- Keeps secrets outside the Git repository
- Uses '.env.example' as a configuration template
- Uses Python virtual environment
- Installs dependencies from 'requirements.txt.'
## Requirements
- Python 3.10 or newer
- Git
## Installation
### 1. Clone repository
'''bash
git clone https://github.com/n3v3rwhere/ForStudy.git
cd my-first-repo



# 1. Create virtual environment
On Windows PowerShell:
python -m venv .venv
# 2. Activate virtual environment
.venv\Scripts\Activate.ps1
After activation, your terminal should show:
(.venv)
# 3. Install dependencies
python -m pip install -r requirements.txt

## Configuration
This project uses environment variable stored in a .env file
Create your local .env file based on .env.example.
Replace the placeholder value with your own API key if one is required.

### IMPORTANT
The .env file contains private configuration and intentionally excluded from Git using .gitignore.
# Never commit real API keys, passwords, tokens, or other secrets to the repository!

# Running the Project
With virtual environment activated run:
python main.py

The program reads the configuration from .env and displays the application name and whether the API key was loaded successfully.

Example output:
App Name: My First Python Repo
API Key loaded: True

# Project structure

- my-first-repo/

- .env                # Local secrets - not tracked by Git
- .env.example        # Example environment variables
- .gitignore          # Files excluded from Git
- main.py             # Main Python application 
- requirements.txt    # Python dependencies
- README.md           # Project documentation
- .venv/              # Virtual environment - not tracked by Git

## Security
Secrets are stored only in .env.

The repository ignores:
- .env
- .venv/
- __pycache__/
- *.pyc

The .env.example file contains the required variable names without exposing real secret values.

# Git Workflow

This project uses the main branch as the primary branch.
- Typical workflow:
- git status
- git add
- git commit -m "Describe your changes"
- git push


# Markdown
## Security Practice
As part of this learning project, a dummy '.env' file was intentionally commiited to Git.

The file was then removed from Git tracking with:
 ''' bash 
 - git rm --cached .env
The .env file was added to .gitignore so it will not be tracked again.