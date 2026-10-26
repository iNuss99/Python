import numpy as np

scores = np.array([-10, 25, 60, 85, 105, 70])
clipped = np.clip(scores, 0, 100)
print("18.2:", clipped)
print("18.3:", np.sum(scores < 0))
print("18.4:", np.sum(scores > 100))