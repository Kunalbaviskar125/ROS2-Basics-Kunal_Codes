import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        super().__init__("Ultron_is_Back")
        self.get_logger().info("Hello World")

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    # node.get_logger().info("Camera Node Connected Securely")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
