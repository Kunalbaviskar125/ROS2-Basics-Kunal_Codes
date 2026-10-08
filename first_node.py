
# import rclpy
# from rclpy.node import Node

# class Mynode(Node):
#     def __init(self):
#         super().__init__("Py_test")
#         self.get_logger().info("Hello_world")



# def main(args=None):
#     rclpy.init(args=args)
#     node = Mynode()
#     node.get_logger().info("Apne Sathi Khud Bano")
#     rclpy.spin(node)
#     rclpy.shutdown()
# if __name__ == "__main__":
#     main()
import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        super().__init__("Py_test")
        self.get_logger().info("Hello_world")


def main(args=None):
    rclpy.init(args=args)

    node = Mynode()

    node.get_logger().info("Apne Sathi Khud Bano")

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()