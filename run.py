import os
from PIL import Image as Pimg

def sortFiles():
    files = os.listdir()
    for i in files:
         if ".jpg" in i :
             img = Pimg.open(i)
             exifData = img._getexif()
             os.rename(i,exifData[36868])

if __name__ == "__main__":
    sortFiles()