

student_scores = [8,65,89,86,55,91,64,89]
print(range(1, 10))
highest_score = 0
for i in range(0,len(student_scores)):
    if(student_scores[i]>highest_score):
        highest_score = student_scores[i]
print(highest_score)
