print('crawl.py operated')

import os
import time
import random as rd

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm

def url_crawl(num_images:int,
              search_url:str,
              first_image_full_xpath:str,
              wide_image_class:str,
              next_button:str
    ) -> list:
    '''
    Input:  num_images : number of images to crawl,
            wide_image_class : class of the widen image,
            next_button : xpath of the next button
    Process: Crawl the image urls
    Output: List of image urls and failed index
    '''
    driver = webdriver.Edge() # Use if you want to use Edge
    # driver = webdriver.Chrome() # Use if you want to use Chrome
    driver.get(search_url)

    time.sleep(1)

    # Initialize list and number of images to crawl
    image_urls = []
    failed_index = []
    i = 0

    # Find the first image
    images = driver.find_elements(By.XPATH, value=first_image_full_xpath)
    
    # While loop to crawl the image urls
    while i < num_images:
        try:
            # Find the first
            image = driver.find_element(By.CLASS_NAME, value=wide_image_class)
            image_url = image.get_attribute('src')
            print(f'{i}th Image URL: {image_url}')
            if image_url is None or image_url in image_urls:
                failed_index.append(i)
            else:
                image_urls.append(image_url)
        except:
            failed_index.append(i)
            print('No image found')

        # Print the next button.
        button = driver.find_element(By.XPATH, value=next_button)
        button.click()

        # Add 1 to i
        i += 1
        time.sleep(rd.uniform(0.3, 1))

    return image_urls, failed_index

def save_image(image_urls:list,
               download_path:str
               ) -> list:
    '''
    Input:  image_urls : list of image urls,
            download_path : path to save the images
    Process: Save the images
    Output: List of success urls and failed urls
    '''
    failed_urls = []
    # Save images if there are any available images
    if len(success_urls) != len(image_urls):

        # Save each images
        for i, image_url in enumerate(tqdm(image_urls, desc="Downloading images")):
            # Set file name and path
            file_name = f'pinterest_whole_{i}.jpg'
            file_path = os.path.join(download_path, file_name)

            # Call image and save
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                # Save the success urls
                success_urls.append(image_url)
            else:
                # Save the failed urls
                failed_urls.append(image_url)
                print(f'Image not saved')
            time.sleep(0.5)
    else:
        print('All images saved')

    return success_urls, failed_urls


# Set variables
num_images = 750 # Change this value by the number of images you want to crawl.
# search_url = 'https://www.google.com/search?sca_esv=ff007314d2b9c596&sca_upv=1&q=pinterest+sketch+storyboard&uds=ADvngMhdznG_IlcWLRNGbp-A0e5TDeEPgSfyAlOO7AeIkoWFbSVV3wQ_U_YTTq9ClGIotncR6AMXGrPEWniFsV2XivR95asnpjxDRMnDZHRn_HM4tb6ffRMUQxZR9EvswBRWHrGLR2BD9ZGJmUJVe_TqJhcEHl4qunFCiRieP38O3JG7K9jSlctJJHRZ27ERI2RojUAUWNZN9fhJXLPwGe4lMCuWlHlXCyMzdR147BC9gWMLCYHAx99GaCw-khN9Hk7dmv-e1YHVbqTuajBd7jrL6qxCLBay0w&udm=2&prmd=isvnbmz&sa=X&ved=2ahUKEwi8t7HWjP6FAxUimVYBHVZsAdIQtKgLegQIDBAB&biw=1488&bih=804&dpr=1.25#vhid=Df6cNVQZRReBxM&vssid=mosaic'
search_url = 'https://www.google.com/search?q=sketch+storyboard&sca_esv=5f0b2fde22dc3a3d&sca_upv=1&udm=2&biw=1488&bih=804&ei=Kiw8ZoHlIIWlvr0P5sCmoA8&ved=0ahUKEwiBorDHuv-FAxWFkq8BHWagCfQQ4dUDCBA&uact=5&oq=sketch+storyboard&gs_lp=Egxnd3Mtd2l6LXNlcnAiEXNrZXRjaCBzdG9yeWJvYXJkMgcQABiABBgTMgcQABiABBgTMggQABgTGAgYHjIIEAAYExgHGB4yCBAAGBMYBxgeMggQABgTGAgYHjIIEAAYExgIGB4yCBAAGBMYCBgeMggQABgTGAgYHjIIEAAYExgIGB5IqAVQAFgAcAB4AJABAJgBXqABXqoBATG4AQPIAQD4AQGYAgGgAmqYAwCSBwMwLjGgB_cG&sclient=gws-wiz-serp#vhid=lF7SwS1rjZbnYM&vssid=mosaic'

# File path to save
# download_path = 'C:/Users/dwdra/documents/2023/4_YBIGTA/2_24-1/2_team_project/2_Conference/2_data_set/dataset/raw/google_crawl'
download_path = 'C:/Users/dwdra/documents/2023/4_YBIGTA/2_24-1/2_team_project/2_Conference/2_data_set/dataset/raw/pinterest'
next_button = '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[1]/div/div[2]/button[2]'
first_image_full_xpath = '/html/body/div[4]/div/div[13]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/h3/a/div/div/div/g-img/img'
wide_image_class = 'sFlh5c.pT0Scc.iPVvYb'
success_urls = [] # Only for preventing error


image_urls, failed_index = url_crawl(num_images, search_url, first_image_full_xpath, wide_image_class, next_button)

print(f'length of image_urls: {len(image_urls)}')
for url in image_urls:
    print(url)

success_urls, failed_urls = save_image(image_urls, download_path)

print('Crawl.py terminated')


