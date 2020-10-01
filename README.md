# Nepalireader

It is a recognizer developed using Convolutional Neural Network. It is used to recognize the Nepali characters from their images.<br/><br/>

<b>Design:</b><br/>
Front-end: Tkinter<br/>
Back-end: Tensorflow<br/>
Core-language: Python<br/><br/>

# Preprocessing:
The preprocessing module involves several other sub modules like Grayscale Conversion, Gaussian Blurring, Contrast Stretching and Binarization.<br/><br/>

<b>Grayscale Conversion</b><br/>
Grayscale conversion can be done in many ways to convert colorful(RGB) images into
monochrome(Gray) form. We have used luminosity method, a weighted mean method
suitable for human eye perception, to convert color image into gray and is carried out
by formula:<br/><br/>

GrayV alue = 0.21 ∗ Red + 0.72 ∗ Green + 0.07 ∗ Blue<br/><br/>

Steps carried out in this process are shown in algorithm below.<br/><br/>

Algorithm:<br/>
1. Read an RGB image with its height and width also.<br/>
2. For any pixel, read the intensity values of Red, Blue and Green channels as R, B
and G respectively.<br/>
3. Calculate the gray value, Gr = 0.21 ∗ R + 0.72 ∗ G + 0.07 ∗ B<br/>
4. Set, R = B = G = Gr <br/>
5. Repeat steps from 2 to 4 until all pixels are scanned <br/><br/>


<b>Gaussian Blurring</b><br/>
Blurring can also be stated as smoothing because this technique helps to smooth the
edges distorted in the input image. Gaussian blur is based on the normal distribution of
intensity of a pixel in the image 2D-plane. The 2D-Gaussian function for calculation of
weight of pixels in a window is given by,<br/><br/>

![gaussian_blur_formula](https://github.com/samirkhanal35/Nepalireader/blob/master/gaussian_blur_formula.png)

<br/><br/>

Where, x and y as (x, y) represent the pixel vector in a window and σ is the standard
deviation of the normal distribution which is determined by using value of radius r
using the relation,<br/><br/>

![gaussian_blur_radius](https://github.com/samirkhanal35/Nepalireader/blob/master/gaussian_blur_radius.png)

<br/><br/>

We have implemented Gaussian blur for 3x3 window i.e. radius r = 2, which results
the standard deviation to be σ = 1.3674.<br/><br/>

Algorithm:<br/>
1. Read the output image from previous process with its height and width.<br/>
2. For any 3x3 window, calculate weights of all pixels using formula of equation. <br/>
3. Calculate products of pixel values and their respective weights.<br/>
4. Calculate sum of all products and set CentralP ixelV alue = sum, go to next pixel window.<br/>
5. Repeat steps 2 to 4 until all pixels are scanned. <br/><br/>

<b>Contrast Stretching</b><br/>
Contrast stretching (often called normalization) is a simple image enhancement tech-
nique that attempts to improve the contrast in an image by stretching the range of in-
tensity values it contains to span a desired range of values, e.g. the full range of pixel
values that the image type concerned allows.<br/><br/>
The general technique, for mono-channel image, uses range [Imin, Imax] of intensity-
levels. Where, minimum intensity level present in the image is stretched to Imin and
maximum intensity level is stretched to Imax.<br/>
General formula for contrast stretching is,<br/><br/>

![contrast_general](https://github.com/samirkhanal35/Nepalireader/blob/master/contrast_general.png)

<br/><br/>
Where, r = pixel intensity value; rmin = minimum intensity with least number of
pixels; rmax = maximum intensity with highest number of pixels; s = new pixel
intensity value.<br/><br/>
For this project, we have used range of [0, 255] i.e. Imin = 0 and Imax = 255. So,
the formula becomes,<br/><br/>

![contrast_simplified](https://github.com/samirkhanal35/Nepalireader/blob/master/contrast_simplified.png)


<br/><br/>
After calculating value of s for each value of r, the pixels with intensity value r is
assigned with corresponding value of s.<br/><br/>

<b>Binarization</b><br/>
An image is called binary if the intensity value of each pixel is either 255 (white color)
or 0 (black color) i.e. logically binary values either 1 (high) or 0 (low) respectively.
27Hence, the process of conversion is called binarization.<br/><br/>
We have used simple thresholding method where threshold value for all pixels of image
is same as the input image is expected to have light background and dark foreground.<br/><br/>

Algorithm:<br/>
1. Read the image output from previous process with its height and width.<br/>
2. For any pixel: Set pixel v alue = 255, if pixel v alue >= threshold v alue OR Set
pixel v alue = 0, if pixel v alue < threshold v alue.<br/>
3. Repeat steps 2 until all pixels are scanned.<br/><br/>


# Segmentation

The segmentation process that extracts constituent symbols images from a word for Devanagari
script follows the following major tasks:<br /><br />
Task 1: Remove the header line.<br />
Task 2: Extract subimages that are vertically separate from their neighbors. These subimages may contain more than one connected component.<br />
Task 3: Select the subimages that need further segmentation due to the presence of lower modifiers. A selection criterion is required for selecting these.<br />
Task 4: Separate the lower modifiers from the subimages selected in step 3.<br />
Task 5: Select the subimages that contain conjuncts characters. A selection criterion is required for selecting these.<br />
Task 6: Segment the conjunct subimages selected in step 5 into constituent consonant subimages.<br /><br />

![segmentation](https://github.com/samirkhanal35/Nepalireader/blob/master/segmentation.png)<br /><br />


# Recognition

The segmented images are ordered according to their positions in the word for better combination of recognized characters.<br />

For recognition, we have used three different CNN models. One for upper modifier, one for lower modefier and one for core characters.
<br/><br/>

# Transliteration

For transliteration we have used IPA(International Phonetic Alphabet) standards for Transliteration and our personal rules that we proposed for better phonetic arrangements of vowels.

# Outputs
![output_1](https://github.com/samirkhanal35/Nepalireader/blob/master/nepali_reader_op.png)

![output_2](https://github.com/samirkhanal35/Nepalireader/blob/master/nepali_reader_op1.png)

# Installation and Execution

To Install(Please search and follow installation according to your operating system):<br /><br />

<b>Prerequisites:</b><br />

Python<br />
For linux users: sudo apt-get install python3<br />
Then install pip: apt install python3-pip<br />
For other users, you can follow <a href="https://www.python.org/downloads/">this</a> link.<br /><br />

OpenCV<br />
For linux users: pip install opencv-python<br /><br /><br />

Tensorflow<br />
Follow <a href="https://www.tensorflow.org/install/pip">this</a> link.<br /><br />

Keras<br />
For linux users: pip install Keras<br /><br />

Image<br />
For linux users: pip install image<br /><br />

Numpy<br />
Follow <a href="https://numpy.org/install/">this</a> link.<br /><br />

Pandas<br />
Follow <a href="https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html">this</a> link.<br /><br />

Tkinter<br />
For linux users: sudo apt-get install python3-tk<br /><br />

For installation guides and problems you can go to their respective wesites.<br />

After installation of <b>Prerequisites</b> , you can clone or download the repo and run gui.py file to run the program.<br />
