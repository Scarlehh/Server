from Server import Server

class ChatServer(Server):
	def __init(self, host, port, sockBuffer=1024):
		super(Server, self, host, port, sockBuffer).__init__()
	
	def handler(self, conn, address, clients):
		command = conn.recv(self.sockBuffer)
		command = command.strip()
		if command == 'join':
			self.onReceipt(conn, address, clients)
		else:
			print "Didn't connect"
		
def main():
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 50010              # Arbitrary non-privileged port

	server = ChatServer(HOST, PORT)
	server.startServer()
	
if __name__ == "__main__": main()
