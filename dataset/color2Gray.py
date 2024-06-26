import os
import cv2


def convert_to_grayscale(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            color_image_path = os.path.join(input_dir, filename)
            gray_image_path = os.path.join(output_dir, filename)

            # Load the color image
            color_image = cv2.imread(color_image_path)

            if color_image is None:
                print(f"Warning: Unable to read image file {color_image_path}")
                continue

            # Convert the color image to grayscale
            gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

            # Save the grayscale image
            cv2.imwrite(gray_image_path, gray_image)
            print(f"Grayscale image saved to {gray_image_path}")


'''def process_directories(base_dir):
    for dir_name in os.listdir(base_dir):
        if dir_name.startswith('color-'):
            input_dir = os.path.join(base_dir, dir_name)
            output_dir = os.path.join(base_dir, 'gray-' + dir_name[6:])
            convert_to_grayscale(input_dir, output_dir)


# Use the current directory as the base directory
base_directory_path = os.path.abspath('./')
process_directories(base_directory_path)
'''
convert_to_grayscale("./color-rough", "./gray-rough")

