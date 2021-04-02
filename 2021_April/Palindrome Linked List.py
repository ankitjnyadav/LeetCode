# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current=head
        val=[]
        while current is not None:
            val.append(current.val)
            current=current.next
        if val[::-1]==val:
            return True
        else:
            return False