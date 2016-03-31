import os

for filename in os.listdir("."):
    if filename.endswith(".jpg"):
        os.rename(filename, 'i_' + filename)



