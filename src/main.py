import pinecone
from options import config

pinecone.init(
    api_key = config["pinecone"]["api_key"],
    environment = config["pinecone"]["environment"]
)