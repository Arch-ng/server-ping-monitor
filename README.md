# Server Ping Monitor

A lightweight Python script that reads a list of server IP addresses or hostnames from a text file, checks their availability using ICMP ping, and logs the uptime results to an audit file.

## Features

- **Batch Server Checks:** Reads multiple IP addresses or hostnames from `server.txt`.
- **Uptime & Downtime Summary:** Counts and displays the total number of reachable and unreachable servers.
- **Persistent Audit Logging:** Appends status results to `up_timeaudit.log` for historical tracking.
- **Zero External Dependencies:** Built entirely with Python's standard library (`subprocess` and `datetime`).

## Prerequisites

- **Python 3.6+**
- **Linux / macOS** (uses `ping -c 1`; on Windows, change `"-c"` to `"-n"` in the script)

## Project Structure

```text
server-ping-monitor/
├── ping_monitor.py    # Main monitoring script
├── server.txt         # Input list of target IPs/hostnames (one per line)
└── up_timeaudit.log   # Generated log file with ping results
