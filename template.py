import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "datascience"

list_of_files = [
    ".github/workflows/.gitkeep", 

    # the init is to convert this entire src into a pacakge, so it can import anywhere
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", # pipeline
    f"src/{project_name}/utils/__init__.py", # generic functionality
    f"src/{project_name}/utils/common.py", # have all the common functionality
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # have info on all the different pipeline to create
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "DockerFile",
    "setup.py", # to create the entire project as a package
    "research/research.ipynb",
    "templates/index.html",
    "app.py"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file :{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")