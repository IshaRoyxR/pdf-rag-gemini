from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

def split_text(text: str):
    raw_chunks = splitter.split_text(text)

    chunks = []
    for i, chunk in enumerate(raw_chunks):
        chunks.append({
            "text": chunk,
            "page": i + 1  # fake page if real page not available
        })

    return chunks