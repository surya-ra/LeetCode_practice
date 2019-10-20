# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        temp = head
        final_lst = []
        if temp is None:
            final_lst = []
        while temp and temp.next:
            temp.val, temp.next.val = temp.next.val, temp.val
            final_lst.append(temp.val)
            final_lst.append(temp.next.val)
            temp = temp.next.next
        if temp:
            final_lst.append(temp.val)
            
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for item in final_lst:
            ptr.next = ListNode(item)
            ptr = ptr.next
        ptr = dummyRoot.next
        return ptr
        
        