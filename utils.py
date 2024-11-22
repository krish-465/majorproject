import os

def ensure_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_files_in_folder(folder_path, extension=".bin"):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(extension)]
