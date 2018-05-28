# -*- Python 3.6 -*-

# mass_file_editor.py

import os

# Set directory for mass edit.
folder = "your directory"
FileList = os.listdir(folder)

# Start looping over all files within the directory.
for files in FileList:
    if " " in files:
        NewName = files.replace(" ", "_")
        os.rename(os.path.join(folder, files), os.path.join(folder, NewName))
