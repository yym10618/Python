"""
날짜 : 2022/03/25
이름 : 양용민
내용 : 코딩테스트 - 1로 만들기
"""
# 정수 x를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 30001

# 6_다이나믹 프로그래밍 진행(바텀업)
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    # 현재의 수가 3로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)

    # 현재의 수가 5로 나누어 떨어지는 경우
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])