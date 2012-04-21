import matplotlib.pyplot as plt
import sys

f = open(sys.argv[1] + '/problem1')
x = []
y = [[], [], [], [], [], [], []]
for line in f.readlines():
    nums = [int(n) for n in line.split(' ')]
    x.append(nums[0])
    for i in xrange(7):
        y[i].append(nums[i + 1] / 5000)
plt.plot(x, y[0], 'bo-', label='4D')
plt.plot(x, y[1], 'g^-', label='8D')
plt.plot(x, y[2], 'rs-', label='12D')
plt.plot(x, y[3], 'cp-', label='16D')
plt.plot(x, y[4], 'md-', label='20D')
plt.plot(x, y[5], 'yx-', label='27D')
plt.plot(x, y[6], 'k+-', label='64D')
plt.xlabel('Number of objects inserted')
plt.ylabel('Number of node access')
plt.legend(('4D', '8D', '12D', '16D', '20D', '27D', '64D'), loc=2)
plt.show()
