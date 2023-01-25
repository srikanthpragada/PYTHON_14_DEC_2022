# Remove blank lines
with open("names.txt", "rt") as f:
    lines = [line for line in f.readlines() if len(line.strip()) > 0]

# write non-blank lines back to file
with open("names.txt", "wt") as f:
    for line in lines:
        f.write(line)
