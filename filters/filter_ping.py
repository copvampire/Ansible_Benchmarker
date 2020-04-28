#!/usr/bin/python3

import re
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname')
    args = parser.parse_args()
    with open(f"/etc/ansible/logs/ping_{args.hostname}.txt", "r") as run_file:
        log = run_file.read().split("\\n")
        out = {}

        for line in log:
            if "Success rate" in line:
                pingRaw = line.split(', ')
                pingSuc = pingRaw[0]
                pingTim = pingRaw[1].replace('\"]', '')

        print({ "Success": pingSuc, "Time": pingTim })
