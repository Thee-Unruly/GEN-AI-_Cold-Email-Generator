import chromadb # import chromadb

chroma_client = chromadb.Client() # client

collection = chroma_client.create_collection(name="my_collection") # create a new collection

# add documents to the collection
collection.add(
    documents=[
        "This is a document about Snakes",
        "This is a document about Nyoks"
    ],
    ids=["id1", "id2"]
)

all_documents = collection.get()
all_documents

