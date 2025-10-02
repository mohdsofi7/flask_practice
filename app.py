from flask import Flask,render_template,request,redirect
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

@app.route("/update/<int:SNo>",methods=['GET', 'POST'])
def update(SNo):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(SNo=SNo).first()
        todo.title = title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/index")

    todo = Todo.query.filter_by(SNo=SNo).first()
    return render_template("update.html",todo=todo)


@app.route('/delete/<int:SNo>')
def delete(SNo):
    todo = Todo.query.filter_by(SNo=SNo).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/index")




if __name__ == "__main__":
    app.run(debug=True)