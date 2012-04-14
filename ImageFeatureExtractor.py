from PIL import Image
import glob, math

def main():
    output_file = open('output', 'w')
    for filename in glob.glob('image/*.JPEG'):
        hg = get_feature(4, filename)
        output_file.write(filename + ' ' + str.join(' ', [str(i) for i in hg]) + '\n')

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
    hg = histogram
    return hg

if __name__ == '__main__':
    main()