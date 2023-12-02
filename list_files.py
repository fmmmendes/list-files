import os 
import sys


def list_files(path):
    """
    Lists all files in a directory and its subdirectories.
    """
    
    res = []
    
    for root, dirs, files in os.walk(path):
        for file in files:
            res_path = os.path.join(root, file)
            print(res_path)
            res.append(res_path)
    
    return res


if __name__ == '__main__':
    
    search_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    list_files(path=search_path)