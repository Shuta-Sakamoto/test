f = open('./dataset/data.txt', 'r')
data = f.readlines()
docs = []
terms = []
for i in range(len(data)-1):
    data[i] = data[i][:-1]
for i in range(len(data)):
    ls = data[i].split("と")
    docs.append(ls)
    terms += ls
terms = list(set(terms))
print("docs :",docs)
print("terms :",terms)
f.close()
