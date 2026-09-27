import torch
import torch.nn as nn


def train_with_scheduler(model: nn.Module, dataloader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer, scheduler: torch.optim.lr_scheduler.StepLR, num_epochs: int) -> dict:
    """
    Returns losses and lrs as lists of Python floats in a dictionary.
    """

    losses = []
    lrs = []
    
    model.train()

    for epoch in range(num_epochs):
        
        lrs.append(optimizer.param_groups[0]['lr'])
        running_loss = 0
        
        for batch_num, data in enumerate(dataloader):

            optimizer.zero_grad()
            
            X, y = data

            y_pred = model(X)

            loss = criterion(y, y_pred)
            running_loss += loss.item()
            loss.backward()

            optimizer.step()

        losses.append(running_loss / (batch_num + 1))
            
        scheduler.step()
        
    
    return {'losses': losses,
            'lrs': lrs}