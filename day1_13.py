docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
tf_v = []

def tf(term, doc):
    for l in doc:
        temp = []
        for w in term:
            cnt = 0
            for l_w in l:
                if l_w == w:
                    cnt += 1
            temp.append(cnt/len(l))
        tf_v.append(temp)
    return


tf(terms, docs)
for i in range(len(docs)):
    for j in range(len(terms)):
        print("tf(", terms[j], ", ", docs[i], ") = ", tf_v[i][j], end="  ", sep="")
    print()