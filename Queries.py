from rtree import index
import random

def query(idx, dimension, queries):
	visits = idx.visits()
	for i in xrange(queries):
		idx.nearest(tuple(random.sample(xrange(10000), dimension)))
	return idx.visits() - visits

def process(dimension, queries):
	features = open('color_feature_%d.txt' % dimension).readlines()[2:-1]
	p = index.Property()
	p.dimension = dimension
	idx = index.Index(properties=p)
	result = []
	for i in xrange(len(features)):
		if i > 0 and i % 200 == 0:
			result.append(query(idx, dimension, queries))
		idx.insert(i, tuple(int(f) for f in features[i].split(' ')[1:]))
	return result

if __name__ == '__main__':
	output = open('problem1', 'w')
	r = [process(i, 5000) for i in xrange(4, 24, 4)]
	for i in xrange(28):
		output.write('%d' % ((i + 1) * 200))
		for j in xrange(5):
			output.write(' %d' % r[j][i])
		output.write('\n')