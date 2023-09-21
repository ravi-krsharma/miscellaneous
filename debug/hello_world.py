import debugpy
debugpy.listen(("localhost", 5678))  # listen for incoming DAP client connections
debugpy.wait_for_client()  # wait for a client to connect

print('Hello World')