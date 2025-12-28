collection = set()
collection.add(1)
collection.add((1,2,3))
# collection.add([1,2,3])
# unhashable type mutable, value can be changed 
# print(type(collection))
# print(len(collection))
collection.clear() # to remove all element of a set
""""print(collection)
print(len(collection))
"""
collection.add("ashish")
collection.add("choudhary")
collection.add("18")
collection.add(1)
collection.add(2)
print(collection)
print(collection.pop()) # set.pop removes one random element and returns the removes value 
print(collection)
print(collection.pop())