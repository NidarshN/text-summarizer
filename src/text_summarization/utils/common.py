import os
from box import ConfigBox 
from box.exceptions import BoxValueError
import yaml
from text_summarization.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Function to read yaml file and return ConfigBox typed yaml file content

    Parameters:
    ___________
                path_to_yaml (str): Path to yaml file

    Raises:
    ___________
            ValueError: If yaml file is empty
            e: empty file

    Returns:
    ___________
            ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            file_content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully!" )
            return ConfigBox(file_content)
    except BoxValueError:
        raise ValueError("yaml file: {path_to_yaml} is empty!")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Function to create a list of directories

    Parameters:
    ___________
                path_to_directories (list): list of path_dictionaries
                verbose (bool, optional): Ignore if multiple directories are to
                                            be created. Default Value is True
    
    Returns:
    ___________
            None
    """ 
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if(verbose):
            logger.info(f"Directory at path: {path} created successfully!")