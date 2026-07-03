food=input("food:")
print("eat") if food=="cake" else print("dont eat")
food1=input("food1:")
print("sweet") if food1=="jalebi" or food1== "rasgulla" else print("not sweet")
age=int(input("age:"))
vote=("no","yes")[age>=18]
print(vote)
sal=int(input("salary:"))
tax=sal*(0.1,0.2)[sal>=50000]
print(tax)