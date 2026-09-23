def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """

    text = text.strip()
    ans = []
    word = ''

    for ele in text:
        
        # check alphanumeric or underscore
        if ele.isalnum() or ele == '_':
            word += ele

        # preserve separate token
        # discard for whitespace
        else: 
            
            # discard if space
            # checking using --> ele != ' ' is the wrong way!
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

    # append the last token    
    if word != '':
        ans.append(word)
        
    return ans
