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
class store(db.Model):
  __table__name = 'store'
  id: int
  storename:str
  productprice:str
  productname:str

  id = db.Column(db.Integer, primary_key=True)
  storename = db.Column(db.String(), nullable=False)
  productprice = db.Column(db.String(), nullable=False)
  productname = db.Column(db.String(), nullable=False)
  
  def __init__(initial,productname,storename,productprice):

    initial.storename = storename
    initial.productprice = productprice
    initial.productname = productname
    

  def format(initial):
    return {
      'storename':initial.storename,
      'productname': initial.productname,
      'productprice': initial.productprice,
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
    return "API for store"

@app.route("/add")
def add_logo():

    storename=request.args.get('storename')
    productprice=request.args.get('productprice')
    productname=request.args.get('productname')
    try:
        st=store(
            storename=storename,
            productprice=productprice,
            productname=productname,
        )
        db.session.add(st)
        db.session.commit()
        return "Store added."
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        sts=store.query.all()
        return  jsonify([e.serialize() for e in logos])
    except Exception as e:
	    return(str(e))

@app.route("/form")
def form():    
    return render_template("form2.html")

@app.route('/itemadd', methods = ['POST', 'GET'])
def stadd():
    if request.method == 'GET':
        return "This is the form to add items"
     
    if request.method == 'POST':
        storename = request.form['storename']
        productprice = request.form['productprice']
        productname = request.form['productname']
        new_item = store(storename=storename,productprice=productprice, productname=productname)
        db.session.add(new_item)
        db.session.commit()
        return f"Done!!"
"""
@app.route("/get/<name_>")
def get_by_productname(name_):
    try:
        name=store.query.filter_by(productname=name_).all()
        return name
        
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run(debug=True)


