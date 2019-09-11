"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from collections import deque
i = -1

class My_Dictionary(dict):
	def __init__(self):
		self = dict()
	def add(self, key, value):
		self[key] = value

class Solution:
	dict_object = My_Dictionary() # Class variables should be properly initialised in leet code to avoid concurrent run issues
	#result_index = []

	def twoSum(self, List, target):
		List_Dq = deque(List)
		result = []
		x = -1
		
		def startLogic(List_Dq, tgt, result_index, i):
			pop_element = List_Dq.popleft()
			residue_to_search = tgt - pop_element
			i = i+1
			value_index = i
			if pop_element in Solution.dict_object:
				result_index.append(Solution.dict_object[pop_element])
				result_index.append(value_index)
			else:
				Solution.dict_object.add(residue_to_search, value_index)
				if List_Dq:
					startLogic(List_Dq, tgt, result_index, value_index)
			return result_index
		#print(startLogic(List_Dq, target))
		return startLogic(List_Dq, target, result, x)
		

sol = Solution()
Lst = [3,3]
print(sol.twoSum(Lst, 6))




