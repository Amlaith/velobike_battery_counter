import os
import pytesseract
import numpy as np
from PIL import Image, ImageEnhance
from scipy.spatial.distance import cdist
import re
# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def remove_green(image):
    green = np.array([(86, 179, 99)])
    i = np.asarray(image).copy()
    shape = i.shape
    i = i.reshape(-1, 3)

    pixels = np.where(cdist(i, green, metric='cosine') < 0.01)[0]
    i[pixels] = (255, 255, 255)
    
    i = i.reshape(shape)
    i = Image.fromarray(i)
    
    return i

def bike_screenshot_to_string(image):
    ocr_text = pytesseract.image_to_string(image, lang='rus')
    time_pattern = re.compile("\d{2}\:\d{2}")
    bike_num_pattern = re.compile(" 2\d{4} ")
    battery_percent_pattern = re.compile("\d{1,3}%")

    times = re.findall(time_pattern, ocr_text)
    bike_nums = re.findall(bike_num_pattern, ocr_text)
    battery_percents = re.findall(battery_percent_pattern, ocr_text)

    # times, bike_nums, battery_percents

    time = times[0] if times else "НЕ УДАЛОСЬ РАСПОЗНАТЬ ВРЕМЯ"
    bike_num = (bike_nums[0] if bike_nums else "НЕ УДАЛОСЬ РАСПОЗНАТЬ НОМЕР ВЕЛОСИПЕДА").strip()
    battery_percent = battery_percents[-1] if battery_percents else "НЕ УДАЛОСЬ РАСПОЗНАТЬ ПРОЦЕНТ ЗАРЯДА"

    time, bike_num, battery_percent

    return f"{bike_num}\n{battery_percent}\n{time}\n1 раз\n\n"