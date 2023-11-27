#Write a Python script to sort (ascending and descending) a dictionary by value

dictionary={"janvi":1, "vrutika":2, "ishita":3, "riddhi":4}

a=sorted(dictionary.items(),key=lambda x:x[1])
print(dict(a))
