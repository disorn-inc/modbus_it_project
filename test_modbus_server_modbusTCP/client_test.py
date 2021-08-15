import enum
from pyModbusTCP.client import ModbusClient

client = ModbusClient('192.168.49.9', port=520)

print(client.open())

#client.write_single_coil(0, True)

# client.write_single_coil(0, False)

# def write_arm(num):
#     index = [8192,2,3]
#     enum_s = enum(index)
#     for i, adress_s in enum_s:
#         if(i == num):
#             client.write_single_coil(adress, True)

# def write_arm(arm,adress):
#     if (sensor2[0]  == True):
#         client.write_single_coil(adress, True)
#     else:
#         client.write_single_coil(adress, False)
        
    

try:
    client.open()
    while(True):
        sensor1 = client.read_coils(8692,1)
        sensor2 = client.read_coils(8693, 1)
        # sensor3 = client.read_single_coils(0, 0)    sensor1 = client.read_single_coils(8692, 0)
        sensor2 = client.read_coils(8693, 1)
        # sensor3 = client.read_single_coils(0, 0)
        # sensor4 = client.read_single_coils(0, 0)
        print(sensor1)
        if (sensor1[0] == True):
            print('recive data from camera sensor')
            
        if (sensor2[0]  == True):
            client.write_single_coil(8192, True)
        else:
            client.write_single_coil(8192, False)
        # sensor4 = client.read_single_coils(0, 0)
        

        
except:
    print('error')