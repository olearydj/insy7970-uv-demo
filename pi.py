import numpy as np

N = 1_000_000
rng = np.random.default_rng(seed=7970)
xy = rng.random((N, 2))                     # N random points in the unit square
pi = 4 * ((xy**2).sum(axis=1) <= 1).mean()  # fraction inside the unit circle, times 4
print("pi is approximately", pi)
