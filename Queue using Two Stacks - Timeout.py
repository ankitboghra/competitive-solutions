N=int(input())
Q1=[]
Q2=[]
for a0 in range(N):
    qry=[int(i) for i in input().split()]
    if qry[0]==1:
        Q1.append(qry[1])
        #print ("After enqueue Q1=",Q1)
    elif qry[0]==2:
        while Q1:
            Q2.append(Q1.pop())
        #print ("While dequeue from Q1 to Q2 - Q1=",Q1)
        #print ("While dequeue from Q1 to Q2 - Q2=",Q2)        
        Q2.pop()    
        while Q2:
            Q1.append(Q2.pop())
        #print ("After dequeue Q1=",Q1)
        #print ("After dequeue Q2=",Q2)
    elif qry[0]==3:
        #print("Output ", Q1[0])
        print (Q1[0])
#print ("Q1=",Q1)
#print ("Q2=",Q2)
