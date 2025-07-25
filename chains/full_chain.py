from chains.sql_chain import sql_chain
from chains.response_chain import response_chain
from db.queries import run_query, format_sql_response

def run_full_chain(question: str) -> str:
    sql_query = sql_chain.invoke({"question": question})
    sql_response = run_query(sql_query)
    formatted = format_sql_response(sql_response)

    return response_chain.invoke({
        "question": question,
        "sql_query": sql_query,
        "sql_response": formatted
    })
