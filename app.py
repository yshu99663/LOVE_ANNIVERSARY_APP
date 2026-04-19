from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/letters')
def letters():
    return render_template('letters.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/final')
def final():
    return render_template('final.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)