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
