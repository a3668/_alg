import random

def hillClimbing(f, x, y, h=0.01):
    failCount = 0
    fxy = f(x, y)

    while (failCount < 10000):
        dx = random.uniform(-h, h)
        dy = random.uniform(-h, h)

        new_fx = f(x + dx, y + dy)

        if new_fx >= fxy:
            if abs(new_fx - fxy) < 1e-8:
                break
            x = x + dx
            y = y + dy
            fxy = new_fx
            print('x={:.3f} y={:.3f} f(x,y)={:.3f}'.format(x, y, fxy))
            failCount = 0
        else:
            failCount = failCount + 1
    return (x, y, fxy)


def f(x, y):
    return -1 * ( x*x -2*x + y*y +2*y - 8 )

hillClimbing(f, 0, 0)
