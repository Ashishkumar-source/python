student ={1,2, 3,4,5}
student1 = {1,3,4,56,6,4,5,8,9,3,2,2,1 ,34}

# combines the two sets and return the new sets 
new_student = student.union(student1)
print(new_student)
print(len(new_student))

# combines the common value and return new 
intersection = student.intersection(student1)
print(intersection)