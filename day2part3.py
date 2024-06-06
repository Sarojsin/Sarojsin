#identity operator and equality operator
a=5
b=5
print(a is b)#this line is true it compare boths address or object id
print(a==b)#this line aslo true but it compare the value
print(id(a))#both have same address
print(id(b))
print(id(a) == id(b))#both address are same so it is true
c=6
d='6'
print(c is d)#this line is false it compare boths address or object id
print(c==int(d))#this line aslo true but it compare the value
print(id(c))#both c and d have different address
print(id(d))
