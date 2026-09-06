import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    
    angles = np.array(angles)

    # angles should be in radians
    # convert to degrees using 
    sin_angles = np.sin(angles)
    cos_angles = np.cos(angles)
    tan_angles = np.tan(angles)

    combined = np.stack([sin_angles, cos_angles, tan_angles], dtype = 'float64')
    
    return combined