from gym.envs.registration import register

# The path is __init__.py of openai_ros, where we import the MovingCubeOneDiskWalkEnv directly
register(
        id='CartPoleStayUp-v0',
        entry_point='openai_ros:task_envs.cartpole_stay_up.stay_up.CartPoleStayUpEnv',
        timestep_limit=1000,
    )