"""
    Test API - Final cut 

    The API tests have no dependencies other than the API

    pytest -s test_api.py 
    Warning: Don't forget to launch the Postgres server 
"""
import uuid
import pytest
import requests

from architecture import config 

@pytest.mark.usefixtures('postgres_db') 
@pytest.mark.usefixtures('restart_api')
#def test_happy_path_returns_201():
def test_root_path_returns_201():
    print('\n\n* test_happy_path_returns_201')
    url = config.get_api_url()
    print(url)
    r = requests.get(f'{url}/')
    print(r.status_code)
    print(r.json)
    assert r.status_code == 201 
    #assert r.json ()[ 'batchref' ] == earlybatch 
