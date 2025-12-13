import numpy as np
#numpy 向量化運算,np.log (以 e 為底, Natural Log),Nats (奈特)

# fixed p
p = np.array([0.5, 0.25, 0.25])

# start q (uniform)
q = np.array([1/3, 1/3, 1/3])

# learning rate for EG
eta = 0.5

def cross_entropy(p, q):
    return -np.sum(p * np.log(q))

for t in range(200):
    # gradient of cross entropy wrt q
    grad = - p / q

    # EG update: multiplicative + renormalize
    q = q * np.exp(-eta * grad)
    q = q / q.sum()

    if t % 20 == 0:
        print(f"t={t}, q={q}, CE={cross_entropy(p, q):.6f}")

print("\nFinal q:", q)
print("Entropy(p):", -np.sum(p * np.log(p)))
print("Cross_entropy(p, q):", cross_entropy(p, q))
