t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    c = int(a + b)
    print("Case #%s: %s + %s = %s" %(i+1, a, b, c) )