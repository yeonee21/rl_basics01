#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:59:48 2023

@author: yekim


Frozen lake involves crossing a frozen lake from Start(S) to Goal(G) without falling into any Holes(H) by walking over the Frozen(F) lake. 
The agent may not always move in the intended direction due to the slippery nature of the frozen lake.

-----------------
Action space
-----------------
0: LEFT

1: DOWN

2: RIGHT

3: UP


------------------
Reward schedule
------------------

Reach goal(G): +1

Reach hole(H): 0

Reach frozen(F): 0


"""


import gym
import matplotlib.pyplot as plt



env = gym.make("FrozenLake-v1", render_mode='human')

observation, info = env.reset()


num_episodes = 1000

steps_total = []


for i in range(num_episodes):
    
    
    step = 0
        
    while True:
        
        step += 1
        
        action = env.action_space.sample() # left(0) or right(1) 
        
        new_state, reward, done, _, info = env.step(action)
        
        #print(new_state) # Observation space: [Cart Position, Cart Velocity, Pole Angle, Pole Angular Velocity] 
        #print(info)
        
        time.sleep(0.4)
        
        env.render()
        
        if done:
            steps_total.append(step)
            print(f"{i} Episode finished after {step} steps")
            observation, info = env.reset()
            break


print("Average number of steps: %.2f" % (sum(steps_total)/num_episodes))
plt.plot(steps_total)
plt.show()

env.close()