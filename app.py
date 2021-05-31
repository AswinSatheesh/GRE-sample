from logging import debug
from flask import Flask, json, render_template, request, redirect, jsonify, redirect, url_for, flash


app=Flask(__name__)

PORT=3000
user_input="words.json"

@app.route('/')
def start():

    word_dict = get_json()

    return  render_template('index.html',json=word_dict["words"],len=len(word_dict["words"]))

def get_json():
    json_file=open(user_input)
    json_data= json.load(json_file)

    return json_data

if __name__=='__main__':
    app.run(host='0.0.0.0',port=PORT , debug=True)



