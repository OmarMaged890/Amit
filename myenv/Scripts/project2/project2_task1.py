import os
import random

def manage_files_in_folder(folder_path, num_files):
    
    # Step 1: Open the whole folder
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    # Create the specified number of files inside it
    for i in range(num_files):
        file_path = os.path.join(folder_path, f"file_{i}.txt")
        with open(file_path, 'w') as f:
            f.write("This is a test file.")

    # Check the number of files in that folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(f"Number of files before deletion: {len(files)}")

    # Delete random half of this folder
    num_to_delete = len(files) // 2
    files_to_delete = random.sample(files, num_to_delete)
    
    for file in files_to_delete:
        os.remove(os.path.join(folder_path, file))
        print(f"Deleted: {file}")

    # Check the result
    remaining_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(f"Number of files after deletion: {len(remaining_files)}")