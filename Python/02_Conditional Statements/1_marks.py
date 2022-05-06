# Write a python program to accept marks of five subjects from student.
# Calculate percentage and display result like First Class,Second Class,Pass,Fail using decision making statements
marks = []
sum1 = 0
for i in range(0, 5):
    marks.append(int(input("Enter marks of subject : ")))
    sum1 = sum1 + marks[i]
per = sum1/5
if per > 90:
    print("A")
elif per > 70:
    print("B")
elif per > 50:
    print("C")
elif per > 30:
    print("D")
else:
    print("Fail")
