import tkinter.filedialog
import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image


def aligning_the_histogram(file_path):
    # Open the image from the selected file
    image = Image.open(file_path).convert('L')
    # Load the image into an array
    arr_image = np.asarray(image)
    # Determine the size of the image
    width, height = image.size

    # Create a 256-element array filled with zeros
    image_histogram = numpy.zeros(256, dtype=int)

    # Calculate how many pixels have a given value 0-255
    for i in range(height - 1):
        for j in range(width - 1):
            image_histogram[arr_image[i, j]] += 1

    # Create an array of empirical cumulative distribution functions
    distributor = numpy.zeros(256, dtype=float)

    # Calculate the number of pixels on the screen
    number_of_pixels = width * height

    # Calculate the cumulative distribution
    sum_gray = 0.0
    for i in range(255):
        sum_gray += (image_histogram[i] / number_of_pixels)
        distributor[i] += sum_gray

    d0min = int(0)
    for i in range(255):
        if distributor[i] != 0:
            break
        else:
            d0min += 1

    # Create the LUC table
    luc_table = numpy.zeros(256, dtype=float)

    for i in range(256):
        luc_table[i] = int(((distributor[i] - distributor[d0min]) / (1 - distributor[d0min])) * (256 - 1))

    # Create an array the size of the image
    new_arr_image = numpy.full_like(arr_image, 0)

    # Algorithm for selecting pixels for the new image
    for i in range(height - 1):
        for j in range(width - 1):
            new_arr_image[i, j] = luc_table[arr_image[i, j]]

    # Create an array for the new histogram
    new_image_histogram = numpy.zeros(256, dtype=int)

    for i in range(height - 1):
        for j in range(width - 1):
            new_image_histogram[new_arr_image[i, j]] += 1

    # Create plots
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Image Histogram")
    plt.plot(image_histogram, 'b')

    plt.subplot(2, 2, 3)
    plt.title('Image after Histogram Equalization')
    plt.imshow(new_arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 4)
    plt.title("Image Histogram")
    plt.plot(new_image_histogram, 'b')

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
        print("Running Histogram Equalization...")
        aligning_the_histogram(file_path)
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
