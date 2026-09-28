import numpy as np

def winsorize(data: list, lo_q: float, hi_q: float) -> np.ndarray:
    """
    Returns float64 slices of clipped values, lower mask, and upper mask.
    """
        
    data = np.array(data, dtype=np.float64)

    # find value of lower and upper bound per column
    lb_val = np.percentile(data, lo_q, axis=0, keepdims=True)
    ub_val = np.percentile(data, hi_q, axis=0, keepdims=True)

    # clip to these lower and upper bounds
    clipped = np.clip(data, lb_val, ub_val)

    # lower and upper masks per cols
    lb_mask = np.where(data >= lb_val, 0.0, 1.0)
    ub_mask = np.where(data <= ub_val, 0.0, 1.0)
    
    return np.stack([clipped, lb_mask, ub_mask], axis = 0)
    