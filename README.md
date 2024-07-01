# Digital-signal-and-image-processing

## Description

This project demonstrates various functionalities for processing both digital signals and images using Python libraries such as NumPy, SciPy, Matplotlib, Seaborn, PIL (Python Imaging Library), and OpenCV. It includes operations like visualizing signals, Fourier transforms, image manipulation, and advanced image enhancement techniques.

## Installation

Ensure you have Python 3.x installed on your system along with the following dependencies:

- `numpy`
- `scipy`
- `matplotlib`
- `seaborn`
- `pillow`
- `opencv-python`

You can install these dependencies using pip:

```bash
pip install numpy scipy matplotlib seaborn pillow opencv-python
```

## Usage

1. **Run the Script:**
   - Clone this repository to your local machine.
   - Navigate to the project directory.

2. **Execute the Script:**
   - Run the main script to interact with the functionalities:

     ```bash
     python main.py
     ```

3. **Functionality Options:**
   - **Display Image:** View the selected image.
   - **Draw Gray Level Plot:** Plot gray level changes along a horizontal or vertical line in the image.
   - **Snip Image Area:** Extract a rectangular area (snippet) from the image.
   - **Multiply by Constant:** Apply multiplication by a constant factor to the image.
   - **Logarithmic Transformation:** Apply a logarithmic transformation to the image.
   - **Grayscale Dynamics:** Adjust grayscale dynamics based on parameters `m` and `e`.
   - **Gamma Correction:** Apply gamma correction to the image based on parameters `y` and `c`.
   - **Histogram Equalization:** Enhance image contrast using histogram equalization.
   - **Local Histogram Equalization:** Enhance local image contrast using adaptive histogram equalization.
   - **Local Statistics-Based Enhancement:** Enhance image using local statistics-based enhancement.
   - **Salt and Pepper Noise:** Introduce salt and pepper noise to the image and filter it using various techniques.
   - **Averaging Filter:** Apply averaging filtering to smooth the image.
   - **Gaussian Filter:** Apply Gaussian filtering to smooth the image.
   - **Edge Detection - Sobel Mask Filter:** Detect edges in the image using the Sobel operator.
   - **Edge Detection - Laplacian:** Detect edges in the image using the Laplacian operator.
   - **Unsharp Masking:** Enhance image details using unsharp masking.
   - **High Boost:** Enhance image details using high boost filtering.
   - **Spatial Filtering:** Enhance image details using a combination of Gaussian smoothing and Laplacian operator.

## Example

- **Applying Spatial Filtering Techniques:**

  ```python
  python main.py
  ```

  Choose an option:
  ```
  [1] Spatial Filtering
  ```

  After selecting the option, the script will prompt you to choose an image file and then apply the spatial filtering technique.

## Features

- **Signal Processing:**
  - Fourier Transforms
  - Signal Visualization

- **Image Processing:**
  - Loading and Displaying Images
  - Drawing Gray Level Plots
  - Snipping Image Areas
  - Multiplication by Constant
  - Logarithmic Transformation
  - Grayscale Dynamics Adjustment
  - Gamma Correction
  - Histogram Equalization
  - Local Histogram Equalization
  - Local Statistics-Based Enhancement
  - Salt and Pepper Noise Addition and Filtering
  - Averaging and Gaussian Filters for Image Smoothing
  - Edge Detection using Sobel and Laplacian Operators
  - Unsharp Masking and High Boost Filtering for Image Enhancement
  - Spatial Filtering using Gaussian Smoothing and Laplacian Operator

---

## Example Code Explanation

The code for part 12 introduces spatial filtering, a technique that enhances image details using Gaussian smoothing followed by the Laplacian operator:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np


def spatial_filtering(image):
    # Step 1: Gaussian Smoothing
    kernel_size = 5
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Step 2: Laplacian Operator
    laplacian_image = cv2.Laplacian(smoothed_image, cv2.CV_64F)
    
    # Convert Laplacian image to uint8
    laplacian_image = np.uint8(np.absolute(laplacian_image))

    # Step 3: Add Laplacian to the Original Image
    enhanced_image = cv2.addWeighted(image, 1.0, laplacian_image, 1.0, 0.0)

    # Display original and enhanced images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(enhanced_image, cmap='gray')
    plt.title('Enhanced Image')

    plt.show()


def read_file():
    import tkinter.filedialog
    import tkinter as tk

    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    file_path = tkinter.filedialog.askopenfilename()

    return file_path


def main():
    file_path = read_file()

    if file_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        spatial_filtering(image)
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
```

## Explanation

1. **Spatial Filtering (`spatial_filtering`):**
   - Opens an image file and converts it into grayscale using OpenCV (`cv2.imread` with `cv2.IMREAD_GRAYSCALE`).
   - Applies Gaussian smoothing to the image using `cv2.GaussianBlur`.
   - Applies the Laplacian operator to the smoothed image using `cv2.Laplacian`.
   - Converts the resulting Laplacian image to `uint8` format.
   - Adds the Laplacian-enhanced image to the original image using `cv2.addWeighted`.
   - Displays the original image and the enhanced image side by side using Matplotlib.

2. **Main Function (`main`):**
   - Prompts the user to select an image file.
   - If a file is selected, it reads the image and applies the spatial filtering technique.
   - If no file is selected, it prints a message indicating that no file was chosen.

## Conclusion

This part adds a spatial filtering technique to your project, enhancing image details by combining Gaussian smoothing with the Laplacian operator. Spatial filtering is useful for sharpening images and highlighting edges, making it a valuable tool in image processing and computer vision applications.