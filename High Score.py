student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_score=0
for x in student_scores:
  if x > highest_score:
    highest_score=x    
print(highest_score)
print(max(student_scores))