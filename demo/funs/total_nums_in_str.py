st = "90,34,45,56,78"

parts = st.split(",")
nums = map(int, parts)
print(sum(nums))

nums = [int(p) for p in st.split(",")]
print(sum(nums))