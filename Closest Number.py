T=int(input())
while T:
    T-=1
    a,b,x=map(int, input().split())
    if a > 1:
        result = int((a ** b) / float(x) + 0.5) * x
    else:
        result = 1
    if result != int(result):
        if result > 0.5 and x == 1:
            print(1)
        else:
            print(0)
    print(result)