def add_to_index(head,index,value):
	if index == 0:
		## special handle the head
		new_head = ListNode(value)
		new_head.next = head
		return new_head

	else:
		## prevNode points to the node that precedes the node at the insertion position
		prevNode = search_by_index(head,index-1)
		if prevNode is None:
			return head 
		new_node = ListNode(value)
		new_node.next = prevNode.next 
		prevnode.next = new_node 
		return head 




