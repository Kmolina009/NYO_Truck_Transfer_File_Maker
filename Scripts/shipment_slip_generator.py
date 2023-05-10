import os
import re
from packed_shipment_filter import packedshipments
# import packedshipments fr

# print(packedshipments)
# END GOAL -> Create the docs neccesary for either a provided directory or have it made,

# Take a provided directory(ask user),
# Take data from packed shipments,✔
# Check the directory for files with names that contain D.IDs ✔
# If matchs are found, remove them from the prep list(Avoid duplicate entries)
# where_the_entries_are =input()
directory = '../files_to_write_docs_too'  # replace with the path to your directory
entries = os.scandir(directory)
starting_patterning = re.compile('^D_ID_')

# Prep List
entries_found = []
entries_for_removal = []

for entry in entries:
    if entry.is_file() and starting_patterning.match(entry.name):
        entries_found.append(entry.name[5:-5])
print(entries_found)

for item in entries_found:
    for doc_entry in packedshipments:
        # found = False
        if doc_entry.get("DID / REF") == item:
            print("This entry already exist")
            entries_for_removal.append(doc_entry)
            # found = True
            break
        # if found:
        #     print( f"item : {doc_entry} is present in original_list.")
        # else:
        #     print( "item is not present in original_list.")
# Refactor Note: Is there a better way to place this variable
entries_to_be_added = [item for item in packedshipments if item not in entries_for_removal]
print(entries_to_be_added)
print(len(entries_to_be_added))
print(len(packedshipments))
# Once it's been determined which emtris are not in the specified directory, then document creation can start
# Have Template
# Have filtered data