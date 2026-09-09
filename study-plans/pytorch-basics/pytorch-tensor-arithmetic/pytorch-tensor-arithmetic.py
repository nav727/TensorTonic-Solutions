import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    
    if op == 'add':
        z = x + y
    
    elif op == 'matmul':
        z = x @ y

    elif op == 'power':
        z = torch.pow(x, y)

    elif op == 'max':
        z = torch.maximum(x, y)

    elif op == 'multiply':
        z = torch.multiply(x, y)
    
    return z.tolist()