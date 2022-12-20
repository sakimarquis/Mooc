"""
This file defines a set of built-in agents that can be used as opponent in
training and evaluation.

Nothing you need to implement in this file, unless you wish to implement a
custom policy or introduce a custom agent as opponent in training and
evaluation.

-----
*2020-2021 Term 1, IERG 5350: Reinforcement Learning. Department of Information Engineering, The Chinese University of
Hong Kong. Course Instructor: Professor ZHOU Bolei. Assignment author: PENG Zhenghao, SUN Hao, ZHAN Xiaohang.*
"""
from competitive_rl import make_envs

from core.ppo_trainer import PPOTrainer, ppo_config


class PolicyAPI:
    """
    This class wrap an agent into a callable function that return action given
    an raw observation or a batch of raw observations from environment.

    Note that if you have implement other arbitrary custom agent, you are
    welcomed to implement a function-like API by yourself. You can write
    another API function or class and replace this one used in evaluation or
    even training.

    Your custom agent may have different network structure and different
    preprocess techniques. Remember that the API take the raw observation with
    shape (num_envs, 1, 42, 42) as input and return an single or a batch of
    integer(s) as action in [0, 1, 2]. Custom agent worth plenty of extra
    credits!
    """

    def __init__(self, env_id, num_envs=1, log_dir=None, suffix=None, _test=False):
        # self.resized_dim = 42
        env = make_envs(env_id=env_id, num_envs=1)
        self.obs_shape = env.observation_space.shape
        self.agent = PPOTrainer(env, ppo_config)
        if log_dir is not None:  # log_dir is None only in testing
            success = self.agent.load_w(log_dir, suffix)
            if not success and not _test:
                raise ValueError("Failed to load agent!")
        self.num_envs = num_envs

    def reset(self):
        pass

    def __call__(self, obs):
        action = self.agent.compute_action(obs, True)[1]
        action = action.detach().cpu().numpy()
        if self.num_envs == 1:
            return action[0]
        return action


if __name__ == '__main__':
    # Testing

    # Load the agent as the opponent agent
    from competitive_rl.car_racing.make_competitive_car_racing import make_competitive_car_racing

    num_envs = 1
    policy = PolicyAPI("cCarRacing-v0", num_envs=num_envs)
    comp_env = make_competitive_car_racing(policy, num_envs=num_envs)
    comp_env = comp_env.envs[0]
    obs = comp_env.reset()
    frames = []
    for i in range(1000):
        obs, rew, term, _ = comp_env.step(policy(obs))  # <= The action represents (steering, acceleration, brake)
        if term:
            break
