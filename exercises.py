import numpy as np
import random
import math
from multiparameter_landscape import multiparameter_landscape
from helper_functions import normalise_filter, Compute_Rivet
from multiparameter_landscape_plotting import compute_mean_landscape, plot_multiparameter_landscapes

def sample_circle(n=100, epsilon=0):
  return np.array([
    [math.cos(r)+random.uniform(-epsilon, epsilon), math.sin(r)+random.uniform(-epsilon, epsilon)] for r in [random.uniform(0, 2*np.pi) for _ in range(n)]
  ])