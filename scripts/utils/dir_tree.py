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
DADOS_GIT_BACEN_DIR = DADOS_GIT_DIR / 'dados-bacen'

DADOS_BRUTOS_DIR = DADOS_DIR / 'brutos'
DADOS_VEQ_ANTT_DIR = DADOS_BRUTOS_DIR / 'trafego-ANTT'

DADOS_DERIVADOS_DIR = DADOS_DIR / 'derivados'
DADOS_PIB_DIR = DADOS_DERIVADOS_DIR / 'PIB'
DADOS_TRAFEGO_DIR = DADOS_DERIVADOS_DIR / 'trafego'
DADOS_ANUAL_DIR = DADOS_TRAFEGO_DIR / 'anual'
DADOS_TRIMESTRAL_DIR = DADOS_TRAFEGO_DIR / 'trimestral'
DADOS_MENSAL_DIR = DADOS_TRAFEGO_DIR / 'mensal'
DADOS_TRAFEGO_AJUSTADOS_DIR = DADOS_TRAFEGO_DIR / 'ajustados-sazonalidade'
DADOS_TRAFEGO_AJUSTADOS_MENSAL_DIR = DADOS_TRAFEGO_AJUSTADOS_DIR / 'mensal'
DADOS_TRAFEGO_AJUSTADOS_TRIMESTRAL_DIR = DADOS_TRAFEGO_AJUSTADOS_DIR / 'trimestral'
DADOS_REGRESSAO_DIR = DADOS_DERIVADOS_DIR / 'regressoes'
DADOS_REGRESSAO_ANUAL_DIR = DADOS_REGRESSAO_DIR / 'anual'
DADOS_REGRESSAO_TRIMESTRAL_DIR = DADOS_REGRESSAO_DIR / 'trimestral'
DADOS_REGRESSAO_MENSAL_DIR = DADOS_REGRESSAO_DIR / 'mensal'

# GLOBAL VARIABLE WITH DIRTREE
PROJECT_DIRS = {name : path for name, path in globals().items() if isinstance(path, Path)}

# Creating the DIRTREE
def make_dirs():    
    for directory in PROJECT_DIRS.values():
        directory.mkdir(parents=True, exist_ok=True)
        
make_dirs()     


    
