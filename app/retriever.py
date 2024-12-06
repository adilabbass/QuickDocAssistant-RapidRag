from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import os


class Retriever:
    def __init__(self, data_path="data/"):
        self.data_path = data_path

        # Initialize the SentenceTransformer model and embeddings
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Load documents and create FAISS vector store
        self.vectorstore = self._load_documents()

    def _load_documents(self):
        """Load and split documents, then create a FAISS index."""
        docs = []

        # Load all files from the specified directory
        loaders = [
            TextLoader(os.path.join(self.data_path, file))
            for file in os.listdir(self.data_path)
            if os.path.isfile(os.path.join(self.data_path, file))
        ]

        # Load and split documents using CharacterTextSplitter
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        for loader in loaders:
            loaded_docs = loader.load()  # Load the document as a string
            split_docs = splitter.split_documents(loaded_docs)  # Split into chunks
            docs.extend(split_docs)

        # Create FAISS index from the loaded documents
        return FAISS.from_documents(docs, self.embeddings)

    def get_relevant_docs(self, query, k=3):
        """Retrieve the top `k` relevant documents for a given query."""
        return self.vectorstore.similarity_search(query, k=k)
