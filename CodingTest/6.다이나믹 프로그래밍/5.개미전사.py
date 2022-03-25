"""
날짜 : 2021/10/15
이름 : 양용민
내용 : 코딩테스트 - 개미 전사
"""
# 정수 n를 입력 받기
n = int(input())

# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 6_다이나믹 프로그래밍 진행(바텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])


# 계산된 결과 출력
print(d[n-1])