s = "パタトクカシーー"
odd = ""
even = ""
for i in range(len(s)):
    if i % 2 == 0:
        odd += s[i]
    else:
        even += s[i]
print(odd)
print(even)
