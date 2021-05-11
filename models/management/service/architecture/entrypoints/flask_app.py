"""
    Flask app 

    - Entrypoints are the places we drive our application from. 
    - In the official ports and adapters terminology, these are adapters too, 
    and are referred to as primary, driving, or outward-facing adapters. 

    export FLASK_APP=entrypoints/flask_app.py  
    export FLASK_ENV=development
"""
from flask import Flask, jsonify, request
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

#from datetime import datetime, timedelta
from datetime import date, timedelta

from architecture.adapters import repository 
from architecture import config
from architecture.domain import model

app = Flask(__name__)

# ------------------------------------ Funcs ------------------------------------------
get_session = sessionmaker(bind = create_engine(config.get_postgres_uri()))
today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)
yesterday = today - timedelta(days=1)
before = today - timedelta(days=10)


# ------------------------------------- Fake -----------------------------------------
class FakeRepository(repository.AbstractRepository):

    def __init__(self, batches): 
        self._batches = set(batches)    #self.session = session 
        
    def add(self, batch): 
        self._batches.add(batch)        #self.session.add(batch)
        
    def get(self, reference): 
        return next(b for b in self._batches if b.reference == reference)  #return self.session.query(model.Batch).filter_by(reference = reference).one()
        
    def list(self): 
        print('FakeRepository - List')
        return list(self._batches)      #return self.session.query(model.Batch).all()

    # Factory function 
    @staticmethod 
    def for_batch(ref, sku, qty, eta = None ):
        return FakeRepository([ model.Batch( ref, sku, qty, eta ), ]) 


# ------------------------------------- Fake -----------------------------------------
class FakeSession(): 
    committed = False     

    def commit(self):
        self.committed = True 


# ------------------------------------ Root ------------------------------------------
@app.route('/')
def index():
    print('*** root')
    return 'Hello, from ARCHITECTURE Flask API !', 201

@app.route('/hello')
def hello():
    print('*** hello')
    return 'Hello world !'

# ------------------------------------ Example from the Percival Gregory book ------------------------------------------
#@flask.route.gubbins 
@app.route("/finance", methods = ['POST'])
def build_finance_report():
    """
    Service layer in Flask 
    - We fetch some objects from the repository. 
    - We make some checks or assertions about the request against the current state of the world. 
    - We call a domain service. 
    - If all is well, we save/update any state we’ve changed.
    """
    print('*** build_finance_report')

    # Init from JSON request
    datebegin = request.json['datebegin']
    dateend = request.json['dateend']
    delta = request.json['delta']
    print(f'Begin: {datebegin}')
    print(f'End: {dateend}')
    print(f'Delta: {delta}')

    # Fetch from Repo
    
    session = get_session()
    print(f'Session: {session}')
    #repo, session = FakeRepository([]), FakeSession() 
    #repo = repository.SqlAlchemyRepository(session)     
    repo = FakeRepository([
        model.Order('order1', 'blue table', 5, before), 
        model.Order('order2', 'red table', 7, yesterday), 
        model.Order('order3', 'green table', 11, today)]
    )

    #orders = SqlAlchemyRepository.list(datebegin, dateend) 
    #orders = repo.list(datebegin, dateend) 
    orders = repo.list() 
    print(f'Orders: {orders}')
    print('Etas')
    for order in orders:
        print(order.eta)

    # Use business logic to build something
    #build_report(orders, datebegin, dateend) 
    #build_report(orders) 

    # Update
    #session.commit() 
    #return 201 
    return 'OK', 201 
