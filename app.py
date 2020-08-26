from flask import Flask, jsonify, request
from flask import after_this_request
from flask_cors import CORS

app=Flask(__name__)

CORS(app)

@app.route('/', methods =['POST'])
def hello():
    response = request.json
    print(response)
    if response:
        text = response['Text: ']
        cleared_text =''
        for ch in text:
            if ch.isalnum() or ch == ' ':
                cleared_text += ch.lower()
        list_of_words = cleared_text.split()
        response['1. Number of Words: '] = len(list_of_words)
        response['2. Shortest Word: '], response['3. Length of the Shortest Word: '], response['4. The Longest Word: '], response['5. Length of the Longest Word: '] = max_min_length(list_of_words)
        response['Dictionary'], response['6. The Most Frequently Used Word: '], response['7. The Highest Frequency: '], response['8. The Least Frequently Used Word: '], response['9. The Lowest Frequency: '] = make_words_dict(list_of_words)
    # @after_this_request
    # def add_header(response):
    #     response.headers['Access-Control-Allow-Origin'] = '*'
    #     return response    
        return response
    return {'Error':'Unable to process the request. Please try again.'}

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

        
def max_min_length(list_of_words):
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

if __name__ == "__main__":
   app.run()