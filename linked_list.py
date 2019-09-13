class Node:
	def __init__(self, data):
		self.value = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = Node(0)

	def append(self,item):
		new_node = Node(item)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
		
	def display(self):
		cur_node = self.head
		#print(cur_node.next.value)
		while cur_node and cur_node.next:
			print(str(cur_node.value) + "->", end = '')
			cur_node = cur_node.next

		"""
		while in_node in type_node:
			ptint(str(in_node.value) + "->", end = '')
			in_node = in_node.next

		if in_node:
			print(in_node.value)

		else:
			print("empty Node")
		"""


if __name__ == '__main__':
	take_it = [1,6,2,4]
	mylist = LinkedList()
	for lst in take_it:
		mylist.append(lst)
	
	mylist.display()
	