# SNS 이벤트를 통해 특정 조건에 맞는 고객에게 상품을 제공하려고 합니다.
# 이를 위해 고객 데이터를 분석하고 필터링하여, 목표 고객들의 이름을 추출하는 작업이 필요합니다.
# 고객 데이터는 댓글의 길이, 좋아요 수, 스팸 여부, 이미지 포함 여부 등 다양한 저보를 포함하고 있으며,
# 이를 바탕으로 필요한 데이터를 정리한 후 분석을 진행하여 최종적으로 상품을 받을 고객을 선정하는 절차가 요구된다.

import numpy as np
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hyemin'],
    'comment_length': [150, 200, 50, 300, 120, 180, 75, 160],
    'likes': [25, 30, 10, 45, 20, 35, 5, 28],
    'is_spam': [False, False, True, np.nan, False, True ,np.nan, False],
    'has_image': [True, False, True, True, False, False, True, True],
}

df = pd.DataFrame(data)

print(df.info())
df['is_spam'] = df['is_spam'].replace(np.nan,False)

print(df.groupby(['has_image'])['likes'].mean())

condition = (
    (df['comment_length'] >= 100)&
    (df['likes'] >= 20)&
    (~df['is_spam'])&
    (df['has_image'])
)
filter_df = df[condition]
print(filter_df)

print(df.tail(3))

# save excel file
df.to_csv('./data_file/customer.csv')