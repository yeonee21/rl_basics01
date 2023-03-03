#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:46:27 2023

@author: yekim
"""

import gym

env = gym.make("CartPole-v1", render_mode='human')

observation, info = env.reset()

#env.render()

num_episodes = 1000

for i in range(num_episodes):
    
    
    for step in range(100):
        
        
        action = env.action_space.sample()     
        
        new_state, reward, done, _, info = env.step(action)
        
        
        if done:
            observation, info = env.reset()
    
env.close()