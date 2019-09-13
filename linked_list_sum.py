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
		cur_node = cur_node.next
		
		while cur_node and cur_node.next:
			print(str(cur_node.value) + "->", end = '')
			#print(cur_node.value)
			cur_node = cur_node.next
			#print(cur_node)
			#print(cur_node.next)
		if cur_node:
			print(cur_node.value)
		else:
			print("empty Node")


if __name__ == '__main__':
	take_it_1 = [1,6,2,4]
	take_it_2 = [7,3,5,6]
	mylist1 = LinkedList()
	mylist2 = LinkedList()
	
	for lst in take_it_1:
		mylist1.append(lst)
	mylist1.display()
	
	
	for lst2 in take_it_2:
		mylist2.append(lst2)
	
	mylist2.display()
	
