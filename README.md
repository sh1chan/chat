# chat
Chatting applictoin

```
(client_application) <-> (middle_server) <-> (server)


[ client ]
	-> send/recv to/from the *middle_server
	-> makes a request to create a server (*middle_server returns the server id)

[ middle_server || client_server ]
	-> hiding the clint/server ip's
	-> (client|server) auth
	-> (client/server) binding
	-> stores all data
		-> clients local data storage
		-> removes the stored data

[ server ]
	-> send/recv to/from the *middle_server
```

```python
HOST_AND_PORT_type = NewType('HOST_AND_PORT_type', Tuple[str, int])

class Token:
	@staticmethod
	def generate(self) -> str:
		return
	@staticmethod
	def register_server(self, token: str, server: HOST_AND_PORT_type) -> None:
		return
	@staticmethod
	def register_client(self, token: str, client: HOST_AND_PORT_type) -> None:
		return

class Server:
	def create(self) -> HOST_AND_PORT_type:
		return

class MiddleServer:
	def __init__(self):
		self.max_clients_per_server = 30
	def create(self, clients: int):
		return
	def create_server(clients: int):
		servers = (clients // self.max_clients_per_server)
		if (clients % self.max_clients_per_server != 0):
			servers += 1
		token = Token.generate()
		for _ in range(servers):
			Token.register_server(token, Server.create())
	def connect(self, token: str, client: HOST_AND_PORT_type):
		Token.register_client(token, client)
	def send_to_clients(self, token: str, msg: Any):
		return
	def send_to_servers(self, token: str, msg: Any):
		return

class Client:
	def __init__(self, host_and_port: HOST_AND_PORT_type):
		self.host_and_port = host_and_port
	def create_server(self, clients: int = 1) -> str:
		return MiddleServer.create_server(clients)
	def connect(self, token: str):
		return self.middle_server.connect(self.host_and_port, token)
```
