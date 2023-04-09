import os
import shutil

# The main folder containing the subfolders to be processed
main_folder = "D:\Downloads\Flank_Unorthodox"

# The name of the destination folder
destination_folder = "D:\Desktop\Chess Data Sets"

# Recursively loop through each subfolder in the main folder
for root, dirs, files in os.walk(main_folder):
    # Loop through each subfolder in the current folder
    for dir_name in dirs:
        # Construct the path to the subfolder
        subfolder_path = os.path.join(root, dir_name)

        # Move the contents of the subfolder to the destination folder
        for file_name in os.listdir(subfolder_path):
            source_file_path = os.path.join(subfolder_path, file_name)
            destination_file_path = os.path.join(destination_folder, file_name)
            shutil.move(source_file_path, destination_file_path)

        # Remove the empty subfolder
        #os.rmdir(subfolder_path)