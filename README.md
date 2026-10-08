# ROS2-Basics-Kunal_Codes
Instead of keeping private notes, I've build a public ROS 2 learning repository where every concept you learn becomes a small lesson + working code + exercises.  I’d structure it so that I can learn first, then documenting what I understood, rather than trying to write a perfect tutorial from day one.
ROS 2 Python — My First Node

This is my first ROS 2 Python program.

The goal of this example is to understand:

    What rclpy is
    What a ROS 2 node is
    How to create a node using Python
    How to use the ROS 2 logger
    Why rclpy.spin() is used
    Why rclpy.shutdown() is required

Code

import rclpy
from rclpy.node import Node


class Mynode(Node):

    def __init__(self):
        super().__init__("Ultron_is_Back")
        self.get_logger().info("Hello World")


def main(args=None):
    rclpy.init(args=args)

    node = Mynode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()

What I Learned
1. import rclpy

rclpy is the Python client library for ROS 2.

It allows a Python program to communicate with the ROS 2 system.
2. from rclpy.node import Node

Node is the base class used to create a ROS 2 node.

My own node inherits from this class:

class Mynode(Node):

3. super().__init__("Ultron_is_Back")

This initializes the parent Node class.

"Ultron_is_Back" is the name given to my ROS 2 node.
4. self.get_logger().info()

This is used to print an informational message through the ROS 2 logging system.

self.get_logger().info("Hello World")

5. rclpy.init()

This initializes the ROS 2 Python client library.

rclpy.init(args=args)

It needs to happen before creating the node.
6. Creating the node

node = Mynode()

This creates an object of my Mynode class.

When this happens, the __init__() function runs.

Therefore, "Hello World" is printed.
7. rclpy.spin(node)

rclpy.spin(node)

This keeps the node alive and allows ROS 2 to process events.

The program continues running here until the node is stopped.
8. rclpy.shutdown()

rclpy.shutdown()

This shuts down the ROS 2 Python client after the node stops.
Execution Flow

Program starts
      ↓
rclpy.init()
      ↓
Create Mynode
      ↓
Node constructor runs
      ↓
"Hello World"
      ↓
rclpy.spin(node)
      ↓
Node stays alive
      ↓
Ctrl + C
      ↓
rclpy.shutdown()
      ↓
Program exits

Practice
Exercise 1

Create a node named:

Robot_Controller

Print:

Robot Controller Started
Exercise 2

Create a node named:

Camera_Node

Print:

Camera Node Started

and

Camera Connected Successfully
What I Want to Learn Next

My next topic is:

ROS 2 Timers
