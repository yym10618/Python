"""
추가, 삭제, 수정, 삽입 예
"""

# (1) 단일 리스트 객체 생성
num = ['one', 'two', 'three', 'four']
print(num)
print(len(num))

# (2) 리스트 원소 추가
num.append('five') # 추가
print(num)

# (3) 리스트 원소 삭제
num.remove('five') # 삭제
print(num)

# (4) 리스트 원소 수정
num[3] = '4' # 수정
print(num)

# (5) 리스트 원소 삽입
num.insert(0, 'zero') # 삽입
print(num)