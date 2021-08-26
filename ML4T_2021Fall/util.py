import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file_path(file):
    return os.path.join(CUR_DIR, "data", file)