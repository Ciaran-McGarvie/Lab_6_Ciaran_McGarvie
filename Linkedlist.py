from node import Node 
class Linkedlist:
	def __init__(self, head = None, size = 0, tail = None):
		self.head    = head 
		self.size     = size 
		self.tail	   = tail

	def gethead(self):
		return(self.head)
	def sethead(self, h):
		self.nhead = h

	def getsize(self):
		return(self.size)
	def setsize(self, s):
		self.nsize = s

	def gettail(self):
		return(self.tail)
	def settail(self, t):
		self.tail = t 

	def isEmpty(self):
		if(self.getsize() > 0):
			return(False)
		return(True)
	def addNode(self, d):
		newNode = Node(data = d)

		if(self.isEmpty()):
			self.sethead(newNode)
		else:
			self.gettail().setnextpointer(newNode)
		self.settail(newNode)
		self.setsize(self.size + 1)
def main():
	ll = Linkedlist()
	ll.addNode(1000)
	ll.addNode(2000)
	print(ll.getsize())


if __name__ == "__main__": 
	main()
