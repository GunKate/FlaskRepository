# чтобы все работало, данный код должен быть скопирован в файл main в корневом каталоге
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template("index.html")

@app.route("/dlog/")
def page2():
    return render_template("blog.html")

@app.route("/contacts/")
def page3():
    return render_template("contacts.html")

@app.route("/datatime/")
def page():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello World! Current date and time is: {current_time}"


if __name__ == "__main__":
    app.run()