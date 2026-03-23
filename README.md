**Linux Threat Monitor**

A lightweight Linux process monitoring tool that detects suspicious activity by reading live kernel data directly from /proc.

**What is this tool?**

A Python-based security monitor that continuously checks all running processes on a Linux system and flags anything that looks suspicious — specifically processes running as root from directories commonly used by malware.

**What does it detect?**

- Processes running as root (UID 0) from suspicious directories
- Suspicious execution paths including /tmp, /dev/shm, /var/tmp
- Displays PID, process name, and privilege level for every running process

**How does it work?**

Linux exposes all running process information through /proc — a virtual filesystem maintained by the kernel. Tools like htop, ps, and btop++ all read from the same place. This monitor reads directly from:

- /proc/[pid]/comm — process name
- /proc/[pid]/status — UID and privilege level
- /proc/[pid]/cmdline — exact command and path that launched the process

If a root process is found running from a suspicious path it flags it as potential malware.

**How to run it**

bash git clone https://github.com/Abishek-Pechiappan/linux-system-monitoring.git
**cd** linux-system-monitoring
python3 DataCollector.py

**What I learned**

- How Linux exposes kernel data through the /proc filesystem
- How to parse system level files in Python
- How tools like btop++ and htop work under the hood
- Process privilege levels and why root detection matters in security
- Tested against a simulated malicious process running from /tmp

**Future Improvements**

- Continuous monitoring with scans every 10 seconds
- Logging detections to a file with timestamps
- Network connection monitoring via /proc/net/tcp
- Auto start on system boot
- Terminal dashboard UI
