import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    
    x = torch.tensor(x, dtype = torch.float32)

    if op == 'flatten':
        z = torch.flatten(x)

    elif op == 'squeeze':
        z = torch.squeeze(x)

    elif op == 'transpose':
        z = x.T
        
    return z.tolist()
