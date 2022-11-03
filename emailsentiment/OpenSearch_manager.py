import pandas as pd
from opensearchpy.client import OpenSearch as OpenSearchClientType
from opensearchpy import  OpenSearch,RequestsHttpConnection, AWSV4SignerAuth
import boto3
from elasticsearch_dsl import Q,Search
import os
from dotenv import dotenv_values
from elasticsearch import Elasticsearch

def OpenSearchClient() -> OpenSearchClientType:
    """
    Output:
    -------
        - return OpenSearch connection client
    """
    env_values = dotenv_values(".env.config")

    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, env_values['AWS_REGION'])

    client = OpenSearch(
            hosts = [{'host': env_values['ELASTICSEARCH_URL'], 'port': env_values['ELASTICSEARCH_PORT']}],
            http_auth = auth,
            use_ssl = True,
            verify_certs = True,
            connection_class = RequestsHttpConnection
    )
    return client


from elasticsearch import Elasticsearch
client = OpenSearchClient()

response = client.search(
    index="quickmail",
    body={
      "size": 100,
        "query": {
            "term": {
                "event_name.keyword": {
                    "value": "reply"
                    }
                }
            }
        }
)

print(response)