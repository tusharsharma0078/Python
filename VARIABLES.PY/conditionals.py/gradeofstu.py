#take the marksof students from the user and if marks greater than 90 print A if marks
#between 80 and 90 print B and if marks between 70 and 80 print C"""
marks=int(input("marks:"))
if(marks>=90):
    print(" grade is A")
elif(marks>=80 and marks<90):
    print("grade is B")
elif(marks>=70 and marks<80):
    print("grade is C") 
else:
  print("grade is D")          