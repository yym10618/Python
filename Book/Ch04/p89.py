"""
결합, 확장, 추가 예
"""
# (1) 리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y  # new object
print(z)

# (2) 리스트 확장
x.extend(y)  # x 확장
print(x)

# (3) 리스트 추가
x.append(y) # x 추가
print(x)

# (4) 리스트 두 배 확장
lst = [1, 2, 3, 4] # list 생성
result = lst * 2 # 각 원소 연산 안됨
print(result)