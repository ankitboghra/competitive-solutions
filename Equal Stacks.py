#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1.reverse()
h2.reverse()
h3.reverse()

sum_h1=sum(h1)
sum_h2=sum(h2)
sum_h3=sum(h3)

while not (sum_h1==sum_h2 and sum_h2==sum_h3):
    if sum_h1>sum_h2 or sum_h1>sum_h3:
        temp=h1.pop()
        sum_h1-=temp
    if sum_h2>sum_h1 or sum_h2>sum_h3:
        temp=h2.pop()
        sum_h2-=temp
    if sum_h3>sum_h1 or sum_h3>sum_h2:
        temp=h3.pop()
        sum_h3-=temp
print (sum_h1)        
      