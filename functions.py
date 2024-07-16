import os
import wordninja
import shutil

class FileSorter:
    def __init__(self, source_dir, dest_dir):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.category_dict = self.create_category_dict()

    def create_category_dict(self):
        return {
            'AWS': ['AWS', 'Amazon'],
            'Google': ['Google'],
            'Azure': ['Azure', 'Micro'],
            'ISC2': ['ISC', 'CCSP'],
            'CompTIA': ['Comptia', 'cv0-002', 'Plus']
        }

    def sort_and_rename_files(self):
        for filename in os.listdir(self.source_dir):
            if filename.endswith('.pdf'):
                original_path = os.path.join(self.source_dir, filename)
                new_name = self.rename_file(filename)
                
                # Check if renaming was successful
                if new_name and new_name != filename:
                    category = self.categorize_file(new_name)  # Use new_name for categorization
                    
                    if category:
                        dest_folder = os.path.join(self.dest_dir, category)
                        os.makedirs(dest_folder, exist_ok=True)
                        new_path = os.path.join(dest_folder, new_name)
                        
                        print(f"Original File: {filename} -> Renamed File: {new_name}")
                        shutil.move(original_path, new_path)
                        print(f"Moved: {original_path} -> {new_path}")
                else:
                    print(f"Skipping file: {filename} (renaming failed or no change)")

    def rename_file(self, filename):
        # Remove the ".pdf" extension
        base_name = filename[:-4] if filename.lower().endswith('.pdf') else filename
        # Use wordninja to segment the filename into words
        words = wordninja.split(base_name)
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