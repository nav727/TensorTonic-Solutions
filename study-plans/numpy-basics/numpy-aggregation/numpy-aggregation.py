import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    
    data = np.array(data, dtype='float64')

    mean_data = np.mean(data, axis=axis)
    std_data = np.std(data, axis=axis)
    min_data = np.min(data, axis=axis)
    max_data = np.max(data, axis=axis)
    
    combined = np.stack([mean_data, std_data, min_data, max_data])
    
    return combined