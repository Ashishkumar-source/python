marks = int(input("enter the marks: "))

if (marks>100 or marks<0) :
    print("Invalid marks please gives correct marks from 0-100")
elif(marks>=90 and marks<=100):
    print("Grade A ")
elif(marks>=80 and marks<90):
    print("Grade B ")
elif(marks>=70 and marks<80):
    print("Grade C")
elif(marks>=60 and marks<70):
    print("Grade D")
elif(marks>=50 and marks<60):
    print("Grade E")
else:
    print("Fail")