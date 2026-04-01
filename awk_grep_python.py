# Run df -ThP
result = subprocess.run(["df", "-ThP"], capture_output=True, text=True)

lines = result.stdout.splitlines()

for line in lines:
    parts = line.split()

    # Skip header and invalid lines
    if len(parts) < 2:
        continue

    filesystem_type = parts[1]  # 2nd column = FS TYPE

    if filesystem_type == "ext4":
        print(parts[6])
