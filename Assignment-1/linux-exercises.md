# Linux System Performance & Process Management - Complete Guide

## Lab Overview
**Platform:** Amazon Linux 2023  
**Duration:** 2-3 hours  
**Goal:** Master process management, CPU, memory, and I/O monitoring


```bash
# Launch EC2 instance (t3.medium recommended for demos)
# Or use existing Amazon Linux system

# Connect via SSH
ssh -i your-key.pem ec2-user@your-instance-ip
sudo yum update -y
sudo yum install -y htop iotop sysstat stress-ng
```
---
![alt text](<Screenshot 2026-02-10 at 4.39.30 PM.png>)


### View All Processes

```bash
# See all processes (snapshot)
ps aux
```
![alt text](<Screenshot 2026-02-10 at 4.45.22 PM.png>)

### Process States

```bash
# View process with states
ps aux | head -20
```
![alt text](<Screenshot 2026-02-10 at 4.47.11 PM.png>)



```bash
ps aux | grep nginx
pgrep nginx
ps -p 1234 -f
pstree
pstree -p
ps -ejH
ps axjf
```
![alt text](<Screenshot 2026-02-10 at 4.50.47 PM.png>)
![alt text](<Screenshot 2026-02-10 at 4.51.12 PM.png>)

**Practice:**
```bash
sleep 300 &
ps aux | grep sleep
ps -o pid,ppid,cmd -p <PID>
```
![alt text](<Screenshot 2026-02-10 at 5.27.19 PM.png>)

---
### Process Hierarchy

```bash
ps -o pid,ppid,cmd -p $$
systemctl status
ps -ef --forest
```
![alt text](<Screenshot 2026-02-10 at 5.33.00 PM.png>)

---



### Real-Time CPU Monitoring with top

```bash
top
```
![alt text](<Screenshot 2026-02-11 at 11.22.35 AM.png>)

### Better Alternative: htop

```bash
# Start htop
htop
htop -t
htop -u ec2-user
```
![alt text](<Screenshot 2026-02-10 at 5.41.50 PM.png>)

### Finding CPU Hogs

```bash
# Top 10 CPU consumers (snapshot)
ps aux --sort=-%cpu | head -11
watch -n 1 'ps aux --sort=-%cpu | head -6'
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head
top -b -n 1 | grep -A 10 "PID USER"
```

![alt text](<Screenshot 2026-02-10 at 5.45.24 PM.png>)

### Load Average Explained

```bash
uptime
top    
w      
cat /proc/loadavg
```
![alt text](<Screenshot 2026-02-10 at 5.49.51 PM.png>)



**Exercise:**
```bash
stress-ng --cpu 2 --timeout 120s
uptime
top
```
![alt text](<Screenshot 2026-02-10 at 6.00.08 PM.png>)
![alt text](<Screenshot 2026-02-10 at 6.17.40 PM.png>)

## Part 3: Memory Monitoring (45 minutes)
---
### Check Memory Usage & Continuous Memory Monitoring

```bash
free
free -h

# Update every 2 seconds
watch -n 2 free -h

# With top
top
# Look at: KiB Mem line

# With htop
htop
# Visual bars at top show memory usage
```
![alt text](<Screenshot 2026-02-10 at 11.32.42 PM.png>)
![alt text](<Screenshot 2026-02-10 at 11.34.04 PM.png>)
---


### Generating Memory Pressure

```bash
stress-ng --vm 2 --vm-bytes 512M --timeout 120s
watch -n 1 free -h
# Terminal 3:
top
```
![alt text](<Screenshot 2026-02-10 at 11.43.14 PM.png>)


**Exercise:**
```bash

free -h | grep Mem | awk '{print $7}'
ps aux --sort=-%mem | head -2
pgrep stress-ng | head -1 | xargs ps -o pid,cmd,%mem -p
```

![alt text](<Screenshot 2026-02-10 at 11.46.03 PM.png>)



## Practice Exercises

### Exercise 1: CPU Hunt

```bash
stress-ng --cpu 2 --timeout 300s &
pgrep stress-ng
ps -p <PID> -o %cpu
renice 10 <PID>
top -p <PID> -d 1 -n 30
kill <PID>
```
![alt text](<Screenshot 2026-02-11 at 10.20.52 AM.png>)

---

### Exercise 2: Memory Investigation

```bash
stress-ng --vm 1 --vm-bytes 500M --timeout 300s &
ps aux | grep stress-ng | grep -v grep | awk '{print $4 "%"}'
ps -p <PID> -o rss
watch -n 5 "ps -p <PID> -o pid,cmd,%mem,rss"
vmstat 1 10 | awk '{print $7, $8}'
```

![alt text](<Screenshot 2026-02-11 at 10.27.23 AM.png>)

---

### Exercise 3: I/O Testing

```bash
# Generate I/O
dd if=/dev/zero of=/tmp/bigfile bs=1M count=5000 &
DD_PID=$!

# Your tasks:
# 1. What's the iowait?
iostat 1 5 | grep -A1 avg-cpu

# 2. Which process is doing I/O?
sudo iotop -o -b -n 1

# 3. How much data written?
iostat -x 1 5 | grep nvme

# 4. Kill the dd process
kill $DD_PID
rm /tmp/bigfile
```
![alt text](<Screenshot 2026-02-11 at 12.03.24 AM.png>)
