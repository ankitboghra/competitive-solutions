#!/bin/python3

import sys

#XORing number with itself gives 0
#i.e. x ^ x =0
#so at last whatever number will not be repeated will remain as the answer.

def lonelyinteger(a):
    ans=0
    for i in a:
        ans= ans^i
    return ans

    '''
    Without using bit-wise operators 
    l=len(a)
    flag=False
    for i in range(0, l):
        flag=False
        for j in range(i+1, l):
            if a[i]==a[j]:
                flag=True
                a[i]=a[j]=101
                break
        if flag==False and a[i]!=101:
            return a[i]
      '''      

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
