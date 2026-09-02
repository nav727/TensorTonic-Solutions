import numpy as np


def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """

    data = np.array(data, dtype='float64')
    m, n = data.shape
    
    if operation == 'flatten':
        # there is no np.flatten()
        return np.matrix.flatten(data)

    elif operation == 'transpose':
        return np.transpose(data)

    elif operation == 'add_batch':
        return np.reshape(data, shape=(1, m, n))
