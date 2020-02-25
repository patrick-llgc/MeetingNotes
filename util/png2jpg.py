"""This script converts png to jpeg with a smaller size"""
import numpy as np
import argparse
import cv2
import os
import glob
from packaging import version
assert version.parse("3") <= version.parse(cv2.__version__) < version.parse("4")
from skimage.filters import threshold_local
from click_and_crop import ScreenPointGetter


def png2jpg(img_path, height=600, width=0, output_dir='./resized'):
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    if height > 0 and width == 0:
        fx = fy = height / h
    elif height == 0 and width > 0:
         fx = fy = width / w
    else:
        raise ValueError
    img = cv2.resize(img, (0, 0), fx=fx, fy=fy)
    assert img_path[-4:] in ['.jpg', '.png']
    os.makedirs(output_dir, exist_ok=True)
    new_filename = os.path.basename(img_path[:-4]).lower() + '.jpg'
    output_path = os.path.join(output_dir, new_filename)
    print('writing to {}'.format(output_path))
    cv2.imwrite(output_path, img)


if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = False,
                    help = "Path to the image to be scanned")
    ap.add_argument("-d", "--directory", required = False,
                    help = "Path to the image directory to be scanned")
    ap.add_argument('--debug', action='store_true')
    ap.add_argument('--mode', default='auto', help='Mode of bright or dark, \
        could be auto, bright, dark or manual selection of four points')
    args = vars(ap.parse_args())

    if args["image"] is not None:
        input_file = args["image"]
        png2jpg(input_file)
    else:
        input_files = glob.glob(os.path.join(args['directory'], '*'))
        for input_file in input_files:
            png2jpg(input_file)