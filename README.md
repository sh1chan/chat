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

[ Remote Storage Server ]
	-> client server to send/recv a client data
```

```python
HOST_AND_PORT_type = NewType('HOST_AND_PORT_type', Tuple[str, int])

class Token:
	@staticmethod
	def generate(*args, **kwargs) -> str:
		return
	@staticmethod
	def register_server(token: str, server: HOST_AND_PORT_type) -> None:
		return
	@staticmethod
	def register_client(token: str, client: HOST_AND_PORT_type) -> None:
		return

class Server:
	@staticmethod
	def create() -> HOST_AND_PORT_type:
		return

class MiddleServer:
	@staticmethod
	def create_server(client: HOST_AND_PORT_type, clients: int) -> str:
		token = Token.generate()
		Token.register_server(token, Server.create())
		Token.register_client(token, client)
		return token
	@staticmethod
	def send_to_clients(token: str, msg: Any):
		return
	@staticmethod
	def send_to_server(token: str, client: HOST_AND_PORT_type, msg: Any):
		return

class Client:
	def __init__(self, host_and_port: HOST_AND_PORT_type):
		self.host_and_port = host_and_port
	def create_server(self, clients: int = 1) -> str:
		return MiddleServer.create_server(clients)
	def send_to_middle_server(token: str, msg: Any):
		MiddleServer.send_to_server(token, self.host_and_port, msg)
```

```json
{
	"ClientTokens": {
		"client": ["token", "..."],
	},
	"TokenClientsAndServers" {
		"token": {
			"client": ["HOST_AND_PORT_type", "..."],
			"server": ["HOST_AND_PORT_type", "..."],
		},
	},
	"RemoteStorageServerConnections": {
		"client": {
			"server": "..."
		}
	}

}
```
