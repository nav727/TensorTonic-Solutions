import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    
    values = torch.tensor(values, dtype=torch.float32, requires_grad=True)

    z = (torch.pow(values, 3) + 2 * values).sum()
    z.backward()
    return values.grad.tolist()
