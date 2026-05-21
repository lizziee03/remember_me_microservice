import requests
session = requests.Session()  # retain cookies between calls

# POST /remember - saves user/password
print("POST /remember")
response = session.post("http://localhost:5000/remember", json={"username": "testuser", "password": "testpass"})
print("Response:", response.json())

# GET /getcookie - returns the user/password cookies
print("\nGET /getcookie")
response = session.get("http://localhost:5000/getcookie")
print("Response:", response.json())

# POST /forget - deletes the user/password cookies
print("\nPOST /forget")
response = session.post("http://localhost:5000/forget")
print("Response:", response.json())
