student = { 
    "name" : "ashish",
    "subjects" : {
        "physics":90,
        "chem": 92,
        "math": 90
    }
    
}
student["name"]='ashish choudhary' # this is used to change the value of keys 
print(type(student))
# in nested dictionary we can print single part of dictionary using square bracket [] and " "
# dictionary is mutable ( value of dictionary is changed ) 
# in dictoinary we can create lists and tuple 
# keys in dictionary must be unique. 

print(student["name"])
print(student["subjects"]["chem"])