import pandas as pd
import numpy as np

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 40],
    'salary': [7000.00, 8000.00, 9000.00, 6000.00, 95000.00]
}
df = pd.DataFrame(data)
# 나이가 30 이상인 직원의 이름과 급여 반환
result = df[df['age'] >= 30][['name', 'salary']]
print(result)

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'math': [88, 92, 85, 95, 90],
    'science': [80, 85, 88, 92, 85],
    'english': [90, 87, 85, 88, 92],
}
df = pd.DataFrame(data)

# 개인별 과목 점수의 평균값 계산
df['average'] = df[['math', 'science', 'english']].mean(axis=1)
print(df.head())

# 이름과 평균값만을 포함하는 새로운 데이터프레임 생성
new_df = df[['name', 'average']]
print(new_df.head())

# filtering
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'comment_length': [150, 200, 50, 300, 120, 180, 75, 160],
    'likes': [25, 30, 10, 45, 20, 35, 5, 28],
    'is_span': [False, False, True, False, False, True, False, False],
    'has_image': [True, False, True, True, False, False, True, True]
}

df = pd.DataFrame(data)

# 댓글 길이가 100자이상, 좋아요 수 30개 이상, 스팸 댓글이 아니어야 한다, 이미지가 포함된 댓글이어야 한다.
condition = (
        (df['comment_length'] >= 100) &
        (df['likes'] >= 30) &
        (~df['is_span']) &
        (df['has_image'])
)

winner_df = df[condition]
print(winner_df.head())

# missing value
netflix = pd.read_csv('./data_file/netflix_selena.csv')
print(netflix.isna().sum())
print(netflix.info)

# 결측치 비율 확인
for i in netflix.columns:
    missingValueRate = netflix[i].isna().sum() / len(netflix) * 100
    if missingValueRate > 0:
        print("{} null rate: {}%".format(i, round(missingValueRate, 2)))

# .fillna()
netflix['country'] = netflix['country'].fillna('No Data')
# .replace()
netflix['director'] = netflix['director'].replace(np.nan,'No Data')
# .dropna()
netflix.dropna(axis=1, inplace=True)
# ,dropna()
# netflix.dropna(subset=['listed_in'], inplace=True)


# statistical function
netflix = pd.read_csv('./data_file/netflix_cleaned.csv')
print(netflix.groupby('type')['duration'].mean())
print(netflix.groupby(['type', 'country'])[['release_year', 'duration']].mean())