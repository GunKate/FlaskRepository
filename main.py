from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def food():

    return render_template("home.html", **context)

@app.route("/food/")
def foodGood():

    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()