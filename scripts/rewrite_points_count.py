import numpy as np
import os
from shutil import copyfile

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

src = '/home/gabriel/Documents/mi-extrinsic-calib-1.0/bin/data_with_board/velodyne_no_zeros/'
dest = '/home/gabriel/Documents/mi-extrinsic-calib-1.0/bin/data_with_board/velodyne/'

files = os.listdir(src)

for fil in files:
    n_lines = file_len(src + fil)
    d = open(dest + fil, 'w+')
    d.write('{}\n'.format(n_lines - 1))
    with open(src + fil) as f:
        for i, l in enumerate(f):
            if i > 0:
                d.write(l)
    d.close()