import numpy as np

student1_score = np.array([85,90,78])
student2_score = np.array([92,88,95])

total_score = student2_score + student2_score
print(total_score)

average_score = total_score / 2
print(average_score)

student1_total = student1_score.sum()
student2_total = student2_score.sum()
student1_average = student1_total / student1_score.size
student2_average = student2_total / student2_score.size

print('학생 1의 총점 : ', student1_total)
print('학생 2의 총점 : ', student2_total)
print('학생 1의 평균 : ', student1_average)
print('학생 2의 평균 : ', student2_average)