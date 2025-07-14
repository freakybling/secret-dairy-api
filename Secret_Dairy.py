from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify("Hello!, welcome to test odf day 6.")

@app.route('/dairy', methods=["POST", "GET"])
def dai():
    if request.method == 'POST':
        auth = request.get_json()
        if auth.get("username") == "admin" and auth.get("password") == "secret123":
            return jsonify({"authorization": "Bearer diary-token-abc"}), 200
        else:
            return jsonify({"error" : "Invalid credentials"}), 401
   
    elif request.method == "GET":
        token = request.headers.get("authorization")
        if token == "Bearer diary-token-abc" :
            return jsonify({"message": "Welcome to your diary, Amer!"})
        else:
            return jsonify({"Error" : "Unauthorized"}), 401
    
    else:
        return "This is the note endpoint. Use POST to send a note."

@app.route('/diary-entry', methods=["POST"])
def diary_entry():
    token = request.headers.get("authorization")
    if token != "Bearer diary-token-abc":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    note = data.get("entry")

    if not note:
        return jsonify({"error": "No diary entry provided"}), 400

    return jsonify({
        "message": "Note saved!",
        "your_entry": note
    }), 201


if __name__ == '__main__':
    app.run(debug=True)