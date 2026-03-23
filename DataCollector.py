import os 

def main():
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]
    for pid in pids:
        path_comm = "/proc/" + pid + "/comm"    #Path for comm
        path_status = "/proc/" + pid + "/status"   #Path for status 
        path_cmdline = "/proc/" + pid + "/cmdline"  #Path for checking where the commad was give from 
        suspious_paths = ["/tmp", "/dev/shm", "/var/tem"]
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
        except FileNotFoundError:
            print 
    print("Total Number Process:", len(pids))   

main()
