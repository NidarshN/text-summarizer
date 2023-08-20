import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

PROJECT_NAME = "text_summarization"
fileList = [
    ".github/workflows/.gitkeep",
    "app.py",
    "config/config.yaml",
    "Dockerfile",
    "main.py",
    "params.yaml",
    "requirements.txt",
    "research/trials.ipynb",
    "setup.py",
    "test.py",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/constants/__init__.py"
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",    
]

for filePath in fileList:
    filePath = Path(filePath)
    filedir, filename = os.path.split(filePath)

    if(filedir != ""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Diretory: {filedir} for file: {filename}.")

    if((not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0)):
        with open(filePath, 'w') as f:
            pass
            logging.info(f"Created Empty File: {filePath}.")
    else:
        logging.info(f"File: {filePath} already exists!")