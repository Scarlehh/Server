from Server import Server

class ChatServer(Server):
	def __init(self, host, port, sockBuffer=1024):
		super(Server, self, host, port, sockBuffer).__init__()

	def handler(self):
		self.startServer()
		
		
def main():
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 50010              # Arbitrary non-privileged port

	server = ChatServer(HOST, PORT)
	server.handler()
	
if __name__ == "__main__": main()
