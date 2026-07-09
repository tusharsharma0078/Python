#WAF to print the length of the list.
cities=["delhi","mumbai","kolkata","chennai"]
heroes=["ironman","captain america","thor","hulk"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#WAF to print the elements of list in single line.
students=["shiva","sachin","rohit","virat"]
marks=[90,80,70,60]

def print_elements(list):

    for i in list:
        print(i,end=" ",)
        
print_elements(students)
print_elements(marks)

#WAF to convert usd into inr.

def convert(USD):
    INR=USD*95.44 #exchange rate
    return INR
USD=float(input("Enter the amount in USD: "))
print("INR=",convert(USD))