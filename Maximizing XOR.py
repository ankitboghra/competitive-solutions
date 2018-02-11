'''
Given two integers,  and , find the maximal value of  xor , where  and  satisfy the following condition:
L<=A<=B<=R

Input Format

The input contains two lines;  is present in the first line and  in the second line.

'''

#!/bin/python3

import sys

def maximizingXor(l, r):
    res=0
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            x= i ^ j
            if x > res:
                res=x
    return res
if __name__ == "__main__":
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    print(result)
