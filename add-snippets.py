import os
import shutil

def clear_and_copy(source, destination, extension):
    """
    Clears all contents of the destination folder and copies all files
    with the specified extension from the source folder recursively.
    
    :param source: Folder to search for files.
    :param destination: Folder where files will be copied.
    :param extension: File extension to copy (e.g., '.txt').
    """
    # 1. Clear the destination folder
    if os.path.exists(destination):
        for item in os.listdir(destination):
            item_path = os.path.join(destination, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
    else:
        os.makedirs(destination)

    # 2. Recursively search and copy files with the specified extension
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(extension):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(destination, file)
                
                # Avoid overwriting files with the same name
                counter = 1
                base_name, ext = os.path.splitext(file)
                while os.path.exists(dest_path):
                    dest_path = os.path.join(destination, f"{base_name}_{counter}{ext}")
                    counter += 1
                
                shutil.copy2(source_path, dest_path)

# Example usage:
clear_and_copy('snippets', '.vscode', '.code-snippets')
