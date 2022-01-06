from flask import Flask, request, jsonify,  render_template
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from json import dumps
from sqlalchemy.orm import class_mapper
app= Flask(__name__)


app.secret_key = 'hackathon'
#Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:hackathon@localhost/htn'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stbecmxjtvukzx:f4ce7b6da0c71f02e7fac1e9a3cfc76737c90a5b347f1dd6c8b484be2127281c@ec2-34-228-100-83.compute-1.amazonaws.com:5432/ddemlcjlr3s30h'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

@dataclass
class logoname(db.Model):
  __table__name = 'product'
  id: int
  companyname:str
  link:str
  productname:str

  id = db.Column(db.Integer, primary_key=True)
  companyname = db.Column(db.String(), nullable=False)
  link = db.Column(db.String, nullable=False)
  productname = db.Column(db.String(), nullable=False)

  def __init__(initial,link,productname,companyname):

    initial.productname = productname
    initial.link = link
    initial.companyname = companyname
    

  def format(initial):
    return {
      'companyname':initial.companyname,
      'productname': initial.productname,
      'link': initial.link,
    }

def serialize(model):
  # first we get the names of all the columns on your model
  columns = [c.key for c in class_mapper(model.__class__).columns]
  # then we return their values in a dict
  return dict((c, getattr(model, c)) for c in columns)

db.create_all()


"""
@app.route("/")
def hello():
    return "API for logoname"

@app.route("/add")
def add_logo():

    productname=request.args.get('productname')
    companyname=request.args.get('companyname')
    link=request.args.get('link')
    try:
        logo=logoname(
            productname=productname,
            companyname=companyname,
            link=link,
        )
        db.session.add(logo)
        db.session.commit()
        return "Logo added."
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        logos=logoname.query.all()
        return  jsonify([e.serialize() for e in logos])
    except Exception as e:
	    return(str(e))

@app.route("/form")
def form():    
    return render_template("form.html")

@app.route('/itemadd', methods = ['POST', 'GET'])
def logoadd():
    if request.method == 'GET':
        return "This is the form to add items"
     
    if request.method == 'POST':
        companyname = request.form['companyname']
        productname = request.form['productname']
        link = request.form['link']
        new_item = logoname(companyname=companyname,productname=productname, link=link)
        db.session.add(new_item)
        db.session.commit()
        return f"Done!!"
"""
@app.route("/get/<name_>")
def get_by_name(name_):
    try:
        name=logoname.query.filter_by(companyname=name_).all()
        return name
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run(debug=True)