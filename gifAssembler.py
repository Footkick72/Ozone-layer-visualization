import os
import PIL
import cv2

files = []
for file in os.listdir("/Users/daniellong/Documents/programming/Python/LandSat/frames"):
    year = file[5:9]
    number = file[9:12]
    files.append([file, year, number])

def compareValue(f1):
    return f1[1] * 10000 + f1[2]

files.sort(key = compareValue)
files.pop()
for i,f in enumerate(files):
    files[i] = f[0]

frame = cv2.imread("/Users/daniellong/Documents/programming/Python/LandSat/frames/" + files[0])
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fourcc = 0
video = cv2.VideoWriter("ozone.avi", fourcc, 2, (width,height))

for image in files:
    video.write(cv2.imread("/Users/daniellong/Documents/programming/Python/LandSat/frames/" + image))

cv2.destroyAllWindows()
video.release()
