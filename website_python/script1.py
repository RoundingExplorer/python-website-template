from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/dev/')
def dev():
    return render_template("dev.html")

@app.route('/kidsunfold/')
def kidsunfold():
    return render_template("kidsunfold.html")

@app.route('/htmltryout/')
def htmltryout():
    return render_template("htmltryout.css")
if __name__ == '__main__':
    app.run(debug=True)
