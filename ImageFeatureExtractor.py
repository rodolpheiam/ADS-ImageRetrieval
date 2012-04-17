from PIL import Image
import glob, math

def generate_feature(dimension):
    feature_file = open('color_feature_%d.txt' % dimension, 'w')
    feature_file.write('tech histogram' + '\n')
    feature_file.write('<< polysilicon >>' + '\n')
    #image_list_file = open('imagelist.txt', 'w')
    for filename in glob.glob('image/*.JPEG'):
        hg = get_feature(dimension, filename)
        feature_file.write('rect ' + str.join(' ', [str(i) for i in hg]) + '\n')
        #image_list_file.write(filename[6:] + '\n')
    feature_file.write('<< end >>')

def get_feature(dimension, filename):
    im = Image.open(filename)
    hg = im.histogram()
    return merge_histogram(dimension, hg)

def merge_histogram(dimension, histogram):
    full_length = len(histogram)
    part_length = int(math.ceil(full_length / float(dimension)))
    hg = [sum(histogram[i : i+part_length]) for i in xrange(0, full_length, part_length)]
    return equalize_histogram(hg)

def equalize_histogram(histogram):
    rate = sum(histogram) / 10000.0
    hg = [int(i / rate) for i in histogram]
    return hg

if __name__ == '__main__':
    generate_feature(4)
    generate_feature(8)
    generate_feature(12)
    generate_feature(16)
    generate_feature(20)
