print('Welcome to my application')
password = input('Enter the password: ')

if password == 'abcd':
    print('Hallo')
    s = input('Enter a word from the options: [[no s]], [[yes s]], [[maybe s]] ')
    
    if s.lower == 'no':
        print('[[ You write no ]]')
    elif s.lower == 'yes':
        print('[[ You write yes ]]')
    elif s.lower == 'maybe':
        print('[[ You write mybe ]]')
    else:
        print('Error: Invalid input')
else:
    print('The password is wrong')