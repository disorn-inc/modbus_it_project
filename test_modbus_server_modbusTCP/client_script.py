from pyModbusTCP.client import ModbusClient

client = ModbusClient('192.168.1.102', port=12345)

client.open()

client.write_single_coil(0, True)

client.write_single_coil(0, False)