import os
import shutil

def organize_files_by_extension(directory):
    """
    Organizes files into folders based on their extensions.
    """
    # Check if the given directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate over each file in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)  # Full path of the file
        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Extract the file extension and convert to lowercase
            extension = file.split('.')[-1].lower()
            # Create a folder name based on extension, e.g., 'pdf_files'
            folder_name = f"{extension}_files"
            folder_path = os.path.join(directory, folder_name)

            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            # Move the file into the appropriate folder
            shutil.move(file_path, os.path.join(folder_path, file))

    print("Files organized successfully!")

if __name__ == "__main__":
    # Ask user to input the directory path to organize
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files_by_extension(target_directory)