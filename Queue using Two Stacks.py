Q1, Q2 = [], []
for a0 in range(int(input())):
    qry=[int(i) for i in input().split()]
    if qry[0]==1:
        Q1.append(qry[1])
    elif qry[0]==2:
        if not Q2:
            while Q1 : Q2.append(Q1.pop())
        Q2.pop()
    elif qry[0]==3:
        if not Q2:
            print (Q1[0])
        else:
            print (Q2[-1])