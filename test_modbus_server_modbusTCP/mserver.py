from pyModbusTCP.server import ModbusServer, DataBank

server = ModbusServer("192.168.49.13", 12345, no_block = True)

try:
    print('Start server...')
    server.start()
    print('Server is online')
    DataBank.set_bits(512,True)
    while True:
        state1 = DataBank.get_bits(8191,5)
        print(state1)
        if(state1[0] == True):
            print('recive data')
            DataBank.set_bits(6000,True)
            #print(state1)
except:
    print("Shutdown server")
    server.stop()
    print("Server is offline")