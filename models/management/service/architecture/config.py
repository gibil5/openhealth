"""
    Config
    
    Gets 
        Api url 
        Postgres uri
"""
import os

# ------------------------------------ Getters ------------------------------------------
def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5000
    return f"http://{host}:{port}"

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 5432
    password = os.environ.get("DB_PASSWORD", "abc123")
    user, db_name = "postgres", "cosmic"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
