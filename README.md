This program is meant to sort through my personal digital library dump and sort titles according to defined keywords. I would like to reuse this program whenever additional titles are added. 



This program needs to:

-Load and Read File Names

-Transform File Names according to defined formatting
    -use title case formatting without spaces

-Categorize Files using a dictionary to map keywords to categories.
    -setup a dictionary to categorize titles into folders
        example: There will be a "Certifications" folder that will house other folders for specific certs. The books or guides about cert X will get sorted into a folder named CertX.

-Save the categorized and formatted file names.





FileScrubber Function: Handles scanning the source directory for PDF files, renaming them using split_and_title_case, and returning a dictionary mapping original filenames to their title-cased versions.

FileSorter Function: Uses FileScrubber to get renamed files, categorizes them based on category_dict, creates destination directories if they don't exist, and moves files accordingly.

main Function: Prompts the user for the source directory path, verifies its existence, and then calls FileSorter to perform the categorization and file sorting operations.