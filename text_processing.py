def make_words_dict(list_of_words):
    word_dict = {}

    for word in list_of_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    max_frequent = max(word_dict, key = word_dict.get)
    min_frequent = min(word_dict, key = word_dict.get)

    return (word_dict, max_frequent, word_dict[max_frequent], min_frequent, word_dict[min_frequent])

def calculate_max_min_length(list_of_words):
    min_word = list_of_words[0]
    max_word = ''
    excluded_words = ['the', 'a', 'an']
    
    for word in list_of_words:
        if word not in excluded_words:
            if len(word) < len(min_word):
                min_word = word
            if len(word) > len(max_word):
                max_word = word

    return (min_word, len(min_word), max_word, len(max_word))