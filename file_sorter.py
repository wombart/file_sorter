"""_summary_
    My Little File Sorter and Mover
Returns:
    _type_: _description_
"""

import os
import logging
import shutil
import yaml

def setup_logging(debug=False):
    """_summary_
        Setup logging
    Args:
        debug (bool, optional): _description_. Defaults to False.
    """
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(filename='move_files.log', level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path):
    """_summary_
        Load config file.
    Args:
        config_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(config_path, mode="r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)
    return config

def move_files(config, debug=False):
    """_summary_
        Move files or simulate.
    Args:
        config (_type_): _description_
        debug (bool, optional): _description_. Defaults to False.
    """
    source_dir = config['source_directory']
    target_dirs = config['target_directories']

    for keyword, target_dir in target_dirs.items():
        keyword_lower = keyword.lower()
        target_path = os.path.join(source_dir, target_dir)

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        for filename in os.listdir(source_dir):
            if keyword_lower in filename.lower():
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_path, filename)

                if debug:
                    logging.debug(f"Would move {filename} to {target_path}")
                else:
                    shutil.move(source_file, target_file)
                    logging.info(f"Moved {filename} to {target_path}")

if __name__ == "__main__":
    CONFIG_PATH = 'file_sorter.yaml'
    DEBUG_MODE = False  # Setze auf False, um den DEBUG-Modus zu deaktivieren

    try:
        setup_logging(debug=DEBUG_MODE)
        logging.info("Starting")

        configuration = load_config(CONFIG_PATH)
        move_files(configuration, debug=DEBUG_MODE)

        logging.info("Finished")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
