import matplotlib.pyplot as plt
import numpy as np
import sys

f = open(sys.argv[1] + '/problem3').readlines()
y = []
COLOR = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
LABEL = ['4D', '8D', '12D', '16D', '20D', '27D', '64D', '9D']
for line in f:
    y.append([float(i) for i in line.split(' ')[:-1]])
for i in xrange(8):
    x = [3.2+1.1*i+j for j in xrange(0, 100, 10)]
    plt.bar(x, y[i], 1.1, color=COLOR[i], label=LABEL[i])
plt.xticks(np.arange(7.6, 100, 10), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
plt.legend()
plt.xlabel('Number of neighbors in query')
plt.ylabel('Correctness rate(%)')
plt.show()
