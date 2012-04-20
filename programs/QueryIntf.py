from rtree import index
import sys
import ImageFeatureExtractor

def build(feature, imagelist, dimension):
	features = open(feature).readlines()[2:-1]
	images = open(imagelist).readlines()
	p = index.Property()
	p.dimension = dimension
	idx = index.Index(properties=p)
	items = []
	for i in xrange(len(images)):
		item = (images[i][:-1], tuple(int(f) for f in features[i].split(' ')[1:]))
		idx.insert(i, item[1], obj=item[0])
		items.append(item)
	return idx, items

def nearest(idx, point, num):
	hits = idx.nearest(point, num, objects='raw')
	item = []
	item.append([str(i) for i in hits])
	return item

def query_by_image(dimension, imagename, num, idx):
	dimension_array = [[4, 1, 2, 2], [8, 2, 2, 2], [12, 2, 2, 3], [16, 2, 2, 4], [20, 2, 2, 5]]
	array = [i for i in dimension_array if i[0] == dimension][0]
	t = tuple(ImageFeatureExtractor.get_histogram(array[1], array[2], array[3], imagename))
	item = nearest(idx, t, num)
	results = []
	results.append(item)
	return results

def query_by_text(dimension, textname, num, idx):
	imagelist = open(textname).readlines()
	results = []
	for i in imagelist:
		item = query_by_image(dimension, i[:-2], num, idx)
		results.append(item[0])
	return results

def print_result(results):
	result_file = open('./query.result', 'w+')
	for item in results:
		result_file.write(str.join(' ', [str(i) for i in item]) + '\n')

# Script starts from here
def main():
	if sys.argv[1] == '--image':
		dimension = int(sys.argv[3])
		idx, items = build('./color_feature_%d.txt' % dimension, './imagelist.txt', dimension)
		results = query_by_image(int(sys.argv[3]), sys.argv[2], int(sys.argv[4]), idx)
		print_result(results)
	elif sys.argv[1] == '--text':
		dimension = int(sys.argv[3])
		idx, items = build('./color_feature_%d.txt' % dimension, './imagelist.txt', dimension)
		results = query_by_text(int(sys.argv[3]), sys.argv[2], int(sys.argv[4]), idx)
		print_result(results)
	else:
		print '''\
query.py [option] [filename] [dimension] [result_number]
option:  --image  Query by given image
         --text  Query by given text'''
	sys.exit()

if __name__ == '__main__':
	main()
