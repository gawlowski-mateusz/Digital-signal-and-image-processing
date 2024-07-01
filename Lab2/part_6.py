import tkinter.filedialog
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def multiplication_by_constant(file_path):
    image = Image.open(file_path).convert('L')
    arr_image = np.asarray(image)
    c = float(input("Enter constant c: "))
    new_image = arr_image * c

    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('Image after multiplication by constant ' + str(c))
    plt.imshow(new_image, cmap='gray', vmin=0, vmax=255)

    plt.show()


def logarithmic_transformation(file_path):
    image = Image.open(file_path).convert('L')
    arr_image = np.asarray(image)
    c = float(input("Enter constant c: "))

    # Apply logarithmic transformation
    # np.log1p is used for log(1 + r)
    new_image = c * np.log1p(arr_image)

    plt.figure(figsize=(15, 10))
    
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('Logarithmic Transformation')
    plt.imshow(new_image, cmap='gray', vmin=0, vmax=255)

    plt.show()


def dynamics_of_grayscale(file_path):
    image = Image.open(file_path).convert('L')
    arr_image = np.asarray(image)
    width, height = image.size

    m = 0.35
    e = 8.0

    new_arr_image = np.full_like(arr_image, 0)

    for i in range(height - 1):
        for j in range(width - 1):
            if arr_image[i, j] == 0:
                new_arr_image[i, j] = arr_image[i, j]
            else:
                new_arr_image[i, j] = (255.0 / (1.0 + (m / (arr_image[i, j] / 255.0)) ** e))

    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('m = ' + str(m) + ', e = ' + str(e))
    plt.imshow(new_arr_image, cmap='gray', vmin=0, vmax=255)

    plt.show()

def gamma_correction(file_path):
    image = Image.open(file_path).convert('L')
    arr_image = np.asarray(image)
    width, height = image.size

    y = 1.2
    c = 0.25

    new_arr_image = np.full_like(arr_image, 0)
    new_arr_image = (arr_image ** y) * c

    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('y = ' + str(y) + ', c = ' + str(c))
    plt.imshow(new_arr_image, cmap='gray', vmin=0, vmax=255)

    plt.show()


def read_file():
    window = tkinter.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    file_path = tkinter.filedialog.askopenfilename()

    return file_path


def main():
    file_path = read_file()

    if file_path:
        print("Choose an option:")
        print("[1] Multiply by constant")
        print("[2] Logarithmic transformation")
        print("[3] Grayscale dynamics")
        print("[4] Gamma correction")

        choice = int(input("Your choice: "))

        if choice == 1:
            multiplication_by_constant(file_path)
        elif choice == 2:
            logarithmic_transformation(file_path)
        elif choice == 3:
            dynamics_of_grayscale(file_path)
        elif choice == 4:
            gamma_correction(file_path)
        else:
            print("Invalid choice")
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
