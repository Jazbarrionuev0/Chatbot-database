from langchain_core.prompts import ChatPromptTemplate

generate_sql_prompt = ChatPromptTemplate.from_template("""
Based on the table schema below, write a plain SQL query for PostgreSQL (do NOT include markdown, code blocks, or explanations):
{schema}
Question: {question}
SQL query:
""")
