import torch

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Returns: tensor of shape (N, D), the batch-normalized output
    """
    
    X = torch.tensor(X, dtype=torch.float32)
    
    mu = torch.mean(X, axis=0)
    var = torch.var(X, axis=0, correction=0)

    normal_X = (X - mu) / torch.sqrt(var + eps)

    return normal_X * gamma + beta
