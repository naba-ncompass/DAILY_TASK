from Utilities import db


def check_column(col_name, value):
    if col_name == 'cgpa':
        return make_float(value)
    else:
        return value



def make_float(value):
    return float(value)



def get_insert_details():
    
    id = input('Enter id of Student: ')
    name = input('Enter name of Student: ')
    department = input('Enter department of Student: ')
    cgpa = float(input('Enter cgpa of student: '))

    return (id, name, department, cgpa)



def get_update_details():

    update_col = input('Enter column to update: ')
    new_value = input('Enter new value: ')

    new_value = check_column(update_col, new_value)

    where_col = input('Enter column to use in where clause: ')
    where_value = input('Enter the where clause column value: ')

    where_value = check_column(where_col, where_value)

    return (update_col, new_value, where_col, where_value)



def get_delete_details():
    
    where_col = input('Enter column to use in where clause: ')
    where_value = input('Enter the where clause column value: ')

    where_value = check_column(where_col, where_value)

    return (where_col, where_value)



while 1:
    user_choice = input('\nPress \n1 for read \n2 for insert \n3 for update \n4 for delete \n5 to exit \n')
    
    match user_choice:
        case '1':
            db.read_from_student()
        case '2':
            data = get_insert_details()
            db.insert_into_student(data)
        case '3':
            data = get_update_details()
            db.update_student(data)
        case '4':
            data = get_delete_details()
            db.delete_from_student(data)
        case '5':
            print('\n Exiting....\n')
            break
        case _:
            print('Wrong choice...')
