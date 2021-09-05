class ListNode(object):

	def __init__(self,value): ## initialize the object that you create
		self.next = None  ## next pointer <-> instance variable 
		self.value = value  ## data 

	def __eq__(self,other):
		return instance(other,ListNode) and self.value == other.value 


node1 = ListNode("H") ## step : python Env creates an object of type ListNode
node2 = ListNode("E")
node1.next = node2



