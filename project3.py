print(
        "*************************************************\n"
        "*                                               *\n"
        "*        🚗 Welcome to the Driving Eligibility App! 🚗       *\n"
        "*                                               *\n"
        "*************************************************\n"
    )
s=str(input('Are you Algerian yes or no'))
if s.upper()=='YES' :
    
    tr=int(input('enter your age'))
    if tr>18:
        print('You can extract the card')
    else:
        print('sorry! ,Wait until you reach 18 years') 
else       :
    print('sorry! ,The service is available to Algerians only')