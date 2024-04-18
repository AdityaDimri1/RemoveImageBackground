from rembg import remove          # rembg Library
from PIL import Image             # PIL Library 
input_path='i/p file name'        # write the i/p file name and its directary
output_path='o/p file name'       # write o/p file name that you want
inpu=Image.open(input_path)
output=remove(inpu)
output.save(output_path)