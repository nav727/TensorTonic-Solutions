import torch
import torch.nn as nn


class CustomLinear(nn.Module):
    
    def __init__(self, in_features: int, out_features: int):
        super().__init__()

        # define params
        self.weight = nn.Parameter(nn.init.kaiming_uniform_(torch.empty(out_features, in_features)))
        self.bias = nn.Parameter(nn.init.normal_(torch.empty(out_features)))
        
        # below wont work
        # self.weight = np.zeros((out_features, in_features))
        # self.bias = np.zeros(out_features)

    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        # (batch, out_feature) = (batch, in_feature) x (in_feature, out_feature) + (out_feature)
        y = x @ self.weight.T + self.bias
        return y
