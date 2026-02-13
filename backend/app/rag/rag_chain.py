from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.rag.vector_store import get_vector_store


def run_rag(question: str) -> str:
    vectordb = get_vector_store()
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join(d.page_content for d in docs)

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful assistant.
Answer the question ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""
    )

    llm = Ollama(model="llama3")

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke({
        "context": context,
        "question": question
    })
