#!/usr/bin/env python3
# ROS2 Libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ValuePublisher(Node):
    def __init__(self):
        super().__init__('serial_port_writer')
        self.value_publisher = self.create_publisher(String, '/serial_port/value', 10)
        self.value_timer = self.create_timer(0.5, self.publish_value)

        self.value_msg = String()
        self.value = 0
        self.max_value = 25

    def publish_value(self):
        self.value_msg.data = f"{self.value}"
        
        print(self.value_msg.data)
        self.value_publisher.publish(self.value_msg)

        if self.value >= self.max_value:
            self.value = self.max_value
        else:
            self.value += 1
    
    

def main(args=None):
    rclpy.init(args=args)
    value_publisher_node = ValuePublisher()
    try:
        rclpy.spin(value_publisher_node)
    except KeyboardInterrupt:
        value_publisher_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()