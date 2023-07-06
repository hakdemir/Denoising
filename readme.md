# MRI-Denoising using KBNet

<img src="figures\denoised.png">

<hr />

Authors: <br />
[Lemar Abdi](https://nl.linkedin.com/in/lemar-abdi-30816317a),
[Halil Akdemir](https://linkedin.com/in/hakdemir),
[Thodoris Chronopoulos](https://www.linkedin.com/in/thodoris-chronopoulos-723694244/)

[Final Report](report/report.pdf)

<hr />

> **Abstract:**  This report discusses the development of a deep learning algorithm for real-time denoising of low-dose X-ray images in C-arms, which will be translated into a start-up. The goal is to reduce radiation exposure for patients and especially medical professionals while maintaining image quality and diagnostic information. 
    A methodology is proposed that involves a literature review, market research, a proof-of-concept phase using maturity steps, testing on real scans, and verification and validation of the technology. Data acquisition, curation, storage and management as well as the business case for thee proposed start-up are discussed. A back-of-the-envelope calculation is performed and shows significant market size and revenue for the start-up. We have chosen to use a  KBNet (Kernel Basis Network
for Image Restoration) for the denoising task. Experimental results using a deep learning model with pre-trained weights have shown promising outcomes, with untapped potential for further improvement through transfer learning techniques. The model evaluated on the test dataset (VinDr-
SpineXR dataset) gives a PSNR (Peak signal-to-noise ratio) of 82.25 dB and a MSE score of 0.0004. Furthermore, stacking grey-scale images along the input
channel dimension utilized temporal information and improves the model performance on video. 
<hr />

## Dicom conversion
The first step in order to process the data is to convert the DICOM files (Digital Imaging and Communications in Medicine). The DICOM standard is widely used in the medical field for storing and transmitting medical images and related data. However, working with DICOM files directly can be challenging for developers and researchers who require more accessible image formats for analysis, visualization, and processing. 


In the notebook [dicom_conversion](dicom_conversion.ipynb) we show how the DICOM files can be converted to .png files. In this notebook we also show steps how to normalize the data, how to downsample it and how to add noise.

<hr />

## Denoising
In the notebook [denoising](denoising.ipynb) we show how to denoising algorithm works. We import the data and convert it to numpy arrays. We load our model with the pretrained weights and we denoise the images. We show the results of the denoising algorithm and we compare it with the original images.

This is first demonstrated for single images. But because we actually want to denoise a sequence of frames we also show how to denoise this. This can be done by denoise every single frame and adding them together. But stacking 3 grayscale images and denoising it as 3 channel images gives better results, because the model can use the temporal information.

<hr />

## Demonstration of the denoising algorithm
The first shown video is composed using the original images. The second video is a simulation of a scenario where the radiation dose is reduced, therefore noise is added. The third and fourth video are the denoised images using the KBNet. The left image is denoised per frame and the right image is denoised using a input of 3 frames.
<p float="left">
  <img src="figures\original.gif" />
  <img src="figures\noised.gif"/> 
</p>

<p float="left">
  <img src="figures\denoised.gif" />
  <img src="figures\denoised_stacked.gif"/> 
</p>

<hr />

## Testing performance
In the notebook [testing.ipynb](testing.ipynb) we show how to test the performance of the denoising algorithm. We use the PSNR (Peak Signal-to-Noise Ratio) and MSE (Mean Squared Error) to test the performance of the denoising algorithm. We test on a test set of 250 images. The results are as follows:

| Dataset       	| PSNR  	|
|---------------	|-------	|
| MNIST         	| 77.93 	|
| VinDr-SpineXR 	| 82.25 	|
| SpineWeb      	| 81.69 	|

<img src="figures\violin.png">

<hr />

## Acknowledgements
* [KBNet](https://github.com/zhangyi-3/KBNet/tree/main)