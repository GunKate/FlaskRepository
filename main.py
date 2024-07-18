from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello World! Current date and time is: {current_time}"

@app.route("/new/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()