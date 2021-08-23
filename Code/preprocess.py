import numpy as np
import skimage
from skimage.transform import resize
import cv2
imageSize = 50
dataDir = "data/data/"
from tqdm import tqdm
import os

def get_data(folder):
    X = []
    y = []
    for folderName in os.listdir(folder):
        if not folderName.startswith('.'):
            if folderName in ['a']:
                label = 0
            elif folderName in ['b']:
                label = 1
            elif folderName in ['c']:
                label = 2
            elif folderName in ['d']:
                label = 3
            elif folderName in ['e']:
                label = 4
            elif folderName in ['f']:
                label = 5
            elif folderName in ['g']:
                label = 6
            elif folderName in ['h']:
                label = 7
            elif folderName in ['i']:
                label = 8
            elif folderName in ['j']:
                label = 9
            elif folderName in ['k']:
                label = 10
            elif folderName in ['l']:
                label = 11
            elif folderName in ['m']:
                label = 12
            elif folderName in ['n']:
                label = 13
            elif folderName in ['o']:
                label = 14
            elif folderName in ['p']:
                label = 15
            elif folderName in ['q']:
                label = 16
            elif folderName in ['r']:
                label = 17
            elif folderName in ['s']:
                label = 18
            elif folderName in ['t']:
                label = 19
            elif folderName in ['u']:
                label = 20
            elif folderName in ['v']:
                label = 21
            elif folderName in ['w']:
                label = 22
            elif folderName in ['x']:
                label = 23
            elif folderName in ['y']:
                label = 24
            elif folderName in ['z']:
                label = 25
            
            for image_filename in tqdm(os.listdir(folder + folderName)):
                img_file = cv2.imread(folder + folderName + '/' + image_filename)
                if img_file is not None:
                    img_file = skimage.transform.resize(img_file, (imageSize, imageSize, 3))
                    #res = kcluster((img_file))
                    img_arr = np.asarray(img_file)
                    X.append(img_arr)
                    y.append(label)
    X2 = np.asarray(X)
    y2 = np.asarray(y)
    return X2,y2

X2, y2 = get_data("dummy/")

np.save("Xfinal.npy",X2)
np.save("Yfinal.npy",y2)
