#print the elements of the following list using for loop.
list=[1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)

#search for the number 36 in the list using for loop.
x=int(input("Enter the number to search in the list: "))
for i in list:
    if i==x:
       print("found")
       
else:
         print("not found")
         
