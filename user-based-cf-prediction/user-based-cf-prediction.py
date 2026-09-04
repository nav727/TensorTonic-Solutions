import numpy as np

def user_based_cf_prediction(similarities: list, ratings: list) -> float:
    """
    Returns the positive-similarity weighted rating prediction.
    """
    
    similarities = np.array(similarities, dtype='float64')
    ratings = np.array(ratings, dtype='float64')

    # Only users with positive similarity are considered
    similarities = np.where(similarities > 0, similarities, 0)

    # If no user has positive similarity, return 0.0
    deno = np.sum(similarities)
    if deno == 0:
        return 0.0
        
    # weighted by how similar they are to the target user
    recomm = np.sum(similarities * ratings) / deno
    
    return float(recomm)