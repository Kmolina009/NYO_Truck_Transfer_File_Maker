"""
Created on Sun Apr  2 15:11:17 2023

@author: Keven
"""
import csv

with open(r"C:\Users\Keven\OneDrive\Desktop\NYO_Stuff\NY_Truck_Transfers_NYO_Dummy_Data_CSV.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []
    # Refactor(Remove Repetition)
    next(csv_file)
    next(csv_file)
    for row in csv_reader:
        data.append(row)
        
    print(data)