import json

def view_contacts():
    print('Your contacts:')
    i = 0
    for contact in book:
        i += 1
        print(i," ",contact['name'])

    num = int(input('Enter contact number or 0 to exit to the main menu: '))
    if num == 0: return
    #for cont in book[num-1]:
    #    print(cont, ": ", book[num-1][cont])

    #Bob Jones
    print(book[num-1]['name'])

    #Primary phone: +4915123123151
    print("Primary phone: "book[num-1]['primary_phone'])

    #Phone 2: +1142312312312
    #Phone 3: +1312312312312
    #E-mail: b.jones@hotmail.com
    #Telegram: @bob123


    print('Choose an option:')


    print('1 - Delete contact')
    print('2 - Go back to the contacts list')
    ch2 = int(input('Your choice: '))

    if ch2 ==2 : 
        view_contacts()

    if ch2 ==1 : 
        ch3 = input('Are you sure you want to delete Waine Smith from your contact list (y/n)? ')
        if ch3 == 'y':
            book.pop(num-1)
            print('Waine Smith successfully deleted from the contact book.')
            input('Press Enter to return to the contact list')
            view_contacts()

def add_new_contact():
    contact = {}
    contact['name'] = input('Enter name: ')
    contact['primary_phone'] = input('Enter primary phone: ')
    contact['additional_phones'] = []

    while True:
        aph = input('Enter additional phone or empty: ')
        if aph == '': break
        contact['additional_phones'].append(aph)
        
    while True:
        evit = input('Select one of the following additional fields (e-mail, vk, instagram, linkedin, telegram) or empty: ')
        if evit == '': break
        if evit not in ['e-mail', 'vk', 'instagram', 'linkedin', 'telegram']:
            print('Field name not recognized')

        if evit == 'e-mail': contact['e-mail']=input('Enter e-mail: ')
        if evit == 'vk': contact['vk']=input('Enter vk: ')
        if evit == 'instagram': contact['instagram']=input('Enter instagram: ')
        if evit == 'linkedin': contact['linkedin']=input('Enter linkedin: ')
        if evit == 'telegram': contact['telegram']=input('Enter telegram: ')

    print('Contact %s successfully created!' % contact['name'])
    book.append(contact)
    
def write():
    f=open('book.txt', 'w')
    f.write(json.dumps(book))
    f.close()

book = []
f=open('book.txt', 'r')
book=json.loads(f.read())
f.close()

while(True):
    print('Choose an option:')
    print('1 - view contacts')
    print('2 - add new contact')
    print('3 - exit the application')
    ch1 = int(input('Your choice: ')) 

    if ch1 == 1 : view_contacts()
    if ch1 == 2 : add_new_contact()
    if ch1 == 3 :
        write()
        break
