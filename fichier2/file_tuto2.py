import os
import shutil

source = "splinter.jpg"
target = "images/splinter.jpg"

shutil.copy(source, target)
os.remove(source)

