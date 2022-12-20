"""
This file shows what we will do when we have collected all students assignments.

[TODO] YOU NEED TO REPORT YOUR AGENT PERFORMANCE BY RUNNING THIS FILE IN THE NOTEBOOK!

First, we merge all students' submitted checkpoints into "data" directory. (
So you need to make sure your submitted checkpoint, i.e. pkl file, have unique name.)

Then, we run this file "tournament.py", which automatically gather all functions in "my_policy.py" and
launch a series matches. So you need to make sure your `my_policy_SID` in `my_policy.py` has unique `SID`.

Finally, we summary the match results of all your agents against others to a winning-rate matrix.

You do not need to modify anything in this file. If you want to make sure
your codes in "my_policy.py" works well, you can run this file directly without modification via:
    python tournament.py
or for quick testing:
    python tournament.py --num-episodes 2 --num-envs 2

The script will generate `data/full_evaluate_result.md` recording the reward matrix of your agent against others.

It may takes a long time since we need to launch M*N*N/2 matches where N is the number of existing agents,
and M is the number of matches held for each pair of policies, including those builtin agents.

-----
*2020-2021 Term 1, IERG 5350: Reinforcement Learning. Department of Information Engineering, The Chinese University of
Hong Kong. Course Instructor: Professor ZHOU Bolei. Assignment author: PENG Zhenghao, SUN Hao, ZHAN Xiaohang.*
"""

import argparse
import my_policy
import pandas as pd
import tabulate
# from competitive_pong.evaluate import evaluate_two_policies_in_batch
from competitive_rl import make_envs
from competitive_rl.utils import PrintConsole  # , get_compute_action_function
from core.utils import Timer
import numpy as np


def evaluate_two_policies_in_batch(compute_action0, compute_action1, envs, num_episodes):
    agent0_rewards = []
    agent1_rewards = []
    episode_rewards = np.zeros([envs.num_envs, 2], dtype=np.float)
    total_episodes = 0
    obs = envs.reset()
    while True:
        agent0_obs, agent1_obs = np.split(obs, 2, axis=1)
        agent0_action, agent1_action = np.asarray(compute_action0(agent0_obs)), np.asarray(compute_action1(agent1_obs))
        if envs.num_envs == 1:
            agent0_action = agent0_action[np.newaxis]
            agent1_action = agent1_action[np.newaxis]
        actions = np.stack([agent0_action, agent1_action], axis=1)
        obs, _, done, info = envs.step(actions)
        for env_index, env_info in enumerate(info):
            for agent_index, agent_info in env_info.items():
                if not isinstance(agent_index, int):
                    continue
                episode_rewards[env_index, agent_index] += agent_info["reward"]
        done = done.reshape(done.shape[0])
        for index, d in enumerate(done):
            if d:
                agent0_rewards.append(episode_rewards[index, 0])
                agent1_rewards.append(episode_rewards[index, 1])
                total_episodes += 1
                if total_episodes % 10 == 0:
                    print("Finish {}/{} episodes.".format(total_episodes, num_episodes))
        masks = 1. - done.astype(np.float32)
        episode_rewards *= masks.reshape(-1, 1)
        if total_episodes >= num_episodes:
            break
    return np.mean(agent0_rewards), np.mean(agent1_rewards)


def launch(my_policy_name, my_policy, agents, envs, num_episodes):
    console = PrintConsole(num_episodes)
    results = []
    timer = Timer()
    print("\nStart evaluating agent ", my_policy_name)
    for k2, a2 in agents.items():
        console.start()
        with timer:
            a1_result, a2_result = evaluate_two_policies_in_batch(my_policy, a2, envs, num_episodes)
        print("Finished combating {} and {}. Cost {}s.".format(my_policy_name, k2, timer.avg))
        print("===== {} VS {} result =====".format(my_policy_name, k2))
        print("Agent 0: {}, Reward: {:.3f}".format(my_policy_name, a1_result))
        print("Agent 1: {}, Reward: {:.3f}".format(k2, a2_result))
        print("\n\n")
        results.append(dict(
            agent0=my_policy_name,
            agent1=k2,
            agent0_reward=a1_result,
            agent1_reward=a2_result,
            num_matches=num_episodes
        ))
    return pd.DataFrame(results)


