import os

config = {

    "pinecone" : {
        "api_key" : os.environ["PINECONE_API"],
        "environment" : "gcp-starter",
        "index" : "image-stuff"
        }
}

