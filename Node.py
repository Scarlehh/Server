import threading
import socket

class Node(threading.Thread):
	EXIT = 'exit'

	def __init__(self, sockBuffer=1024):
		super(Node, self).__init__()
		self.sockBuffer=sockBuffer
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	def onReceipt():
		return
	
	def run(self):
		return

#def main():
#	node = Node()
#	node.makeServer('', 50007)
#	node.start()
