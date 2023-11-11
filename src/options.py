import os
from dotenv import load_dotenv

load_dotenv()
config = {

    "pinecone" : {
        "api_key" : os.environ["PINECONE_API"],
        "environment" : "gcp-starter",
        "index" : "image-stuff"
        }
}

