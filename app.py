from flask import Flask, render_template, request
from pymongo import MongoClient
from user import User

app = Flask(__name__)
# MongoDB connection
client = MongoClient("mongodb+srv://coumbaka72_db_user:Jassmine17#@cluster0.cxyephq.mongodb.net/?tls=true&tlsAllowInvalidCertificates=true")
client.admin.command('ping')
db = client["healthcare_db"]
collection = db["survey"]

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        user = User(
            request.form["age"],
            request.form["gender"],
            request.form["income"],

            request.form["utilities_amount"],
            request.form["entertainment_amount"],
            request.form["school_amount"],
            request.form["shopping_amount"],
            request.form["healthcare_amount"]
        )

        data = user.to_dict()

        collection.insert_one(data)

        return "Data submitted successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
