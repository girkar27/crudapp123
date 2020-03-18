from flask import Flask
from sqlalchemy import create_engine



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # import pdb
    # pdb.set_trace()
    #students = Students.query.all()
    #std = None
    #if request.form:
    # std = Students(firstname=request.form.get("firstname"))
    # db.session.add(std)
    # db.session.commit()
    return render_template("hi")



if __name__ == "__main__":
    app.run(debug=True)