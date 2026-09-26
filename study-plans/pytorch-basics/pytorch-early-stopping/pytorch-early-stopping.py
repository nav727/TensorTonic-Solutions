import torch
import torch.nn as nn
import math

def train_with_early_stopping(model: nn.Module, train_loader: torch.utils.data.DataLoader, val_loader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer, max_epochs: int, patience: int) -> dict:
    """
    Returns train_losses and val_losses as float lists, and stopped_epoch as an int.
    """
    
    train_losses = []
    val_losses = []
    prev_best_val_loss = math.inf
    patience_left = patience


    for epoch in range(max_epochs):

        running_loss = 0
        
        #### Train pass ####
        model.train()
        for batch_num, data in enumerate(train_loader):

            X, y = data
            
            # clear prev grads
            optimizer.zero_grad()

            y_pred = model(X)

            loss = criterion(y, y_pred)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        
        train_losses.append(running_loss / (batch_num + 1))

        
        #### validation pass ####
        model.eval()
        with torch.no_grad():

            for X, y in val_loader:
                y_pred = model(X)
                loss = criterion(y, y_pred).item()

                val_losses.append(loss)

        
        ## check early stopping due to non improvement
        if loss < prev_best_val_loss:
            prev_best_val_loss = loss
            patience_left = patience
        else:
            patience_left -= 1

        if patience_left <= 0:
            break
        
    return {"train_losses" : train_losses,
            "val_losses" : val_losses,
            "stopped_epoch" : len(val_losses)
           }
