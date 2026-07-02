marks=[94.4, 88.5, 76.0, 92.3, 85.6, 79, 91.2, 87.4, 90, 82]
print(type(marks))
marks.append(100) #foradding an element at the end ofthe list.
print(marks)
marks.remove(82) #forremoving the element fromthe list.
print(marks)
marks[2]=94 #for changing the value ofthe element in the list by their indexnumber.
print(marks)
marks.pop(3) #for popping the elemnt fromthe list by their indexnumber.
print(marks) 
marks.sort() #for sorting the list in ascending order.
print(marks)
marks.sort(reverse=True) #for sorting the list in descending order.
print(marks)
marks.insert((2),3) #for inserting the element in the list at a specific indexnumber.
print(marks)
marks.reverse() #for reversing the list.
print(marks)
marks.count(3) #for counting the number of occurances of an element in the list.
print(marks)
marks.index(85.6) #for finding the indexnumber of an element in the list.
print(marks)
marks.clear() #for clearing the list
print(marks)