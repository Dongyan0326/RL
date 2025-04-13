import numpy as np 
import pandas as pd

np.random.seed(2)

N_STATES = 6
ACTIONS = ['left', 'right']
EPSILON = 0.9 # greedy policy
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13
FRESH_TIME = 0.3

def bulid_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),
        columns=actions
    )