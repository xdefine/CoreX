# file_cleaner.py
import os
import tempfile
import shutil

def clean_temp_files():
    temp_dir = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                except:
                    pass
        return f"Temp files deleted from {temp_dir}"
    except Exception as e:
        return str(e)
