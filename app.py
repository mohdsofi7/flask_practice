from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<p>WElcome to products page</p>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "<p>This is my home page</p>"

if __name__=="__main__":
    app.run(debug=True)