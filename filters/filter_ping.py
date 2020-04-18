
#!/usr/bin/python3

import re

if __name__ == "__main__":
    with open("/etc/ansible/logs/ping_run.txt", "r") as run_file:
        log = run_file.read().split("\\n")
        out = {}

        for line in log:
            if "Success rate" in line:
                pingRaw = line.split(', ')
                pingSuc = pingRaw[0]
                pingTim = pingRaw[1].replace('\"]', '')

        print({ "Success": pingSuc, "Time": pingTim })



