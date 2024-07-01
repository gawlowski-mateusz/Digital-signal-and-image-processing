import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def salt_and_pepper_noise(file_path):
    # Open the image from the selected file
    image = Image.open(file_path)
    # Load the image into an array
    arr_image = np.asarray(image)
    # Determine the size of the image
    width, height = image.size

    # Defined constants
    # sp = 0.5
    # amount = 0.05

    # Copy the image to an array
    arr_image_salt_pepper = np.copy(arr_image)

    # Create salt and pepper noise
    # num_salt = np.ceil(amount * arr_image.size * sp)
    # coords = [np.random.randint(0, i - 1, int(num_salt)) for i in arr_image.shape]
    # arr_image_salt_pepper[tuple(coords)] = 1

    # num_pepper = np.ceil(amount * arr_image.size * (1. - sp))
    # coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in arr_image.shape]
    # arr_image_salt_pepper[tuple(coords)] = 0

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    # plt.subplot(2, 3, 3)
    # plt.title('Image with "Salt and Pepper" Noise')
    # plt.imshow(arr_image_salt_pepper, cmap='gray', vmin=0, vmax=255)

    print("Which filter to use:\n"
          "[1] Averaging filter with square mask\n"
          "[2] Nonlinear median filter\n"
          "[3] Minimum filter\n"
          "[4] Maximum filter")

    choose = int(input("Your choice: "))

    if choose == 1:
        square_mask_filter(arr_image_salt_pepper)
    elif choose == 2:
        nonlinear_median_filter(arr_image_salt_pepper)
    elif choose == 3:
        minimum_filter(arr_image_salt_pepper)
    elif choose == 4:
        maximum_filter(arr_image_salt_pepper)
    else:
        print("Invalid choice")


def square_mask_filter(arr_image_salt_pepper):
    # Filtering with a square mask
    new_image_mask_3x3 = cv2.blur(arr_image_salt_pepper, (3, 3))
    new_image_mask_9x9 = cv2.blur(arr_image_salt_pepper, (9, 9))
    new_image_mask_15x15 = cv2.blur(arr_image_salt_pepper, (15, 15))

    plt.subplot(2, 3, 4)
    plt.title('"Salt and Pepper" Noise, 3x3 Mask')
    plt.imshow(new_image_mask_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('"Salt and Pepper" Noise, 9x9 Mask')
    plt.imshow(new_image_mask_9x9, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('"Salt and Pepper" Noise, 15x15 Mask')
    plt.imshow(new_image_mask_15x15, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Averaging Filter with Square Mask", fontsize=16)
    plt.show()


def nonlinear_median_filter(arr_image_salt_pepper):
    # Median filtering
    new_image_salt_pepper = np.array(arr_image_salt_pepper, dtype=np.uint8)
    new_image_mask_3x3 = cv2.medianBlur(new_image_salt_pepper, 3)
    new_image_mask_9x9 = cv2.medianBlur(new_image_salt_pepper, 9)
    new_image_mask_15x15 = cv2.medianBlur(new_image_salt_pepper, 15)

    plt.subplot(2, 3, 4)
    plt.title('"Salt and Pepper" Noise, 3x3 Mask')
    plt.imshow(new_image_mask_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('"Salt and Pepper" Noise, 9x9 Mask')
    plt.imshow(new_image_mask_9x9, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('"Salt and Pepper" Noise, 15x15 Mask')
    plt.imshow(new_image_mask_15x15, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Median Filtering", fontsize=16)
    plt.show()


def minimum_filter(arr_image_salt_pepper):
    # Applying minimum filter
    min_filtered_3x3 = cv2.erode(arr_image_salt_pepper, np.ones((3, 3)))
    min_filtered_5x5 = cv2.erode(arr_image_salt_pepper, np.ones((5, 5)))
    min_filtered_7x7 = cv2.erode(arr_image_salt_pepper, np.ones((7, 7)))

    plt.subplot(2, 3, 4)
    plt.title('"Salt and Pepper" Noise, 3x3 Minimum Filter')
    plt.imshow(min_filtered_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('"Salt and Pepper" Noise, 5x5 Minimum Filter')
    plt.imshow(min_filtered_5x5, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('"Salt and Pepper" Noise, 7x7 Minimum Filter')
    plt.imshow(min_filtered_7x7, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Minimum Filtering", fontsize=16)
    plt.show()


def maximum_filter(arr_image_salt_pepper):
    # Applying maximum filter
    max_filtered_3x3 = cv2.dilate(arr_image_salt_pepper, np.ones((3, 3)))
    max_filtered_5x5 = cv2.dilate(arr_image_salt_pepper, np.ones((5, 5)))
    max_filtered_7x7 = cv2.dilate(arr_image_salt_pepper, np.ones((7, 7)))

    plt.subplot(2, 3, 4)
    plt.title('"Salt and Pepper" Noise, 3x3 Maximum Filter')
    plt.imshow(max_filtered_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('"Salt and Pepper" Noise, 5x5 Maximum Filter')
    plt.imshow(max_filtered_5x5, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('"Salt and Pepper" Noise, 7x7 Maximum Filter')
    plt.imshow(max_filtered_7x7, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Maximum Filtering", fontsize=16)
    plt.show()


def read_file():
    import tkinter.filedialog
    window = tkinter.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    file_path = tkinter.filedialog.askopenfilename()

    return file_path


def main():
    file_path = read_file()

    if file_path:
        salt_and_pepper_noise(file_path)
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
