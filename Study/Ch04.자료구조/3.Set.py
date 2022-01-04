"""
날짜 : 2022/01/04
이름 : 양용민
내용 : 파이썬 자료구조 Set 실습하기 교재 p96
"""

# Set(집합) : 순서X, 중복X 자료구조
set1 = {1, 2, 3, 4, 5, 3, 2}
print('set1 type :', type(set1))
print('set1 :', set1)

set2 = set("Hello World")
print('set2 type :', type(set2))
print('set2 :', set2)

# List로 변환해서 출력
list1 = list(set1)
print('list1 :', list1)

list2 = list(set2)
print('list2 :', list2)
