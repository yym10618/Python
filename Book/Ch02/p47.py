"""
외부상수 출력 예
"""

name = "홍길동"
age = 35
price = 125.456

print("이름 : %s, 나이 : %d, data = %.2f" %(name, age, price))
# (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, data={}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data={2}".format(age, name, price))

# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query) # member 테이블에서 uid가 hong인 레코드 검색