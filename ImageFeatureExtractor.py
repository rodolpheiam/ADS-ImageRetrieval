from PIL import Image
import glob, math

def main():
    feature_file = open('color_feature.txt', 'w')
    feature_file.write('tech nmos' + '\n')
    feature_file.write('<< polysilicon >>' + '\n')
    image_list_file = open('imagelist.txt', 'w')
    for filename in glob.glob('image/*.JPEG'):
        hg = get_feature(12, filename)
        feature_file.write('rect' + ' ' + str.join(' ', [str(i) for i in hg]) + '\n')
        image_list_file.write(filename + '\n')
    feature_file.write('<< end >>')

def get_feature(dimension, filename):
    im = Image.open(filename)
    hg = im.histogram()
    return divide_histogram(dimension, hg)

def divide_histogram(dimension, histogram):
    full_length = len(histogram)
    part_length = int(math.ceil(full_length / float(dimension)))
    hg = []
    for i in xrange(0,full_length, part_length):
        hg.append(sum(histogram[i:i+part_length]))
    hg = equalize_histogram(hg)
    return hg

def equalize_histogram(histogram):
    rate = float(sum(histogram)) / 500000
    hg = []
    for i in histogram:
        hg.append(int(i / rate))
    return hg

if __name__ == '__main__':
    main()