def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """

    # set membership is cheaper to compare
    stopwords = set(stopwords)
    ans = []
    for token in tokens:

        # retained tokens must remain in their original order
        if token not in stopwords:
            ans.append(token)
            
    return ans