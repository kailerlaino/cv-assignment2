import os

import numpy as np
import scipy.ndimage
# Use scipy.ndimage.convolve() for convolution.
# Use same padding (mode = 'reflect'). Refer docs for further info.

from common import (find_maxima, read_img, visualize_maxima,
                    visualize_scale_space)


def gaussian_filter(image, sigma):
    """
    Given an image, apply a Gaussian filter with the input kernel size
    and standard deviation

    Input
      image: image of size HxW
      sigma: scalar standard deviation of Gaussian Kernel

    Output
      Gaussian filtered image of size HxW
    """
    H, W = image.shape
    # -- good heuristic way of setting kernel size
    kernel_size = int(2 * np.ceil(2 * sigma) + 1)
    # Ensure that the kernel size isn't too big and is odd
    kernel_size = min(kernel_size, min(H, W) // 2)
    if kernel_size % 2 == 0:
        kernel_size = kernel_size + 1
    # TODO implement gaussian filtering of size kernel_size x kernel_size
    radius = kernel_size // 2
    base = np.arange(-radius, radius + 1)
    oned_gauss = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((base**2) / (2 * sigma**2)))
    kernel_gaussian = np.outer(oned_gauss, oned_gauss)
    kernel_gaussian = kernel_gaussian / np.sum(kernel_gaussian)

    # Similar to Corner detection, use scipy's convolution function.
    # Again, be consistent with the settings (mode = 'reflect').
    output = scipy.ndimage.convolve(image, kernel_gaussian, mode='reflect')
    return output




def main():
    image = read_img('polka.png')
    # import pdb; pdb.set_trace()
    # Create directory for polka_detections
    if not os.path.exists("./polka_detections"):
        os.makedirs("./polka_detections")

    # -- TODO Task 7: Single-scale Blob Detection --

    # (a), (b): Detecting Polka Dots
    # First, complete gaussian_filter()
    print("Detecting small polka dots")
    # -- Detect Small Circles
    # sigma_1, sigma_2 = 7.778174593, 3.5355339 
    sigma_1, sigma_2 = 3.5, np.sqrt(2) * 3.5
    gauss_1 = gaussian_filter(image, sigma_1)  # to implement
    gauss_2 = gaussian_filter(image, sigma_2)  # to implement

    # calculate difference of gaussians
    DoG_small = gauss_2 - gauss_1 # to implement

    # visualize maxima
    maxima = find_maxima(DoG_small, k_xy=10)
    visualize_scale_space(DoG_small, sigma_1, sigma_2 / sigma_1,
                          './polka_detections/polka_small_DoG.png')
    visualize_maxima(image, maxima, sigma_1, sigma_2 / sigma_1,
                     './polka_detections/polka_small.png')

    # -- Detect Large Circles
    print("Detecting large polka dots")
    sigma_1, sigma_2 = 7.7, np.sqrt(2) * 7.7
    gauss_1 = gaussian_filter(image, sigma_1)  # to implement
    gauss_2 = gaussian_filter(image, sigma_2)  # to implement

    # calculate difference of gaussians
    DoG_large = gauss_2 - gauss_1 # to implement

    # visualize maxima
    # Value of k_xy is a sugguestion; feel free to change it as you wish.
    maxima = find_maxima(DoG_large, k_xy=10)
    visualize_scale_space(DoG_large, sigma_1, sigma_2 / sigma_1,
                          './polka_detections/polka_large_DoG.png')
    visualize_maxima(image, maxima, sigma_1, sigma_2 / sigma_1,
                     './polka_detections/polka_large.png')


    # # -- TODO Task 8: Cell Counting --
    print("Detecting cells")
    # Detect the cells in any four (or more) images from vgg_cells
    # Create directory for cell_detections
    if not os.path.exists("./cell_detections"):
        os.makedirs("./cell_detections")

    image = read_img('./cells/001cell.png')

    sigma_1, sigma_2 = 4.25, 6
    gauss_1 = gaussian_filter(image, sigma_1)  
    gauss_2 = gaussian_filter(image, sigma_2)

    DoG_cell = gauss_2 - gauss_1 

    maxima = find_maxima(DoG_cell, k_xy=13)
    visualize_scale_space(DoG_cell, sigma_1, sigma_2 / sigma_1,
                          './cell_detections/cell_1_DoG.png')
    visualize_maxima(image, maxima, sigma_1, sigma_2 / sigma_1,
                     './cell_detections/cell_1.png')
    
    image = read_img('./cells/051cell.png')

    sigma_1, sigma_2 = 4.25, 6
    gauss_1 = gaussian_filter(image, sigma_1)
    gauss_2 = gaussian_filter(image, sigma_2)

    DoG_cell = gauss_2 - gauss_1 

    maxima = find_maxima(DoG_cell, k_xy=12)
    visualize_scale_space(DoG_cell, sigma_1, sigma_2 / sigma_1,
                          './cell_detections/cell_51_DoG.png')
    visualize_maxima(image, maxima, sigma_1, sigma_2 / sigma_1,
                     './cell_detections/cell_51.png')
    
    image = read_img('./cells/101cell.png')

    sigma_1, sigma_2 = 4.25, 6
    gauss_1 = gaussian_filter(image, sigma_1)
    gauss_2 = gaussian_filter(image, sigma_2) 

    DoG_cell = gauss_2 - gauss_1 

    maxima = find_maxima(DoG_cell, k_xy=14)
    visualize_scale_space(DoG_cell, sigma_1, sigma_2 / sigma_1,
                          './cell_detections/cell_101_DoG.png')
    visualize_maxima(image, maxima, sigma_1, sigma_2 / sigma_1,
                     './cell_detections/cell_101.png')
    
    image = read_img('./cells/151cell.png')

    sigma_1, sigma_2 = 4.25, 6
    gauss_1 = gaussian_filter(image, sigma_1)
    gauss_2 = gaussian_filter(image, sigma_2)

    DoG_large = gauss_2 - gauss_1 

    maxima = find_maxima(DoG_large, k_xy=13)
    visualize_scale_space(DoG_large, sigma_1, sigma_2 / sigma_1,
                          './cell_detections/cell_151_DoG.png')
    visualize_maxima(image, maxima, sigma_1, sigma_2 / sigma_1,
                     './cell_detections/cell_151.png')


if __name__ == '__main__':
    main()
