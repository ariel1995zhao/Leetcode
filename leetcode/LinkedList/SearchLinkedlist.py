def search_by_index(head,index):
	## assuming valid index should be >= 0
	## returns a node object if found, None otherwise
	if head is None or index < 0 :
		return None

	for move_times in range(index):
		head = head.next 
		if not head:
			return None
		return head 



def search_by_value(head,value):
	if not head:
		return None

	current_node = head

	while current_node is not None:
		if current_node.val == value:
			return current_node
		current_node = current_node.next 

	return None 


