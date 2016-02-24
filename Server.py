import socket
from Node import Node

class Server(Node):
	isConnected = False

	def __init__(self, host, port):
		super(Server, self).__init__()
		self.makeServer(host, port)
	
	def makeServer(self, host, port, backlog=0):
		self.socket.bind((host, port))
		self.socket.listen(backlog);
		#self.start()
		print 'Waiting for connection...'
		self.conn, self.address = self.socket.accept()
		print 'Connected to', self.address
		self.isConnected = True
		self.onReceipt()
		#self.listenConnections()
	
	def listenConnections(self):
		while self.isConnected:
			print 'Waiting for connection...'
			conn, address = self.socket.accept()
			self.conn.append(conn)
			self.address.append(address)
			print 'Connected to', self.address
			
	def onReceipt(self):
		while self.isConnected:
			data = self.conn.recv(self.sockBuffer)
			if not data:
				print 'Connection lost'
				self.conn.close()
				self.isConnected = False
			elif data == self.EXIT:
				print 'Client has exited'
				self.conn.close()
				self.isConnected = False
			else:
				print 'Received', data
				self.conn.sendall(data)
		self.socket.close()
		
	def run(self):
		while self.isConnected:
			print 'Waiting for connection...'
			conn, address = self.socket.accept()
			self.conn.append(conn)
			self.address.append(address)
			print 'Connected to', self.address
			self.isConnected = True

def main():
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 50010              # Arbitrary non-privileged port

	server = Server(HOST, PORT)
	
if __name__ == "__main__": main()
