import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import utils

from tqdm import tqdm

# TOOD:
#   Obtain all universities
#   Shuffle list of universities
#   Use ADM_RATE to get response from university
#   Run experiments to determine optimal threshold of universities to apply to based on ADM_RATE

if __name__ == "__main__":
    df = pd.read_csv('data/filtered-data.csv')
    univ = [()]

    NUM_CANDIDATES = 100    # number of universities
    NUM_EXPERIMENTS = 1000  # constant number of experiments to run

    solution_found_count = [0 for _ in range(NUM_CANDIDATES)]
    optimal_solution_found_count = [0 for _ in range(NUM_CANDIDATES)]
    
    for _ in tqdm(range(NUM_EXPERIMENTS)):
        candidates = [np.random.normal(loc=50, scale=10) for _ in range(NUM_CANDIDATES)]    # shuffle list of universities rather than creating new list
        optimal_candidate = max(candidates) # optimal based on heuristic function
        
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

    threshold = utils.find_peak(optimal_solution_found_count)[0] / NUM_CANDIDATES

