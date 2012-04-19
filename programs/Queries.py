from rtree import index
import random
import sys

def build(feature, imagelist, dimension):
	features = open(feature).readlines()[2:-1]
	images = open(imagelist).readlines()
	p = index.Property()
	p.dimension = dimension
	idx = index.Index(properties=p)
	items = []
	for i in xrange(len(images)):
		item = (images[i][:9], tuple(int(f) for f in features[i].split(' ')[1:]))
		idx.insert(i, item[1], obj=item[0])
		items.append(item)
	return idx, items

def process(feature, dimension):
	features = open(feature).readlines()[2:-1]
	p = index.Property()
	p.dimension = dimension
	idx = index.Index(properties=p)
	result = []
	for i in xrange(len(features)):
		if i > 0 and i % 200 == 0:
			result.append(random_query(idx, 5000, dimension))
		idx.insert(i, tuple(int(f) for f in features[i].split(' ')[1:]))
	return result


def nearest(idx, point, type, num):
	hits = idx.nearest(point, num, objects='raw')
	return len([i for i in hits if i == type])


def random_query(idx, times, dimension):
	visits = idx.visits()
	for i in xrange(times):
		idx.nearest(tuple(random.sample(xrange(10000), dimension)))
	return idx.visits() - visits


def relevance(feature, imagelist, dimension, times, num):
	idx, items = build(feature, imagelist, dimension)
	sum = 0
	for i in xrange(times):
		item = random.choice(items)
		sum += nearest(idx, item[1], item[0], num)
	return 100.0 * sum / times / num


def histogram():
	output = open('../data/problem1', 'w')
	r = [process('../data/color_feature_%d.txt' % i, i) for i in xrange(4, 24, 4)]
	for i in xrange(28):
		output.write('%d' % ((i + 1) * 200))
		for j in xrange(5):
			output.write(' %d' % r[j][i])
		output.write('\n')


def moment():
	output = open('../data/problem2', 'w')
	r = process('../data/color_feature_9.txt', 9)
	for i in xrange(28):
		output.write('%d %d\n' % ((i + 1) * 200, r[i]))


def main():
	if sys.argv[1] == 'relevance':
		output = open('../data/problem3', 'w')
		for i in xrange(4, 24, 4):
			for j in xrange(10, 110, 10):
				output.write('%.1f ' % relevance('../data/color_feature_%d.txt' % i, '../data/imagelist.txt', i, 100, j))
			output.write('\n')
		for j in xrange(10, 110, 10):
			output.write('%.1f ' % relevance('../data/color_feature_9.txt', '../data/imagelist_9.txt', 9, 100, j))
		output.write('\n')
	elif sys.argv[1] == 'queries':
		histogram()
		moment()


if __name__ == '__main__':
	main()