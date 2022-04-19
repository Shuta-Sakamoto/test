ls = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
dic = {}
for i in range(len(ls)):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dic[ls[i][:1]] = i+1
    else:
        dic[ls[i][:2]] = i+1
print(dic)
