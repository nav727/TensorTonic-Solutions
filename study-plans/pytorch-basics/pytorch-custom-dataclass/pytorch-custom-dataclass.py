import torch
from torch.utils.data import Dataset
import numpy as np


class CSVDataset(Dataset):
    
    def __init__(self, data: list, label_col: int):
        
        data = torch.tensor(data, dtype=torch.float32)

        feature_cols_idx = [col_idx for col_idx in range(data.shape[1]) if col_idx != label_col]
        self.X = data[:, feature_cols_idx]
        self.y = data[:,[label_col]]
      
    def __len__(self) -> int:
        """
        Returns the number of rows.
        """
        return self.X.shape[0]

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Returns (features, label) as float32 tensors of shapes (D,) and (1,).
        """
        return (self.X[idx, :], self.y[idx, :])
