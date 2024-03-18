import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos import CosmosClient
import os
import json
import subprocess

subprocess.run(["./dbinit.sh", "arguments"], shell=True)

# URL = os.getenv('ACCOUNT_URI')
# KEY = os.getenv('ACCOUNT_KEY')
# client = CosmosClient(URL, credential=KEY)
client = CosmosClient.from_connection_string('AccountEndpoint=https://builtin-chicago.documents.azure.com:443/;AccountKey=JVo5kxxqB4lxWojaM8Ihi89WIh6MwJEx8an0OpSm37mIM8NF4JiXXzzp9Vyh05QDGaHGPE1yiceMACDbecJfXg==;')
DATABASE_NAME = "BuiltInChicagoDB"
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME = "BuiltInChicagoContainer"
container = database.get_container_client(CONTAINER_NAME)


# query = "SELECT * FROM BuiltInChicagoContainer"
# for item in container.query_items(query=query, enable_cross_partition_query=True, max_item_count=1):
#     print("*" * 20)
#     print(item)


# To update: id and categoryId need to match existing document, otherwise new doc will be created
container.upsert_item({
        "id": "FCF95DBC-BBAD-467B-9639-FC6E4EC42B4C",
        "categoryId": "4F34E180-384D-42FC-AC10-FEC30227577F",
        "categoryName": "Inserting 4",
        "sku": "Inserting 4",
        "name": "Inserting 4",
        "description": "Inserting 4",
        "price": "784.99",
        "tags": [
            {
                "id": "Inserting 4",
                "name": "Inserting 4"
            },
            {
                "id": "Inserting 4",
                "name": "Inserting 4"
            }
        ]
    }
)

# container.replace_item( "TEST 1", {
#         "id": "TEST 1",
#         "categoryId": "Inserting 4",
#         "categoryName": "Inserting 4",
#         "sku": "Inserting 4",
#         "name": "Inserting 4",
#         "description": "Inserting 4",
#         "price": "784.99",
#         "tags": [
#             {
#                 "id": "Inserting 4",
#                 "name": "Inserting 4"
#             },
#             {
#                 "id": "Inserting 4",
#                 "name": "Inserting 4"
#             }
#         ]
#     })



