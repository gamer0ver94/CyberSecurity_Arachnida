import sys
import requests
from bs4 import BeautifulSoup
import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import imghdr

def extract_images(images):
    images_urls = []
    for img in images:
        print(img)

def createDir(dir, name):
    path = os.path.join(name, dir)
    try:
        os.mkdir(path)
    except:
        print("No directory created.")

def extractImage(url, filename):
    r = requests.get(url, stream = True)
    if r.status_code == 200:
        with open("data/" + filename, "wb") as myImg:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, myImg)
            imgType = imghdr.what("data/" + filename)
            if imgType:
                os.rename("data/" + filename, "data/" + filename + "." + imgType)
            else:
                os.rename("data/" + filename, "data/" + filename + ".jpeg")
    else:
        print("Cant do it")
    


def main():
    if len(sys.argv) < 2:
        print("This Program does not contain an argument")
    else:
        try :
            createDir("data", os.getcwd())
        except:
            print("Directory already exist")
        r = requests.get(sys.argv[1])
        if r.status_code == 200:
            htmlParser = BeautifulSoup(r.content, "html.parser")
            images = htmlParser.find_all("img")
            n = 0
            l = len(images)
            for img in images:
                extractImage(img.attrs['src'], str(n))
                n += 1
                print(l)
                l -= 1
            
main()
