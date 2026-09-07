import numpy as np

def catalog_coverage(recommendations: list, n_items: int) -> float:
    """
    Returns the fraction of catalog items that were recommended.
    """
    
    if n_items == 0:
        return 0
        
    unique = set()
    for recommendation in recommendations:
        unique.update(recommendation)
    
    return len(unique) / n_items