def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """

    
    ans = []
    word = ''

    text = text.strip()
    for ele in text:
        
        # check alphanumeric or underscore
        # continue the token
        if ele.isalnum() or ele == '_':
            word += ele
    
        else: 
            
            # discard if space
            if ele.isspace():
                if word != '':
                    ans.append(word)
                word = ''
    
            # add punc separately
            else:
                if word != '':
                    ans.append(word)
                word = ''
                ans.append(ele)
    
    if word != '':
        ans.append(word)
        
    return ans
