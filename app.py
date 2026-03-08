from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD Pipeline. github webhook. test 2. " \
    "changes from local and then push"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
