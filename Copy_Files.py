"""
My task: I have a folder containing many folders named after projects. 
These project folders have various amounts/levels of subfolders. I want 
to create new folders with the same name as the project folders in another 
folder. Then I want to copy files with specific names into the correct 
newly created project folder. 

Copyright (c) 2025 CHLAU5206
"""
from concurrent.futures import ThreadPoolExecutor
import os
import shutil
import logging
#from glob import glob
 
# Define the search keywords
search_words = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.mov']
#['Genomförandebeskrivning', 'administrativa föreskrifter', 'AF', 'GB', 'mervärdersbeskrivning']
 

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Define the input and output directories
PROJECT_ROOT = r'c:\Testing'
input_dir = os.path.join(PROJECT_ROOT, 'input')
output_dir = os.path.join(PROJECT_ROOT, 'output')
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.mov','mp4','HEIC')

""" create logging module"""
class Logger:
    
    def create_logger_in_diff_files(log_folder):
        import logging
        # Create loggers and set the overall logging level
        logger = logging.getLogger("app")
        logger.setLevel(logging.DEBUG)

        # Create file handlers for each level
        info_handler = logging.FileHandler("info.log")
        info_handler.setLevel(logging.INFO)

        warning_handler = logging.FileHandler("warning.log")
        warning_handler.setLevel(logging.WARNING)

        error_handler = logging.FileHandler("error.log")
        error_handler.setLevel(logging.ERROR)

        # Create a formatter and attach it to each handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        info_handler.setFormatter(formatter)
        warning_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(info_handler)
        logger.addHandler(warning_handler)
        logger.addHandler(error_handler)

        # Log messages of different levels
        logger.info("This is an INFO message.")
        logger.warning("This is a WARNING message.")
        logger.error("This is an ERROR message.") 

        return logger

""" copy files by extensions """
def copy_file_ext(input_dir, output_dir, search_words):

    # Create the target folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    def copy_file(source_path):
        try:
            shutil.copy2(source_path, output_dir)
            logs_pass.append(source_path)
        except Exception as e:
            logs_fail[source_path] = e

    # Log file for errors
    logs_pass = []
    logs_fail = {}

    # Collect all image files
    image_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(os.path.join(root, file))  # do I need dirs?

    # Use ThreadPoolExecutor with controlled max_workers
    # Adjust max_workers based on system resources.  A value of 5-10 is usually safe 
    # for I/O-bound operations like file copying. 
    with ThreadPoolExecutor(max_workers=5) as executor:  
        executor.map(copy_file, image_files)

    # Save results to a log file at the end
    logs_pass_file = os.path.join(output_dir, "log_pass.txt")
    logs_fail_file = os.path.join(output_dir, "log_fail.txt")
    with open(logs_pass_file, "w") as pf:
        for file_path in logs_pass:
            pf.writelines(file_path)
            # pf.write(file_path)

    with open(logs_fail_file, "w") as ff:
        for file_path, status in logs_fail.items():
            ff.write(f"{file_path}: {status}\n")


    print("File copy operation completed. Check results_log.txt for details.")


""" Sample #1 """
def copy_file1(input_dir, output_dir, search_words):
    # Walk through the directories and files in the input directory
    for dirpath, dirnames, filenames in os.walk(input_dir):
        # Get the corresponding subdirectory path in the output directory
        rel_dirpath = os.path.relpath(dirpath, input_dir)
        output_subdir = os.path.join(output_dir, rel_dirpath)
        os.makedirs(output_subdir, exist_ok=True)
    
        # Loop through the files in the current directory
        for filename in filenames:
            # Check if the file contains any of the search keywords
            if any(word in filename for word in search_words):
                # Copy the file to the output directory
                input_filepath = os.path.join(dirpath, filename)
                output_filepath = os.path.join(output_subdir, filename)
                shutil.copy2(input_filepath, output_filepath)

""" Sample #1 """
def copy_file2(input_dir, output_dir, search_words):

    # Create the target folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Supported image extensions
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.mov']

    # Log file for errors
    error_log = os.path.join(output_dir, "error_log.txt")

    # Open the log file
    with open(error_log, "w") as log:
        for ext in image_extensions:
            # Get all files with the current extension
            for file_path in glob(os.path.join(input_dir, '**', ext), recursive=True):
                try:
                    # Copy file to target folder
                    shutil.copy(file_path, output_dir)
                except Exception as e:
                    # Log the error and continue
                    log.write(f"Failed to copy {file_path}: {e}\n")

    print("Picture files copied. Check error_log.txt for any issues.")
