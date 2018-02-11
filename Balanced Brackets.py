#!/bin/python3

import sys
left="{(["
right="})]"

def isBalanced(s):
    stack=[]
    for c in s:
        if c in left:
            stack.append(c)
        elif c in right:
            if not stack:
                return "NO"
            if right.index(c)!=left.index(stack.pop()):
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
