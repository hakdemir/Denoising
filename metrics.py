import math
import numpy as np

def mse(og_image, denoise_image):
    """
    Mean Square Error calculation

    Parameters
    ----------
    og_image : numpy.ndarray
        Original image
    denoise_image : numpy.ndarray
        Denoised image
    """
    return np.mean((og_image - denoise_image) ** 2)

def psnr(og_image, denoise_image):
    """
    Peak Signal to Noise Ratio calculation

    Parameters
    ----------
    og_image : numpy.ndarray
        Original image
    denoise_image : numpy.ndarray
        Denoised image
    """
    mse_value = mse(og_image, denoise_image)
    return 20 * math.log10(255 / math.sqrt(mse_value))



