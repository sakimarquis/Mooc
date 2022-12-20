import gym

#%%

env = gym.make("Taxi-v3")
observation = env.reset()
agent = load_agent()

# %%
import gym
env = gym.make('CartPole-v0')
env.reset()
env.render() # display the rendered scene
action = env.action_space.sample()
observation, reward, done, info = env.step(action)
# %%
