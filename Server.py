import socket
from Node import Node
import threading
import sys
import time

class Server(object):
	END_CONNECTION = False
	CONNECTIONS = []
	CLIENTS = []
	TIMEOUT = 0.1

	def __init__(self, host, port, sockBuffer=1024):
		self.sockBuffer=sockBuffer
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.makeServer(host, port)
	
	def makeServer(self, host, port, backlog=0):
		self.socket.bind((host, port))
		self.socket.listen(backlog)
	
	def startServer(self):
		manager = ThreadManager(self)
		manager.daemon = True
		manager.start()	
		input = ''
		while input != '.bye':
			input=raw_input("Type .bye to exit\n")
		self.END_CONNECTION = True
		print('Closing server...')
		sys.exit()		# tidy this
		
class ThreadManager(threading.Thread):
	END_CONNECTION = False
	CONNECTIONS = []
	CLIENTS = []
	TIMEOUT = 0.1

	def __init__(self, server):
		super(ThreadManager, self).__init__()
		self.server = server
	
	def run(self):
		listener = threading.Thread(target=self.listenConnections)
		listener.daemon = True
		listener.start()
		while self.END_CONNECTION is False:
			for i in range (0,len(self.CONNECTIONS)):
				self.CONNECTIONS[i].join(self.TIMEOUT)
				if not self.CONNECTIONS[i].isAlive():
					del self.CONNECTIONS[i]
		print 'Server closed.'
	
	def listenConnections(self):
		print 'Waiting for connection...'
		while 1:
			conn, address = self.server.socket.accept()
			self.CLIENTS.append(conn)
			print 'Connected to', address
			thread = threading.Thread(target=self.onReceipt, args=(conn, address))
			thread.daemon = True
			thread.start()
			self.CONNECTIONS.append(thread)
			# Make new thread for connection + run
	
	def onReceipt(self, conn, address):
		user = 'User' + str(address[1])
		while 1:
			data = conn.recv(self.server.sockBuffer)
			if not data:
				print 'Client has quit', address
				conn.close()
				break
			else:
				data = user + ' ' + data
				sys.stdout.write(data)
				for i in range (0,len(self.CONNECTIONS)):
					self.CLIENTS[i].sendall(data)
		conn.close()

def main():
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 50010              # Arbitrary non-privileged port

	server = Server(HOST, PORT)
	server.startServer()
	
if __name__ == "__main__": main()
