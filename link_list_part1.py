# List items are ordered, changeable, and allow duplicate values.
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# feature of list
# Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#The search will start at index 2 (included) and end at index 5 (not included).
thislist1 = ["litchy", "grapes", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5])
# the items from "orange" (-4) to, but NOT including "mango" (-1)
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[-4:-1])
#if a specified item is present in a list use the in keyword
thislist3 = ["apple", "banana", "cherry"]
print(thislist3)
if "apple" in thislist3:
  print("Yes, 'apple' is in the fruits list")
else:
  print("no, 'apple' is not the fruits list")
  
    