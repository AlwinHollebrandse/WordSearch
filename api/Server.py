# based on code explained here: https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

from flask import Flask, request
from WordSearchGenerator import WordSearchGenerator
from WordSearchSolver import WordSearchSolver

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

wordList = [
  'hello',
  'world',
  'test'
]

sampleWordSearchInfoJSON = '{"wordList": ["HELLO", "WORLD", "TEST"], "wordSearch": [[["X", "F", "N", "N", "R", "B", "C", "I"], ["D", "L", "R", "O", "W", "J", "U", "H"], ["T", "Q", "R", "R", "K", "P", "H", "V"], ["Q", "H", "F", "X", "V", "U", "X", "X"], ["P", "H", "N", "O", "H", "H", "T", "O"], ["R", "K", "Q", "E", "E", "E", "S", "W"], ["R", "L", "Q", "L", "L", "B", "E", "J"], ["P", "U", "L", "N", "H", "J", "T", "H"], ["M", "O", "N", "Y", "S", "Q", "C", "H"]]], "wordSearchDepth": 1, "wordSearchHeight": 9, "wordSearchWidth": 8}'

@app.route("/")
def hello_world():
  return "Hello, World!"


@app.route('/solveWordSearch')
def get_wordSearch():
  global sampleWordSearchInfoJSON
  wordSearchSolver = WordSearchSolver()
  return wordSearchSolver.solveWordSearch(wordSearchInfoJSON = sampleWordSearchInfoJSON) # TODO make these the front end params 


@app.route('/generateWordSearch') # TODO both are GETs?    , methods=['POST'])
def generate_WordSearch(): # TODO add params from front end - words to be used Replace wordList/WordSearchWords.txt
  global wordList # TODO delete once both generation and solver work. Replace with params
  wordSearchGenerator = WordSearchGenerator()
  return wordSearchGenerator.generateWordSearch(twoDimensional = True, wordList = wordList) # TODO make these the front end params 
