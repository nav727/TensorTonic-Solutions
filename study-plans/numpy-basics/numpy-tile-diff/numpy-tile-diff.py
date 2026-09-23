import numpy as np

def tile_diff(data: list, reps: int) -> np.ndarray:
    """
    Returns float64 slices of tiled values and next-row differences with a final zero row.
    """
    
    data = np.array(data, dtype='float64')

    tiled = np.tile(data, (reps, 1))
    diff = np.vstack([np.diff(tiled, axis=0), np.zeros(tiled.shape[1])])

    return np.stack([tiled, diff], axis=0)
