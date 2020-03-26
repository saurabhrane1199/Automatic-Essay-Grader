from flask import Flask,render_template,request
from flask import jsonify
import pickle
import essay_grader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def recommend():
    f = request.files['file'] 
    score = f.read()
    score = str(score.strip())
    final_score = str(essay_grader.grade_score('1',score))
    return render_template("index.html",score=final_score)

if __name__ == '__main__':
    app.run(debug=False)