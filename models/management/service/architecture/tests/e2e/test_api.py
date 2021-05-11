"""
    Test API - Final cut 

    The API tests have no dependencies other than the API

    pytest -s test_api.py 
    Warning: Don't forget to launch the Postgres server 
"""
import uuid
import pytest
import requests
from datetime import date, timedelta

from architecture import config 

# ------------------------------------ Funcs ------------------------------------------
today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)
yesterday = today - timedelta(days=1)
before = today - timedelta(days=10)

# ------------------------------------ Test ------------------------------------------
#@pytest.mark.usefixtures('postgres_db') 
#@pytest.mark.usefixtures('restart_api')
def test_root_path_returns_201():
    print('\n\n* test_root_path_returns_201')
    url = config.get_api_url()
    print(url)
    r = requests.get(f'{url}/')
    print(r.status_code)
    print(r.json)
    assert r.status_code == 201 
    #assert r.json ()[ 'batchref' ] == earlybatch 


# ------------------------------------ Test ------------------------------------------
@pytest.mark.usefixtures('postgres_db') 
#@pytest.mark.usefixtures('restart_api')    # creates an empty flask_app.py 
def test_happy_path_returns_201():
    print('\n\n* test_happy_path_returns_201')
    url = config.get_api_url()
    print(url)
    datebegin = before.isoformat() 
    dateend = today.isoformat()
    delta = str(today - before)
    data = { 'datebegin': datebegin, 'dateend': dateend, 'delta': delta } 

    #r = requests.get(f'{url}/')
    r = requests.post(f'{url}/finance', json = data) 

    print(r.status_code)
    print(r.json)
    assert r.status_code == 201 
    #assert r.json ()[ 'batchref' ] == earlybatch 



