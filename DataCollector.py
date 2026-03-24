import os 
import time
import datetime 
import socket

def Process_monitor():
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]
    for pid in pids:
        path_comm = "/proc/" + pid + "/comm"    #Path for comm
        path_status = "/proc/" + pid + "/status"   #Path for status 
        path_cmdline = "/proc/" + pid + "/cmdline"  #Path for checking where the commad was give from 
        suspious_paths = ["/tmp", "/dev/shm", "/var/tmp"]
        try:
            with open(path_comm) as pids_comm:   #Reading the comms file in /proc
                comm = pids_comm.read().rstrip("\n")
            with open(path_status) as pids_status:    
                status_content = pids_status.read()
                for line in status_content.splitlines():   #From the saved makes it to lines 
                    if "Uid" in line:                     #From the lines checkes for the work Uid 
                        check = line.split()            #Makes the line to diff parts to check if it's root 
                        if check[1] == '0':
                            status = "ROOT"
                        else:
                            status = "USER"
                        print("PID: ",pid,"|",comm,"|",status)  #Printing in single line 
            with open(path_cmdline) as pids_cmdline:
                cmd = pids_cmdline.read().replace('\x00',' ').rstrip("\n")    #To make the content in the file visble as it's kernel level we use the .replace()
                if any(path in cmd for path in suspious_paths) and status == "ROOT":
                    print("Malware Found")
                    with open("log.txt", "a") as log:
                        timestamp = str(datetime.datetime.now())   #Changes the Time and Date to strings
                        log.write(timestamp)                        # Writes the date and time in file 
                        log.write(f"PID: {pid} | {comm} | {status} \n")   #Logs the data if there malware is found
        except FileNotFoundError:
            print 
    print("Total Number Process:", len(pids))   

def network_monitor():
    suspicious_ports = [
    21,    # FTP (Unencrypted data exfiltration)
    22,    # SSH (Brute-force entry point)
    23,    # Telnet (Botnet command & control)
    511,   # T0rn Rootkit
    666,   # Satanz Backdoor / Ripper
    1008,  # Li0n Worm
    1337,  # Common Reverse Shell port
    1524,  # Trinoo DDoS tool / Ingres backdoor
    2222,  # Alternate SSH (often used to hide SSH or by malware)
    3040,  # Ramen Worm
    4444,  # Metasploit default listener
    6667,  # IRC-based Botnet C2
    31337, # Back Orifice / Elite Backdoors
    33567, # Lion Worm rootshell
    33568  # Lion Worm trojaned SSH 
    ]   
    path_netowrk = "/proc/net/tcp"
    with open(path_netowrk) as network:
        next(network)
        net = network.read()
        for line in net.splitlines():
            part = line.split()
            localhex = part[1].split(":")
            localip = socket.inet_ntoa(bytes.fromhex(localhex[0])[::-1])
            port = int(localhex[1], 16)
            if port in suspicious_ports:
                with open("network_log.text", "a") as log:
                    timestamp = str(datetime.datetime.now())
                    log.write(f"{timestamp} | ")
                    log.write(f" The IP {localip} is suspicious in the port {port} \n") 

def main():
    while True:
        Process_monitor()
        network_monitor()
        time.sleep(10)

main()
