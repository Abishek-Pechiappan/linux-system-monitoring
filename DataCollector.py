import os 

def main():
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]
    for pid in pids:
        print("PID", pid, end=" | ")
        path_comm = "/proc/" + pid + "/comm"    #Path for comm
        path_status = "/proc/" + pid + "/status"   #Path for status 
        try:
            with open(path_comm) as pids_comm:   #Reading the comms file in /proc
                print(pids_comm.read(),end = " | ")
            with open(path_status) as pids_status:    
                status_content = pids_status.read()
                for line in status_content.splitlines():   #From the saved makes it to lines 
                    if "Uid" in line:                     #From the lines checkes for the work Uid 
                        check = line.split()            #Makes the line to diff parts to check if it's root 
                        if check[1] == '0':
                            print("ROOT")
                        else:
                            print("USER")
        except FileNotFoundError:
            print 

    print("Total Number:", len(pids))   

main()
