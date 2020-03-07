import matplotlib.pyplot as plt

T = [1,2,3,4,5,6]
Y = []
for t in T:
	Y.append(t**2)

plt.plot(T,Y)
plt.show()