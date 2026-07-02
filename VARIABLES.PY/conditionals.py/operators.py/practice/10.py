#WAP to check if a list contains a palindrome of elements .



list=[1,2,3,2,1]
print(list)
reverse=list[::-1]
print(reverse)

if(list==reverse):
    print("list is palindrome")
else:
    print("list is not palindrome")    
