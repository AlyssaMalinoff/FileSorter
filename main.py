import os
import shutil
from functions import FileSorter  # Update import

def main():
    source_directory = input("Please enter the source directory path: ") #U:\Coding\PersonalProjects\LibraryTestSource

    if not os.path.isdir(source_directory):
        print("The provided source directory does not exist.")
        return

    destination_directory = input("Please enter the destination directory path: ") #U:\Coding\PersonalProjects\LibraryTestDest
    category_dict = {
        'AWS': ['AWS', 'Amazon'],
        'Google': ['Google'],
        'Azure': ['Azure', 'Micro'],
        'ISC2': ['ISC', 'CCSP'],
        'CompTIA': ['Comptia', 'cv0-002', 'Plus']
    }

    FileSorter(source_directory, destination_directory, category_dict)

if __name__ == "__main__":
    main()