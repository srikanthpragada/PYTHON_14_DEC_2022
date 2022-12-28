s1 = "how are you"
s2 = "are"

pos = s1.find(s2)
if pos >= 0:
    print(f"Found at {pos} position")
else:
    print("Not found")
