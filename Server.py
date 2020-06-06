# based on code explained here: https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

from flask import Flask, jsonify, request
from WordSearchGenerator import WordSearchGenerator
# from WordSearchSolver import WordSearchSolver

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

wordList = [
  'hello',
  'world',
  'test'
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204


@app.route("/")
def hello_world():
  return "Hello, World!"


# @app.route('/wordSearch')
# def get_wordSearch():
#   return jsonify(incomes)


@app.route('/wordSearch') # TODO both are GETs?    , methods=['POST'])
def generate_WordSearch(): # TODO add params from front end - words to be used Replace wordList/WordSearchWords.txt
  global wordList # TODO delete once both generation and solver work. Replace with params
  wordSearchGenerator = WordSearchGenerator()
  return wordSearchGenerator.generateWordSearch(twoDimensional = True, wordList = wordList) # TODO make these the front end params 
