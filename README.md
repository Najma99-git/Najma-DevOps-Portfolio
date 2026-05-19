 HEAD
HEAD
# AWS EC2 Beginner Project

## Project Overview
This project demonstrates a **basic EC2 web server setup** with NGINX.  
- **EC2:** Virtual server (the manager)  
- **NGINX:** Web server (the receptionist)  
- **Goal:** Serve a simple “Hello World” webpage accessible publicly

## Steps Taken

### 1. Launch EC2 Instance
- Ubuntu 26.04 LTS
- t2.micro (free tier)
- Auto-assign public IP ✅
- Security group: SSH from my IP, HTTP from anywhere

![EC2 Instance](screenshots/1-ec2-instance.png)

### 2. Configure Security Group
- Allowed SSH and HTTP traffic

![Security Group](screenshots/2-security-group.png)

### 3. Connect via SSH
```bash
ssh -i ~/tango00.pem ubuntu@13.40.153.75

# Najma-DevOps-Portfolio
Portfolio of DevOps learning and projects
>>>>>>> origin/Najma99-git-patch-1

# Flask-Redis-Demo

A multi-container application demonstrating a **Python Flask web app** integrated with a **Redis database**, using Docker Compose. This project showcases containerization, environment setup, and basic web application state management using Redis.

---

## Objective

The goal of this assignment is to:

- Create a Flask web application.
- Use Redis to store and retrieve data (visitor counts).
- Containerize both the Flask app and Redis database using Docker and Docker Compose.
- Demonstrate understanding of multi-container orchestration and networking in Docker.

---

Flask-Redis-Demo/
│
├── app/ # Flask application source code
│ ├── app.py # Main Flask app
│ ├── requirements.txt # Python dependencies
│ └── Dockerfile # Dockerfile for Flask container
│
├── docker-compose.yml # Compose file defining services (Flask + Redis)
├── README.md # Project documentation
├── docs/ # Additional documentation (optional)
└── screenshots/ # Evidence of project output and logs



## Steps Completed

### Step 1: GitHub Sync
Ensured the local WSL terminal was synced with the remote GitHub repository to document progress:

```bash
cd ~/Najma-DevOps-Portfolio/Containers\ and\ Docker

Step 2 Project Setup

mkdir Flask-Redis-Demo
cd Flask-Redis-Demo
git init
git branch -m main

Step 3: Folder & File Structure

mkdir app docs screenshots
touch README.md docker-compose.yml

Step 4: Flask Application

cd app
touch app.py requirements.tx

Step 5: Docker Compose Setup

docker compose up --build

Step 6: Testing

Homepage: http://localhost:5000/
Visitor counter: http://localhost:5000/count



Key Commands:

docker compose up --build
docker compose up -d
docker ps
docker logs
docker compose down


71af5c3 (Add Flask-Redis-Demo assignment with Docker, Flask, and Redis)
