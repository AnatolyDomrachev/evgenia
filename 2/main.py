def view_contacts():
    print('Your contacts:')
    #1 - Andrew Warrick
    #2 - Bob Jones
    #3 - Claire Mitchell
    #4 - Waine Smith
    ch2 = int(input('Enter contact number or 0 to exit to the main menu: '))

def add_new_contact():
    print(2)
    #Bob Jones
    #Primary phone: +4915123123151
    #Phone 2: +1142312312312
    #Phone 3: +1312312312312
    #E-mail: b.jones@hotmail.com
    #Telegram: @bob123
    #Choose an option:
    #1 - Delete contact
    #2 - Go back to the contacts list
    #Your choice: 2
    #Your contacts:
    #1 - Andrew Warrick
    #2 - Bob Jones
    #3 - Claire Mitchell
    #4 - Waine Smith
    #Enter contact number or 0 to exit to the main menu:
    #Your choice: 4
    #Waine Smith
    #Primary phone: +491232123123
    #E-mail: waine789@gmail.com
    #Choose an option:
    #1 - Delete contact
    #2 - Go back to the contacts list
    #Your choice: 1
    #Are you sure you want to delete Waine Smith from your contact
    #list (y/n)? y
    #Waine Smith successfully deleted from the contact book. Press any
    #key to return to the contact list
    #continues on the next page...
    #Your contacts:
    #1 - Andrew Warrick
    #2 - Bob Jones
    #3 - Claire Mitchell
    #Enter contact number or 0 to exit to the main menu:
    #Your choice: 0
    #Choose an option:
    #1 - view contacts
    #2 - add new contact
    #3 - exit the application
    #Your choice: 2
    #Enter name: Mike Evans
    #Enter primary phone: +44123123123
    #Enter additional phone or empty: +44298009123
    #Enter additional phone or empty:
    #Select one of the following additional fields (e-mail, vk,
    #instagram, linkedin, telegram) or empty: e-mail
    #Enter e-mail: mike.evans@gmail.com
    #Select one of the following additional fields (e-mail, vk,
    #instagram, linkedin, telegram) or empty: instagramm
    #Field name not recognized
    #Select one of the following additional fields (e-mail, vk,
    #instagram, linkedin, telegram) or empty: instagram
    #Enter instagram account: mikeevans89
    #Select one of the following additional fields (e-mail, vk,
    #instagram, linkedin, telegram) or empty:
    #Contact Mike Evans successfully created!
    #
    
while(True):
    print('Choose an option:')
    print('1 - view contacts')
    print('2 - add new contact')
    print('3 - exit the application')
    ch1 = int(input('Your choice: ')) 

    if ch1 == 1 : view_contacts()
    if ch1 == 2 : add_new_contact()
    if ch1 == 3 : break
