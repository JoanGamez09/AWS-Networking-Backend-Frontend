# Project: EC2 Instances with Public and Private Subnet Setup

This project involves a network setup where two **Amazon EC2 instances** are deployed within the same **Virtual Private Cloud (VPC)**. One EC2 instance is located in a **public subnet**, while the other resides in a **private subnet**. The EC2 instance in the private subnet connects to an **RDS database**, and the public EC2 instance fetches data from the database via an API. The fetched data is then displayed on a website served by **Nginx** on the public EC2 instance.

## Architecture Overview

- **VPC**: A Virtual Private Cloud (VPC) that includes both public and private subnets.
- **Public Subnet EC2 Instance**: This instance hosts an **Nginx web server** that displays information fetched from the private EC2 instance.
- **Private Subnet EC2 Instance**: This instance is used for **connecting to the RDS database** and fetching the data.
- **RDS Database**: A managed database service (MySQL).
- **API**: The public EC2 instance communicates with the private EC2 instance via an API to retrieve the data from the RDS database.

![image](https://github.com/user-attachments/assets/785017ee-ae95-4a54-a74e-f393a4f7e573)

  

## Resources Deployed

- **VPC** with public and private subnets.
- **Two EC2 instances**: One in a public subnet and the other in a private subnet.
- **RDS Database** (MySQL).
- **Nginx Web Server** running on the public EC2 instance.
- **Security Groups** to control the traffic between EC2 instances and RDS.

## Steps to Deploy

### 1. **Create VPC, Subnets, and Security Groups**

In this step, we will create the **Virtual Private Cloud (VPC)**, configure two **subnets** (public and private), and set up **Security Groups** to control the access between resources. The goal is to create a secure and isolated network environment where the public and private instances can communicate but follow the necessary security protocols.


- **VPC**: Create a VPC with CIDR block.
  ![image](https://github.com/user-attachments/assets/61bcbbe7-470f-4421-bc84-73f431a4805a)
  ![image](https://github.com/user-attachments/assets/e8f764e7-0402-49fa-aeb4-2580c475eaf5)

- **Subnets**: Create two subnets:
  - **Public Subnet** with **auto-assign public IP** enabled.
  - **Private Subnet** without a public IP.
- **Internet Gateway**: Attach an Internet Gateway to the VPC for public internet access.
- **Route Tables**: 
  - Public Route Table should route traffic to the Internet Gateway.
  - Private Route Table should route traffic through a **NAT Gateway** for internet access.

### 2. **Launch EC2 Instances**

#### Public EC2 Instance:
- Launch an EC2 instance in the VPC created and the public subnet.
- Ensure this instance has a **public IP** and **Security Group** allowing HTTP/HTTPS access and SSH access from your IP.
- The instance should generate a new key pair in .pem format to be able to connect via SSH.
- When connected, perform sudo **apt-get update** and **sudo apt-get upgrade**.
- Install **Nginx** on the EC2 instance with **sudo apt install nginx**.
- Configure Nginx to serve the website which will display the data from the private EC2 instance with **sudo nano /etc/nginx/sites-available/default** (Public Instance/config_public.config).

#### Private EC2 Instance:
- Launch an EC2 instance in the private subnet and the private subnet.
- This instance should have a **private IP**.
- Configure the **Security Group** to allow access from the public EC2 instance and ensure it can connect to the RDS instance.
- The instance should generate a new key pair in .pem format to be able to connect via SSH.
- When connected, perform sudo **apt-get update** and **sudo apt-get upgrade**.
- Install **Nginx** on the EC2 instance with **sudo apt install nginx**.
- Configure Nginx to serve the website which will display the data from the private EC2 instance with **sudo nano /etc/nginx/sites-available/default** (Private Instance/config_private.config).
- Create a virtual environment for Python and, install Flaskand and Flask CORS . 
- Create a **main.py** file with **sudo nano /home/USER/main.py** (Public Instance/config_public.config). This is for set up the API to interact with the RDS instance and fetch data.
- After done setting both files you must restart Nginx with **sudo systemctl restart nginx**.
- Finally, run your main.py file with **python3 main.py**
![image](https://github.com/user-attachments/assets/21478d68-eae1-43ef-94b1-66e11fcc2488)


### 3. **Set Up RDS Database**

- If you are going to create or select an existing **RDS Database instance**, make sure it is in the same VPC.
- Make sure the RDS instance is in a **private subnet** and is accessible from the private EC2 instance.
- Configure database security groups to allow inbound connections from the private EC2 instance on the appropriate port (e.g., 3306 for MySQL).

### 4. **Connect Public EC2 to API**
- In this step, the public EC2 instance will serve an **HTML file** that fetches data from the API running on the private EC2 instance.
  
#### **Create the HTML File on the Public EC2 Instance**
- Create the html file with **sudo vi /var/www/html/index.html** and edit it to fecth the API data (Public Instance/index.html)
- Ensure the security group allows communication between the public EC2 and private EC2 instances.
- Execute **sudo systemctl restart nginx** to restart nginx services.
- Finally. for testing the consuming of the API, execute **curl -v http://PRIVATE-IP-FROM-PRIVATE-INSTANCE/API-ENDPOINT** 
  ![image](https://github.com/user-attachments/assets/43369db0-92d9-4ce0-a23a-4e0e87fd80c3)



### 5. **Display Data on Nginx Web Server**

- Open a browser and navigate to the public IP of the public EC2 instance to view the data displayed via the Nginx server.


---

## Course Certifications (/AWS Networking courses)
