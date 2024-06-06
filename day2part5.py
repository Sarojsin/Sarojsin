#f string function
name='saroj'
classs=12
home='kanchanpur'
print(f'my name is {name}.class is {classs} and finally my home address {home}')
#this is the easyiest way to print the whole thing in only one '' or"" it is the mostly used and famous
# sum using this function 
a=input('Enter first number')
b=input('Enter second number')
print(f'the sum of {a} and {b} is {a+b}')#sum will not add like 2+2=4 but 2+2=22 because of string
'''
c=input('Enter first number')
d=input('Enter second number')
int(c)                                                  #not working
int(d)
print(f'the sum of {c} and {d} is {c+d}') 
'''
c=2
d= 4  
print(f'the sum of {c} and {d} is {c*2}')                   #but this works
print(f'the sum of {c} and {d} is {c+d}') 
#another way
e=int(input('Enter first number'))
f=int(input('Enter second number'))
print(f'the sum of {c} and {d} is {e+f}')                      #but this also works
print(f'the sum of {c} and {d} is {e*8}')