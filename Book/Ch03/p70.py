"""
for 반복문 예
"""
# (1) 문자열 열거형객체 이용
string = "홍길동"
print(len(string)) # 문자 길이 : 3
for s in string : # 문자 -> 변수 넘김 : 3회
    print(s)

# (2) list 열거형객체 이용
lstset = [1, 2, 3, 4, 5] # 5개 원소를 갖는 열거형객체

for e in lstset :
    print('원소 : ', e)