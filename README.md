# Healthcare Spending Survey Project

## Project Overview

The Healthcare Spending Survey Project is a web-based application developed using Python, Flask, and MongoDB. The application allows users to submit information related to their income and spending habits, especially healthcare-related expenses. The collected data is stored in a MongoDB database and can later be analyzed for business intelligence and healthcare market research.

This project was created as part of a data analysis and web development assignment focused on:

* Web application development using Flask
* Database integration with MongoDB Atlas
* Data collection and storage
* Data export and analysis
* Cloud deployment using AWS EC2

---

# Features

## User Survey Form

The application collects the following information from users:

* Age
* Gender
* Total Income
* Utilities Expenses
* Entertainment Expenses
* School Fees Expenses
* Shopping Expenses
* Healthcare Expenses

## MongoDB Database Integration

All submitted survey data is stored inside MongoDB Atlas.

## Data Export

The project includes functionality to export survey data into CSV format for further analysis.

## Data Analysis

The project contains data visualization and analysis files including:

* Age vs Income Chart
* Spending Categories Chart
* Jupyter Notebook Analysis

## Cloud Deployment

The application was deployed on AWS EC2 and configured with:

* Security Groups
* Flask server configuration
* External public access

---

# Technologies Used

| Technology       | Purpose                      |
| ---------------- | ---------------------------- |
| Python           | Backend programming language |
| Flask            | Web framework                |
| MongoDB Atlas    | Cloud database               |
| PyMongo          | MongoDB connection library   |
| HTML             | Frontend form page           |
| AWS EC2          | Cloud hosting                |
| Jupyter Notebook | Data analysis                |
| CSV              | Data export                  |

---

# Project Structure

```bash
healthcare-survey-project/
│
├── app.py
├── user.py
├── export_csv.py
├── survey_data.csv
├── analysis.ipynb
├── README.md
├── age_income_chart.png
├── spending_categories_chart.png
│
├── templates/
│   └── index.html
│
└── __pycache__/
```

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone <repository-url>
cd healthcare-survey-project
```

---

## 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

### Linux / MacOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install flask pymongo dnspython pandas matplotlib
```

---

# MongoDB Atlas Configuration

## 1. Create MongoDB Atlas Account

Visit:

[https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)

---

## 2. Create a Cluster

Create a free shared cluster.

---

## 3. Create Database User

Create a MongoDB database user with:

* Username
* Password
* Read and Write permissions

---

## 4. Add IP Address

Go to:

Security → Database & Network Access

Add:

```text
0.0.0.0/0
```

This allows external access to the cluster.

---

## 5. Update MongoDB Connection String

Inside `app.py`, update the MongoDB URI:

```python
client = MongoClient("your_mongodb_connection_string")
```

---

# Running the Application

## Start Flask Application

```bash
FLASK_APP=app.py flask run --host=0.0.0.0
```

The application will run on:

```text
http://127.0.0.1:5000
```

or

```text
http://your-public-ip:5000
```

---

# AWS EC2 Deployment

## Steps Performed

### 1. Launch EC2 Instance

* Ubuntu Server
* t3.micro instance

### 2. Configure Security Groups

Opened ports:

| Port | Purpose              |
| ---- | -------------------- |
| 22   | SSH                  |
| 80   | HTTP                 |
| 443  | HTTPS                |
| 5000 | Flask Application    |
| 8000 | File Download Server |

---

### 3. Connect to EC2

Using AWS EC2 Instance Connect.

---

### 4. Install Python Environment

```bash
sudo apt update
sudo apt install python3-pip python3-venv zip -y
```

---

### 5. Run Flask App

```bash
FLASK_APP=app.py flask run --host=0.0.0.0
```

---

# Screenshots

## Main Survey Interface

The application provides a healthcare spending survey form where users can input personal and spending information.

## Successful Submission

After submission, the data is successfully stored in MongoDB Atlas.

---

# Data Analysis

The project includes data analysis and visualization components.

## Age vs Income Analysis

Visualization file:

```text
age_income_chart.png
```

## Spending Categories Analysis

Visualization file:

```text
spending_categories_chart.png
```

## Jupyter Notebook

Analysis notebook:

```text
analysis.ipynb
```

---

# Future Improvements

Possible future enhancements include:

* User authentication system
* Dashboard and analytics page
* Advanced data visualization
* Machine learning prediction models
* Improved frontend design using Bootstrap or React
* REST API integration
* Docker deployment

---

# Challenges Faced

During the development and deployment process, several technical challenges were encountered:

* MongoDB Atlas SSL connection errors
* Flask template loading issues
* AWS Security Group configuration
* Public IP accessibility problems
* ZIP file export and download issues

These issues were resolved through debugging, proper configuration, and server management.

---

# Learning Outcomes

This project helped develop practical skills in:

* Flask web development
* MongoDB database integration
* Cloud deployment using AWS EC2
* Python backend programming
* Data collection and management
* Debugging and server configuration

---# Conclusion

The Healthcare Spending Survey Project demonstrates the integration of web development, cloud computing, and database management into a complete functional application. The project successfully collects, stores, and analyzes user spending data while being deployed on a cloud infrastructure.

This project highlights the practical use of Python technologies for healthcare-related market research and data analysis.

---

# Author

Coumba Ka

