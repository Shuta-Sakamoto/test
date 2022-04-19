import numpy as np
x1 = np.array([1, 0, 0, 1])
x2 = np.array([0, 1, 0, 1])


def cosine_sim(x1, x2):
    return np.dot(x1, x2) / np.sqrt(np.dot(x1,x1) * np.dot(x2,x2))

if __name__ == "__main__":
    print(cosine_sim(x1, x2))
