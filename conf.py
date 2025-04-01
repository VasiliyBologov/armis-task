import os

from pydantic import BaseModel, Field
from dotenv import load_dotenv

class Config(BaseModel):
    crowdstrike_url: str = Field(
        description="CrowdStrike API endpoint for hosts"
    )
    qualys_url: str = Field(
        description="Qualys API endpoint for hosts"
    )
    api_token: str = Field(
        description="API authentication token"
    )
    mongo_url: str = Field(
        description="MongoDB connection URL"
    )
    mongo_db: str = Field(
        description="MongoDB database name"
    )
    crowdstrike_hosts_collection: str = Field(
        description="MongoDB collection name for crowdstrike hosts"
    )
    qualys_hosts_collection: str = Field(
        description="MongoDB collection name for qualys hosts"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def load_config() -> Config:
    load_dotenv(override=False)

    crowdstrike_url = os.getenv("CROWDSTRIKE")
    if crowdstrike_url is None or crowdstrike_url == "":
        raise Exception("CrowdStrike environment variable not set")
    qualys_url = os.getenv("QUALIS")
    if qualys_url is None or qualys_url == "":
        raise Exception("QUALIS environment variable not set")
    api_token = os.getenv("TOKEN")
    if api_token is None or api_token == "":
        raise Exception("API token not set")
    mongo_url = os.getenv("MONGO_URL")
    if mongo_url is None or mongo_url == "":
        raise Exception("MONGO_URL environment variable not set")
    mongo_db = os.getenv("MONGO_DB")
    if mongo_db is None or mongo_db == "":
        raise Exception("MONGO_DB environment variable not set")
    crowdstrike_hosts_collection = os.getenv("CROWDSTRIKE_COLLECTION")
    if crowdstrike_hosts_collection is None or crowdstrike_hosts_collection == "":
        raise Exception("CROWDSTRIKE_COLLECTION environment variable not set")
    qualys_hosts_collection = os.getenv("QUALIS_COLLECTION")
    if qualys_hosts_collection is None or qualys_hosts_collection == "":
        raise Exception("QUALIS_COLLECTION environment variable not set")

    return Config(
        crowdstrike_url=crowdstrike_url,
        qualys_url=qualys_url,
        api_token=api_token,
        mongo_url=mongo_url,
        mongo_db=mongo_db,
        crowdstrike_hosts_collection=crowdstrike_hosts_collection,
        qualys_hosts_collection=qualys_hosts_collection,
    )
