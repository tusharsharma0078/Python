#average of 3 numbers
def avg(a,b,c):
    avg=(a+b+c)/3
    return avg
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print("Average of three numbers:", avg(a, b, c))