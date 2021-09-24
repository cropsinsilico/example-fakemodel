import os
import numpy as np

exp_file = os.path.join('Output', 'expected.txt')
obs_file = os.path.join('Output', 'output.txt')

exp_data = np.genfromtxt(exp_file)
obs_file = np.genfromtxt(obs_file)

np.testing.assert_array_equal(exp_data, obs_file)
