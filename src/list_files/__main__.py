import sys

from . import list_files, save_to_txt
#from src.list_files import list_files

if __name__ == '__main__':
    
    print('run main')
    search_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    res = list_files(path=search_path)
    
    save_to_txt(list_of_files = res)