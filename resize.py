import os,sys
import glob
from PIL import Image

source = sys.argv[1]
width = sys.argv[2]
height = sys.argv[3]

files = glob.glob('./' + source + '/*.png')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(width), int(height)))
    if len(sys.argv) == 5 and sys.argv[4] == 'rotate':
        img_resize = img_resize.rotate(180)
    title, ext = os.path.splitext(f)
    title = title.replace(source, 'img')
    img_resize.save(title + ext)
    print("resizing " + title + ext)
