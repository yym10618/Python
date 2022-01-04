"""
날짜 : 2021/12/31
이름 : 양용민
내용 : 파이썬 연산자 실습하기 교재 p38
"""

#대입연산자
a = 1
b = c = d = 0
e, f, g = 7, True, 'Apple'

print('a :', a)
print('c :', c)
print('f :', f)
print('g :', g)

#산술연산자
num1 = 1
num2 = 2
num3, num4 = 3, 4

r1 = num1 + num2
r2 = num1 - num2
r3 = num2 * num3
r4 = num4 / num3  #나눗셈 실수
r5 = num4 // num3 #나눗셈 정수
r6 = num4 % num3  #나눗셈 나머지
r7 = num3 ** num2 #거듭제곱

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)
print('r4 =', r4)
print('r5 =', r5)
print('r6 =', r6)
print('r7 =', r7)

#복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8

num5 += 1 #num5 = num5 + 1
num6 -= 2 #num6 = num6 - 2
num7 *= 3 #num7 = num7 * 3
num8 /= 4 #num8 = num8 / 4

print('num5 = ', num5)
print('num6 = ', num6)
print('num7 = ', num7)
print('num8 = ', num8)

#비교연산자
var1 = 1
var2 = 2

rs = var1 > var2  #var1이 var2보다 크다
rs = var1 < var2  #var1이 var2보다 작다
rs = var1 >= var2 #var1이 var2보다 크거나 같다
rs = var1 <= var2 #var1이 var2보다 작거나 같다
rs = var1 == var2 #var1이 var2보다 서로 같다
rs = var1 != var2 #var1이 var2보다 서로 다르다

#논리연산자
var3 = 3
var4 = 4

res1 = var3 > 2 and var4 > 3 #var3은 2보다 크다 그리고 var4는 3보다 크다
res2 = var3 > 2 and var4 > 4 #var3은 2보다 크다 그리고 var4는 4보다 크다
res3 = var3 > 2 or var4 > 4  #var3은 2보다 크다 또는  var4는 4보다 크다
res4 = var3 > 4 or var4 > 5  #var3은 4보다 크다 또는  var4는 5보다 크다
res5 = not var3 > var4       #var3은 var4보다 크지 않다

print('res1 = ', res1)
print('res2 = ', res2)
print('res3 = ', res3)
print('res4 = ', res4)
print('res5 = ', res5)