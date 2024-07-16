import os
import wordninja
import shutil

class FileSorter:
    #creates a new instance 
    def __init__(self, source_dir, dest_dir):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.category_dict = self.create_category_dict()

    #move this into categorize_files to condense methods
    #values can be lowercase because categorize_file runs .lower()
    def create_category_dict(self):
        return {
            'AWS': ['AWS', 'Amazon'],
            'Google': ['Google'],
            'Azure': ['Azure', 'mca'],
            'ISC': ['isc','isc2'],
            'CompTIA': ['comptia', 'cv0-002', 'plus'],
            'Hashicorp':['hashi', 'terraform',],
            'ISACA':['isaca', 'crisc', 'cisa', 'cism', 'certifiedinformationsecuritymanager'],
            'LPI':['lpi', "lpic"],
            'SQL':['sql', 'mysql'],
            'Python': ['python', 'pytorch', 'ansible'],
            'Oracle':['Oracle', 'ocp', 'database'],
            'Java': ['java'],
            'PMP':['pmp', 'projectmanagement'],
            'Cisco':['cisco', 'ccna', 'ccnp', 'ccie'],
            'Containers': ['kubernetes', 'kube', 'k8', 'docker'],
            'Linux': ['linux', 'unix', 'bash', 'grep', 'awk', 'vim', 'shell', 'scripting', 'PowerShell'],
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
                    print(f"Skipping file: {filename} (renaming failed or no keyword match)")

    def rename_file(self, filename):
        # Remove the ".pdf" extension
        base_name = filename[:-4] if filename.lower().endswith('.pdf') else filename
        # Use wordninja to segment the filename into words
        words = wordninja.split(base_name)
        #Might need to run the output through some regex to fix the acronym situation (AwS, CcNa)
        # Capitalize each word and join them into title case
        new_name = ''.join(word.capitalize() for word in words) + '.pdf'
        return new_name

    def categorize_file(self, filename):
        category = None
        for key, keywords in self.category_dict.items():
            if any(keyword.lower() in filename.lower() for keyword in keywords):
                category = key
                break

        else:
            category = 'Unsorted'  # Set category to 'Unsorted' if no match is found for manual sorting
        return category