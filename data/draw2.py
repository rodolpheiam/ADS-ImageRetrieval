import matplotlib.pyplot as plt
import sys

f = open(sys.argv[1] + '/problem1').readlines()
f2 = open(sys.argv[1] + '/problem2').readlines()
x = []
y = [[], [], [], [], [], [], [], []]
for j in xrange(len(f)):
    nums = [int(n) for n in f[j].split(' ')]
    x.append(nums[0])
    for i in xrange(7):
        y[i].append(nums[i + 1] / 5000)
    y[7].append(int(f2[j].split(' ')[1]) / 5000)
plt.plot(x, y[0], 'bo-', label='4D')
plt.plot(x, y[1], 'g^-', label='8D')
plt.plot(x, y[2], 'rs-', label='12D')
plt.plot(x, y[3], 'cp-', label='16D')
plt.plot(x, y[4], 'md-', label='20D')
plt.plot(x, y[5], 'yx-', label='27D')
plt.plot(x, y[6], 'kh-', label='64D')
plt.plot(x, y[7], 'm+-', label='9D')
plt.xlabel('Number of objects inserted')
plt.ylabel('Number of node access')
plt.legend(('4D', '8D', '12D', '16D', '20D', '27D', '64D', '9D'), loc=2)
plt.show()
