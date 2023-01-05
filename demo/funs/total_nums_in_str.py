st = "90,34,45,a,56,78"

parts = st.split(",")
valid_parts = filter(str.isdigit, parts)
nums = map(int, valid_parts)
print(sum(nums))

nums = [int(p) for p in st.split(",") if p.isdigit()]
print(sum(nums))