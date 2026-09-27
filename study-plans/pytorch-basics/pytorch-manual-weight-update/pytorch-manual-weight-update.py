import torch
import torch.nn as nn


def manual_train_step(model: nn.Module, X: torch.Tensor, y: torch.Tensor, criterion: nn.Module, lr: float) -> float:
    """
    Returns the pre-update batch loss as a Python float.
    """

    model.train()
    
    # get outputs from model
    y_pred = model(X)

    # calculate loss
    loss = criterion(y, y_pred)
    loss.backward()

    # update params
    with torch.no_grad():

        for param in model.parameters():
            param -= lr * param.grad

            param.grad.zero_()
                
    return float(loss.item())
    