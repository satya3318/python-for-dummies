#!/usr/bin/env python3

# ============================================
# 1. VARIABLES
# ============================================

name = "Satyawan"
age = 35
is_admin = True

print("Variables:")
print(name, age, is_admin)
print("-" * 50)


# ============================================
# 2. DATA TYPES: STRING, INT, LIST, DICT
# ============================================

# List (similar to array in shell)
servers = ["srv1", "srv2", "srv3"]

# Dictionary (like key=value pairs)
server_info = {
    "hostname": "srv1",
    "ip": "10.10.10.5",
    "os": "AIX"
}

print("List and Dictionary:")
print("Servers:", servers)
print("Server Info:", server_info)
print("Hostname:", server_info["hostname"])
print("-" * 50)


# ============================================
# 3. LOOPS: FOR and WHILE
# ============================================

print("For Loop Example:")
for s in servers:
    print("Server:", s)

print("-" * 30)

print("While Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("-" * 50)


# ============================================
# 4. FUNCTIONS
# ============================================

def greet(user):
    print("Hello", user)

def add(a, b):
    return a + b

print("Functions:")
greet("Satyawan")

result = add(10, 20)
print("10 + 20 =", result)
print("-" * 50)


# ============================================
# 5. FILE HANDLING
# ============================================

print("File Handling Example:")

# Write to a file
with open("output.txt", "w") as f:
    f.write("This is a sample output file.\n")
    f.write("Name: " + name + "\n")

# Read the file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)

print("-" * 50)


# ============================================
# 6. RUNNING LINUX/AIX COMMANDS
# ============================================

import subprocess

print("Running System Commands:")

# Run a simple command (like `uptime`)
cmd = ["uptime"]
result = subprocess.run(cmd, capture_output=True, text=True)

print("Uptime Output:")
print(result.stdout)

print("-" * 50)


# ============================================
# 7. LOOP THROUGH SERVERS AND RUN COMMANDS
# (Just example - assumes SSH trust or keys)
# ============================================

print("Loop Through Servers and Run Commands:")

for s in servers:
    print(f"Checking uptime on {s} ...")
    ssh_cmd = ["ssh", s, "uptime"]
    
    try:
        output = subprocess.run(
            ssh_cmd, capture_output=True, text=True, timeout=5
        )
        print(output.stdout)
    except Exception as e:
        print("Error connecting to", s, ":", e)

print("-" * 50)

print("All demonstrations completed.")
