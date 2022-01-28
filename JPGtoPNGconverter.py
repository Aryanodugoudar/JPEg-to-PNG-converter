import sys
import os
from PIL import Image

input_image = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(input_image):
  img = Image.open(f'{input_image}{filename}')
  clean_name = os.path.splitext(filename)[0] 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done')  