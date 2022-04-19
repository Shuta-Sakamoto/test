import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s_new = s.replace(",", "")
s_new = s_new.replace(".", "")
s_ls = s_new.split()
ls = []
for w in s_ls:
    ls.append(len(w))
print(ls)
