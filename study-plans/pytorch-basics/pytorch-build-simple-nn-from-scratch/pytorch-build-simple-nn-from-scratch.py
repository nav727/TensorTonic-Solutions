import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    """
    Returns: two-layer MLP output (linear -> ReLU -> linear)
    """

    def __init__(self, in_features, hidden_size, out_features):
        
        super().__init__()

        # create instances of components
        self.l1 = torch.nn.Linear(in_features, hidden_size)
        self.act1 = torch.nn.ReLU()
        self.l2 = torch.nn.Linear(hidden_size, out_features)
        

    def forward(self, x):
        
        # fix the sequence
        h_1 = self.l1(x)
        a_1 = self.act1(h_1)
        h_2 = self.l2(a_1)

        return h_2
        