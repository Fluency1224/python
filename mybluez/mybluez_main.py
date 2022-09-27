import bluetooth as bt

#######################################################
# Scan
#######################################################
#print(bt.discover_devices())

target_name = "FELIX-01"   # target device name
target_address = "D1:43:56:CE:25:F8"
port = 7         # RFCOMM port

nearby_devices = bt.discover_devices(10)

# scanning for target device
for bdaddr in nearby_devices:
    print(bdaddr)
    if bdaddr == target_address:
        print("found target bluetooth %s - %s ", bt.lookup_name( target_address ), target_address)
        services = bt.find_service(target_address)
        for svc in services:
            print("Service Name: %s"    % svc["name"])
            print("    Host:        %s" % svc["host"])
            print("    Description: %s" % svc["description"])
            print("    Provided By: %s" % svc["provider"])
            print("    Protocol:    %s" % svc["protocol"])
            print("    channel/PSM: %s" % svc["port"])
            print("    svc classes: %s "% svc["service-classes"])
            print("    profiles:    %s "% svc["profiles"])
            print("    service id:  %s "% svc["service-id"])
            print("")
# try:
#     sock=bt.BluetoothSocket(bt.RFCOMM)
#     sock.connect((target_address, port))

#     while True:         
#         try:
#             recv_data = sock.recv(1024)
#             print(recv_data)
#             sock.send(recv_data)
#         except KeyboardInterrupt:
#             print("disconnected")
#             sock.close()
#             print("all done")
# except bt.btcommon.BluetoothError as err:
#     print('An error occurred : %s ' % err)
#     pass