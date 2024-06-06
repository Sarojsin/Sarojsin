#duplicate iteam are not allowed it is immutable

saroj={1,'saroj',True,2.2,5}
print(saroj)                      # it can print random order.it does not have any order
saroj1={'saroj','sagar','sujal','roshan'}
saroj2={'nirmala','roshan','nisha','simran'}
print(saroj1.union(saroj2))         #gives the union of the set saroj1 and saroj2
# rember it wont update the set saroj1 by saroj2 it just print the union of the both set saroj1 and saroj2.
#this method is called by passiing argument

print(saroj1.union(('baby','how','are'))) # by passing tuple.we can pass list aslo

# how to update 
saroj1.update(saroj)   #it can not print in one line only
print(saroj1)           #now it is update saroj1 set by saroj set

print(saroj1 | saroj2)    # it is by both set only 
set1={1,2,3,4,5}
set2={2,4,6,7,8}
set2 |= set1
print(set2)  

# intersection of the two set
sagar={1,2,3,4,5}
sagar1={6,3,7,8,9}
sagar2={4,5,34,56,8,9}
print(sagar.intersection(sagar1,sagar2)) #it is empty set which is set()set()set()
