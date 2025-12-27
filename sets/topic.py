# sets automatically removes duplicate values 
"""sets is a collection of unordered items.
Each element in the sets must be unique and immutable. 

"""
null_set =set() # this syntax creates the empty sets 

print(type(null_set))
collection ={1,1,2,3,3,"hello","helllo","hello"}
print(collection)
print(len(collection))

# to add value in sets
null_set.add(1)
null_set.add(2)
null_set.add(3)
print(null_set)

# to remove the values 
null_set.remove(1)
print(null_set)