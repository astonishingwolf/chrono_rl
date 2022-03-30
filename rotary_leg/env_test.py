# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:46:34 2022

@author: dasgu
"""

import rotary_leg_env
#import matplotlib.pyplot as plt
import numpy as np
env = rotary_leg_env.Model(True)
ac_dim = 1        
n_episodes = 1        
T=2
trajectories = []    
for episode in range(n_episodes):
    done = False
    env.reset()  
    while not done:
        env.step()    
    
    
    