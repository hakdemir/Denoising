# MRI-Denoising using KBNet

<img src="figures\denoised.png">

[Lemar Abdi](https://nl.linkedin.com/in/lemar-abdi-30816317a),
[Halil Akdemir](linkedin.com/in/hakdemir),
[Thodoris Chronopoulos]()

<hr />

> **Abstract:**  This report discusses the development of a deep learning algorithm for real-time denoising of low-dose X-ray images in C-arms, which will be translated into a start-up.
The goal is to reduce radiation exposure for patients and especially medical professionals while maintaining image quality and diagnostic information.
A methodology is proposed that involves a literature review, market research, a proof-of-concept phase using maturity steps, testing on real scans, and verification and validation of the technology.
The report also discusses various deep learning-based denoising techniques such as CNNs, autoencoders, U-Net architecture and transformers.
We have chosen to use a NAFNet (Nonlinear Activation Free Network) baseline for the denoising task. Data acquisition, curation, storage and management as well as the business case for thee proposed start-up are discussed.
A back-of-the-envelope calculation is performed and shows significant market size and revenue for the start-up. 

<hr />

## Dicom conversion
The first step in order to process the data is to convert the DICOM files (Digital Imaging and Communications in Medicine). The DICOM standard is widely used in the medical field for storing and transmitting medical images and related data. However, working with DICOM files directly can be challenging for developers and researchers who require more accessible image formats for analysis, visualization, and processing. 

In the notebook [dicom_conversion](dicom_conversion.ipynb). We show how the DICOM files can be converted to .png files. In this notebook we also show steps how to normalize the data, how to downsample it and how to add noise.

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



## Acknowledgements
* [KBNet](https://github.com/zhangyi-3/KBNet/tree/main)