import os
import wordninja
import shutil


#using a class instead of individual functions
class FileSorter:
    def __init__(self, source_dir, dest_dir, category_dict):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.category_dict = category_dict

    def sort_and_rename_files(self):
        for filename in os.listdir(self.source_dir):
            if filename.endswith('.pdf'):
                original_path = os.path.join(self.source_dir, filename)
                new_name = self.rename_file(filename)
                category = self.categorize_file(filename)
                
                if category:
                    dest_folder = os.path.join(self.dest_dir, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    new_path = os.path.join(dest_folder, new_name)
                    
                    print(f"Original File: {filename} -> Renamed File: {new_name}")
                    shutil.move(original_path, new_path)
                    print(f"Moved: {original_path} -> {new_path}")

    def rename_file(self, filename):
        # Remove the "Pdf" suffix if it exists
        if filename.lower().endswith("pdf"):
            filename = filename[:-3]
        # Use wordninja to segment the filename into words
        words = wordninja.split(filename)
        # Capitalize each word and join them into title case
        new_name = ''.join(word.capitalize() for word in words) + '.pdf'
        return new_name
    def categorize_file(self, filename):
        category = None
        for key, keywords in self.category_dict.items():
            if any(keyword.lower() in filename.lower() for keyword in keywords):
                category = key
                break
        return category      


