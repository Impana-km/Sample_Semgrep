from flask import Flask, request
import sqlite3
import os
import subprocess

app = Flask(__name__)

# 1️⃣ SQL Injection Vulnerability
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    result = conn.execute(query).fetchall()
    return str(result)


# 2️⃣ Command Injection Vulnerability
@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.getoutput("ping -c 1 " + host)


# 3️⃣ Debug Mode Enabled (Security Risk)
if __name__ == "__main__":
    app.run(debug=True)
