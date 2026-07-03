# for loop is used to repeat a block of code for each item in a sequence.[string,list,dict,tuple or range] basic syntax of for loop is:for variable in sequence:print(variable)
#let's see some examples of for loop in python.
list=[1,2,3,4,]
for i in list:
    print(i)

    #another example of for loop is to print the multiplication table of n
n=5
for i in range(1,11):#loop will run from 1 to 10
    print(n*i)

     #example for string
name="TUSHAR"
for i in name:
    print(i)

         #example for dictionary

dict={
    "name":"tushar",
    "age":22,
    "city":"hapur"
}
for i in dict:
    print(i,dict[i])