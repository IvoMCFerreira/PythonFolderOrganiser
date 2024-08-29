import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Define the mapping of file extensions to folder names
file_type_folders = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'music': ['.mp3', '.wav', '.aac', '.flac'],
    'archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    # Add more categories and extensions as needed
}

# Function to create a folder if it doesn't exist
def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to move files into their corresponding folders
def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder_name, extensions in file_type_folders.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(folder_path, folder_name)
                    create_folder_if_not_exists(destination_folder)
                    shutil.move(file_path, destination_folder)
                    print(f"Moved {filename} to {folder_name} folder")
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder_path, 'others')
                create_folder_if_not_exists(other_folder)
                shutil.move(file_path, other_folder)
                print(f"Moved {filename} to others folder")

# Function to open the folder selection dialog and organize the selected folder
def select_folder_and_organize():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory()  # Open the folder selection dialog
    if folder_selected:
        organize_folder(folder_selected)
        print(f"Organized folder: {folder_selected}")

# Run the script
if __name__ == "__main__":
    select_folder_and_organize()
