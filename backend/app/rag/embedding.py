from langchain_community.embeddings import OllamaEmbeddings


def embed_texts(texts: list[str]):
    model = OllamaEmbeddings(model="nomic-embed-text")
    return model.embed_documents(texts)
