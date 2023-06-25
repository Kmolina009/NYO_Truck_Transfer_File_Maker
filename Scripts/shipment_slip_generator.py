import os
import re
from docxtpl import DocxTemplate
from packed_shipment_filter import packedshipments

date_of_departure = input("When will the Truck be leaving?")
truck_origin =input("Where is it coming from?") 
truck_destination =input("Where is it going?") 
origin_to_destination = f"{truck_origin} to {truck_destination}"

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
        # context = {'Destination':f"{origin_to_destination}",
        # Bug Report - For some reason, it will write NYO without it being provided.
        context = {'Destination':f"{origin_to_destination}",
                'Date_of_Departure':f"{date_of_departure}", #Placeholder
                # 'Date_of_Departure':"1/12/1234", #Placeholder
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
process_shipments('../files_to_write_docs_too')