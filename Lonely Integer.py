/*
Consider an array of  integers, , where all but one of the integers occur in pairs. In other words, every element in  occurs exactly twice except for one unique element.
Given , find and print the unique element.
*/
#!/bin/python3

import sys

def lonelyinteger(a):
    ans=0
    for i in a:
        ans= ans^i
    return ans
    '''
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
