AWS NETWORKING - HANDS-ON EXERCISE
===================================

OBJECTIVE: Build a complete VPC architecture with public and private subnets, 
configure networking components, and understand how traffic flows in AWS.

═══════════════════════════════════════════════════════════════════════════

PART 1: VPC CREATION

Create Custom VPC

![alt text](<Screenshot 2026-02-11 at 3.56.04 PM.png>)


═══════════════════════════════════════════════════════════════════════════

PART 2: SUBNET CREATION

Create Public Subnet & Private Subnet

![alt text](<Screenshot 2026-02-11 at 4.00.22 PM.png>)

═══════════════════════════════════════════════════════════════════════════

PART 3: INTERNET GATEWAY (IGW)
═══════════════════════════════════════════════════════════════════════════

Create Internet Gateway & Attach IGW to VPC
   
![alt text](<Screenshot 2026-02-11 at 4.01.32 PM.png>)

═══════════════════════════════════════════════════════════════════════════

PART 4: ROUTE TABLES
═══════════════════════════════════════════════════════════════════════════

Create Public Route Table & Configure Public Route Table

![alt text](<Screenshot 2026-02-11 at 4.04.47 PM.png>)

Associate Public Subnet with Public Route Table


![alt text](<Screenshot 2026-02-11 at 4.05.23 PM.png>)



═══════════════════════════════════════════════════════════════════════════

PART 5: SECURITY GROUPS (FIREWALL)
═══════════════════════════════════════════════════════════════════════════


Create/Modify Security Group
   
![alt text](<Screenshot 2026-02-11 at 4.12.02 PM.png>)
═══════════════════════════════════════════════════════════════════════════

PART 6: EC2 INSTANCES - PUBLIC
═══════════════════════════════════════════════════════════════════════════

12. Launch Public EC2 Instance, Network Settings (Critical!) &  Connect to Public Instance

![alt text](<Screenshot 2026-02-11 at 4.38.59 PM.png>)

![alt text](<Screenshot 2026-02-11 at 4.39.29 PM.png>)

═══════════════════════════════════════════════════════════════════════════

PART 7: EC2 INSTANCES - PRIVATE
═══════════════════════════════════════════════════════════════════════════

16. Launch Private EC2 Instance & Network Settings & Copy SSH Key to Public Instance


![alt text](<Screenshot 2026-02-11 at 4.50.14 PM.png>)

![alt text](<Screenshot 2026-02-11 at 4.50.27 PM.png>)
    
    
    
20. Connect to Private Instance via Jump Box

![alt text](<Screenshot 2026-02-11 at 4.54.37 PM.png>)

═══════════════════════════════════════════════════════════════════════════

PART 8: NAT GATEWAY (OUTBOUND ONLY ACCESS)
═══════════════════════════════════════════════════════════════════════════

PROBLEM: Private instance cannot reach internet for updates/patches.

SOLUTION: NAT Gateway - allows OUTBOUND traffic only, blocks INBOUND.

CONCEPT: Like using WiFi without port forwarding - you can browse internet, 
but no one can initiate connection to you.

21. Allocate Elastic IP
![alt text](<Screenshot 2026-02-11 at 4.58.10 PM.png>)

22. Create NAT Gateway

![alt text](<Screenshot 2026-02-11 at 5.05.47 PM.png>)

23. Create Private Route Table, Configure Private Route Table & Associate Private Subnet

 ![alt text](<Screenshot 2026-02-11 at 5.07.34 PM.png>)

26. Test Outbound Connectivity
  
  ![alt text](<Screenshot 2026-02-11 at 5.11.45 PM.png>)


═══════════════════════════════════════════════════════════════════════════

