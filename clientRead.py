import client

state = ""

client.connectClient()

while True:
    state = client.recvStr()

    print(state)
