from flask import Flask, jsonify
from sqlalchemy import create_engine, MetaData
from flask import render_template
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from flask import request
from sqlalchemy.orm import sessionmaker
import json
#from flask import redirect



app = Flask(__name__)


engine = create_engine('mysql://root:@localhost/studentdatabase.db',echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
meta =  MetaData(bind=engine)

from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True) 
    firstname = Column(String(30))     
    lastname = Column(String(30))
    age = Column(Integer)

    def __repr__(self):
        return "<User(firstname='%s', lastname='%s', age='%d')>" % (self.firstname, self.lastname, self.age)

Base.metadata.create_all(engine)

@app.route("/", methods=["GET", "POST"])
def user1():

    firstname=request.form.get("firstname")
    lastname=request.form.get("lastname")
    age=request.form.get("age")
    user1 = Students(firstname=firstname, lastname=lastname, age=age)
    session.add(user1)
    session.commit()
    a = session.query(Students).all()
    return render_template("h1.html")
    


@app.route("/display/<int:id>", methods=["GET"])
def display(id):
    a = session.query(Students).filter(Students.id==id).first()
 
    return jsonify({"firstname":a.firstname,"lastname":a.lastname, "age":a.age})
  


@app.route("/update", methods=["GET","POST"])
def update():
    newfirstname = request.form.get("newfirstname")
    oldfirstname = request.form.get("oldfirstname")
    a = session.query(Students).filter_by(firstname=oldfirstname).first()
    a.firstname = newfirstname
    session.commit()


    newlastname = request.form.get("newlastname")
    oldlastname = request.form.get("oldlastname")
    b = session.query(Students).filter_by(lastname=oldlastname).first()
    b.lastname = newlastname
    session.commit()

    newage = request.form.get("new_age")
    oldage = request.form.get("old_age")
    c = session.query(Students).filter_by(age=oldage).first()
    c.age = newage
    session.commit()
    if request.form:
        return jsonify({"new_firstname": a.firstname,
            "new_lastname": b.lastname, "age":c.age})
    else:
        return render_template("h1.html")


    




@app.route("/display", methods=["GET"])
def display1():
    results = [{"id":a.id, "firstname":a.firstname,"lastname":a.lastname, "age":a.age} for a in session.query(Students).all()]
    
    return jsonify(results)

@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    
    a = session.query(Students).filter(Students.id==id).delete()
    session.commit()
    return ("User Deleted") 

    
    
if __name__ == "__main__":
    app.run(debug=True)