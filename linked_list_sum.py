"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number_l1 = 0
        number_l2 = 0
        
        number_l1 = self.createNumbers(l1)
        number_l2 = self.createNumbers(l2)
        sum_list = number_l1 + number_l2
        
        res = deque(map(int, str(sum_list)))
        reversed_dq = deque(reversed(res))
        final_ans = self.append(reversed_dq)
        return final_ans
    
    def createNumbers(self, l):
        print(l)
        number = 0
        starter = 0
        while l.next != None:
            number = number + l.val * pow(10, starter)
            starter = starter + 1
            l = l.next
        if l:
            number = number + l.val * pow(10, starter)
            starter = starter + 1
        return number
    
    def append(self, item):
        #print(item)
        ptr = ListNode(0)
        cur_node = ptr
        for nums in item:             
            cur_node.next = ListNode(nums)
            cur_node = cur_node.next
        cur_node = ptr.next
        return cur_node
            
            

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()