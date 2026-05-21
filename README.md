# RememberMe Microservice

Microservice written with the Flask library that stores a provided username and password in cookies to allow for autofill functionality, running on `http://localhost:5000`.

Three endpoints are provided

`/remember` : POST : Saves the username & password as cookies
`/getcookie`: GET : Returns the saved cookies
`/forget` : POST : Deletes the saved cookies

## Requesting data

Requests for login data are made over HTTP using a locally hosted REST API. Cookies need to remain persistent between calls, as the microservice does not store them locally. Recommended to use `requests.Session()` to this effect.

```
import requests
session = requests.Session()

# Saving credentials
session.post("http://localhost:5000/remember", json={"username": "user", "password": "password"})

# Reading credentials back
session.get("http://localhost:5000/getcookie")

# Delete credentials
session.post("http://localhost:5000/forget")
```

## Receiving data

All endpoints return JSON. Recommended to handle the JSON object through `response.json()`.

```
response = session.get("http://localhost:5000/getcookie")

data = response.json()

print(data["username"], data["password"])
```
# Remember Me Microservice

Microservice written with the Flask library that stores a provided username and password in cookies to allow for autofill functionality, running on `http://localhost:5000`.

Three endpoints are provided

`/remember` : POST : Saves the username & password as cookies
`/getcookie`: GET : Returns the saved cookies
`/forget` : POST : Deletes the saved cookies

## Requesting data

Requests for login data are made over HTTP using a locally hosted REST API. Cookies need to remain persistent between calls, as the microservice does not store them locally. Recommended to use `requests.Session()` to this effect.

```
import requests
session = requests.Session()

# Saving credentials
session.post("http://localhost:5000/remember", json={"username": "user", "password": "password"})

# Reading credentials back
session.get("http://localhost:5000/getcookie")

# Delete credentials
session.post("http://localhost:5000/forget")
```

## Receiving data

All endpoints return JSON. Recommended to handle the JSON object through `response.json()`.

```
response = session.get("http://localhost:5000/getcookie")

data = response.json()

print(data["username"], data["password"])
```
<img width="553" height="616" alt="Screenshot 2026-05-21 164749" src="https://github.com/user-attachments/assets/cd8d8b00-e9ee-4f34-aaae-01e5a4fb4ee6" />
