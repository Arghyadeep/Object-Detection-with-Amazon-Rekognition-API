from flask import Flask, render_template, request
from driver import create_strings


app = Flask(__name__)
app.config['SECRET_KEY']

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/", methods =['POST'])
def result():
	url = request.form['text']
	label,face,celeb = create_strings(url)
    #processed_text = text.upper()
	return render_template("result.html",text0 = url, text1 = label, text2 = face, text3 = celeb)

if __name__ == "__main__":
	app.run(debug=True)

