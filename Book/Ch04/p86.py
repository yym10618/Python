"""
단일 리스트 색인 예
"""
# (2) 단일 list 색인
x = list(range(1, 11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2])  # 홀수 색인
print(x[1::2])  # 1부터 시작하는 짝수 색인