'''
Given an array A of integers, convert the array into a special array.
Special array is a sequence such that a(1) >= a(2) <= a(3) >= a(4) <= a(5) and so on...
Input Format

First line of input contains n, the length of array A.
Second line of input contains n space separated integers, elements of array.
Constraints

3 <= n <= 100000
0 <= a(i) <= 1000000
'''

N=int(input())
ary=list(map(int, input().split()))
ary.sort();

for i in range(0,len(ary)-1,2):
    tmp=ary[i]
    ary[i]=ary[i+1]
    ary[i+1]=tmp
    
for i in ary:
    print(i,end=" ")
