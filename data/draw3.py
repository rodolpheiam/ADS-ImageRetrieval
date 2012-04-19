import matplotlib.pyplot as plt
import numpy as np
import sys

f = open(sys.argv[1] + '/problem3').readlines()
y = []
COLOR = ['b', 'g', 'r', 'c', 'm', 'y']
LABEL = ['4D', '8D', '12D', '16D', '20D', '9D']
for line in f:
    y.append([float(i) for i in line.split(' ')[:-1]])
for i in xrange(6):
    x = [4+1.2*i+j for j in xrange(0, 100, 10)]
    plt.bar(x, y[i], 1.2, color=COLOR[i], label=LABEL[i])
plt.xticks(np.arange(7.6, 100, 10), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
plt.legend()
plt.xlabel('Number of neighbors in query')
plt.ylabel('Correctness rate(%)')
plt.show()
