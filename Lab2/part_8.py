import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def local_histogram_equalization(arr_image):
    # Local histogram equalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized_image = clahe.apply(arr_image)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(arr_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Local Histogram Equalization')

    plt.show()


def local_statistics_based_enhancement(arr_image):
    # Local statistics-based enhancement
    kernel = np.ones((5, 5), np.float32) / 25
    smoothed_image = cv2.filter2D(arr_image, -1, kernel)
    enhanced_image = cv2.addWeighted(arr_image, 1.5, smoothed_image, -0.5, 0)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(arr_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(enhanced_image, cmap='gray')
    plt.title('Local Statistics-Based Enhancement')

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

        print("Choose an option:")
        print("[1] Local Histogram Equalization")
        print("[2] Local Statistics-Based Enhancement")

        choice = int(input("Your choice: "))

        if choice == 1:
            local_histogram_equalization(image)
        elif choice == 2:
            local_statistics_based_enhancement(image)
        else:
            print("Invalid choice")
    else:
        print("No file selected")

if __name__ == "__main__":
    main()