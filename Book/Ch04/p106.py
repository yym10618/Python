"""
선택정렬 알고리즘 예
"""
# (1) 오름차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1):  # 1 ~ n-1
    for j in range(i+1, n):  # i+1 ~ n
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print(dataset)  # 각 회전 정렬내용

# (2) 내림차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1):  # 1 ~ n-1
    for j  in range(i+1, n):  # i+1 ~ n
        if dataset[i] < dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print(dataset)

print(dataset)