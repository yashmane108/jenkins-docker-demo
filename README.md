*simple real CI/CD practice project* using:

- Jenkins
- GitHub
- Docker
- AWS EC2 Service

This is a **basic CI/CD pipeline**.

# 1️⃣ Create Project Folder
On your local machine:

```bash
mkdir jenkins-docker-demo
cd jenkins-docker-demo
```
---

# 2️⃣ Create Simple Python App
Create file:
```bash
nano app.py
```
Add code in app.py:
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
return "Hello from Jenkins CI/CD Pipeline!"
if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)
```

# 3️⃣ Create Requirements File
```bash
nano requirements.txt
```
Add:
```text
flask
```

# 4️⃣ Create Dockerfile
```bash
nano Dockerfile
```
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

# 5️⃣ Test Docker Locally if you want else move next step 
If Docker installed:
```bash
docker build -t jenkins-demo .
docker run -p 5000:5000 jenkins-demo
```
Open browser:
```text
http://localhost:5000
```
You should see:
```text
Hello from Jenkins CI/CD Pipeline!
```

# 6️⃣ Push Project to GitHub
Create repo in GitHub.
Example repo name:
```
jenkins-docker-demo
```
Then push:
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/YOUR_USERNAME/jenkins-docker-demo.git
git push -u origin main
```

# 7️⃣ Install Docker, Jenkins on Server
On your EC2 server:
```
sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version 
```
```
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
  
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
```
```
sudo apt update
sudo apt install jenkins
```

```bash
sudo apt update
sudo apt install docker.io -y
```

Add Jenkins to docker group:
```bash
sudo usermod -aG docker jenkins
```

Restart Jenkins:
```bash
sudo systemctl restart jenkins
```

add 8080 port in ec2 instance with 0.0.0.0/0 in source 

before dashboard you will see unlock jenkins page that required administrator password to get that password follow given path of page copy that password and paste it there  
set useranme and password and login 

# 8️⃣ Create Jenkins Pipeline Job
In Jenkins dashboard:
click 
New Item

Name:
```
docker-demo-pipeline
```
Select:
Pipeline

# 9️⃣ Pipeline Script
Paste this in **Pipeline Script** section:

```groovy
pipeline {
agent any

stages {

    stage('Clone Repository') {
        steps {
            git branch: 'main', url: 'https://github.com/YOUR_USERNAME/jenkins-docker-demo.git'             
            
            # if your branch is main or any other instead of master then only add branch: 'main'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t jenkins-demo .'
        }
    }

    stage('Run Docker Container') {
        steps {
            sh 'docker run -d -p 5000:5000 jenkins-demo || true'
        }
    }

}
}
```
Replace:

```
YOUR_USERNAME
```
with your GitHub username.

---

# 🔟 Run Pipeline
Click:

```
Build Now
```
Jenkins will execute:

```
Clone repo
↓
Build Docker image
↓
Run container
```
---

# 1️⃣1️⃣ Test Application
Open browser:

```
http://EC2_PUBLIC_IP:5000
```


You should see:

```
Hello from Jenkins CI/CD Pipeline!
```
---

# Pipeline Architecture
Your DevOps pipeline now looks like:

```
Developer
│
▼
GitHub
│
▼
Jenkins Pipeline
│
▼
Docker Build
│
▼
Run Container
```
