from pathlib import Path
import os

# BASE DIR
def find_base_dir_with_pyproject():
    current_dir = Path.cwd()
    while True:
        if (current_dir / "pyproject.toml").exists():
            return current_dir
        # Move one level up
        parent_dir = current_dir.parent
        if parent_dir == current_dir:  # If we reach the root directory
            raise FileNotFoundError("Could not find 'pyproject.toml' in any parent directory.")
        current_dir = parent_dir

BASE_DIR = find_base_dir_with_pyproject()

# DIRECTORIES

DADOS_DIR = BASE_DIR / 'dados'
DADOS_GIT_DIR = BASE_DIR / 'dados-git'

DADOS_BRUTOS_DIR = DADOS_DIR / 'brutos'
DADOS_VEQ_ANTT_DIR = DADOS_BRUTOS_DIR / 'trafego-ANTT'

DADOS_DERIVADOS_DIR = DADOS_DIR / 'derivados'
# DADOS_CONSOL_VEQ_ANTT = DADOS_DERIVADOS_DIR / 'trafego-VEQ-ANTT'

# GLOBAL VARIABLE WITH DIRTREE
PROJECT_DIRS = {name : path for name, path in globals().items() if isinstance(path, Path)}

# Creating the DIRTREE
def make_dirs():    
    for directory in PROJECT_DIRS.values():
        directory.mkdir(parents=True, exist_ok=True)
        
make_dirs()     


    
