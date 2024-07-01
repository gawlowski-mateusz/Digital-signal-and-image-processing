import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def averaging_filter(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert("L")
    # Load the image into an array
    arr_image = np.asarray(image)

    # Averaging filtering
    new_image_mask_3x3 = cv2.blur(arr_image, (3, 3))
    new_image_mask_9x9 = cv2.blur(arr_image, (9, 9))
    new_image_mask_15x15 = cv2.blur(arr_image, (15, 15))

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 4)
    plt.title('Averaging Filter, 3x3')
    plt.imshow(new_image_mask_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('Averaging Filter, 9x9')
    plt.imshow(new_image_mask_9x9, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('Averaging Filter, 15x15')
    plt.imshow(new_image_mask_15x15, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Averaging Filter", fontsize=16)
    plt.show()


def gaussian_filter(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert("L")
    # Load the image into an array
    arr_image = np.asarray(image)

    # Gaussian filtering
    new_image_mask_3x3 = cv2.GaussianBlur(arr_image, (3, 3), 0)
    new_image_mask_9x9 = cv2.GaussianBlur(arr_image, (9, 9), 0)
    new_image_mask_15x15 = cv2.GaussianBlur(arr_image, (15, 15), 0)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 4)
    plt.title(' Gaussian Filter, 3x3')
    plt.imshow(new_image_mask_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('Gaussian Filter, 9x9')
    plt.imshow(new_image_mask_9x9, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('"Gaussian Filter, 15x15')
    plt.imshow(new_image_mask_15x15, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Gaussian Filter", fontsize=16)
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
        print("[1] Averaging Filter")
        print("[2] Gaussian Filter")

        choice = int(input("Your choice: "))

        if choice == 1:
            averaging_filter(file_path)
        elif choice == 2:
            gaussian_filter(file_path)
        else:
            print("Invalid choice")
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
