try:
 num1,num2=eval(input('enter two numbers,seperated by a comma: '))
 result=num1/num2
 print('result is',result)
except ZeroDivisionError:
 print('Divsion by Zero is error!!')
except SyntaxError:
 print('comma is missing enter numbers sperated by comma like this 1,2')
except:
 print('Wrong input')
else:
 print('No exceptions')
finally:
 print('This will execute no matter what')