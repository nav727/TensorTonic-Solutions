import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    
    x = torch.tensor(x, dtype=torch.float32)

    # select your activation!
    if method == 'relu':
        activation = torch.nn.ReLU()
        
    elif method == 'sigmoid':
        activation = torch.nn.Sigmoid()

    elif method == 'tanh':
        activation = torch.nn.Tanh()

    elif method == 'leaky_relu':
        activation = torch.nn.LeakyReLU()

    z = activation(x)
    
    return z.tolist()
    