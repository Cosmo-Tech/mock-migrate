import os

COSMOS_URI = os.environ.get("COSMOS_URI")
COSMOS_DB = os.environ.get("COSMOS_DB")
COSMOS_KEY = os.environ.get("COSMOS_KEY")
API_URL = os.environ.get("API_URL")
API_SCOPE = os.environ.get("API_SCOPE")

print(COSMOS_DB, COSMOS_KEY, COSMOS_URI, API_SCOPE, API_URL)
