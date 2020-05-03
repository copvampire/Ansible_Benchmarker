#!/usr/bin/python3

import re
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname')
    args = parser.parse_args()
    with open(f"/etc/ansible/logs/int_{args.hostname}.txt", "r") as run_file:
        log = run_file.read().split("\\n")
        out = {}
        for line in log:
            if line[0] != " ":
                interface_up = True
                if "administratively down" in line:
                    interface_up = False
                interface = line.split(" ")[0].replace('[\"', '')
            elif "MTU" in line and "BW" in line and interface_up is True:
                interfaceData = line.split(", ")
                mtu = int(re.search(r"\d+", interfaceData[0]).group())
                bw = int(re.search(r"\d+", interfaceData[1]).group())
                out[interface] = {"MTU": mtu, "BW": bw}

        print(out)
