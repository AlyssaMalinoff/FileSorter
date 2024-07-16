import os
import shutil
from functions import FileSorter  # Update import

'''
TODO
-Fix the file move process to make sure the files are renamed beforehand
    -or dont? it might be easier to move the files first because we know all the source files will be lowercase. 
    Once they're sorted we can run FileScrubber? This would also make sorting easier as the dict values could just be lowercase 
'''

def main():
    source_directory = input("Please enter the source directory path: ") #E:\LibraryTestSource
    
    if not os.path.isdir(source_directory):
        print("The provided source directory does not exist.")
        return

    destination_directory = input("Please enter the destination directory path: ") #E:\LibraryTestDest
    category_dict = {
        'AWS': ['AWS', 'Amazon'],
        'Google': ['Google'],
        'Azure': ['Azure', 'Micro'],
        'ISC2': ['ISC', 'CCSP'],
        'CompTIA': ['Comptia', 'cv0-002', 'Plus']
    }

    sorter = FileSorter(source_directory, destination_directory, category_dict)
    sorter.sort_and_rename_files()

if __name__ == "__main__":
    main()