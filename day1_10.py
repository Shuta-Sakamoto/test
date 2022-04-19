import sys
ls = sys.argv[1:]
# print(ls)
s = "".join(ls)
# print(s)


def n_gram_maker(Ls, S, n=2):
    ng_w = []
    ng_c = []
    for i in range(len(Ls)-n+1):
        l = []
        for j in range(i, i+n):
            l.append(Ls[j])
        ng_w.append(l)
    for i in range(len(S)-n+1):
        ng_c.append(S[i:i+n])
    print("単語bi-gram: ", ng_w)
    print("文字bi-gram: ", ng_c)
    return


n_gram_maker(ls, s, 2)
