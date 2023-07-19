student_heights= input("Kindly enter a list of student heights:").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
Total_Students=0
for Total in student_heights:
    Total_Students+=Total
print(Total_Students)
Student=0
for Students in student_heights:
    Student += 1
print(Student)