import os
from packed_shipment_filter import packedshipments
# import packedshipments fr

# print(packedshipments)
# END GOAL -> Create the docs neccesary for either a provided directory or have it made,

# Take a provided directory(ask user),
# Take data from packed shipments,
# Check the directory for files with names that contain D.IDs
# If matchs are found, remove them from the prep list(Avoid duplicate entries)
# where_the_entries_are =input()
directory = '../files_to_write_docs_too'  # replace with the path to your directory
entries = os.scandir(directory)

for entry in entries:
    if entry.is_file():
        print('File:', entry.name)
    elif entry.is_dir():
        print('Directory:', entry.name)
            # do something with the contents of the file

# Once it's been determined which emtris are not in the specified directory, then document creation can start
# Have Template
# Have filtered data