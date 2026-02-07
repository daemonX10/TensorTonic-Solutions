import numpy as np
from collections import defaultdict

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    if len(y_train) == 0:
        return np.array([])

    mapp = defaultdict(int)
    for val in y_train:
        mapp[val] += 1

    max_freq = max(mapp.values())
    # deterministic tie-breaking: smallest label
    ans_class = min(k for k, v in mapp.items() if v == max_freq)

    return np.full(len(X_test), ans_class)
