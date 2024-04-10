while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    choice = int(input('Please enter an option: '))
    if choice == 3:
        break
    else:
        password = input('Please enter your password to encode: ')
        if choice == 2:
            print('Your password has been encoded and stored!')
        elif choice == 3:
            print('me m')