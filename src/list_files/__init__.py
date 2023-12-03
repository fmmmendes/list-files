import os 
import sys
import csv

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
