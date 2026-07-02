# Here i create a dict with my name ,age,city.
dict={
    "name":"TUSHAR",
    "AGE" : 22,
    "CITY":"delhi"
}
print(dict)
 
 # now i want to add a new key value pair in dict
dict["hobby"]="cricket"
print(dict)
dict["AGE"]=34 # heere i chnge my previous age with new age
print(dict)
print(dict.items()) # here i print allthe key value pairs of  dict

dict.pop("CITY") #here i pop the city key value pair from the dict
print(dict)
