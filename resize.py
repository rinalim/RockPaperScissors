import os,sys
import glob
from PIL import Image

if not os.path.exists('./img_org'):
    os.system('cp -r ./img ./img_org')

width = sys.argv[1]
height = sys.argv[2]

files = glob.glob('./img_org/*.png')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(width), int(height)))
    if len(sys.argv) == 4 and sys.argv[3] == 'rotate':
        img_resize = img_resize.rotate(180)
    title, ext = os.path.splitext(f)
    title = title.replace('img_org', 'img')
    img_resize.save(title + ext)
    print("resizing " + title + ext)
