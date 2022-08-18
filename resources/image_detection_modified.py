# modified image_detection for template collection
import pyautogui as gui
import cv2 as cv
import numpy as np
from PIL import ImageGrab, Image, ImageChops
import time 
import os
# class superAutoPets_CV():
#     def __init__(self):
def get_animal_from_screen():
    time.sleep(1)
    img = ImageGrab.grab(bbox=(450, 620, 1500, 750))
    img_00 = img.crop((10,0,140,130))
    img_01 = img.crop((155,0,285,130))
    img_02 = img.crop((300,0,430,130))
    img_03 = img.crop((445,0,575,130))
    img_04 = img.crop((590,0,720,130))
    img_05 = img.crop((730,0,860,130))
    img_06 = img.crop((875,0,1005,130))
    images0 = [img_00, img_01, img_02, img_03, img_04, img_05,img_06]
    images = []
    for i in images0:
        images.append(cv.cvtColor(np.array(i), cv.COLOR_RGB2BGR))
    img = img.save(r'.\tool_res\region_of_interest.jpg')
    img_00 = img_00.save(r'.\tool_res\first.jpg')
    img_01 = img_01.save(r'.\tool_res\second.jpg')
    img_02 = img_02.save(r'.\tool_res\third.jpg')
    img_03 = img_03.save(r'.\tool_res\fourth.jpg')
    img_04 = img_04.save(r'.\tool_res\fiveth.jpg')
    img_05 = img_05.save(r'.\tool_res\sixth.jpg')
    img_06 = img_06.save(r'.\tool_res\seventh.jpg')
    return images, images0

def matching(image, needle_img):
    result = cv.matchTemplate(image,needle_img, cv.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv.minMaxLoc(result)
    # print(max_val)
    if max_val > 0.7:
        return 1, max_val
    return 0, max_val 

# returns the filename one by one
def get_image_directory(directory):
    # print(directory)
    dir = os.listdir(directory)
    for folder in dir:
        for filename in os.listdir(os.path.join(directory, folder)):
            file = os.path.join(folder, filename)
            # print(file)
            if os.path.isfile(os.path.join(directory,file)):
                # print(file)
                yield os.path.join(directory,file)

def find_the_animals(directory = '.\\SAP_res\\'):
    time.sleep(2)
    list_of_animals = []
    max_val_animals = []
    images, references = get_animal_from_screen()
    #go through all the animals images in the directory
    for i in images:
        for j in get_image_directory(directory):
            im = cv.imread(j, cv.IMREAD_UNCHANGED)
            #matching returns which animals
            k, max_val = matching(i, im)
            # print(k)
            if k == 1:
                list_of_animals.append(j)
                max_val_animals.append(max_val)
                break
    if len(list_of_animals) > 7:
        return 0
    list_of_animals1 = []
    for i in list_of_animals:
        temp = i.split('\\')
        list_of_animals1.append(temp[2])
    list_of_animals1 = tuple(list_of_animals1)
    print(list_of_animals1)
    references = tuple(references)
    if len(list_of_animals1) == 0:
        return list_of_animals1
   
    img_01 = img_01.save(r'.\tool_res\second.jpg')
    img_02 = img_02.save(r'.\tool_res\third.jpg')
    img_03 = img_03.save(r'.\tool_res\fourth.jpg')
    img_04 = img_04.save(r'.\tool_res\fiveth.jpg')
    return list_of_animals1, max_val_animals,  references

# ('ant', 'ant', 'horse', 'nothing', 'nothing', 'nothing', 'honey')
# [0.9955806136131287, 0.8385165333747864, 0.9044007658958435, 0.7936922907829285, 0.7866852283477783, 0.797288715839386, 0.9933444261550903]
