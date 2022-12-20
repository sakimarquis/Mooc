# Cross Entropy Method

How do we solve  for the policy optimization problem which is to **maximize** the total reward given some parametrized policy? 

## Discounted future reward

To begin with, for an episode the total reward is the sum of all the rewards. If our environment is stochastic, we can never be sure if we will get the same rewards the next time we perform the same actions. Thus the more we go into the future the more the total future reward may diverge. So for that reason it is common to use the **discounted future reward** where the parameter `discount` is called the discount factor and is between 0 and 1. 

A good strategy for an agent would be to always choose an action that maximizes the (discounted) future reward. In other words we want to maximize the expected reward per episode.

## Parametrized policy

A stochastic policy is defined as a conditional probability of some action given a state. A family of policies indexed by a parameter vector `theta` are called parametrized policies. These policies are defined analogous to the supervised learning classification or regression problems. In the case of discrete policies we output a vector of probabilities of the possible actions and in the case of continuous policies we output a mean and diagonal covariance of a Gaussian distribution from which we can then sample our continous actions.

## Cross entropy method (CEM)

So how do we solve for the policy optimization problem of maximizing the total (discounted) reward given some parametrized policy? The simplest approach is the derivative free optimization (DFO) which looks at this problem as a black box with respect to the parameter `theta`. We try out many different `theta` and store the rewards for each episode. The main idea then is to move towards good `theta`.

One particular DFO approach is called the CEM. Here at any point in time, you maintain a distribution over parameter vectors and move the distribution towards parameters with higher reward. This works surprisingly well, even if its not that effictive when `theta` is a high dimensional vector.

## Algorithm

The idea is to initialize the `mean` and `sigma` of a Gaussian and then for `n_iter` times we:

1. collect `batch_size` samples of `theta` from a Gaussian with the current `mean` and `sigma`
2. perform a noisy evaluation to get the total rewards with these `theta`s 
3. select `n_elite` of the best `theta`s into an elite set
4. upate our `mean` and `sigma` to be that from the elite set

## Discrete linear policy

For the `CartPole-v0` case let us define the linear parametrized policy as the following diagram:

```
         │               ┌───theta ~ N(mean,std)───┐
         │
   4 observations        [[ 2.2  4.5 ]
[-0.1 -0.4  0.06  0.5] *  [ 3.4  0.2 ]  + [[ 0.2 ]
         |                [ 4.2  3.4 ]     [ 1.1 ]]
         │                [ 0.1  9.0 ]]
         |                     W              b
    ┌────o────┐
<─0─│2 actions│─1─>    = [-0.4  0.1] ──argmax()─> 1
    └─o─────o─┘
```

Which means we can use the `Space` introspection of the `env` to create an appropriatly sized `theta` parameter vector from which we can use a part as the matrix `W` and the rest as the bias vector `b` so that the number of output probabilities correspond to the number of actions of our particular `env`.

## Extra noise

We can also add extra decayed noise to our distribution in the form of `extra_cov` which decays after `extra_decay_time` iterations.

## Discounted total reward

We can also return the discounted total reward per episode via the `discount` parameter of the `do_episode` function:

```python
...
for t in xrange(num_steps):
  ...
  disc_total_rew += reward * discount**t
  ...
```
