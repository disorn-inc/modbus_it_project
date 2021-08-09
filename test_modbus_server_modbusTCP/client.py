from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient('192.168.1.102', port=12345) 
client.connect()
print(client.connect())
while True:
    try:
        BitInput = client.read_coils(0).bits
        BitVar1 = BitInput[0]
        print(BitVar1)

    except AttributeError:
        print("Connection Lost")
        
