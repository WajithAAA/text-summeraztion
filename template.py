import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(levelname)s: %(message)s')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/cofig.yaml",
    "developer_guide/developer_guide.md",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockeerfile",
    "setup.py",
    "requirements.txt",
    "research/trail.ipynb",
    "developer_guide/developer_guide.md"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {} for the file {}".format(filedir, filename))

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0:
        with open(filepath, "w") as f:
            pass
            logging.info("Creating empty file: {}".format(filepath))

    else:
        logging.info("{} is already exists".format(filename))


