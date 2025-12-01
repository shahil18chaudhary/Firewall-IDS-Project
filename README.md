Network Firewall & Intrusion Detection Simulator

This project is a simple and interactive Firewall & Intrusion Detection Simulator designed to demonstrate basic network security concepts such as IP blocking, port blocking, attack simulation, and real-time event logging.
It provides a safe environment to understand how firewalls react to different attack patterns and how intrusion detection mechanisms help monitor suspicious activity.

🔎 Overview

The system simulates a lightweight firewall that can:

  -> Block and unblock IP addresses

  -> Block and unblock ports

  -> Detect suspicious or repeated activities

  -> Log events in real-time

  -> Simulate multiple attack patterns

  -> Display system activity neatly inside a terminal-based GUI

It is built using Python, and includes an enhanced interactive interface that helps students and beginners understand how firewalls and IDS systems function.

🚀 Key Features
1. IP & Port Control

  -> Block any IP address

  -> Block specific ports

  -> Temporarily block IPs for a given duration

  -> Unblock IPs when needed

2. Real-Time Intrusion Detection

  -> Detect repeated connection attempts

  -> Identify suspicious port scans

  -> Monitor multiple ports at once

  -> Log every action in event history

3. Attack Simulation

  -> Includes multiple attack scenarios such as:

  -> Random IP attacks

  -> Random port attacks

  -> Combined multi-vector attacks

  -> Massive attack bursts (multiple IP + port attempts)

  -> These attacks help visualize how a firewall handles sudden bursts of malicious traffic.

4. Honeypot Monitoring

  -> A fake port/service used to trap attackers and record unauthorized access attempts.

5. Terminal-Based GUI

  -> A clean dual-panel interface:

  -> Left side: Menu (Select options)

  -> Right side: Output Field (History of all events)

  -> The output panel keeps previous logs visible, giving a clearer view of firewall activity over time.

6. Event Logging

  -> All activity is recorded and saved

  -> Easy to review blocked IPs, port scans, and attack attempts

  -> Helps analyze the detection logic

📁 Project Contents

  -> final.py – Main project script

  -> Internal data structures for logs and rules

  -> Integrated GUI layout (curses-style)

🎯 Purpose

This simulator is built mainly for learning and demonstration.
It shows how a simple firewall reacts to attacks, how detection logic works, and how logs are maintained — without touching any real system configuration or iptables.

Perfect for:

  -> Students practicing cybersecurity

  -> Beginners exploring firewall concepts

  -> Demo for academic projects

  -> Small simulations of attack/defense cycles

📌 Note

This is a simulation and does not modify real networking hardware or OS firewall settings.
Its purpose is educational and safe to run in any environment.
