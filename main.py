from chains.full_chain import run_full_chain

question = "How many departments are and which are them?"
answer = run_full_chain(question)
print("Generated answer:\n", answer)
