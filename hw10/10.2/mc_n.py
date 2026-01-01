import random

def mcInt_nD(f, bounds, n=100000):
    dim = len(bounds) #計算維度
    total = 0.0
    
    for _ in range(n): 
        point = []
        for (low, high) in bounds:
            value = random.uniform(low, high)
            point.append(value)
        total += f(*point)

    volume = 1.0
    for (low, high) in bounds:
        length = high - low
        volume *= length

    average = total / n
    result = volume * average

    return result


def f2(x, y):
    return x**2 + 2*y**2

print(mcInt_nD(f2, [(0,1), (0,1)]))

def f3(x, y, z):
    return x**2 + y*z + 1

print(mcInt_nD(f3, [(0,1), (0,1), (0,1)]))

def f10(*xs):
    return sum(x*x for x in xs)

bounds = [(0,1)] * 10
print(mcInt_nD(f10, bounds))
