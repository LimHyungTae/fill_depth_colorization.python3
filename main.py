import cv2
from convert_str2nparray import *

import numpy as np
import matplotlib.pyplot as plt
from fill_depth import fill_depth_colorization
cmap = plt.cm.jet

def colored_depthmap(depth, d_min=None, d_max=None):
    if d_min is None:
        d_min = np.min(depth)
    if d_max is None:
        d_max = np.max(depth)
    depth_relative = (depth - d_min) / (d_max - d_min)
    # depth_relative = (d_max - depth) / (d_max - d_min)
    return 255 * cmap(depth_relative)[:, :, :3] # H, W, C

if __name__ == "__main__":
    csv_path = "input/sa0331_0.csv"
    rgb_path = "input/img.png"
    sparse_depth = convert_csv_str2nparray(csv_path)
    img = cv2.imread(rgb_path)

    depth_colored = colored_depthmap(sparse_depth, np.min(sparse_depth), np.max(sparse_depth))[:, :, ::-1]
    depth_colored = np.array(depth_colored, dtype=np.uint8)

    print("[Info]: On filling depth..")
    depth_filled = fill_depth_colorization(img/255.0, sparse_depth, alpha=1.0)
    print("[Info]: filling depth complete")

    filled_colored = colored_depthmap(depth_filled, np.min(depth_filled), np.max(depth_filled))[:, :, ::-1]
    filled_colored = np.array(filled_colored, dtype=np.uint8)
    cv2.imwrite("result.png", filled_colored)


    # cv2.imwrite("img.png", img)
