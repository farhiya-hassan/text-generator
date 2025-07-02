import random
def random_words(num_words, capitalize_random_words=False):
    '''
    Purpose: 
        To make some randomly generated text that looks like English.
    Parameter(s):
        num_words = number of words in the text (int)
        capitalize_random_words = what it says (bool), defaults to False
    Return Value:
        Returns a string of randomly generated words (str)
    '''
    # FIX: Find a way to add sentences. Right now, it's just one big sentence. ---- RESOLVED
    # FIX: Find a way to make it sound like actual words (Vowels?) ---- RESOLVED
    # FIX: Add random punctuation, not just periods ---- RESOLVED
    # FIX: Add paragraphs ---- 
    num_words += 1
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u'] # ignores 'y'
    average_length_of_a_word = 11 # It's 4.7 but I rounded it up and added some
    
    # gets a string with a lot of words
    output = [] 
    for word_index in range(num_words):
        word = ''
        num_letters = random.randrange(1, average_length_of_a_word // 2) # could get rid of the variable but I'm keeping it for clarity, plus accounts for num of vowels
        for letter in range(num_letters):
            word += random.choice(alphabet)
            vowel_or_no = random.choice([True, True, True, False]) # 1 in 3 chance of having a random vowel attached to the letter
            if vowel_or_no:
                word += random.choice(vowels)
        capitalize = random.choice([False, False, False, True]) # 1 in 5 chance of capitalizing a random word
        if capitalize_random_words and capitalize: # if we are capitaliing random words
            word = word.capitalize()
        if output == []: # AKA we're just now adding the first word, capitalizes anyways if random cap is false
            output.append(word.capitalize())
        elif word_index == num_words - 1: # AKA end of the sentence
            output.append(' ' + word + '.')
        else: # all other words
            output.append(' ' + word)
    
    # makes it into sentences, and then paragraphs.
    average_length_of_a_sentence = 20
    num_sentences_per_paragraph = random.randint(4,7) # average length of sentences, gets reset after each paragraph 
    num_sentences_in_current_paragraph = 0 # counts number of sentences until num_sentences_per_paragraph is reached 
    punctuation = ['.', '?', '!']

    word_index = 0
    while word_index < len(output):
        random_length_of_a_sentence = random.randint(10, average_length_of_a_sentence)
        put_punctuation = random.choice([True, True, False, True, True, True, True])
        put_punctuation_after_first_word = random.choice([False, False, True])
        if put_punctuation and put_punctuation_after_first_word:
            random_punctuation = random.choice([False, False, True])
            if random_punctuation:
                output[word_index] = output[word_index] + random.choice(punctuation) # random punctuation
                if (word_index + 1 < len(output)):
                    output[word_index + 1] = ' ' + output[word_index + 1][1:].capitalize() # weird logic just to capitalize the first letter of the first word after the puctuation
            else:
                output[word_index] = output[word_index] + '.' # a period
                if (word_index + 1 < len(output)):
                    output[word_index + 1] = ' ' + output[word_index + 1][1:].capitalize()
            
            # just made a sentence, so incrementing the count for that
            num_sentences_in_current_paragraph +=1
            # also, if num sentences per paragraph is reached, make it into a paragraph and reset
            if (num_sentences_in_current_paragraph == num_sentences_per_paragraph):
                output[word_index] += '\n\n'
                num_sentences_per_paragraph = random.randint(4,7)
                num_sentences_in_current_paragraph = 0
        
        word_index += random_length_of_a_sentence

    return ''.join(output)
def random_file(file_name, num_words, capitalize_random_words=False):
    '''
    Purpose: 
        Makes a randomly generated txt file of words, seperated into lines
    Parameter(s):
        file_name = the name of the file to be created. (str)
        num_words = argument for random_words(). Number of words in the file. (str)
        capitalize_random_words = argument used for random_words(). Whether or not to capitalize random words. Defaults to False. (bool)
    Return Value:
        None. Creates a new file instead.
    '''
    file_name = file_name + '.txt'
    with open(file_name, 'w') as fp:
        content = random_words(num_words, capitalize_random_words).split(' ')
        lines = []
        for i in range(0, len(content), 20):
            line = ' '.join(content[i:i+20])
            lines.append(line + '\n')
        fp.writelines(lines)       

if __name__ == "__main__":
    # testing the function 'random_words'
    print("Test 1:")
    print(" " + random_words(4, capitalize_random_words=True)) # four random words with the first word and random words capitalized and the last having a period.
    print("Test 2:")
    print(" " + random_words(4)) # same thing as above just no random words capitalized.
    print("Test 3:")
    print(" " + random_words(44)) # same as above, just a little longer.
    
    # testing the function 'random_file'
    random_file('one', 400) # creates a file with 400 randomly generated words with the name 'one'
    random_file('two', 700, True) # creates a file with 700 randomly generated words with the name 'two' and with having random words capitalized
    random_file('three', 10000, True) # creates a file with 10 thousand randomly generated and randomly capitalized words with the name 'three'