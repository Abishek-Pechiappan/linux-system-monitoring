import os 

def count_file():
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]
    for pid in pids:
        print("PID", pid)
        path = "/proc/" + pid + "/comm"
        try:
            with open(path) as pids_comm:
                print("Comm File :", pids_comm.read())
        except FileNotFoundError:
            print("There is no file :(")
    print("Total Number:", len(pids))   

count_file()
