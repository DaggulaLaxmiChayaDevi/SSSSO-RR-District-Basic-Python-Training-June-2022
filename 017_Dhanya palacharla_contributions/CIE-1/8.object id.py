name=input("enter the name:")
print(id(name))
rollno=int(input("enter the roll.no:"))
print(id(rollno))
marks=int(input("enter the marks:"))
print(id(marks))
grade=input("enter the grade:")
print(id(grade))
list=[]
list.append(name)
list.append(rollno)
list.append(marks)
list.append(grade)
print("list is:",list)
