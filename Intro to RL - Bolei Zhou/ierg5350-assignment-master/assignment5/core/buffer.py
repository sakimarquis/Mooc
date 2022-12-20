"""
This file defines A2C and PPO rollout buffer.

You need to implement the compute_returns function.

-----
*2020-2021 Term 1, IERG 5350: Reinforcement Learning. Department of Information Engineering, The Chinese University of
Hong Kong. Course Instructor: Professor ZHOU Bolei. Assignment author: PENG Zhenghao, SUN Hao, ZHAN Xiaohang.*
"""
import torch
from torch.utils.data.sampler import BatchSampler, SubsetRandomSampler
import numpy as np


class PPORolloutStorage:
    def __init__(self, num_steps, num_processes, obs_shape, act_dim, device,
                 use_gae=True, gae_lambda=0.95):
        def zeros(*shapes, dtype=None):
            return torch.zeros(shapes, dtype=dtype).to(device)

        self.observations = zeros(num_steps + 1, num_processes, *obs_shape, dtype=torch.uint8)
        self.rewards = zeros(num_steps, num_processes, 1)
        self.value_preds = zeros(num_steps + 1, num_processes, 1)
        self.returns = zeros(num_steps + 1, num_processes, 1)
        self.action_log_probs = zeros(num_steps, num_processes, 1)
        self.actions = zeros(num_steps, num_processes, act_dim).to(torch.long)
        self.masks = torch.ones(num_steps + 1, num_processes, 1, dtype=torch.bool).to(device)

        self.num_steps = num_steps
        self.step = 0

        self.gae = use_gae
        self.gae_lambda = gae_lambda

    def feed_forward_generator(self, advantages, mini_batch_size):
        """A generator to provide samples for PPO. PPO run SGD for multiple
        times so we need more efforts to prepare data for it."""
        num_steps, num_processes = self.rewards.size()[0:2]
        batch_size = num_processes * num_steps
        sampler = BatchSampler(SubsetRandomSampler(range(batch_size)),
                               mini_batch_size, drop_last=True)
        for indices in sampler:
            observations_batch = self.observations[:-1].view(
                -1, *self.observations.size()[2:])[indices]
            actions_batch = self.actions.view(-1, self.actions.size(-1))[indices]
            return_batch = self.returns[:-1].view(-1, 1)[indices]
            masks_batch = self.masks[:-1].view(-1, 1)[indices]
            old_action_log_probs_batch = self.action_log_probs.view(-1, 1)[indices]
            adv_targ = advantages.view(-1, 1)[indices]

            yield observations_batch, actions_batch, return_batch, \
                  masks_batch, old_action_log_probs_batch, adv_targ

    def compute_returns(self, next_value, gamma):
        if self.gae:
            self.value_preds[-1] = next_value
            gae = 0
            for step in reversed(range(self.rewards.size(0))):
                # [TODO] Implement GAE advantage computing here.
                # Hint:
                #  1. The return at timestep t should be (advantage_t + value_t)
                #  2. You should use reward, values, mask to compute TD error
                #   delta. Then combine TD error of timestep t with advantage
                #   of timestep t+1 to get the advantage of timestep t.
                #  3. The variable `gae` represents the advantage
                #  4. The for-loop is in a reverse order.

                self.returns[step] = None
                pass

        else:
            # Ignore this part
            raise NotImplementedError("Not for this assignment.")

    def insert(self, current_obs, action, action_log_prob, value_pred, reward, mask):
        if isinstance(current_obs, np.ndarray):
            current_obs = torch.from_numpy(current_obs.astype(np.uint8))
        self.observations[self.step + 1].copy_(current_obs)
        self.actions[self.step].copy_(action)
        self.action_log_probs[self.step].copy_(action_log_prob)
        self.value_preds[self.step].copy_(value_pred)
        self.rewards[self.step].copy_(reward)
        self.masks[self.step + 1].copy_(mask)
        self.step = (self.step + 1) % self.num_steps

    def after_update(self):
        self.observations[0].copy_(self.observations[-1])
        self.masks[0].copy_(self.masks[-1])

    def before_update(self, obs):
        if isinstance(obs, np.ndarray):
            obs = torch.from_numpy(obs)
        self.observations[0].copy_(obs)
