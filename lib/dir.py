import os
import shutil

def get_files(path):
    if not os.path.exists(path):
        return []
    
    listed_dir = os.listdir(path)
    files = list(filter(lambda x: ".mp3" in x, listed_dir))
    return files

def clean():
    temp_dir = "temp/"
    if not os.path.exists(temp_dir):
        return
    
    shutil.rmtree(temp_dir)
