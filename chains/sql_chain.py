from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from db.queries import get_schema
from prompts.generate_sql import generate_sql_prompt
from llm.model import llm

sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | generate_sql_prompt
    | llm
    | StrOutputParser()
)
