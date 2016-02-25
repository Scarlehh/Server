import socket
from Node import Node
import threading
import os

class Server(Node):
	def __init__(self, host, port):
		super(Server, self).__init__()
		self.makeServer(host, port)
	
	def makeServer(self, host, port, backlog=0):
		self.socket.bind((host, port))
		self.socket.listen(backlog);
	
	def exit(self):
		input = ''
		while input != '.bye':
			input=raw_input("Type .bye to exit")
		print('Closing server...')
		os._exit(1)		# tidy this
	
	def run(self):
		self.listenConnections()
	
	def listenConnections(self):
		self.connections = []
		self.amount = 0
		while 1:
			print 'Waiting for connection...'
			conn, address = self.socket.accept()
			print 'Connected to', address
			thread = threading.Thread(target=self.onReceipt, args=(conn, address,))
			self.connections.append(thread)
			self.amount+=1
			thread.start()
			# Make new thread for connection + run
	
	def onReceipt(self, conn, address):
		while 1:
			data = conn.recv(self.sockBuffer)
			if not data:
				print 'Connection lost with', address
				conn.close()
				break
			elif data == self.EXIT:
				print 'Client', address, 'has exited'
				conn.close()
				break
			else:
				print 'Received', data, 'from', address
				conn.sendall(data)
		conn.close()
		

def main():
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 50010              # Arbitrary non-privileged port

	server = Server(HOST, PORT)
	server.start()
	server.exit()
	
if __name__ == "__main__": main()
