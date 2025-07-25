from db.database import db

def get_schema(_):
    return db.get_table_info()

def run_query(query):
    return db._execute(query)

def format_sql_response(response):
    if isinstance(response, list) and response and isinstance(response[0], dict):
        return ', '.join(f"{k}: {v}" for k, v in response[0].items())
    return str(response)
