import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine('mysql://root:MyNewPass@localhost/airport')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("info.csv")
    reader = csv.reader(f)

    for origin,destination,time in reader:
        db.execute("INSERT INTO FLIGHT(origin,destination,time) VALUES(:origin,:destination,:time)",{"origin": origin,"destination":destination,"time":time})
        print(f"Added flights from {origin} to {destination} with travel time of{time}hrs")
        db.commit()

if __name__ == "__main__":
    main()

