import requests
import db
#import sys

BASE = "http://127.0.0.1:7003/"

# Test 1 -- GET document data from ID 

documents = db.get_documents()
i = 1
while i < (len(documents)+1):
    response = requests.get(BASE + "documents/" + str(i))
    print("Output of id: ",str(i))
    print(response.json(), "\n")
    i += 1
