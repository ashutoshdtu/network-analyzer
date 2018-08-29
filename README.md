Network Analyzer
========

# Installation

Clone the repository and go to its root folder and run:

```
sudo pip install -e .
```

# Run Server

To run JSON-RPC server over http on port 5000:

```
sh serve_rpc.sh
```

To run RPC server over web socket (socket.io) on port 5050:

```shellscript
sh serve_socket.sh
```

# Client

## Python (2.7)

Sample Python 2.7 client code to access JSON-RPC API

```python
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.http import HttpPostClientTransport
from tinyrpc import RPCClient

rpc_client = RPCClient(
    JSONRPCProtocol(),
    HttpPostClientTransport('http://localhost:5000/v1/jsonrpc')
)

rpc_server = rpc_client.get_proxy()

print "pinging..."
pong = rpc_server.ping()
print "ping response: " + pong
resp = rpc_server.hello("Ashutosh")
print "hello world response: " + resp
```