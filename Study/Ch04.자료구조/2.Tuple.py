"""
날짜 : 2022/01/04
이름 : 양용민
내용 : 파이썬 자료구조 Tuple 실습하기 교재 p92
"""
#List(동적), Tuple(정적)

# 튜플
dataset = (1, 2, 3, 4, 5)
print('dataset type :', type(dataset))
print('dataset :', dataset)
print('dataset[0] :', dataset[0])
print('dataset[2] :', dataset[2])
print('dataset[3] :', dataset[3])

# 튜플 수정, 추가, 삭제
dataset[1] = 7
print('dataset :', dataset) #수정, 추가, 삭제 불가(튜플은 정적리스트이므로 데이터 수정 안됨)
