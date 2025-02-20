#!/usr/bin/env python

import os
import json
import sys
import signal


# Terminal Emulator used to spawn the processes
terminal = "kitty"

# Blockchain node configuration file name
server_configs = [
    "correctConfig.json",
    "ignoreRequestsConfig.json",
    "badLeaderProposeConfig.json",
    "uponPrepareQuorumWrongValue.json",
    "uponRoundChangeQuorumWrongValue.json"
]

# Client configuration file name
client_config = [
    "clientConfig.json"
]


server_config = server_configs[1]
client_config = client_config[0]

def quit_handler(*args):
    os.system(f"pkill -i {terminal}")
    sys.exit()


# Compile classes
os.system("mvn clean install")

# Spawn blockchain nodes
with open(f"resources/{server_config}") as f:
    data = json.load(f)
    processes = list()
    for key in data:
        pid = os.fork()
        if pid == 0:
            os.system(
                f"{terminal} sh -c \"cd Blockchain; mvn exec:java -Dexec.args='{key['id']} {server_config} {client_config}' ; sleep 500\"")
            sys.exit()

with open(f"resources/{client_config}") as f:
    data = json.load(f)
    processes = list()
    for key in data:
        pid = os.fork()
        if pid == 0:
            os.system(
                f"{terminal} sh -c \"cd Client; mvn exec:java -Dexec.args='{key['id']} {client_config} {server_config}' ; sleep 500\"")
            sys.exit()

signal.signal(signal.SIGINT, quit_handler)

while True:
    print("Type quit to quit")
    command = input(">> ")
    if command.strip() == "quit":
        quit_handler()
