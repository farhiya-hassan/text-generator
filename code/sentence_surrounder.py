def surround_all_sentences(text, surrounding_character='"'):
    '''
    Purpose: 
        Takes a chunk of text in and returns the same text with all sentences surrounded by something without changing anything.
    Parameter(s):
        text = a string of containing sentences (str)
        surrounding_character = the surrounding character. Defaults to a double quote. (str)
    Return Value:
        the same text with the sentences surrounded (spaces between the sentences and the period of the last sentence remain outside the surrounding character). (str) 
    '''
    sentences = text.split('.')
    for i in range(len(sentences) - 1):
        sentences[i] += '.'
        if sentences[i][0] == ' ':
            sentences[i] = sentences[i][1:]
    sentences[0] = surrounding_character + sentences[0]
    sentences[-2] = sentences[-2] + surrounding_character
    return (surrounding_character + ' ' + surrounding_character).join(sentences[:-1]) # sentences[-1] is an empty string. 


if __name__ == '__main__':
    comment = 'takes in a chunk of text and returns the same text with all sentences surrounded by quotes or whatever without changing anything. Defaults to double quotes.'
    random = "People here and there. Three and two. WATER."
    print(surround_all_sentences(comment, surrounding_character='\''))
    print(surround_all_sentences(random))