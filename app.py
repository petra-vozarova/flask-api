from flask import Flask, jsonify, request
from flask import after_this_request
from flask_cors import CORS
from text_processing import (make_words_dict, calculate_max_min_length )
app=Flask(__name__)

CORS(app)

@app.route('/', methods =['POST'])

def start_processing():
    response = request.json
    if response:
        text = response['Text: ']
        cleared_text = ''
        for character in text:
            if character.isalnum() or character == ' ':
                cleared_text += character.lower()
        list_of_words = cleared_text.split()
        
        response['1. Number of Words: '] = len(list_of_words)
        (response['2. Shortest Word: '], 
        response['3. Length of the Shortest Word: '], 
        response['4. The Longest Word: '], 
        response['5. Length of the Longest Word: ']) = calculate_max_min_length(list_of_words)
        (response['Dictionary'], 
        response['6. The Most Frequently Used Word: '], 
        response['7. The Highest Frequency: '], 
        response['8. The Least Frequently Used Word: '], 
        response['9. The Lowest Frequency: ']) = make_words_dict(list_of_words)  
        return response
    return {'Error':'Unable to process the request. Please try again.'}

if __name__ == "__main__":
   app.run()