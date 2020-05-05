from flask import Flask,render_template,request
from flask import jsonify
import essay_grader
import pandas as psd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def recommend():
    f = request.files['file'] 
    score = f.read()
    score = str(score.strip())
    setNo = request.form['set']
    final_score = str(essay_grader.grade_score(str(setNo),score))
    return render_template("index.html",score=final_score)

@app.route('/trainer')
def trainer():
    return render_template("trainer.html")

@app.route('/trainer', methods=['POST'])
def trainEssays():
    f = request.files['file']
    train = f.read()
    add_new_topic = pd.read_csv(('adding_essay_data.csv'), encoding='unicode_escape')

if __name__ == '__main__':
    app.run(debug=False,threaded=False)    