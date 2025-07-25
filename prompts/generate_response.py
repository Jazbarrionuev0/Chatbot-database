from langchain_core.prompts import ChatPromptTemplate

generate_response_prompt = ChatPromptTemplate.from_template("""
You are a helpful data assistant.

Given the schema, user question, SQL query, and SQL result below, answer ONLY using the SQL result. Do NOT assume anything. Just interpret the SQL result to answer the question in natural language.

Schema:
{schema}

Question:
{question}

SQL query:
{sql_query}

SQL result:
{sql_response}

Answer:
""")
