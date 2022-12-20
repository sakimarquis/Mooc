"""
A suits of blackbox tests of PPO algorithm. Run this file to make sure your
computer can run the system.

Usages:
    python test_ppo.py

-----
*2020-2021 Term 1, IERG 5350: Reinforcement Learning. Department of Information Engineering, The Chinese University of
Hong Kong. Course Instructor: Professor ZHOU Bolei. Assignment author: PENG Zhenghao, SUN Hao, ZHAN Xiaohang.*
"""

from train import train, parser


def test_single_env_pong():
    args = parser.parse_args([
        "--env-id", "cPong-v0",
        "--max-steps", "6000",
        "--num-envs", "1",
        "--algo", "PPO",
    ])
    train(args)


def test_multiple_env_pong():
    args = parser.parse_args([
        "--env-id", "cPong-v0",
        "--max-steps", "10000",
        "--num-envs", "3",
        "--algo", "PPO",
    ])
    train(args)


def test_single_env_car_racing():
    args = parser.parse_args([
        "--env-id", "cCarRacing-v0",
        "--max-steps", "6000",
        "--num-envs", "1",
        "--algo", "PPO",
    ])
    train(args)


def test_multiple_env_car_racing():
    args = parser.parse_args([
        "--env-id", "cCarRacing-v0",
        "--max-steps", "10000",
        "--num-envs", "3",
        "--algo", "PPO",
    ])
    train(args)


if __name__ == '__main__':
    # test_single_env_car_racing()
    # test_multiple_env_car_racing()
    # test_single_env_pong()
    test_multiple_env_pong()
