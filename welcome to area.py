rint ('welcome to area appel')
s=input('chose an area : \n               [[ALGERIAN]]  ,,  [[MAROCCO]] \n               [[TONISIAN]]  ,,  [[LIBYA]] \n ::')
if s.upper()==('ALGERIAN') :
    print('welconme to algerian')
elif s.upper()==('MAROCCO') :
    print('welconme to marocco')
elif s.upper()==('TONISIAN') :
        print('welconme to tonisian')
elif s.upper()==('LIBYA') :
    print('welconme to libya')
else :
     print(f'sorry, [[{s}]] is not on our list') 