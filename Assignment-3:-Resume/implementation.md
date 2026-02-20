# Portfolio Implementation Documentation

## Project Overview
This documentation outlines the implementation of a portfolio project structure.

## Implementation Details

1) Basic Structure created through

The following screenshot illustrates the basic structure generated with the help of Codex.

![alt text](<Screenshot 2026-02-19 at 3.32.39 PM.png>)

2) HTML Structure

The following screenshot illustrates how a basic HTML structure looks like in a local environment.

![alt text](<Screenshot 2026-02-19 at 3.33.48 PM.png>)

3) Gunicorn

Using Gunicorn locally allows developers to simulate a production-like environment, ensuring that the application behaves consistently when deployed. 

Issue face:- flask need specific version of python3(>3.9), so wrote script acc. to that.

![alt text](<Screenshot 2026-02-19 at 5.05.10 PM.png>) 
![alt text](<Screenshot 2026-02-19 at 5.05.02 PM.png>) 
![alt text](<Screenshot 2026-02-19 at 5.04.36 PM.png>)

4) Nginx config file for port forwarding

The Nginx configuration file for port forwarding is essential for directing traffic to the appropriate services. Below is a sample configuration that demonstrates how to set up port forwarding for a web application.

![alt text](<Screenshot 2026-02-19 at 3.50.39 PM.png>)

![alt text](<Screenshot 2026-02-19 at 3.51.09 PM.png>)

5) Committing and Pushing Code to GitHub

**Stage your changes,Commit your changes, Push to GitHub**

Make sure to replace `main` with your branch name if it's different. This process ensures that your changes are saved in the version control system and are available to collaborators.

![alt text](<Screenshot 2026-02-19 at 3.56.00 PM.png>) 
![alt text](<Screenshot 2026-02-19 at 3.55.47 PM.png>)

6) Starting ec2 instance to host flask app

To start an EC2 instance for hosting a Flask application, follow these steps:

**Log in to AWS Management Consol, Launch Instance, select Instance Type, Configure Security Group,Review and Launch, Connect to Your Instance**

![alt text](<Screenshot 2026-02-19 at 4.11.27 PM.png>)

7) Changing nginx port forwding config.

![alt text](<Screenshot 2026-02-19 at 5.14.52 PM.png>)

8) Installing SSL certificates in EC2 

![alt text](<Screenshot 2026-02-19 at 5.28.39 PM.png>)
![alt text](<Screenshot 2026-02-19 at 6.40.22 PM.png>)

9) Configuring domain and subdomain(www) on route 53

![alt text](<Screenshot 2026-02-19 at 6.41.52 PM.png>)

10) Running code inside EC2 and checking public IP and dom

![alt text](<Screenshot 2026-02-19 at 5.21.57 PM.png>)
![alt text](<Screenshot 2026-02-19 at 5.22.06 PM.png>) 
![alt text](<Screenshot 2026-02-19 at 6.38.35 PM.png>)
![alt text](<Screenshot 2026-02-19 at 6.36.25 PM.png>)

11) Running Scripting as service

![alt text](<Screenshot 2026-02-21 at 2.21.54 AM.png>)

![alt text](<Screenshot 2026-02-21 at 2.25.55 AM.png>)

I learned even if AI knows what to generate, it needs hand holding in walking step by step towards trouble shooting,
if we put and run service file without killing existing processes of nginx, gunicorn, it will create issue while running service.