import socket
from Node import Node

class Client(Node):
	isConnected = False

	def __init__(self, host, port):
		super(Client, self).__init__()
		self.connect(host, port)
	
	def connect(self, host, port):
		self.socket.connect((host, port))
		self.isConnected = True
		self.start()
		#self.onReceipt()

	def onReceipt(self):
		while self.isConnected:
			data = self.socket.recv(self.sockBuffer)
			if not data:
				print 'Connection lost'
				self.isConnected = False
			elif data == self.EXIT:
				print 'Client has exited'
				self.isConnected = False
			else:
				print 'Received', data
		self.socket.close()
		
	def run(self):
		while self.isConnected:
			text = raw_input("Insert message: ")
			if text == self.EXIT:
				self.isConnected = False
			self.socket.sendall(text)
		print 'Ended message stream'
		
def main():
	HOST = 'localhost'		# The remote host
	PORT = 50010			# The same port as used by the server
	
	client = Client(HOST, PORT)
	
if __name__ == "__main__": main()
