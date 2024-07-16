import re
import os
import wordninja
import shutil

def FileScrubber(source_directory):
    def split_and_title_case(filename):
    # Remove the "Pdf" suffix if it exists
        if filename.lower().endswith("pdf"):
            filename = filename[:-3]  # Remove the last 3 characters ("Pdf")
    # Use wordninja to segment the filename into words
        words = wordninja.split(filename)
    # Capitalize each word and join them into title case
        title_case_name = ''.join(word.capitalize() for word in words)
        return title_case_name
    
    # Print statement to verify source_directory input during testing
    print(f"Scanning files in directory: {source_directory}")

    files = os.listdir(source_directory)
    #Only looking for pdf files at the moment
    files = [file for file in files if os.path.isfile(os.path.join(source_directory, file)) and file.lower().endswith('.pdf')]
    
    renamed_files = {}
    for file in files:
        title_case_name = split_and_title_case(file)
        renamed_files[file] = title_case_name
    
        # Print statement to show input and output of each file during testing
        print(f"Original File: {file} -> Renamed File: {title_case_name}")

    return renamed_files



def FileSorter(source_directory, destination_directory, category_dict):
    renamed_files = FileScrubber(source_directory)
    
    categorized_files = {}
    for original_file, title_case_name in renamed_files.items():
        for category, keywords in category_dict.items():
            if any(keyword.lower() in title_case_name.lower() for keyword in keywords):
                if category not in categorized_files:
                    categorized_files[category] = []
                categorized_files[category].append(original_file)
    
    for category in categorized_files.keys():
        category_path = os.path.join(destination_directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    for category, files in categorized_files.items():
        category_path = os.path.join(destination_directory, category)
        for file in files:
            original_path = os.path.join(source_directory, file)
            new_path = os.path.join(category_path, file)
            shutil.move(original_path, new_path)
            print(f'Moved: {original_path} -> {new_path}')
