"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""
from collections import deque
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_lst = []
        x = True
        dq_arr1 = deque(nums1)
        dq_arr2 = deque(nums2)
        
        while x:
            try:
                if( dq_arr1[0] >= dq_arr2[0] ):
                    final_lst.append(dq_arr2.popleft())
                else:
                    final_lst.append(dq_arr1.popleft())
            except IndexError:
                try:
                    if dq_arr1:
                        final_lst.append(dq_arr1.popleft())
                    else:
                        final_lst.append(dq_arr2.popleft())
                except IndexError:
                    x = False
        
        return median(final_lst)