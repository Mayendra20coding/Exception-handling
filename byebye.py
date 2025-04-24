vaild = False
while not vaild:
 try:
  n=int(input('enter a number'))
  while n%2==0:
   print('bye')
  vaild = True
 except ValueError:
   print('Invaild')