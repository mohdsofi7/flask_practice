from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Integer, String


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
db = SQLAlchemy(app)


class Todo(db.Model):
    SNo= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(200), nullable=False)
    desc= db.Column(db.String(500), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.datetime.now) 

    def __repr__(self)-> str:
        return f"{self.SNo}-{self.title}"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/show")
def products():
    allTodo = Todo.query.all()
    return "<p>This is product page which shows tables</p>"

@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

@app.route("/home")
def home():
    return "<p>This is my home page</p>"

@app.route("/update")
def update():
    return "<p>This is my home page</p>"


@app.route("/delete/<int")
def delete():
    allTodo = Todo.query.filter_by(SNO=SNO)
    db.session.delete(todo)
    return "<p>This is my home page</p>"




if __name__=="__main__":
    app.run(debug=True)