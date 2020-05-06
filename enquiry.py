from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine('mysql://root:MyNewPass@localhost/airport')
db = scoped_session(sessionmaker(bind=engine))

def main():
    #Printing all the rows present in the table
    values = db.execute("SELECT id,origin,destination,time FROM flight").fetchall()
    for flights in values:
        print(f"Flight no {flights.id} from {flights.origin} to {flights.destination} in {flights.time}hrs")

    #To choose a flight
    fl_id = int(input("Enter the flight id"))
    func = db.execute("SELECT id,origin,destination,time from flight where id = :id",{"id":fl_id}).fetchone()

    if func is None:
        print("No such flight")
    #Getting the name of the passengers
    passen = db.execute("SELECT passengers_name from passengers where flight_id = :flight_id",{"flight_id" : fl_id})
    for data in passen:
        print(data.flight_id)
    if len(passen==0):
        print("No such passengers")


if __name__ == "__main__":
    main()


