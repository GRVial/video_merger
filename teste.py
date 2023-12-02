import os


def find_files(root_folder, file_extension=".srt"):
    found_files = []

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(file_extension):
                found_files.append(os.path.join(root, file))
    return found_files

# Specify the root folder to start the search
root_directory = 'sub'

# Call the function to find all text files
text_files = find_files(root_directory, file_extension=".srt")

# Print the list of found text files
for text_file in text_files:
    print(text_file)