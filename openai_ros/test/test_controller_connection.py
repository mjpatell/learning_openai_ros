#!/usr/bin/env python

import rospy
#from openai_ros.task_envs.cartpole_stay_up.stay_up import CartPoleStayUpEnv
from openai_ros.controllers_connection import ControllersConnection

print("Test controller connection")
test_controller_connection = ControllersConnection(namespace='arm', controllers_list=[])
print("Finish controller testing ...")