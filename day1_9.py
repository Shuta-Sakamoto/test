import random
import sys
ls = sys.argv[1:]

for i in range(len(ls)):
    if len(ls[i]) >= 3:
        random_ls = list(range(len(ls[i])-2))
        random.shuffle(random_ls)
        print(ls[i][0] + "".join(ls[i][j+1]
              for j in random_ls)+ls[i][-1], end=" ")
    else:
        print(ls[i], end=" ")
print()
