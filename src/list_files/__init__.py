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


def save_to_txt(list_of_files):
    
    # with open('output.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
        
    #     for i in list_of_files:
    #         writer.writerow([i])
            
    with open('output.txt', 'w') as f:
        f.write('\n'.join(list_of_files))
