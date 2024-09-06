
from flask import Flask, jsonify, request
from flask_cors import CORS

from model import predict_text
from mysqlconnector import MySQL

# import dbconnector


app = Flask(__name__)
CORS(app)

# API for React
@app.route("/api/predict", methods =["POST"])
def predict():
    data = request.json # {user:, prompt:, }
    prompt = data.get("prompt")
    
    prediction = predict_text(prompt)

    response = "Human Text" if prediction == 0 else "AI Text"

    db = MySQL("root", "password", "localhost", "llmnouser")

    try:
        db.connect()

        query = "INSERT INTO PROMPTS (prompt, isGenerated) VALUES (%s, %s);"
        db.dml_query(query, (prompt, prediction))

        db.disconnect()
    except:
        print("Error")

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
