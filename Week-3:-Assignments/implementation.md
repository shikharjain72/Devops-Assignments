# Week 3 Implementation Guide (ASG + ALB + HTTPS)

Use this file to document your practical execution. Each step includes:
- What to do
- Why it matters
- Screenshot section (paste your screenshot path or image)

---

## Step 1. Clone and Prepare Application Code & Create Launch Template
**Description:** Clone the reference repository, verify app files, and ensure the startup script works.

![alt text](<Screenshot 2026-02-22 at 1.01.52 AM.png>)

## Step 2. Test Launch Template Instance
**Description:** Launch one temporary EC2 from template and verify app starts.

![alt text](<Screenshot 2026-02-22 at 10.53.15 AM.png>)

## Step 3. Create Auto Scaling Group (ASG)

![alt text](<Screenshot 2026-02-23 at 11.29.50 PM.png>)


## Step 4. Create Target Group
**Description:** Create target group for EC2 instances running app on port 8000.
![alt text](<Screenshot 2026-02-23 at 2.54.22 AM.png>)


## Step 5. Create Application Load Balancer (ALB)
**Description:** Configure ALB across both public subnets and attach target group.

![alt text](<Screenshot 2026-02-22 at 5.03.48 PM.png>)

## Step 6. Attach ASG to Target Group
**Description:** Link ASG with target group so instances auto-register with ALB.

![alt text](<Screenshot 2026-02-23 at 11.29.50 PM-1.png>)

## Step 7. Configure Domain / Subdomain in Route53
**Description:** Point domain/subdomain to ALB using Alias record.

![alt text](<Screenshot 2026-02-23 at 10.28.18 PM.png>)

## Step 8. Enable HTTPS Certificate (ACM Recommended)
**Description:** Request public certificate in ACM and validate via DNS.

![alt text](<Screenshot 2026-02-23 at 10.30.29 PM.png>)
![alt text](<Screenshot 2026-02-23 at 10.42.56 PM.png>)

## Step 9. Add HTTPS Listener on ALB
**Description:** Add 443 listener, attach ACM certificate, and forward to target group.

![alt text](<Screenshot 2026-02-23 at 10.56.26 PM.png>)

## Step 13. Final Validation and Evidence
**Description:** Verify scaling, app access, and SSL certificate details.

![alt text](<Screenshot 2026-02-23 at 11.06.07 PM.png>)
![alt text](<Screenshot 2026-02-23 at 11.44.29 PM.png>)
![alt text](<Screenshot 2026-02-24 at 12.23.09 AM.png>)

