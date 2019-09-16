import numpy as np
import os
from shutil import copyfile

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

src_bumblebee = '/dados/calib_bumblebee/'
# src_velodyne = '/dados/calib_velodyne/'
src_velodyne = '/dados/vel_pngs/'
dest_bumblebee = '/dados/bb3/'
dest_velodyne = '/dados/velodyne/'

img_list = os.listdir(src_bumblebee)
pointcloud_list = os.listdir(src_velodyne)

img_times = [float(a.rsplit('.', 1)[0].split('-')[0]) for a in img_list]
pointcloud_times = [float(a.rsplit('.', 1)[0]) for a in pointcloud_list]

for idx, img_name in enumerate(img_list):
    time = img_times[idx]
    pointcloud_idx = find_nearest(pointcloud_times, time)
    if pointcloud_times[pointcloud_idx] <= 1563468272.5:
        copyfile(src_bumblebee+img_name, dest_bumblebee+'img'+'{0:04d}'.format(idx+1)+'.png')
        copyfile(src_velodyne+pointcloud_list[pointcloud_idx], dest_velodyne+'cloud'+'{0:04d}'.format(idx+1)+'.png')
        print(img_name, pointcloud_list[pointcloud_idx])
