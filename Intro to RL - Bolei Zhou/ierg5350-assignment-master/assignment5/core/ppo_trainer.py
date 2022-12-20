"""
This file implement PPO algorithm.

You need to implement `compute_loss` function.

-----
*2020-2021 Term 1, IERG 5350: Reinforcement Learning. Department of Information Engineering, The Chinese University of
Hong Kong. Course Instructor: Professor ZHOU Bolei. Assignment author: PENG Zhenghao, SUN Hao, ZHAN Xiaohang.*
"""
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim

from .base_trainer import BaseTrainer
from .buffer import PPORolloutStorage


class PPOConfig:
    """Not like previous assignment where we use a dict as config, here we
    build a class to represent config."""

    def __init__(self):
        # Common
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.eval_freq = 100
        self.save_freq = 50
        self.log_freq = 5
        self.num_envs = 1

        # Sample
        self.num_steps = 200  # num_steps * num_envs = sample_batch_size
        self.resized_dim = 42

        # Learning
        self.gamma = 0.99
        self.lr = 5e-4
        self.grad_norm_max = 10.0
        self.entropy_loss_weight = 0.01
        self.ppo_epoch = 10
        self.mini_batch_size = 500
        self.ppo_clip_param = 0.1
        self.USE_GAE = True
        self.gae_lambda = 0.95
        self.value_loss_weight = 1.0


ppo_config = PPOConfig()


class PPOTrainer(BaseTrainer):
    def __init__(self, env, config):
        super(PPOTrainer, self).__init__(env, config)

        # There configs are only used in PPO
        self.num_sgd_steps = config.ppo_epoch
        self.mini_batch_size = config.mini_batch_size
        self.num_mini_batches = int(
            self.num_steps // self.mini_batch_size)
        self.clip_param = config.ppo_clip_param

    def setup_optimizer(self):
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr, eps=1e-5)

    def setup_rollouts(self):
        act_dim = 1 if self.discrete else self.num_actions
        self.rollouts = PPORolloutStorage(self.num_steps, self.num_envs, self.num_feats, act_dim, self.device,
                                          self.config.USE_GAE, self.config.gae_lambda)

    def compute_loss(self, sample):
        """Compute the loss of PPO"""
        observations_batch, actions_batch, return_batch, masks_batch, \
        old_action_log_probs_batch, adv_targ = sample

        assert old_action_log_probs_batch.shape == (self.mini_batch_size, 1)
        assert adv_targ.shape == (self.mini_batch_size, 1)
        assert return_batch.shape == (self.mini_batch_size, 1)

        values, action_log_probs, dist_entropy = self.evaluate_actions(
            observations_batch, actions_batch)

        assert values.shape == (self.mini_batch_size, 1)
        assert action_log_probs.shape == (self.mini_batch_size, 1)
        assert values.requires_grad
        assert action_log_probs.requires_grad
        assert dist_entropy.requires_grad

        # [TODO] Implement policy loss
        policy_loss = None
        pass

        # [TODO] Implement value loss
        value_loss = None
        pass

        # This is the total loss
        loss = policy_loss + self.config.value_loss_weight * value_loss - self.config.entropy_loss_weight * dist_entropy

        return loss, policy_loss, value_loss, dist_entropy

    def update(self, rollout):
        # Get the normalized advantages
        advantages = rollout.returns[:-1] - rollout.value_preds[:-1]
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-5)

        value_loss_epoch = []
        policy_loss_epoch = []
        dist_entropy_epoch = []
        total_loss_epoch = []

        # Train for num_sgd_steps iterations (compared to A2C which only
        # train one iteration)
        for e in range(self.num_sgd_steps):
            data_generator = rollout.feed_forward_generator(advantages, self.mini_batch_size)

            for sample in data_generator:
                total_loss, policy_loss, value_loss, dist_entropy = self.compute_loss(sample)
                self.optimizer.zero_grad()
                total_loss.backward()
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.config.grad_norm_max)
                self.optimizer.step()

                value_loss_epoch.append(value_loss.item())
                policy_loss_epoch.append(policy_loss.item())
                total_loss_epoch.append(total_loss.item())
                dist_entropy_epoch.append(dist_entropy.item())

        return np.mean(policy_loss_epoch), np.mean(value_loss_epoch), \
               np.mean(dist_entropy_epoch), np.mean(total_loss_epoch)
