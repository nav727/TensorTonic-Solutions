import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    
    result = [ele if ele >= 0 else (alpha * ele) for ele in x]
    return np.array(result)