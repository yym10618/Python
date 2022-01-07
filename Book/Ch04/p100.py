"""
요소 검사와 반복 예
"""
dic = dict(key = 100, key2 = 200, key3 = 300)
print(dic)

person = {'name':'홍길동', 'age':'35', 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

person['age'] = 45
print(person)

del person['address']
print(person) # {'name':'홍길동', 'age':'45'}

person['pay'] = 350
print(person) # {'name':'홍길동', 'pay':'350', 'age':'45'}

# (1) 요소 검사
print(person['age']) # 45
print('age' in person) # True

# (2) 요소 반복
for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print('name', '홍길동')