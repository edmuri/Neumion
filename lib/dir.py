import os
import shutil

def clean():
    temp_dir = "temp/"
    if not os.path.exists(temp_dir):
        return
    
    shutil.rmtree(temp_dir)