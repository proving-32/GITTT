print('Welcome to my application')
password = input('Enter the password: ')

if password == 'abcd':
    print('Hallo')
    s = input('Enter a word from the options: [[no s]], [[yes s]], [[maybe s]] ')
    
    if s == 'no':
        print('[[ You wrote no ]]')
    elif s == 'yes':
        print('[[ You wrote yes ]]')
    elif s == 'maybe':
        print('[[ You wrote  ]]')
    else:
        print('Error: Invalid input')
else:
    print('The password is wrong')