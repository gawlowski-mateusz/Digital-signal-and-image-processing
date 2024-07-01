import cv2 as cv
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def sobel_mask_filter(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert("L")
    # Load the image into an array
    arr_image = np.asarray(image)

    # Edge detection
    sobel_x = cv.Sobel(arr_image, -1, 1, 0, ksize=3)
    sobel_y = cv.Sobel(arr_image, -1, 0, 1, ksize=3)

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 3, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 3, 2)
    plt.title('Sobel X')
    plt.imshow(sobel_x, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 3, 3)
    plt.title('Sobel Y')
    plt.imshow(sobel_y, cmap='gray', vmin=0, vmax=255)
    plt.show()


def laplacian(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert("L")
    # Load the image into an array
    arr_image = np.asarray(image)

    laplac3 = cv.Laplacian(arr_image, -1, ksize=3)
    laplac5 = cv.Laplacian(arr_image, -1, ksize=5)
    laplac11 = cv.Laplacian(arr_image, -1, ksize=11)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title('3x3 Mask')
    plt.imshow(laplac3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 3)
    plt.title('5x5 Mask')
    plt.imshow(laplac5, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 4)
    plt.title('11x11 Mask')
    plt.imshow(laplac11, cmap='gray', vmin=0, vmax=255)
    plt.show()


def unsharp_masking(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert("L")
    # Load the image into an array
    arr_image = np.asarray(image)

    # Applying unsharp masking
    blurred = cv.GaussianBlur(arr_image, (5, 5), 10.0)
    sharpened = cv.addWeighted(arr_image, 1.5, blurred, -0.5, 0)

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('Unsharp Masking')
    plt.imshow(sharpened, cmap='gray', vmin=0, vmax=255)
    plt.show()


def high_boost(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert("L")
    # Load the image into an array
    arr_image = np.asarray(image)

    # Applying high boost filter
    blurred = cv.GaussianBlur(arr_image, (5, 5), 10.0)
    high_boost = cv.addWeighted(arr_image, 1.5, blurred, -0.5, 0)

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('High Boost')
    plt.imshow(high_boost, cmap='gray', vmin=0, vmax=255)
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
        print("Choose an option:")
        print("[1] Sobel Mask Filter")
        print("[2] Laplacian")
        print("[3] Unsharp Masking")
        print("[4] High Boost")

        choice = int(input("Your choice: "))

        if choice == 1:
            sobel_mask_filter(file_path)
        elif choice == 2:
            laplacian(file_path)
        elif choice == 3:
            unsharp_masking(file_path)
        elif choice == 4:
            high_boost(file_path)
        else:
            print("Invalid choice")
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
