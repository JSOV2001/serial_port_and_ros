#!/usr/bin/env python3
# ROS2 Libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Python Libraries
import serial

class SerialPortWriter(Node):
    def __init__(self):
        super().__init__('serial_port_writer')
        # Subscribing to variable to control
        self.value_subscriber = self.create_subscription(String, '/serial_port/value', self.write_to_serial_port, 10)
        self.value_msg = String()

        # Serial port's information
        self.microcontroller_port = "/dev/ttyACM0"
        self.microcontroller_baudrate = 9600
        self.serial_port = serial.Serial(self.microcontroller_port, self.microcontroller_baudrate, timeout=10)

    def write_to_serial_port(self, value_msg):
        self.value_msg = value_msg
        data_out = str(self.value_msg.data) # Saving ROS2 message data into a variable (common practice)
        self.serial_port.write(bytes(data_out, 'utf-8')) # Writing ROS2 message data into microcontroller
        print(f"{data_out}")

def main(args=None):
    rclpy.init(args=args)
    serial_port_writer_node = SerialPortWriter()
    try:
        rclpy.spin(serial_port_writer_node)
    except KeyboardInterrupt:
        serial_port_writer_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()