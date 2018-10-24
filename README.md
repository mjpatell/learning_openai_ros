## Install Dependencies

Execute the following commands:<br>
`cd ~/ros_ws/src`<br>
`git clone https://bitbucket.org/theconstructcore/openai_ros.git`<br>
`cd ~/ros_ws`<br>
`catkin_make`<br>
`source devel/setup.bash`<br>
`rosdep install openai_ros`<br>


## Use
Launch Gazebo model:<br>
`roslaunch cartpole_description main.launch`<br>
<br>
Run cartpole-example: (Go to roscd cartpole_tests/script)<br>
`python reinforcement_q_learning.py` <br>
<br>
make sure python version should be 3.7.0. To check python version<br>
`python -V`





