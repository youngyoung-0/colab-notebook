# requirements
# 각 학급에 4명의 학생, 각 학생이 3과목의 시험 점수를 가지고 있 배열 생성
import numpy as np

scores = np.random.randint(0, 101, size=(3,4,3))


print(scores)
print(scores.shape)
print("학급별 학생들의 점수 배열 (3차원 배열) : ")

for class_index in range(scores.shape[0]):
    print(f"\nClass  {class_index}")
    for student_index in range(scores.shape[1]):
        korean, english, math = scores[class_index, student_index]
        print(f"student {student_index + 1} Korean:{korean} English:{english} Math:{math} ")




