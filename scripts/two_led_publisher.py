#!/usr/bin/env python3
# ROS2 Libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ValuePublisher(Node):
    def __init__(self):
        super().__init__('serial_port_writer')
        self.value_publisher = self.create_publisher(String, '/serial_port/value', 10)
        self.value_timer = self.create_timer(1.0, self.publish_value)

        self.value_msg = String()
        self.actuator1_value = 0
        self.actuator1_max_value = 25
        self.actuator2_value = 0
        self.actuator2_max_value = 25

    def publish_value(self):
        self.value_msg.data = f"{self.actuator1_value} {self.actuator1_value}"

        if self.actuator1_value < 10 and self.actuator2_value < 10:
            self.value_msg.data = f"0{self.actuator1_value} 0{self.actuator2_value}"

        elif self.actuator1_value < 10 and self.actuator2_value >= 10:
            self.value_msg.data = f"0{self.actuator1_value} {self.actuator2_value}"

        elif self.actuator1_value >= 10 and self.actuator2_value < 10:
            self.value_msg.data = f"{self.actuator1_value} 0{self.actuator2_value}"

        elif self.actuator1_value >= 10 and self.actuator2_value >= 10:
            self.value_msg.data = f"{self.actuator1_value} {self.actuator2_value}"
        
        print(self.value_msg.data)
        self.value_publisher.publish(self.value_msg)

        if self.actuator1_value >= self.actuator1_max_value:
            self.actuator1_value = self.actuator1_max_value
        else:
            self.actuator1_value += 1
        
        if self.actuator2_value >= self.actuator2_max_value:
            self.actuator2_value = self.actuator2_max_value
        else:
            self.actuator2_value += 1
    

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