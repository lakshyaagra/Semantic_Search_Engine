import chromadb
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

DB_PATH = "./chroma_db"
COLLECTION_NAME = "knowledge_base"

model = SentenceTransformer(MODEL_NAME)

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)