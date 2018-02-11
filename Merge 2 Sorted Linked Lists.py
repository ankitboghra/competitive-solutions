"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA
    
    s=t=Node()
        
    while not (headA is None or headB is None):
        if headA.data<headB.data:
            c=headA
            headA=headA.next
        else:
            c=headB
            headB=headB.next
        t.next=c
        t=t.next

    if headA is None:
        t.next=headB
    if headB is None:
        t.next=headA
    return s.next
            