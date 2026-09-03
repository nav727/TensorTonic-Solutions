def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """

    pct_chnge = []
    for idx_i in range(1, len(series)):
        x_i, x_i_minus_1 = series[idx_i], series[idx_i - 1]
        
        if x_i_minus_1 == 0:
            pct_chnge.append(0.0)
        else:
            pct_chnge.append(float((x_i - x_i_minus_1) / x_i_minus_1))
            
    return pct_chnge