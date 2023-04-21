"""
Created on Sun Apr  2 15:11:17 2023

@author: Keven
"""
import csv

# with open(r"C:\Users\Keven\OneDrive\Desktop\NYO_Stuff\Dummy_Data\Test_Copy\NY_Truck_Transfers_NYO_Dummy_Data_CSV.csv","r") as csv_file:
with open(r"Dummy_Data\Test_Copy\NY_Truck_Transfers_NYO_Dummy_Data_CSV.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
#    NOTE - Variable names need to be cleaned up, refer to style guide
# Entries to be zipped
    Names = []
    Status =[]
    Item_Numbers = []
    Client_Numbers = []
    DIDs = []
    Descriptions = []
    Senders = []
    Recipients = []
    Venues = []
    Sales_Numbers = []
    Sale_Deadlines = []
    Values = []
    Item_Counts = []
    Locations = []
    Bin_Numbers = []
    Box_Counts = []
    data = []
    # Refactor(Remove Repetition)
    next(csv_file)
    next(csv_file)
    for row in csv_reader:
        # Name, Status, Item#, Client#, DID, Description, Sender, Recipient, Venue, Sale#, Sale_Deadline, Value, Item_Count, Location, Bin#, Box_Count,
        # print( row['Name'], row['Status'], row['Item #'], row['Client #'], row['DID / REF'], row['Description'], row['Sender'], row['Recipient'], row['Venue'], row['Sale #'], row['Sale Deadline'], row['Value'], row['Item Count'], row['Location'], row['Bin #'], row['Box Count'] )
        Names.append( row['Name'])
        Status.append( row['Status']) 
        Item_Numbers.append( row['Item #'])              
        Client_Numbers.append(  row['Client #'])
        DIDs.append( row['DID / REF'])
        Descriptions.append( row['Description'])
        Senders.append( row['Sender'])
        Recipients.append( row['Recipient'])
        Venues.append( row['Venue'])
        Sales_Numbers.append( row['Sale #'])
        Sale_Deadlines.append( row['Sale Deadline'])
        Values.append( row['Value'])
        Item_Counts.append( row['Item Count'])
        Locations.append( row['Location'])
        Bin_Numbers.append( row['Bin #'])
        Box_Counts.append( row['Box Count'])
        # data.append(row['Name'],row['Status'],row['Item_Number'],row['Client'],row['DID'],row'[Description'],row['Sender'],row['Recipient'],row['Venue'],row['Sales_Number'],row['Sale_Deadline'],row['Value'],row['Item_Count'],row'[Location'],row['Bin'],row['Box_Count'])
        
        shipments = []
        
        for i in range(len(Names)-1):
            dictionary = {}
            dictionary['Name'] = Names[i]
            dictionary['Status'] = Status[i]
            dictionary['Item #'] = Item_Numbers[i]
            dictionary['Client #'] = Client_Numbers[i]
            dictionary['DID / REF'] = DIDs[i]
            dictionary['Description'] = Descriptions[i]
            dictionary['Sender'] = Senders[i]
            dictionary['Recipient'] = Recipients[i]
            dictionary['Venue'] = Venues[i] 
            dictionary['Sale #'] = Sales_Numbers[i]
            # dictionary['Sale Deadline'] = Sale_Deadlines[i] Needs work issue with entries that are just hashtags
            dictionary['Value'] = Values[i]
            dictionary['Item Count'] = Item_Counts[i]
            dictionary['Location'] = Locations[i]
            shipments.append(dictionary)