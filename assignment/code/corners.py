import os

import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
# Use scipy.ndimage.convolve() for convolution.
# Use zero padding (Set mode = 'constant'). Refer docs for further info.

from common import read_img, save_img


def corner_score(image, u=5, v=5, window_size=(5, 5)):
    """
    Given an input image, x_offset, y_offset, and window_size,
    return the function E(u,v) for window size W
    corner detector score for that pixel.
    Use zero-padding to handle window values outside of the image.

    Input- image: H x W
           u: a scalar for x offset
           v: a scalar for y offset
           window_size: a tuple for window size

    Output- results: a image of size H x W
    """
    shifted_image = np.roll(image, shift=(v, u), axis=(0, 1))
    
    squared_diff = (image - shifted_image) ** 2
    
    kernel = np.ones(window_size)
    
    output = scipy.ndimage.convolve(squared_diff, kernel, mode='constant', cval=0.0)
    return output


def harris_detector(image, window_size=(5, 5)):
    """
    Given an input image, calculate the Harris Detector score for all pixels
    You can use same-padding for intensity (or 0-padding for derivatives)
    to handle window values outside of the image.

    Input- image: H x W
    Output- results: a image of size H x W
    """
    # compute the derivatives
    Ix = scipy.ndimage.convolve(image, np.array([[-1, 0, 1]]), mode='constant')
    Iy = scipy.ndimage.convolve(image, np.array([[-1], [0], [1]]), mode='constant')

    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    window_kernel = np.ones(window_size)
    
    Sxx = scipy.ndimage.convolve(Ixx, window_kernel, mode='constant')
    Syy = scipy.ndimage.convolve(Iyy, window_kernel, mode='constant')
    Sxy = scipy.ndimage.convolve(Ixy, window_kernel, mode='constant')

    det_M = (Sxx * Syy) - (Sxy ** 2)
    trace_M = Sxx + Syy

    k = 0.05
    response = det_M - k * (trace_M ** 2)

    return response

def save_heatmap(R, filename):
    """
    Plots the response R as a heatmap and saves it.
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(R, cmap='jet') # 'jet' or 'hot' are standard for heatmaps
    plt.colorbar(label='Harris Response Score')
    plt.title('Harris Corner Detector Heatmap')
    plt.axis('off')
    plt.savefig(filename)
    plt.close()


def main():
    img = read_img('./grace_hopper.png')

    # Feature Detection
    if not os.path.exists("./feature_detection"):
        os.makedirs("./feature_detection")

    # -- TODO Task 5: Corner Score --
    # (a): Complete corner_score()

    # (b)
    # Define offsets and window size and calulcate corner score
    W = (5, 5)

    # score = corner_score(img, u, v, W)
    # save_img(score, "./feature_detection/corner_score.png")

    # Computing the corner scores for various u, v values.
    score = corner_score(img, 0, 5, W)
    save_img(score, "./feature_detection/corner_score05.png")

    score = corner_score(img, 0, -5, W)
    save_img(score, "./feature_detection/corner_score0-5.png")

    score = corner_score(img, 5, 0, W)
    save_img(score, "./feature_detection/corner_score50.png")

    score = corner_score(img, -5, 0, W)
    save_img(score, "./feature_detection/corner_score-50.png")

    # (c): No Code

    # -- TODO Task 6: Harris Corner Detector --
    # (a): Complete harris_detector()

    # (b)
    if not os.path.exists("./harris_corner"):
        os.makedirs("./harris_corner")

    harris_response = harris_detector(img)
    
    # Pass the full path to the save function
    save_heatmap(harris_response, "./harris_corner/q6_heatmap.png")
    print(f"./harris_corner/q6_heatmap.png is saved!")

if __name__ == "__main__":
    main()
