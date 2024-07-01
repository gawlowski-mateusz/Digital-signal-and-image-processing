import tkinter.filedialog
import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image
        

def draw_gray_plot(file_path):
    # Opening the image from the selected file
    image = Image.open(file_path).convert("L")
    # Loading the image into an array
    arr_image = np.asarray(image)
    # Determining the size of the image
    width, height = image.size

    # Choosing the line option
    print("Plot:\n"
          "[1] From horizontal line\n"
          "[2] From vertical line")

    choose = int(input("Your choice: "))

    if choose == 1:
        y = int(input("Enter y (0," + str(height - 1) + ") "))
        # Saving the pixel values from the specified horizontal line into an array
        one_gray_line_array = arr_image[y, :]
    elif choose == 2:
        x = int(input("Enter x (0," + str(width - 1) + ") "))
        # Saving the pixel values from the specified vertical line into an array
        one_gray_line_array = arr_image[:, x]


    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.plot(one_gray_line_array,'b')
    plt.title('Gray level changes plot')
    plt.xlabel('Pixel number')
    plt.ylabel('Gray level')
    plt.show()

    plt.show()


def snipping_area(file_path):
    # Opening the image from the selected file
    image = Image.open(file_path).convert('RGB')
    # Loading the image into an array
    arr_image = np.asarray(image)
    # Determining the size of the image
    width, height = image.size

    print("Enter the starting point of the snip: ")
    y1 = int(input("Enter x1 (0," + str(height - 1) + ") "))
    x1 = int(input("Enter y1 (0," + str(width - 1) + ") "))
    print("Enter the ending point of the snip: ")
    y2 = int(input("Enter x2 (0," + str(height - 1) + ") "))
    x2 = int(input("Enter y2 (0," + str(width - 1) + ") "))

    # Creating an array of appropriate size
    arr_snipping_area = numpy.zeros((x2 - x1, y2 - y1, 3), dtype=np.uint8)

    # Snipping the appropriate fragment into the array
    for i in range(x2 - x1):
        for j in range(y2 - y1):
            arr_snipping_area[i, j] = arr_image[x1 + i, y1 + j]

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('Snipped image')
    plt.imshow(arr_snipping_area, cmap='gray', vmin=0, vmax=255)

    plt.show()
    new_image = Image.fromarray(arr_snipping_area, 'RGB')
    new_image.save('new.png')
    new_image.show()


def read_file():
    window = tkinter.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    file_path = tkinter.filedialog.askopenfilename()

    return file_path


def open_image(file_path):
    if file_path is None:
        print("File path is null")
    else:
        image = Image.open(file_path)
        arr_image = np.asarray(image)

        plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)
        plt.show()
        

def main():
    file_path = read_file()

    if file_path:
        print("Choose an option:")
        print("[1] Display image")
        print("[2] Draw gray level plot")
        print("[3] Snip image area")

        choice = int(input("Your choice: "))

        if choice == 1:
            open_image(file_path)
        elif choice == 2:
            draw_gray_plot(file_path)
        elif choice == 3:
            snipping_area(file_path)
        else:
            print("Invalid choice")
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
