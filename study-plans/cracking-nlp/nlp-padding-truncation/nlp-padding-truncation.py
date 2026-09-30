def pad_and_truncate(sequences: list, max_length: int, pad_value: int = 0) -> list:
    """
    Returns one integer list of length max_length per input sequence.
    """

    # dont modify the original input
    ans = []
    
    for idx in range(len(sequences)):
        
        curr_len = len(sequences[idx])
        curr_lst = sequences[idx]

        # truncate
        if curr_len > max_length:
            ans.append(curr_lst[0:max_length])

        # pad
        elif curr_len < max_length:
            pad_count = max_length - curr_len
            ans.append(curr_lst + [pad_value]*pad_count)

        else:
            ans.append(curr_lst)
    
    return ans
    