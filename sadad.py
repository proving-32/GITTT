print('Welcome to my application')
password = input('Enter the password: ')

if password == 'abcd':
    print('Hallo')
    s = input('Enter a word from the options: [[no s]], [[yes s]], [[maybe s]] ')
    
    if s == 'no':
        print('[[ You write no ccccsss,DD,]]')
    elif s == 'yes':
        print('[[ You write yes cccccssss,DD,]]')
    elif s == 'maybe':
        print('[[ You write mybe  cccccsssss,DD,]]')
    else:
        print('Error: Invalid input')
else:
    print('The password is wrong')