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