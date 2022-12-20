"""
This file defines the API of your agent.

Usages:
1. Get your policy through: `my_agent_SID(num_envs)`
2. Test your policy through: `python my_policy.py`

You need to finish my_agent_SID, change the function name and make sure passing the tests.

-----
*2020-2021 Term 1, IERG 5350: Reinforcement Learning. Department of Information Engineering, The Chinese University of
Hong Kong. Course Instructor: Professor ZHOU Bolei. Assignment author: PENG Zhenghao, SUN Hao, ZHAN Xiaohang.*
"""
import os.path as osp

import numpy as np
from competitive_rl import make_envs
from load_agents import PolicyAPI


# Please change the function name but keep the prefix as "my_policy"! For example, "my_policy_1155136634".
def my_policy_SID(num_envs=1):
    """We will use this function to load your agent and then testing.

    Make sure this function can run bug-free, when the working directory is
    "ierg5350-assignment/assignment5/"

    You can rewrite this function completely if you have custom agents, but you
    need to make sure the codes is bug-free and add necessary description on the notebook.

    Please rename this function!!! We will use program to automatically detect your agent, so a wrong function name
    will fail the evaluation. Run this file directly to make sure everything is fine.
    """
    # [TODO] rewrite this function
    # [TODO] CAUTION! PLEASE CHANGE THE NAME OF THIS FUNCTION!!! Otherwise our program can't find your agent!
    my_agent_log_dir = None
    my_agent_suffix = None

    # checkpoint_path = osp.join(my_agent_log_dir, "checkpoint-{}.pkl".format(my_agent_suffix))
    # if not osp.exists(checkpoint_path):
    #     raise ValueError("Can't find anything at {}!".format(checkpoint_path))
    # else:
    #     print("Found your checkpoint at {}!".format(checkpoint_path))

    return PolicyAPI(
        "cCarRacing-v0",
        num_envs=num_envs,
        log_dir=my_agent_log_dir,
        suffix=my_agent_suffix
    )


def my_policy_zhenghao(num_envs=1):
    return PolicyAPI("cCarRacing-v0", num_envs=num_envs, log_dir="data/alphacar", suffix="zhenghao")


def my_policy_alphacar(num_envs=1):
    return PolicyAPI("cCarRacing-v0", num_envs=num_envs, log_dir="data/alphacar", suffix="alphacar")


def test():
    # Run this function to make sure your API is runnable
    policy_names = [function_name for function_name in locals() if function_name.startswith("my_policy")]
    assert len(policy_names) == 1, "Found {}, the potential  policies {}".format(dir(), policy_names)
    policy_name = policy_names[0]
    policy_creator = locals()[policy_name]

    num_envs = 1
    policy = policy_creator(num_envs)
    env = make_envs("cCarRacing-v0", num_envs=num_envs, asynchronous=False)
    o = env.reset()
    for i in range(1000):
        a = policy(o)
        assert np.asarray(a).shape == (num_envs, 2)
        assert env.action_space.contains(a[0])
        o, _, d, _ = env.step(a)
        if d:
            o = env.reset()
    env.close()

    num_envs = 3
    policy = policy_creator(num_envs)
    env = make_envs("cCarRacing-v0", num_envs=num_envs, asynchronous=False)
    o = env.reset()
    for i in range(1000):
        a = policy(o)
        assert np.asarray(a).shape == (num_envs, 2)
        o, _, d, _ = env.step(a)
        if d:
            o = env.reset()
    env.close()

    print("Test passed!")


if __name__ == '__main__':
    # test()

    # Run this function to make sure your API is runnable
    policy_names = [function_name for function_name in locals() if function_name.startswith("my_policy")]
    assert len(policy_names) == 1, "Found {}, the potential  policies {}".format(dir(), policy_names)
    policy_name = policy_names[0]
    policy_creator = locals()[policy_name]

    num_envs = 1
    policy = policy_creator(num_envs)
    env = make_envs("cCarRacing-v0", num_envs=num_envs, asynchronous=False)
    o = env.reset()
    for i in range(1000):
        a = [policy(o)]
        o, _, d, _ = env.step(a)
        if d:
            o = env.reset()
    env.close()

    num_envs = 3
    policy = policy_creator(num_envs)
    env = make_envs("cCarRacing-v0", num_envs=num_envs, asynchronous=False)
    o = env.reset()
    for i in range(1000):
        a = policy(o)
        o, _, d, _ = env.step(a)
        if d[0]:
            o = env.reset()
    env.close()

    print("Test passed!")
