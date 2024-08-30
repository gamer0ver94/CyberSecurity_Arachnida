import sys
import requests
from bs4 import BeautifulSoup
import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import imghdr
import argparse
from PIL import Image
import math

def createDir(dir, name):
    path = os.path.join(name, dir)
    try:
        os.mkdir(path)
    except:
        print("Directory " + dir + " Already Exist.")

def extractImage(url, filename, path):
    try :
        response = requests.get(url, stream = True)
        if response.status_code == 200:
            with open(path + filename, "wb") as myImg:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, myImg)
        else:
            print("Cant do it")
        img = Image.open(path + filename, 'r')
        imgType = img.format
        os.rename(path + filename, path + filename + "." + imgType)
    except:
        print('Image from url ' + url + ' could not be downloaded')  
    
    
    
def checkInput():
    parser = argparse.ArgumentParser(
        prog = "spider",
        description = "Download Images from a Website"
    )
    parser.add_argument(
        'website',
        action='store',
        help='Place the website link'
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default='stdout',
        required=True,
        help="Download Images Recursively",
    )
    parser.add_argument(
        "-l",
        "--length",
        action="store",
        type = int,
        default="5",
        required=False,
        dest="length",

        help="Number of images to download",
    )
    parser.add_argument(
        "-p",
        "--path",
        action="store",
        default="./data/",
        required=False,
        dest="path",

        help="Number of images to download",
    )
    
    
    args = parser.parse_args()
    return args


def main():

    args = checkInput()
    try :
        response = requests.get(args.website)
        createDir(args.path, os.getcwd())
    except :
        print("Request Failed.")
    if response.status_code == 200:
        htmlParser = BeautifulSoup(response.content, "html.parser")
        images = htmlParser.find_all("img")
        l = args.length
        if args.length > len(images) :
                l = len(images)
        n = 0
        print("downloading " + str(l) + " images.")
        for i in range(l):
            print("Extracting image")
            print(str(math.floor( n / l * 100)) + "%")
            #name = images[i].attrs['span']
            #print(images[i])
            extractImage(images[i].attrs['src'], str(n), args.path)
            n += 1
        print("100%")
main()
