#NESTED DICTIONARY
Student={
    "name":"john",
    "age":20,
    "marks":{
        "physics":70,
        "chemistry":80,
        "english":90,
    }

}
print(Student)
print(Student["marks"])
print(Student["marks"]["english"]) # here i print the marks of english subject
print(Student.keys()) # here i print the keys of the dict
print(Student.values()) # here i print the values of the dict
print(Student.items()) # here i print the key value pairs of the dict
print(Student.get("marks")) # here i print the marks of the student using get method
print(list(Student.items())) # here i print the key value pairs of the dict in list format

