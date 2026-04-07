# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = int(self.get_int(l1)[::-1])
        l2 = int(self.get_int(l2)[::-1])
        sp = list(map(int,list(str(l1+l2))))
        return self.to_listnode(sp, 1, ListNode(sp[0], None))
        
    def to_listnode(self, sp, ind, ln):
        if ind != len(sp):
            a = ListNode(sp[ind], ln)
            ind += 1
            return self.to_listnode(sp, ind, a)
        return ln

            

    def get_int(self,n):
        if n.next==None:
            return str(n.val)
        else:
            return str(n.val) + self.get_int(n.next)