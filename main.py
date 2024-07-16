import os
import shutil
from functions import FileSorter  # Update import

'''
-move create_category_dict into categorize_file for clarity

-add exception for keyword not matching (currently files are not moved until key match)
    -we can just leave anything that doesnt match in a special folder in the dest dirctory for manual (human) sorting
    -make sure this folder is created within the dest directory
'''

def main():
    source_directory = input("Please enter the source directory path: ") #E:\LibraryTestSource
    
    if not os.path.isdir(source_directory):
        print("The provided source directory does not exist.")
        return

    destination_directory = input("Please enter the destination directory path: ") #E:\LibraryTestDest
    sorter = FileSorter(source_directory, destination_directory)
    sorter.sort_and_rename_files()

if __name__ == "__main__":
    main()