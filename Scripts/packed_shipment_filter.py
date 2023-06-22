"""
Created on Sun Apr  2 15:11:17 2023

@author: Keven
"""
import csv

# with open(r".\Dummy_Data\Test_Copy\NY_Truck_Transfers_NYO_Dummy_Data_CSV.csv","r") as csv_file:
with open(r".\Dummy_Data\Test_Copy\NY_Truck_Transfers_NYO_Dummy_Data_CSV.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
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
        Names.append( row['Name'])
        Status.append( row['Status']) 
        Item_Numbers.append( row['Item #'])              
        Client_Numbers.append(  row['Client #'])
        DIDs.append( row['DID / REF'])
        Descriptions.append( row['Description'])
        Senders.append( row['Sender'])
        Recipients.append( row['Recipient'])
        Venues.append( row['Venue'])
        Values.append( row['Value'])
        Item_Counts.append( row['Item Count'])
        Locations.append( row['Location'])
        Bin_Numbers.append( row['Bin #'])
        Box_Counts.append( row['Box Count'])
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
            dictionary['Value'] = Values[i]
            dictionary['Item Count'] = Item_Counts[i]
            dictionary['Location'] = Locations[i]
            shipments.append(dictionary)
    packedshipments = list(filter(lambda x : x["Status"] ==  "Packed", shipments))