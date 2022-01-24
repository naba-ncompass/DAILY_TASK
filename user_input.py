from Utilities.db import *

def dml(choice):
    match choice:
        case 1:
            id = int(input("Enter the id: "))
            name = input("Enter the name: ")
            dept = input('Enter the dept: ')

            record = {
                'id':id,
                'name':name,
                'dept':dept
            }

            row_count = create_single_record(record)
            print(row_count," row/s insert")

        case 2:
            records = read_all_records()
            for record in records:
                print(record)
        
        case 3:
            id = int(input("Enter the id: "))
            record = read_specific_record(id)
            print(record)

        case 4:
            id = int(input("Enter the id: "))
            column_name = input("Enter the column name: ")
            value = input("Enter the value: ")

            info = {
                'id':id,
                'column_name':column_name,
                'value':value
            }

            row_count = update_record(info)
            print(row_count," row/s updated")

        case 5:
            id = int(input("Enter the id: "))
            row_count = delete_record(id)
            print(row_count," row/s deleted")
    



choice = -1
while(choice!=6):
    print("\nEnter \n1.CREATE record\n2.READ records\n3.READ specific record\n4.UPDATE record\n5.DELETE record\n6.Exit")
    choice = int(input())
    dml(choice)

