"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 파이썬 최대공약수 연습문제
"""

a = int(input('첫 번째 수 입력 : '))
b = int(input('두 번째 수 입력 : '))

result = min = 0

if a < b:
    min = a
else:
    min = b

while True:

    if a % min == 0 and b % min == 0:
        result = min
        break

    min -= 1

print('%d와 %d의 최대 공약수는 %d 입니다.' % (a, b ,result))