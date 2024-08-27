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

def createDir(dir, name):
    path = os.path.join(name, dir)
    try:
        os.mkdir(path)
    except:
        print("No directory created.")

def extractImage(url, filename, path):
    r = requests.get(url, stream = True)
    if r.status_code == 200:
        with open(path + filename, "wb") as myImg:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, myImg)
            
            
            # if imgType:
            #     
    else:
        print("Cant do it")
    try:
        img = Image.open(path + filename, 'r')
        imgType = img.format
        print(imgType)
        os.rename(path + filename, path + filename + "." + imgType)
    except:
        print("invalid format image")
    
    
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
        required=False,
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
    print(args.length)
    return args


def main():

    args = checkInput()
    try :
        createDir(args.path, os.getcwd())
    except:
        print("Directory already exist")
    try :
        request = requests.get(args.website)
    except :
        print("Invalid Request")
    if request.status_code == 200:
        htmlParser = BeautifulSoup(request.content, "html.parser")
        images = htmlParser.find_all("img")
        print(images[1].date)
        n = 0
        l = len(images)
        print("number is " + str(len(images)))
        for i in range(args.length):
            if args.length > len(images) :
                break
            extractImage(images[i].attrs['src'], str(n), args.path)
            n += 1
main()
