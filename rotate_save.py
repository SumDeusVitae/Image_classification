from PIL import Image 
import os
import argparse
import time
from datetime import timedelta

def rotate_save(adress: str, file: str) -> None:
    format = file[-3:]
    name = file[:-4]
    Original_Image = Image.open(fr'{adress}\{file}') 
    rotated_image1 = Original_Image.rotate(180)
    rotated_image1 = rotated_image1.save(fr'{adress}\{name}_180.{format}')
    rotated_image2 = Original_Image.transpose(Image.ROTATE_90) 
    rotated_image2 = rotated_image2.save(fr'{adress}\{name}_90.{format}')
    rotated_image3 = Original_Image.rotate(60)
    rotated_image3 = rotated_image3.save(fr'{adress}\{name}_60.{format}')

def main(path: str) -> None:
    start_time = time.monotonic()
    dir_list = os.listdir(path)
    for im in dir_list:
        rotate_save(adress=path, file=im)
        # print(path)
    print(f'Worked on {len(dir_list)} pictures')
    end_time = time.monotonic()
    print(f'Took {round(end_time - start_time, 4)} seconds to complete')
   


parser = argparse.ArgumentParser(description = 'rotates and saves images')
parser.add_argument('path', metavar = 'path', type=str, help='*. path to the folder')
args = parser.parse_args()
path = args.path
main(path)