import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    
    if method == 'zeros':
        result = torch.zeros(shape)
        
    elif method == 'ones':
        result = torch.ones(shape)

    elif method == 'full':
        result = torch.full(shape, value)

    return result.tolist()