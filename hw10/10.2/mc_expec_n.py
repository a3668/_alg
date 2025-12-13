import random

def mcInt_expectation_nD(f, bounds, n=100000):
    dim = len(bounds)
    total = 0.0
    
    for _ in range(n):
        # 逐維度取樣
        point = []
        for (low, high) in bounds:
            value = random.uniform(low, high)
            point.append(value)

        # 呼叫 f(x1, x2, ..., xk)
        total += f(*point)

    # 計算高維區域的超體積
    volume = 1.0
    for (low, high) in bounds:
        length = high - low
        volume *= length

    average = total / n
    result = volume * average

    return result


def f2(x, y):
    return x**2 + 2*y**2

print(mcInt_expectation_nD(f2, [(0,1), (0,1)]))

def f3(x, y, z):
    return x**2 + y*z + 1

print(mcInt_expectation_nD(f3, [(0,1), (0,1), (0,1)]))

def f10(*xs):
    return sum(x*x for x in xs)

bounds = [(0,1)] * 10  # 10 維超立方體
print(mcInt_expectation_nD(f10, bounds))

