# WAP to enter marks of 3 subjects from the user and store them in dictionary.Start with an empty dictionaryu & add one by one .Use subject name as key band marks as value.
marks={} #empty dictionary make with braces 
 # input from user
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))
maths=int(input("enter your maths marks"))
#now we add marks and subjects in the dictionary one by one
marks["physics"]=physics
print(marks)
marks["chemistry"]=chemistry
print(marks)
marks["maths"]=maths
print(marks)
