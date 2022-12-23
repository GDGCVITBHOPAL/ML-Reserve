import os
import sys
from PIL import Image

print("Enter your file path: ")
file = str(input())
if(file):
    if os.path.exists(file):
        image = Image.open(file)
        tfile = file.removesuffix('.png')
        target = tfile + ".jpg"
        RGB_IMAGE = image.convert('RGB')
        RGB_IMAGE.save(target)
        print("Your file is saved with "+target+" name.")
    else:
        print("Your "+file+" is not found!")
else:
    print("[+] Syntax: toJPG.py <FILE_PATH>")
