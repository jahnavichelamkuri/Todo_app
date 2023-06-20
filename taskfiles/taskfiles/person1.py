from pprint import pprint as pp
class Person:

    def __init__(self):
        
        self.name=input("\nName: ")
        self.age=int(input("Age: "))
        self.mobile=input("Mobile No.: ")
        self.email=input("Email: ")

    def __repr__(self):
        return f"(Name: {self.name} Age: {self.age} Mobile: {self.mobile} Mail: {self.email})"
    
class Flight:

    def __init__(self):
        self.flightid=input("flightd: ")
        self.airlines=input("airlines: ")
        self.source=input("source: ")
        self.destination=input("destination: ")
        self.num_rows=input("Num_rows: ")
        self.seats_per_row=input("seats_per_row: ")
        self.coach=input("coach: ")
        self.seats_available=input("available_seats: ")


    def __repr__(self):
        return f"({self.flightid}:{self.airlines}:{self.source}:{self.destination}:{self.num_rows}:{self.seats_per_row}:{self.coach}:{self.seats_available})"

class Ticket:

    def __init__(self):
        self.ticketid=input("ticketid: ")
        self.time=input("time: ")
        self.flightid=input("flightid: ")
        self.price=input("price: ")

    def __repr__(self):
        return f"({self.ticketid}:{self.time}:{self.flightid}:{self.price})"


class DataIngestion(Person,Flight,Ticket):
    def __init__(self):
        Person.__init__(self)
        Flight.__init__(self)
        Ticket.__init__(self)
    def __repr__(self):
        return f"(Name: {self.name} Age: {self.age} Mobile: {self.mobile} Mail: {self.email})({self.ticketid}:{self.time}:{self.flightid}:{self.price})({self.flightid}:{self.airlines}:{self.source}:{self.destination}:{self.num_rows}:{self.seats_per_row}:{self.coach}:{self.seats_available})"

personlist=[]

for i in range(0,2):
    obj=DataIngestion()
    personlist.append(obj)

pp(personlist)