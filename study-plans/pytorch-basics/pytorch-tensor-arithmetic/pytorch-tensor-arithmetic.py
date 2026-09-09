import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """

    # "float32" in string format will be an error
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    
    if op == 'add':
        z = x + y

    # Handle "matmul": matrix multiplication
    elif op == 'matmul':
        z = x @ y

    # Handle "power": element-wise exponentiation
    elif op == 'power':
        z = torch.pow(x, y)

    # Handle "max": element-wise maximum of both tensors
    elif op == 'max':
        z = torch.maximum(x, y)

    # Handle "multiply": element-wise multiplication
    elif op == 'multiply':
        z = torch.multiply(x, y)
    
    return z.tolist()