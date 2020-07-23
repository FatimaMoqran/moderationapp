import helper
from flask import Flask, request, Response, render_template, redirect, jsonify
import json
import os.path
import requests
from pprint import pprint
import time
import moderate


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/comment/new', methods=['POST'])
def add_comment():
    # Get comment from the POST body
    if request.method == "POST":
        req = request.form.to_dict()
        comment = req["comment"]
        response = moderate.moderate(comment)
        if response["Terms"]== None :
           texte = "Votre commentaire a été enregistré"
        elif  len(response["Terms"]) == 1:
            texte = "Votre commentaire a ete modéré à cause du mot {}".format(response["Terms"][0]['Term'])
        elif len(response["Terms"]) > 1:
            texte = "Votre commentaire a été supprimé !!"
        #return (response)
        return render_template("index.html",commentaire = comment, message = texte)

    
    req_data = request.get_json()
    comment = req_data['comment']
    res_data = helper.add_to_list(comment)

    if res_data is None:
        response = Response("{'error': 'comment not added - " + comment + "'}", status=400 , mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')

    return render_template("index.html")

@app.route('/comment/moderate', methods = ['POST'])
def moderate_text():
    data = request.get_json()
    text_input = data['text']
    response = moderate.moderate(text_input)
    return jsonify(response)

    
    