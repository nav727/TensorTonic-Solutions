import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows, cols = len(A), len(A[0])
    A_t = np.zeros(shape=(cols, rows))

    for r in range(rows):
        for c in range(cols):
            A_t[c][r] = A[r][c]
            
    return A_t
