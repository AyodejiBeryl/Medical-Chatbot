
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

system_prompt = (
    "You are a helpful medical assistant." 
    "Use the following retrieved context to answer the question at the end." 
    "If you don't know the answer, just say that you don't know, don't try to make up an answer."
    "Use three sentences maximum, and keep it concise."
    "\n\n"
    "{context}"
    )

prompt = ChatPromptTemplate.from_messages(
    [
    ("system", system_prompt),
    ("human", "Answer the following questions: {input}"),
]
)