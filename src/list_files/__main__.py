import sys

from . import list_files
#from src.list_files import list_files

if __name__ == '__main__':
    
    print('run main')
    search_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    list_files(path=search_path)
    