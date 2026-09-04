def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    
    freq_counter = {}

    for sentence in sentences:
        for word in sentence:
            
            if word in freq_counter:
                freq_counter[word] += 1
            
            else:
                freq_counter[word] = 1
                
    return freq_counter