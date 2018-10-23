#!/usr/bin/env python
import rospy
from controller_manager_msgs.srv import ListControllers
from openai_ros import robot_gazebo_env


class OrderPickingRobotEnv(robot_gazebo_env.RobotGazeboEnv):
    """Superclass for all Robot environments.
    """

    def __init__(self):
        """Initializes a new Robot environment.
        """
        # Variables that we give through the constructor.

        # Internal Vars, read data from controller by calling service
        self.controllers_list = ['my_robot_controller1','my_robot_controller2', ..., 'my_robot_controllerX']

        self.robot_name_space = "my_robot_namespace"

        reset_controls_bool = True or False
        
        # We launch the init function of the Parent Class robot_gazebo_env.RobotGazeboEnv
        
        super(MyRobotEnv, self).__init__(controllers_list=self.controllers_list,
                                                robot_name_space=self.robot_name_space,
                                                reset_controls=reset_controls_bool)

    # Methods needed to get controller list by calling ROS service
    # ----------------------------
    def _get_controller_list(self):
        rospy.wait_for_service("/arm/controller_manager/list_controllers")
        client = rospy.ServiceProxy("/arm/controller_manager/list_controllers", ListControllers)

        pass


    # Methods needed by the RobotGazeboEnv
    # ----------------------------
    def _check_all_systems_ready(self):
        """
        Checks that all the sensors, publishers and other simulation systems are
        operational.
        """
        # TODO
        return True
    
    # Methods that the TrainingEnvironment will need to define here as virtual
    # because they will be used in RobotGazeboEnv GrandParentClass and defined in the
    # TrainingEnvironment.
    # ----------------------------
    def _set_init_pose(self):
        """Sets the Robot in its init pose
        """
        raise NotImplementedError()
    
    
    def _init_env_variables(self):
        """Inits variables needed to be initialised each time we reset at the start
        of an episode.
        """
        raise NotImplementedError()

    def _compute_reward(self, observations, done):
        """Calculates the reward to give based on the observations given.
        """
        raise NotImplementedError()

    def _set_action(self, action):
        """Applies the given action to the simulation.
        """
        raise NotImplementedError()

    def _get_obs(self):
        raise NotImplementedError()

    def _is_done(self, observations):
        """Checks if episode done based on observations given.
        """
        raise NotImplementedError()
        
    # Methods that the TrainingEnvironment will need.
    # ----------------------------


# if __name__ == '__main__':
#     rospy.init_node("OrderPicking_Env")
