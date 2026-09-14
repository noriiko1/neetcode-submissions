# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr != None:
            nxt = curr.next # creates pointer to next 
            curr.next = prev # set next equal to prev
            prev = curr # move prev to curr
            curr = nxt # shifts the node 
        return prev