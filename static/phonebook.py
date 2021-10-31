#Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52)
import collections


# function to welcome the user and presents the menu options.

def menu():
    print("Main Menu:\n")
    print('1. Add a new contact')
    print('2. Update a contact')
    print('3. Search for a contact')
    print('4. Remove a contact')
    print('5. View existing contacts')
    print('6. Exit Phonebook')



# function to ask the user to select an option from the menu.
# display message if invalid entry otherwise returns input value.

def menuchoice():
    choice = "string"
    while choice.isdigit()==False :
        choice = input("--------------------------------------------------------------\n\nEnter an option(1,2,3,4,5 or 6) or press Enter for main menu: ")
        if choice.isdigit()==False:
            menu()
        else:
            return int(choice)
    


#function to ask user for name and number to be added to the phonebook
#checks if the name already exists and present the data if present otherwise it adds a new contact
#only whole numbers allowed for phone number.

def add_contact():
    print("Add a new Contact")
    name = input("Name: ")
    if name.upper() in numbers:
        print("Attention !!!...Name already exist! and the number is: ", numbers[name.upper()])
        print()     

    elif len(name.upper()) ==0:
        print("Attention !!!...Invalid entry! no name supplied! Please try again by choosing option 2.")
    else:
        phone = input("Number: ")
        if phone.isdigit()==True:
            numbers[name.upper()] = phone
        else:
            print()
            print("Attention !!!...Invalid phone number entered! Contact is not created ") 



#function to ask user for a contact to be updated.
#if the contact  does not exist, display a message otherwise allow user to update phone number.
    
def update_contact():
    print("Update a Contact")
    name = input("Name: ")
    if name.upper() in numbers:
        phone = input("Number: ")
        if phone.isdigit()==True:
            numbers[name.upper()] = phone
            print("Contact updated, new number for",name.upper(),"is",phone)
        else:
            print()
            print("Attention !!!...Invalid phone number entered! Contact is not updated ")
                      
    else:
        print("Attention !!!...", name.upper(), "was not found")



# function to ask user for a contact to be looked up
 
def search_contact():
    name = input("Enter the name of the contact you wish search: ")
    if name.upper() in numbers:
        print("The number is", numbers[name.upper()])
    else:
        print("Attention !!!...Name:",name.upper(), "was not found!")




# function to ask the user for a contact to be removed.
# if the contact does not exist, display a message otherwise prompt for user confirmation
# and remove contact if confirmed.
        
def remove_contact():
    print("Remove a Contact")
    name = input("Name: ")
    if name.upper() in numbers:
        confir = input("are you sure that you want to remove contact: Y/N? ")
        if confir== "Y" or confir== "y" :
            del numbers[name.upper()]
            print("Contact:",name,"has been removed")
        elif confir== "N" or confir== "n":
            print("Contact",name.upper(), "not removed.")
        else:
            print("Attention !!!...incorrect entry!")
            print()
            
    else:
        print("Attention !!!...Name:",name.upper(), "was not found!")        
 



# If the phonebook is not empty, ask the user how they want the data sorted: ascending or descending
# and list contacts based on the selection.

def list_contact():
    print()
    if len(numbers) ==0:
        print("Phonebook is empty!!")
    else:
        print("How do you want the contacts ordered?\n1. Names in ascending order\n2. Names in descending order:\n ")
        lo = input("Type in a number (1 or 2): ")
        if lo.isdigit()==False:
            print()
            print("That is not a valid option!\n ")
        elif int(lo)== 1 :
            print("Name and Telephone Numbers:")
            lca = sorted(numbers.items(),reverse=False)
            for x in lca:
                print("Name: ", x[0] , "\t\t\t\t\tNumber:" , x[1] )
                
        elif int(lo)== 2:
            print("Name and Telephone Numbers:")
            lcd = sorted(numbers.items(),reverse=True)
            for x in lcd:
                print("Name: ", x[0] , "\t\t\t\t\tNumber:" , x[1] )
               
        else:
             print("Attention !!!...That is not a valid option!\n ")
             menu()




     
# create empty dictionary for storing names and  numbers            
numbers = {}

# Print welcome massage only when the application starts
print("**********************************************************")
print("                 Welcome to Phonebook")
print("**********************************************************\n")

#call the menu function that will present Menu options. 
menu()

#if dictionary is empty then ask user to add up to 5 initial contacts
if len(numbers) == 0:
    print()
    rows = input("Please enter initial number of contacts to be added (up to 5 contacts): ")
    if rows.isdigit()==False:
       print("That is not a valid option!\nPlease use option 1 to add contacts")
    elif int(rows) >5:
        print("maximum entry allowed is 5. please use option 1 to add contacts")
    else:
        for i in range(int(rows)):
            add_contact()
            i=+1

# Initiate a while loop to run the phonebook application continuously.
# Calls the menuchoice function to prompt for user input and returns the value
# Based on user's input (output of function menuchoice) calls sub function or exits the loop ending the application.
menu_choice = 0
while menu_choice != 6:
   menu_choice = menuchoice()
   # condition for making decision based on the option selected by the user.     
   if menu_choice == 1:
        add_contact()    
        print()
   elif menu_choice == 2:
        update_contact()
        print()
   elif menu_choice == 3:
        search_contact()
        print()
   elif menu_choice == 4:
        remove_contact()
        print()
   elif menu_choice == 5:
        list_contact()
        print()
   elif menu_choice == 6:
        print("Goodbye!")
        print()
   elif menu_choice != 6:
        print()
        print("Attention!!!...That is not a valid option!")
        print()
        menu()
