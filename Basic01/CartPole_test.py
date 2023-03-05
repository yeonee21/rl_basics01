#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:46:27 2023

@author: yekim

The goal is to balance the pole by applying forces in the left and right direction on the cart.

"""

import gym
import matplotlib.pyplot as plt



env = gym.make("CartPole-v1", render_mode='human')

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
        
        #env.render()
        
        if done:
            steps_total.append(step)
            print(f"{i} Episode finished after {step} steps")
            observation, info = env.reset()
            break


print("Average number of steps: %.2f" % (sum(steps_total)/num_episodes))
plt.plot(steps_total)
plt.show()

env.close()