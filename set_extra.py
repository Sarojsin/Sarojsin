#some other things we can do in set
set={1,2,3,4}
set1={4,5,6,7}
print('set',set)
print('set1',set1)

#to add new members
set.add(7)                   #here we can pass only one valu or argument
# set.add(7,8,9) not allowed .its error
print(set.add(9))             # this will print none  it will remove but not return the value
print(set)
# to remove members
set.remove(1)                  #here we can pass only one valu or argument
print(set.remove(3))          # this will print none  it will remove but not return the value
print(set)

#discard and pop
set1.discard(4)               #here we can pass only one valu or argument
print(set1)
print(set1.discard(5))        # this will print none  it will remove but not return the value

#poping
set2={5,4,3,7,9}
set2.pop(3)                  #here we can pass only one valu or argument
print(set2)
   