from Utilities import db

def naba():
    print('Available Options:\n C=INSERT \nI=INSERT \n R=Read \n U=Update \n D=Delete \n T= TRUNCATE \n X= CLOSE ')
    choice = input('Choose your option = ')
    conn = db.connect()
    try:
        if choice == 'I':
            id = input('Enter id of Student: ')
            first_name = input('Enter FRIST name of Student: ')
            last_name = input('Enter LASTname of Student: ')
            email = input('ENTER email id:')
            gender = input('ENTER gender: ')
            phone = input('Enter Phone Number: ')
            password = input('ENTER THE PASSWORD ')
            db.insert(id,first_name,last_name,email,gender,phone,password)      
        elif choice == 'R':
            db.get_all()   
        elif choice == 'U':
            input_id = input("WHICH ID YOU WANT TO UPDATE: ")
            input_name = input("WHAT NAME WOULD YOU LIKE TO UPDATE: ")
            db.update(input_name,input_id)
        elif choice == 'D':
            input_id = input("WHICH ID YOU WANT TO DELETE: ")
            db.delete(input_id)
        elif choice == 'T':
            db.truncate()
        elif choice == 'X':
            conn.close()
        else:
            print('Wrong choice, You are going exist.')
            conn.close()
    except Exception as e:
        print("NOTHING MUCH RESTART THE PROGRAM ")


print('------------------------------------------------------------------------------------------')
print("YOU ARE WORKING IS HARD CODEDED AND THE OPERATION IS PERFORMED IN EMPLOYEE TABLE")
db.connect()
naba()

