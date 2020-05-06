from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine('mysql://root:MyNewPass@localhost/airport')
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def index():
    planes = db.execute("SELECT * from flight").fetchall()
    return render_template("index.html",planes = planes)

@app.route("/book",methods=['POST'])
def book():
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("planes_id"))
    except ValueError:
        return render_template("error.html",message="ERROR 101")

    if db.execute("SELECT * FROM flight WHERE id = :id",{"id":flight_id}).rowcount == 0:
        return render_template("error.html",message="You have entered a wrong id")
    db.execute("INSERT INTO passengers(passenger_name,flight_id) VALUES(:name,:flight_id)",{"name":name,"flight_id":flight_id})
    db.commit()

    return render_template("success.html")
app.run(port=5000)