"""
날짜 : 2022/02/04
이름 : 양용민
내용 : 코딩테스트 그리디 알고리즘 실습
"""
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    a = min(data)
    result = max(result, a)

print(result)