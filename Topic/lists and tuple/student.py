student = [ 6,1,3, 2 , 5, 4]
print(type(student))
print(len(student))
print(student[0:2]) # ending ind not included 

print(student)

# add one element at the ends of any lists 
student.append(7)
print(student)
 
# list in ascending order 
print(student.sort())
print("list of student in ascending order : ",student)

# list in descending order 
print(student.sort(reverse=True))
print("list of student in descending order: " , student)

# reverse the list 
print(student.reverse())
print("reverse of the lists : ",student)

# insert element at index 
student.insert(7,9)
print(student)

# remove first occurence of element
student.remove(1)
print(student)

# removes element at index 
student.pop(3)
print(student)
