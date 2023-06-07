import os

def delete_empty_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.stat(file_path).st_size == 0:
                os.remove(file_path)
                print(f"Deleted empty file: {file_path} ")

path = "/home/jerripat/PythonProjects"
delete_empty_files(path)
