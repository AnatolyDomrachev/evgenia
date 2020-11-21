def view_contacts():
    print('Your contacts:')
    #1 - Andrew Warrick
    #2 - Bob Jones
    #3 - Claire Mitchell
    #4 - Waine Smith
    ch2 = int(input('Enter contact number or 0 to exit to the main menu: '))

def add_new_contact():
    print(2)

def exit_the_application():
    print(3)

print('Choose an option:')
print('1 - view contacts')
print('2 - add new contact')
print('3 - exit the application')
ch1 = int(input('Your choice: ')) 

if ch1 == 1 : view_contacts()
if ch1 == 2 : add_new_contact()
if ch1 == 3 : exit_the_application()
