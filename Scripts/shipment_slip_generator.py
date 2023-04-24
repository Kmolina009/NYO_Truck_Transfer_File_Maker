# import os
from packed_shipment_filter import packedshipments
# import packedshipments fr

print(packedshipments)
# END GOAL -> Create the docs neccesary for either a provided directory or have it made,

# Take a provided directory(ask user),
# Take data from packed shipments,
# Check the directory for files with names that contain D.IDs
# If matchs are found, remove them from the prep list(Avoid duplicate entries)

# directory = '/path/to/directory'  # replace with the path to your directory
# for filename in os.listdir(directory):
#     if filename.endswith('.txt'):  # replace with the file extension you want to read
#         filepath = os.path.join(directory, filename)
#         with open(filepath) as f:
#             contents = f.read()
            # do something with the contents of the file

# Once it's been determined which emtris are not in the specified directory, then document creation can start
# Have Template
# Have filtered data