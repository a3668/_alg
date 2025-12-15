import matplotlib.pyplot as plt
import numpy as np
import hc

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)

p = [0.0, 0.0]
# 2. 呼叫 hillClimbing
# h 是步伐大小(隨機範圍)，類似 learning rate。
# 爬山法通常需要多一點嘗試次數，或者 h 要設對。
plearn = hc.hillClimbing(loss, p, h=0.01) 

print('Final parameters:', plearn)

# Plot the graph
y_predicted = list(map(lambda t: plearn[0]+plearn[1]*t, x))
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()
