import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""

    X = np.array(X, dtype='float64')
    W = np.array(W, dtype='float64')

    linear_transform = X @ W
    norm = np.linalg.norm(linear_transform, axis=1)

    # get mask on row idx based on
    mask = (norm >= threshold)
    mask = mask[:, np.newaxis]

    # zero out based on mask
    return np.where(mask > 0, linear_transform, 0)