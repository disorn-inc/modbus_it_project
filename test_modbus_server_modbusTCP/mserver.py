from pyModbusTCP.server import ModbusServer, DataBank

server = ModbusServer("192.168.1.103", 12345, no_block = True)

try:
    print('Start server...')
    server.start()
    print('Server is online')
    while True:
        state1 = DataBank.get_bits(0,5)
        print(state1)
        if(state1[0] == True):
            print('recive data')
            #print(state1)
except:
    print("Shutdown server")
    server.stop()
    print("Server is offline")