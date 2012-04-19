from PIL import Image
import glob, math

def generate_feature(r_dimension, g_dimension, b_dimension):
    dimension = r_dimension * g_dimension * b_dimension
    feature_file = open('color_feature_%d.txt' % dimension, 'w')
    feature_file.write('tech histogram' + '\n')
    feature_file.write('<< polysilicon >>' + '\n')
    image_list_file = open('imagelist_%d.txt' % dimension, 'w')
    for filename in glob.glob('image/*.JPEG'):
        hg = get_histogram(r_dimension, g_dimension, b_dimension, filename)
        feature_file.write('rect ' + str.join(' ', [str(i) for i in hg]) + '\n')
        image_list_file.write(filename[6:] + '\n')
    feature_file.write('<< end >>')

def get_histogram(r_dimension, g_dimension, b_dimension, filename):
    image = Image.open(filename)
    data = list(image.getdata())
    full_len = 0x100
    r_piece_len = int(math.ceil(full_len / float(r_dimension)))
    g_piece_len = int(math.ceil(full_len / float(g_dimension)))
    b_piece_len = int(math.ceil(full_len / float(b_dimension)))
    hg = [0 for i in xrange(r_dimension * g_dimension * b_dimension)]
    for pixel in data:
        hg[pixel[0]/r_piece_len * g_dimension * b_dimension + pixel[1]/g_piece_len * b_dimension + pixel[2]/b_piece_len] += 1
    return equalize_histogram(hg)

def equalize_histogram(histogram):
    rate = sum(histogram) / 10000.0
    histogram = [int(i / rate) for i in histogram]
    return histogram

if __name__ == '__main__':
    generate_feature(1, 2, 2)
    generate_feature(2, 2, 2)
    generate_feature(2, 2, 3)
    generate_feature(2, 2, 4)
    generate_feature(2, 2, 5)

