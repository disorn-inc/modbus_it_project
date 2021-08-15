from pyModbusTCP.client import ModbusClient

client = ModbusClient('192.168.49.9', port=502)

client.open()

client.write_single_coil(0, True)

client.write_single_coil(0, False)