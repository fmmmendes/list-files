import os
import sys
import pytest
from list_files import list_files

FOLDER_TEST = "./test_folder"

def test_list_files_is_list():
    # Test if list_files returns a list
    assert isinstance(list_files(FOLDER_TEST), list)
    
def test_list_files_check_content():
    # Test if list_files returns the correct files in the current directory
    assert list_files(FOLDER_TEST) == ["./test_folder/file1.txt", "./test_folder/file2.md"]
    
    