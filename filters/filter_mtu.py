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
        interface = None
        for line in log:
            if "down" not in line and line[0] != " ":
                interface = line.split(" ")[0].replace('[\"', '')
            else:
                if "MTU" in line and "BW" in line:
                    interfaceData = line.split(", ")
                    mtu = int(re.search(r"\d+", interfaceData[0]).group())
                    bw = int(re.search(r"\d+", interfaceData[1]).group())
                    out.update({interface: {"MTU": mtu, "BW": bw}})

        print(out)
