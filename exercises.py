import numpy as np
import random
import math
from mpl_toolkits import mplot3d

from multiparameter_landscape import multiparameter_landscape
from helper_functions import normalise_filter, Compute_Rivet
from multiparameter_landscape_plotting import compute_mean_landscape, plot_multiparameter_landscapes

def sample_circle(n=100, epsilon=0):
    ''' Generate n random points on a circle with noise epsilon. '''
    return np.array([
    [math.cos(r)+random.uniform(-epsilon, epsilon), math.sin(r)+random.uniform(-epsilon, epsilon)] for r in [random.uniform(0, 2*np.pi) for _ in range(n)]
    ])

def add_sp_noise(X, n=50):
    ''' Add salt and pepper noise to the dataset X. '''
    mx = np.max(X, axis=0)
    mn = np.min(X, axis=0)
    for i in range(n):
        x = np.random.rand(mx.shape[0])
        p = np.asarray([mn[i]+(x[i]*(mx[i]-mn[i])) for i in range(mx.shape[0])])
        X = np.vstack((X, p))
    return X

def add_local_noise(X, amplitude=2):
    ''' Add local Gaussian noise to dataset X. '''
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            X[i, j] *= math.exp((-1 if random.random()<0.5 else 1)*random.random())/amplitude
    return X

def plot_critical_points(X, point_lables=None):
    if not point_lables:
        point_lables = [1 for _ in X]
    xs = X[:, 0]
    ys = X[:, 1]
    fig = plt.figure()
    if X.shape[1] == 2:
        plt.plot(X[:, 0], X[:, 1], '*')
    else:
        ax = fig.add_subplot(projection='3d')

        zs = X[:, 2]
        ax.scatter(xs, ys, zs, c=point_lables)
    
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
