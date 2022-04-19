import math
docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
idf_v = []

def idf(term, doc):
    for w in term:
        cnt_all = 0
        for l in doc:
            cnt = 0
            if w in l:
                cnt += 1
            if cnt > 0:
                cnt_all += 1
        idf_v.append(math.log10(len(doc)/cnt_all) + 1)
    return

idf(terms, docs)
for i in range(len(terms)):
    print("idf(", terms[i], ") = ", idf_v[i], sep="")