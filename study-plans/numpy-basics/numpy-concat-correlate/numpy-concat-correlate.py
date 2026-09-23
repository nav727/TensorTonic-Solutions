import numpy as np

def compare_correlations(a: list, b: list) -> np.ndarray:
    """
    Returns float64 correlation matrices for a, b, and their combined rows.
    """
    
    a = np.array(a, dtype='float64')
    b = np.array(b, dtype='float64')
    # using np.stack will be wrong here!
    combo = np.concatenate([a, b], axis=0)
    
    corr_a = np.corrcoef(a, rowvar=False)
    corr_b = np.corrcoef(b, rowvar=False)
    corr_combo = np.corrcoef(combo, rowvar=False)

    return np.stack([corr_a, corr_b, corr_combo], axis=0)