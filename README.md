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
