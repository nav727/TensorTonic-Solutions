import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    
    trace = 0
    
    for idx in range(len(A)):
        trace += A[idx][idx]
    
    return float(trace)