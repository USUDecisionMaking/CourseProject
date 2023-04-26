import random

import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def find_peak(array):
    index = 0
    max = 0

    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            index = i

    return index, max

def get_response(probability):
    if random.random() > probability:
        return True
    else:
        return False

def find_optimal_threshold():
    NUM_CANDIDATES = 100
    NUM_EXPERIMENTS = 1000

    solution_found_count = [0 for _ in range(NUM_CANDIDATES)]
    optimal_solution_found_count = [0 for _ in range(NUM_CANDIDATES)]
    
    for _ in tqdm(range(NUM_EXPERIMENTS)):
        candidates = [np.random.normal(loc=50, scale=10) for _ in range(NUM_CANDIDATES)]
        optimal_candidate = max(candidates)
        
        for i in range(1, NUM_CANDIDATES):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    solution_found_count[i] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[i] += 1

                    break

    plt.plot(optimal_solution_found_count, label='Normal Optimal Solutions')
    plt.title("General Stopping Optimum Threshold")
    plt.legend()
    plt.show()

    return find_peak(optimal_solution_found_count)[0] / NUM_CANDIDATES
