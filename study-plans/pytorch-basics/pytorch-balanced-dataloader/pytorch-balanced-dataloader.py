import torch
from torch.utils.data import DataLoader, TensorDataset, WeightedRandomSampler


def create_balanced_loader(features: torch.Tensor, labels: torch.Tensor, batch_size: int) -> DataLoader:
    """
    Returns a DataLoader with inverse-frequency sampling and replacement.
    """

    # counts for each label    
    count = torch.bincount(labels)

    # for inverse sampling
    proportions = 1 / count
    weights = proportions[labels]
    
    sampler = WeightedRandomSampler(weights=weights, num_samples=len(features), replacement=True)
    
    dataset = TensorDataset(features, labels)

    return DataLoader(dataset=dataset, batch_size=batch_size, sampler=sampler)
    
    