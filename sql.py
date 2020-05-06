from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine('mysql://root:MyNewPass@localhost/airport')
db = scoped_session(sessionmaker(bind=engine))

def main():
    aflight = db.execute("SELECT origin,destination,time FROM flight").fetchall()
    for flights in aflight:
        print(f"{flights.origin} to {flights.destination} in {flights.time}hrs")

if __name__ == "__main__":
    main()


