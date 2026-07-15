#Recurssion is a programming technique where a function calls itself to solve a smaller version of same problem

def show(n):
    if(n==0): #base case
        return
    print(n)
    show(n-1)
show(5)
 
 #factorial n
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(2))

#print the sum of natural numbers
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
sum=calc_sum(5)
print(sum)

