#https://huggingface.co/Salesforce/blip-image-captioning-base

import os
import csv
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Define the main folder containing all subfolders with images
main_folder = '/root/text2storyboard/dataset/commercial_storyboard'

# Check if the main folder exists
if not os.path.exists(main_folder):
    print(f"Directory {main_folder} does not exist.")
else:
    # Iterate over all subfolders in the main folder
    for subfolder in os.listdir(main_folder):
        image_folder = os.path.join(main_folder, subfolder)
        
        if os.path.isdir(image_folder):
            folder_name = os.path.basename(image_folder)

            # Create the CSV file path
            csv_file_path = os.path.join('/root/text2storyboard/dataset/commercial_storyboard_caption', f'{folder_name}.csv')

            # List all files in the subfolder
            image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

            # Open the CSV file for writing
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the header
                writer.writerow(['Image Path', 'Conditional Caption', 'Unconditional Caption'])

                for image_file in image_files:
                    # Construct the full path to the image file
                    image_path = os.path.join(image_folder, image_file)

                    try:
                        # Open the image
                        raw_image = Image.open(image_path).convert('RGB')

                        # Conditional image captioning
                        text = "a storyboard of"
                        inputs = processor(raw_image, text, return_tensors="pt")

                        out = model.generate(**inputs)
                        caption_conditional = processor.decode(out[0], skip_special_tokens=True)

                        # Unconditional image captioning
                        inputs = processor(raw_image, return_tensors="pt")

                        out = model.generate(**inputs)
                        caption_unconditional = processor.decode(out[0], skip_special_tokens=True)

                        # Write the image filename and captions to the CSV file
                        writer.writerow([image_path, caption_conditional, caption_unconditional])

                    except Exception as e:
                        print(f"Error processing {image_file}: {e}")

            print(f"Captions saved to {csv_file_path}")
