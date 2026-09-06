def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed size token chunks with the requested overlap
    """
    
    chunks = []

    window_start = 0
    window_end = 0
    while window_end < len(tokens):

        window_end = min(window_start + chunk_size, len(tokens))
        chunks.append(tokens[window_start : window_end])
        window_start = window_end - overlap
        
    return chunks
    