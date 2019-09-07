class TreeNode:
	def __init__(self,key):
		self.left = None
		self.val = key
		self.right = None

class Solution:
	def preorderTraversal(self,root: TreeNode):
		List = list()
		List = []
		
		def traverseImplement(node):
			if node:
				List.append(node.val)
				traverseImplement(node.left)
				traverseImplement(node.right)

		traverseImplement(root)
		print(List) 

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(5)
solutionInstance = Solution()
solutionInstance.preorderTraversal(root)
