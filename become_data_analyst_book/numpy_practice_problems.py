import numpy as np

# problem
# 회사는 SNS 이벤트를 통해 특정 조건에 맞는 고객에게 상품을 제공하려고 합니다.
# 이를 위해 고객 데이터를 넘파이 배열로 분석하고 필터링하여, 목표 고객들의 정보를 추출하는 작업이 필요합니다.
# 곡객 데이터는 댓글 길이, 좋아요 수 , 스팸여부가 포함하고 있으며, 이 데이터를 정리하고 분석하여 최종적으로 상품을 받을 고객을 선정합니다.

# 1 create data
customer_data = np.array([[150,25,0],[200, 30,0],[50,10,1],[300,45,0]])
print(customer_data)

# 2 combine array
the_other_customer_data = np.array([[120,20,0],[180,35,1],[75,5,0],[160,25,0]])
combined_data = np.vstack((customer_data, the_other_customer_data))
print(combined_data)

# 3 calculation comment and like count
total_comment_length, total_likes, total_spam_count = combined_data.sum(axis=0)
average_comment_length, average_likes, average_spam_count = combined_data.mean(axis=0)
print(f"댓글 길이 총합 : {total_comment_length}")
print(f"좋아요 수 총합 : {total_likes}")
print(f"댓글 길이 평균 : {average_comment_length}")
print(f"좋아요 수 평균 : {average_likes}")

# 4 split the array
groups = np.vsplit(combined_data, 4)
print(groups)

# 5 index array
selected_customers = combined_data[[0, 2, 4], :]
print(selected_customers)

# 6 transpose array
transpose_data = combined_data.T
print(transpose_data)

# 7
new_customers = np.zeros((2,3))
print(new_customers)

# 8 specific index's value add value
combined_data[: ,1] = combined_data[:, 1] + 10
print(combined_data)

# 9 filtering
selected_customers = combined_data[(combined_data[:, 0] >= 100) & (combined_data[:, 1] >= 20) & (combined_data[:, 2] == 0)]
print(selected_customers)

# 10 find out number of winners
num_selected_customers = selected_customers.shape[0]
print(f"상품을 받은 고객수 : {num_selected_customers}")