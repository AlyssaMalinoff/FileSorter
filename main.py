import os
import shutil
from functions import FileSorter  # Update import

def main():
    source_directory = input("Please enter the source directory path: ")

    if not os.path.isdir(source_directory):
        print("The provided source directory does not exist.")
        return

    destination_directory = 'path/to/your/destination/files'
    category_dict = {
        'Reports': ['report', 'summary', 'analysis'],
        'Essays': ['essay', 'paper', 'article'],
        'Theses': ['thesis', 'dissertation', 'study']
    }

    FileSorter(source_directory, destination_directory, category_dict)

if __name__ == "__main__":
    main()