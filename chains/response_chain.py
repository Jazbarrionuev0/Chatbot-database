from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from db.queries import get_schema
from prompts.generate_response import generate_response_prompt
from llm.model import llm

response_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | generate_response_prompt
    | llm
    | StrOutputParser()
)
