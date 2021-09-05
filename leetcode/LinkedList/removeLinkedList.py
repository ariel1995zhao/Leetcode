## remove linkedlist 


def remove_from_index(head,index):
	## assuming index >= 0 
	## this function will try to remove node at position indicated by index
	## if such position does not exist, this function does nothing 
	fake_head = ListNode(None)
	fake_head.next = head
	remove_place = search_by_index(fake_head,index)
	if remove_place is None or remove_place.next is None:
		return fake_head.next 
	remove_node = remove_place.next
	remove_place.next = remove_node.next 
	remove_node.next = None 
	return fake_head.next 
	





