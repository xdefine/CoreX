# file_manager.py
import os
import shutil

def list_files(directory):
    return os.listdir(directory)

def copy_file(src, dst):
    shutil.copy(src, dst)

def delete_file(path):
    os.remove(path)
