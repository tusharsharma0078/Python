#python function is the reusable block of code that perform specific task ,function help make program organized and reusable and easier to maintain. function is defined using the def keyword followed by the function name and parentheses. the code block within every function starts with a colon (:) and is indented.
a=5
b=5
def calc_sum(a,b): #here a and b are parameters
    sum = a+b #return statement is used to send the result back to the caller
    return sum
print(calc_sum(a,b))
print(calc_sum(10,20)) #here 10 and 20 are arguments
print(calc_sum(100,200))