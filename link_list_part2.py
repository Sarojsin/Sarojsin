#Change Item Value
#the value of a specific item, refer to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Specific range, define a list with the new values,
# And refer to the range of index numbers where you want to insert the new values
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist2,'before changing')
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2,'after changing')
print(thislist2)
