"""
중복 제거 예
"""
# 중복 원소를 갖는 리스트
gender = ['남', '여', '남', '여']

# 중복 원소 제거
sgender = set(gender)
lgender = list(gender)
print(lgender)

print(lgender[1])