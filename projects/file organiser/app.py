import os
import shutil
from datetime import datetime

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def get_file_extension(filename):
    """Get the file extension."""
    return os.path.splitext(filename)[1][1:].lower()

def organize_files(source_dir):
    """Organize files in the source directory based on their extensions."""
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file)):
            extension = get_file_extension(file)
            if not extension:
                extension = "no_extension"
            
            target_dir = os.path.join(source_dir, extension)
            create_directory(target_dir)
            
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, file)
            
            shutil.move(source_path, target_path)
            log_operation(f"Moved {file} to {extension}")

def log_operation(message):
    """Log the operation with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# TODO: Implement error handling

if __name__ == "__main__":
    # TODO: Get the source directory from user input or use a default
    source_directory = r"C:\Users\DeanThornton\OneDrive - De Montfort University"
    
    # TODO: Call the organize_files function
    organize_files(source_directory)
    # TODO: Print a summary of the operations performed
    print("File organization completed successfully.")
