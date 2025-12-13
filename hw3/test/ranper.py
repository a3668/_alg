import random

def permutation(pA):
    shuffled = pA.copy()   
    for _ in range(random.randrange(0, len(shuffled)*10)):
        i = random.randrange(0, len(shuffled))
        j = random.randrange(0, len(shuffled))
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

A = ["a", "b", "c"]  # 外面還是叫 A
for _ in range(10):
    print(permutation(A))
