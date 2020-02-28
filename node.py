class Node: 
	def __init__(self, data, nextpointer = None):
		self.data    = data 
		self.nextpointer = nextpointer

	def getData(self):
		return(self.data)

	def setData(self, nData):
		self.data = nData

	def getnextpointer(self):
		return(self.nextpointer)
	def setnextpointer(self, n):
		self.nextpointer = n 

