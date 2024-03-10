from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regex', methods=['POST'])
def regex():
    pattern = request.form['pattern']
    text = request.form['text']
    matches = []
    count = 0
    
    try:
        matches = re.findall(pattern, text)
        count = len(matches) 
        return render_template('index.html', pattern=pattern, text=text, matches=matches, count=count)
    except re.error:
        return render_template('index.html', error="Invalid regex pattern")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)