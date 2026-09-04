import numpy as np


def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """

    # this won't work due to unequal lens
    # seqs = np.array(seqs)

    # If seqs is empty, return an array of shape (0, 0)
    if len(seqs) == 0:
        return np.empty(shape=(0, 0), dtype='int')
        
    result = []
    
    if max_len == None:
        all_lens = [len(seq) for seq in seqs]
        max_len = max(all_lens)
        
    # loop and extend
    for seq in seqs:
        
        # how much to pad?
        pad_len = max_len - len(seq)

        # If some sequences are shorter, pad them at the end with pad_value
        if pad_len > 0:
            result.append(seq + [pad_value] * pad_len)

        # If some sequences are longer than max_len, truncate them at the end
        elif pad_len < 0:
            result.append(seq[0 : max_len])

        else:
            result.append(seq)

        
    # Output must be a NumPy array of dtype int
    return np.array(result, dtype='int')
        