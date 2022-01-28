t = int(input())
tsc = list(map(int, input().split()))
max_tsc = max(tsc)

nsc = []
for score in tsc:
    nsc.append(score / max_tsc * 100)
avg = sum(nsc)/t
print(avg)