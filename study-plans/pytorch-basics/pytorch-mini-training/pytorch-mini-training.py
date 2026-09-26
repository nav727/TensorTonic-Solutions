import torch
import torch.nn as nn


def train_epoch(model: nn.Module, dataloader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer) -> float:
    """
    Returns the mean batch loss as a Python float
    """

    running_loss = 0
    model.train()
    
    # loop on whole dataset
    EPOCHS = 1
    for epoch in range(EPOCHS):

        # loop on curr batch
        for batch_num, data in enumerate(dataloader):

            input, y = data
            
            # clear prev grads
            optimizer.zero_grad()
            
            # make pred
            y_pred = model(input)
            
            # calculate curr loss
            loss = criterion(y, y_pred)
            
            # get grads
            loss.backward()
            
            # update weights        
            optimizer.step()

            running_loss += loss.item()


    return running_loss / (batch_num + 1)
