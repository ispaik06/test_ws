import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ispaik06/test_ws/install/my_first_ros_rclpy_pkg'
