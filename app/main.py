from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Genesis @ " + datetime.utcnow().strftime("%H:%M:%S, %d/%m/%Y")

if __name__ == "__main__":
    app.run(host='0.0.0.0')