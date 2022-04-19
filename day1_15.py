import math
import numpy as np
docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]


def tf(term, doc):
    tf_v = []
    for l in doc:
        temp = []
        for w in term:
            cnt = 0
            for l_w in l:
                if l_w == w:
                    cnt += 1
            temp.append(cnt/len(l))
        tf_v.append(temp)
    return tf_v


def idf(term, doc):
    idf_v = []
    for w in term:
        cnt_all = 0
        for l in doc:
            cnt = 0
            if w in l:
                cnt += 1
            if cnt > 0:
                cnt_all += 1
        idf_v.append(math.log10(len(doc)/cnt_all) + 1)
    return idf_v


tf_v = tf(terms, docs)
idf_v = idf(terms, docs)

ans = np.zeros((len(docs), len(terms)))

for i in range(len(docs)):
    for j in range(len(terms)):
        ans[i][j] = tf_v[i][j] * idf_v[j]

if __name__ == "__main__":
    print(ans)
