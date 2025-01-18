import os

def find_seaborn_files(start_dir, keyword="seaborn"):
    """Search for files containing the keyword 'seaborn' in their paths."""
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))

# Replace with the directory you want to search. Example: the site-packages directory of your Python installation.
python_lib_dir = os.path.join(os.path.dirname(os.__file__), "site-packages")

print(f"Searching for '{keyword}' in {python_lib_dir}...\n")
find_seaborn_files(python_lib_dir)