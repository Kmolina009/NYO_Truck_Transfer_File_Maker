import os
import re
from docxtpl import DocxTemplate
from packed_shipment_filter import packedshipments
# # import packedshipments fr

# print(packedshipments)
# # END GOAL -> Create the docs neccesary for either a provided directory or have it made,

# # Take a provided directory(ask user),
# # Take data from packed shipments,✔
# # Check the directory for files with names that contain D.IDs ✔
# # If matchs are found, remove them from the prep list(Avoid duplicate entries)
# # where_the_entries_are =input()
directory = '../files_to_write_docs_too'  # replace with the path to your directory

entries = os.scandir(directory)
starting_patterning = re.compile('^D_ID_')

# Find matching file names
entries_found = [entry.name[5:-5] for entry in entries if entry.is_file() and starting_patterning.match(entry.name)]

# Convert packedshipments list to dictionary
packedshipments_dict = {item['DID / REF']: item for item in packedshipments}

# Filter items in packedshipments list
entries_to_be_added = [item for item in packedshipments if item['DID / REF'] not in entries_found]

# # Once it's been determined which entris are not in the specified directory, then document creation can start
# # Have Template
# # Have filtered data

# TEMPLATE will pull from a specifed note in a provided directory (Destination and Departure Date), and from provided entries
    # The provided entries 

doc = DocxTemplate("nyo_template.docx")
# Context is used in an iteration -> Lambda Function or Loop
# The package quantity will be determine whether package will be " " or 1.
#   if package qty is 1, then package number is one  -  Else package is " "
#   Type checking might be required for error checking as well - Verifying that numbers are numbers or of a certain lenght
print(len(entries_to_be_added))
for item in entries_to_be_added:
    print(f"{item['Recipient']} - {item['Item #']} - {item['Client #']} -{item['Item Count']}")
# print(f"This is the first entry\n\n {entry_in_list}") 
    context = {'Destination':"Dal",
            'Date_of_Departure':"1/1/2022",
            'recipient':f"{item['Recipient']}",
            'line_item':f"{item['Item #']}",
            'client_number':f"{item['Client #']}",
                'package':" ",
                'package_quantity':f"{item['Item Count']}"
            }
    if(int(item['Item Count']) > 1):
        context['package'] = ' '
    else:
        context['package'] = '1'

    doc.render(context)
    doc.save(f"../files_to_write_docs_too/D_ID_{item['DID / REF']}.docx")

# Where will these things be saved?