import nlp.day1_15
import nlp.day1_16
import numpy as np

docs = [['リンゴ', 'リンゴ', 'リンゴ'], ['リンゴ', 'レモン', 'レモン', 'ミカン'], ['リンゴ', 'イチゴ', 'ミカン'], ['レモン', 'イチゴ', 'ミカン'], ['ミカン', 'ミカン', 'ブドウ', 'ブドウ']]
terms = ['ミカン', 'レモン', 'リンゴ', 'ブドウ', 'イチゴ']
ans = np.zeros((len(terms),len(terms)))
tf_v = nlp.day1_15.tf(terms, docs)
idf_v = nlp.day1_15.idf(terms, docs)
tf_idf = np.zeros((len(docs), len(terms)))

for i in range(len(docs)):
    for j in range(len(terms)):
        tf_idf[i][j] = tf_v[i][j] * idf_v[j]


for i in range(len(docs)):
    for j in range(len(docs)):
        ans[i][j] = nlp.day1_16.cosine_sim(tf_idf[i],tf_idf[j])

print(ans)

