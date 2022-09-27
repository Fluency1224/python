#/usr/bin/env python
# 通过 pc-ble-driver-py 控制 nRF52 连接设备
"""
This example simply demonstrates scanning for peripheral devices
"""
from traceback import print_tb
from blatann import BleDevice
from blatann.services import nordic_uart
from blatann.utils import setup_logger

logger = setup_logger(level="INFO")

target_address = "D1:43:56:CE:25:F8,s"
peer_addr = ""

def on_data_rx(service, data):
    """
    Called whenever data is received on the RX line of the Nordic UART Service

    :param service: the service the data was received from
    :type service: nordic_uart.service.NordicUartClient
    :param data: The data that was received
    :type data: bytes
    """
    hex_data = data.hex()
    logger.info("Received data (len {}): '{}'".format(len(data), hex_data))

def main(serial_port):
    # Create and open the device
    ble_device = BleDevice(serial_port)
    ble_device.configure(att_mtu_max_size=247)
    ble_device.open()

    logger.info("Scanning...")
    # Set scanning for 4 seconds
    ble_device.scanner.set_default_scan_params(timeout_seconds=5)
    ble_device.set_default_peripheral_connection_params(7.5, 15, 4000)
    # Start scanning and iterate through the reports as they're received
    for report in ble_device.scanner.start_scan().scan_reports:
        if not report.duplicate:
            if(report.peer_address == target_address):
                peer_addr = report.peer_address
                logger.info(report)
    
    logger.info("Found match: connecting to address {}".format(peer_addr))
    peer = ble_device.connect(peer_addr).wait()
    if not peer:
        logger.warning("Timed out connecting to device")
        return
    logger.info("Connected, conn_handle: {}".format(peer.conn_handle))
    
    logger.info("Exchanging MTU")
    peer.exchange_mtu(peer.max_mtu_size).wait(10)
    logger.info("MTU Exchange complete, discovering services")

    # Wait up to 10 seconds for service discovery to complete
    _, event_args = peer.discover_services().wait(10, exception_on_timeout=False)
    logger.info("Service discovery complete! status: {}".format(event_args.status))

    uart_service = nordic_uart.find_nordic_uart_service(peer.database)
    if not uart_service:
        logger.info("Failed to find Nordic UART service in peripheral database")
        peer.disconnect().wait()
        ble_device.close()
        return

    # Initialize the service
    uart_service.initialize().wait(5)
    uart_service.on_data_received.register(on_data_rx)

    # 登录验证
    data_test = 'AA00010000000108313233343536373847EB0D'
    logger.info("Send data (len {}): '{}'".format(len(data_test), data_test))
    data_test_byte = bytes.fromhex(data_test)
    uart_service.write(data_test_byte).wait(10)
    while True:
        data = input("Enter data to send to peripheral (q to exit): ")
        if data == "q":
            break
        uart_service.write(data).wait(10)
    
    # gatt disconnect
    peer.disconnect().wait()
    # Clean up and close the device
    ble_device.close()

if __name__ == '__main__':
    main("COM4")



