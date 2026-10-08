import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node =Node("Ultron_A91s")
    node.get_logger().info("Ultron Abhi Jinda Hai")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()