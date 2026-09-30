import re


def text_normalize(text: str, operations: list) -> str:
    """
    Returns the normalized string
    """
    
    for operation in operations:
        
        if operation == "lowercase":
            text = text.lower()

        elif operation == "remove_punctuation":
            text = re.sub(r'[^\w\s]|_', '', text)

        elif operation == "remove_digits":
            text = re.sub(r'\d','',text)

        elif operation == "collapse_whitespace":
            text = re.sub(r"\s+",' ',text)

        elif operation == "strip":
            text = text.strip()
                        
    return text
    