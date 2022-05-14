import numpy as np
import matplotlib.pyplot as plt
import sys

G1 = np.loadtxt(sys.argv[1])
plt.ylabel("#Aliens Shot")
plt.xlabel("Time Steps")
plt.plot(G1[:,0], color='blue', marker="^", label='blue')
plt.plot(G1[:,1], color='red', marker="^", label='red')
plt.plot(G1[:,2], color='green', marker="^", label='green')
plt.legend()
plt.title(f'{sys.argv[1]} Statistics on Alien Killings')
plt.show()
