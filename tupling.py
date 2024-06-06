saroj=(1,2,3,4,5,2,6,7,2,4)       #this is tuppling 
sagar=(5,6,7,8,9,1,'saroj',6)  # it is immutable
SSD=(saroj,sagar)        #it is also tupel
print(saroj)
print(sagar)
print(len(saroj))
print(len(sagar))
print(SSD)
print(len(SSD))
print(max(saroj)) #it is allowed
print(saroj.count(2)) #it count the repetation of 2 in the tuple
#print(max(sagar))  it is not allowed cause it is mixed 
SSC=saroj+sagar        #it is concatenation
print(SSC)
print(len(SSC))
tuple=(69,)*3  #only multiplication is allowed it is also how many time to repeat the value 
print(tuple)
# tuple1=(69,)+3 addition ,subtraction ,division is not allowed
