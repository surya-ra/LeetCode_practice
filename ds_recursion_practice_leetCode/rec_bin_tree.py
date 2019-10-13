class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder tree traversal 
def printInorder(root): 
    if root:
        # First recur on left child 
        printInorder(root.left)
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 
  
  
  
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right)

# Driver code 
root = Node('+') 
root.left      = Node('*') 
root.right     = Node(5) 
root.left.left  = Node(4) 
root.left.right  = Node('-')
root.right  = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(2)
""" 
print ("Preorder traversal of binary tree is")
printPreorder(root) 
  
print ("Inorder traversal of binary tree is")
printInorder(root) 
  """
print ("\nPostorder traversal of binary tree is")
printPostorder(root)