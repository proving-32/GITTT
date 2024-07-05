age = int(input("Please enter your age : "))
help= input ("Please do you have a license ? : [[YES]] ,, [[NO]]")
if age>=18 and help.upper()=='YES':
     
     
     
     print ("Welcome You can drive!")


elif  age < 18 or help.upper()=='NO':            
     print ("Sorry, can,t drive")

else:
    print(f'sorry, [[{help}]] is not on our list')

