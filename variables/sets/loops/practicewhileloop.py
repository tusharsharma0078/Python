#print number from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1
#print number from 100 to 1.

i=100
while i>=1:
    print(i)
    i-=1

#print the multiplication table of n

n=int(input("Enter the number to print multiplication table: ")) 
i=1
while i<=10:
   print(n*i)
   i+=1

   # print the elements of the list using while loop
   list=[1,4,9,16,25,36,49,64,81,100]
   idx=0
while idx<len(list):
         print(list[idx])
         idx+=1
