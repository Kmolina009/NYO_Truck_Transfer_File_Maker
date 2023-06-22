import os
import re
from docxtpl import DocxTemplate
from packed_shipment_filter import packedshipments

# # Take a provided directory(ask user),
directory =str(input("Please provide directory for these files")) 
#Use this path for the time being...'../files_to_write_docs_too'  # replace with the path to your directory

def process_shipments(provided_directory):
    entries = os.scandir(provided_directory)
    starting_patterning = re.compile('^D_ID_')

    # Find matching file names
    entries_found = [entry.name[5:-5] for entry in entries if entry.is_file() and starting_patterning.match(entry.name)]

    # Convert packedshipments list to dictionary
    packedshipments_dict = {item['DID / REF']: item for item in packedshipments}

    # Filter items in packedshipments list
    entries_to_be_added = [item for item in packedshipments if item['DID / REF'] not in entries_found]

    # Make docs
    doc = DocxTemplate("nyo_template.docx")
    print(len(entries_to_be_added))
    for item in entries_to_be_added: 
        context = {'Destination':"Dal",
                'Date_of_Departure':"1/1/2022", #Placeholder
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
        return "Entries added to provided directory! 🙂"

# Where will these things be saved/written too?
def directory_exist
if os.path.exists(directory):
    process_shipments(directory)
else:
    print("This directory does not exist.")