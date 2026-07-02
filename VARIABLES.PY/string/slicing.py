#slicing is the way to extract a portion fromthe list ,string or tuple.
str1="10,20,30,40"
print(str1[:]) # for copy all string
print(str1[1:4]) #print the elements from index 1 to 3 because last index not exclude.
print(str1[::-1]) #for reverse the string
print(str1[:5]) #from beginning to 4index because 5 one is not excluded
print(str1[1:6:2]) # every 2 element from index 1 to 5
print(str1[-2::]) # for last threee elements
print(str1[:-1]) #all expect the the last element