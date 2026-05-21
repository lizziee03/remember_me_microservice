from flask import *

app =  Flask(__name__) # Starts the flask instance

# Remember route endpoint
@app.route('/remember', methods=['POST']) # Defining the endpoint

def set_cookie():
    """Retrieves the provided JSON user/password data and converts
    it into a cookie for persistent storage."""

    try:    # Error handling in case of malformed/missing data
        data = request.get_json()       # Converts the request data into a dictionary

        response = make_response(jsonify({"status": "cookies created"}))

        response.set_cookie("username", data["username"],
                            max_age=2592000, httponly=True, samesite="Lax") # Sets a new cookie with the username field
        response.set_cookie("password", data["password"],
                            max_age=2592000, httponly=True, samesite="Lax") # Both expire in 30 days

        return response

    except Exception:
        return make_response(jsonify({"status": "error", "message": "invalid data"})), 400

# Forget route endpoint
@app.route("/forget", methods=['POST'])

def forget():
    """Removes a specified user/password cookie"""
    try:
        response = make_response(jsonify({"status": "cookies deleted"}))

        response.delete_cookie("username")  # Deletes the username and password cookies
        response.delete_cookie("password")

        return response

    except Exception:
        return make_response(jsonify({"status": "error", "message": "could not delete cookies"})), 500

# GetCookie route endpoint
@app.route("/getcookie", methods=['GET'])

def get_cookie():
    """Returns the relevant user/password info when provided
    with the relevant user cookie."""
    username = request.cookies.get("username", "")  # Returns default empty string if no cookie found
    password = request.cookies.get("password", "")

    return {"username": username, "password": password} # Returns the cookie data as a JSON object

if __name__ == '__main__':      # Run the server on start at port 5000 (http://localhost:5000)
    app.run(port=5000)