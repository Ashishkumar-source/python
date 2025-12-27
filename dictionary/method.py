info = {
    "name" : "ashish",
    "subject" : ["python","c" ,"c++","java"],
    "address": ("alipur kalan","muzaffarnagar","uttarpradesh"),
    "age": 18
    
}
info["name"]="ashish choudhary"
print(type(info))
print(info)
null_dict = {}
print(type(null_dict))
null_dict["name"]= "ashish"
print(null_dict)

# different method of dictionary 

print(info.keys()) # the all  keys of dictionary 

print("dictionary convert into list = ",list(info.keys()))
print(len(info)) # if use of len it gives number of keys value pair present in a dictionary

print(info.values()) # returns a view object containing all the values of the dictionary.

pairs = list(info.items())
print(pairs[0])

print(info["name"]) # in this case if keys is exists it gives keys value otherwise it gives error 

# in case of .get gives none if keys is not exists 
print(info.get("name1"))

# insert the specified items to the dictionary 
info.update({"city": "delhi"})
print(info)

# use of .update are different method 
new_dict ={"age1": 18 , "city1": "muzaffarnagar","city2":"shamli"}
info.update(new_dict)
print("new information : ",info)
