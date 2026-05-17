from pymongo import MongoClient
import csv

# MongoDB connection
client = MongoClient("mongodb+srv://coumbaka72_db_user:<password>@cluster0.cxyephq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Database and collection
db = client["healthcare_db"]
collection = db["survey"]

# Get all data from MongoDB
data = collection.find()

# Create CSV file
with open("survey_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # CSV headers
    writer.writerow([
        "age",
        "gender",
        "income",
        "utilities_amount",
        "entertainment_amount",
        "school_amount",
        "shopping_amount",
        "healthcare_amount"
    ])

    # Loop through data and write rows
    for user in data:
        writer.writerow([
            user.get("age"),
            user.get("gender"),
            user.get("income"),
            user.get("utilities_amount"),
            user.get("entertainment_amount"),
            user.get("school_amount"),
            user.get("shopping_amount"),
            user.get("healthcare_amount")
        ])

print("CSV file created successfully!")