def build_matrix(result, single_line=False):
    """
    Build the wining rate matrix.

    matrix[a0, a1] represent the wining rate of agent a0 when competing
    with agent1.
    """
    assert isinstance(result, pd.DataFrame)

    agent_names = result.agent0.unique()
    if single_line:
        # win_rate_matrix = pd.DataFrame(columns=agent_names)
        reward_matrix = pd.DataFrame(columns=agent_names)
    else:
        # win_rate_matrix = pd.DataFrame(index=agent_names, columns=agent_names)
        reward_matrix = pd.DataFrame(index=agent_names, columns=list(agent_names) + ["average"])

    for _, record in result.iterrows():
        # agent0 win rate against agent1
        # win_rate_matrix.loc[record.agent0, record.agent1] = record.agent0_win / record.num_matches
        reward_matrix.loc[record.agent0, record.agent1] = record.agent0_reward

        if single_line:
            continue

        # agent1 win rate against agent0
        # win_rate_matrix.loc[record.agent1, record.agent0] = record.agent1_win / record.num_matches
        reward_matrix.loc[record.agent1, record.agent0] = record.agent1_reward

    if not single_line:
        for row_id, row in reward_matrix.iterrows():
            reward_matrix.loc[row_id, "average"] = row.iloc[:len(row) - 1].mean()

    return reward_matrix


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-episodes", "-M", default=20, type=int, help="Number of episodes to run.")
    parser.add_argument("--num-envs", default=10, type=int, help="Number of parallel environments.")
    parser.add_argument("--test", action="store_true", help="Test the code.")
    args = parser.parse_args()
    num_envs = args.num_envs
    num_episodes = args.num_episodes

    # ===== Load student policies =====
    student_function_names = [
        function_name for function_name in dir(my_policy) if function_name.startswith("my_policy")
    ]
    assert student_function_names
    student_functions = {}
    for f in student_function_names:
        studnet_policy_creator = my_policy.__dict__[f]
        studnet_id = f.split("my_policy_")[-1]
        student_functions[studnet_id] = studnet_policy_creator(num_envs)
    print("Collected policies: ", student_functions.keys())

    # ===== Setup environment =====
    # envs = make_envs("CompetitivePongDouble-v0", num_envs=num_envs, asynchronous=True)
    seed = np.random.randint(10000)
    envs = make_envs("cCarRacingDouble-v0", num_envs=num_envs, asynchronous=True, seed=seed)
    print("Environment ready")

    # ===== Run Matches =====
    visited_agent = set()
    result_list = []
    for name, policy in student_functions.items():
        # Remove repeat agents
        opponent_functions = student_functions.copy()
        for opponent in visited_agent:
            opponent_functions.pop(opponent)

        print("Start match between agent {} with {}.".format(name, opponent_functions.keys()))

        result = launch(name, policy, opponent_functions, envs, num_episodes)
        result_list.append(result)
        visited_agent.add(name)
    envs.close()

    result_list = pd.concat(result_list)
    # winning_rate_matrix, reward_matrix = build_matrix(result_list)
    reward_matrix = build_matrix(result_list)
    # print("===== Winning Rate Matrix (row vs column) =====")
    # print(winning_rate_matrix)
    print("===== Reward Matrix (row vs column) =====")
    print(reward_matrix)

    with open("evaluation_result.md", "w") as f:
        # f.write("winning rate matrix:\n\n")
        # f.write(tabulate.tabulate(winning_rate_matrix, winning_rate_matrix.keys(), tablefmt="pipe"))
        # f.write("\n\n\n\n\n")
        f.write("reward matrix\n\n")
        f.write(tabulate.tabulate(reward_matrix, reward_matrix.keys(), tablefmt="pipe"))

    result_list.to_csv("evaluation_result.csv")

    print("\nEvaluate result is saved at:\n{}\n{}".format(
        "evaluation_result.md",
        "evaluation_result.csv"
    ))
