import albumentations as A 
import cv2
import os
from tqdm import tqdm
import numpy as np

aug = A.Compose([
    A.LongestMaxSize(max_size=1024),
    A.PadIfNeeded(min_height=1024, min_width=1024, border_mode=0,p=1.0),
    A.ShiftScaleRotate(shift_limit=.25, scale_limit=0.2, p=0.3),
    A.RandomSizedCrop((900, 1000), 1024, 1024, p=.2),
    A.HorizontalFlip(p=.5),
    A.Rotate(limit=30,p=.8),
    A.MultiplicativeNoise(p=.2),
    A.RGBShift(r_shift_limit=40, g_shift_limit=40, b_shift_limit=40, p=.3),
    A.Blur(blur_limit=25, p=.2),
    A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.35,p=.5),
    A.HueSaturationValue(p=.3),
    A.CoarseDropout(max_holes=9,min_width=30, max_width=250, min_height=30, max_height=250,p=.2),
    A.OneOf([A.IAAAdditiveGaussianNoise(),
        A.GaussNoise(var_limit=(10, 50),mean=50)], p=0.2),
    A.OneOf([
        A.MotionBlur(p=0.2),
        A.MedianBlur(blur_limit=3, p=0.1),
        A.Blur(blur_limit=3, p=0.1)], p=0.2),
    A.OneOf([
        A.IAASharpen(),
        A.IAAEmboss(),
        A.RandomBrightnessContrast(),
        A.RandomGamma(gamma_limit=[50,200], p=.2),
        A.ToGray()], p=0.3),
        A.NoOp(p=.04)
])


src = "dummy"


def create_dataset():
    for folder in tqdm(os.listdir(src)):
    	if folder == '.DS_Store':
    		continue
    	else:
    		for count,filename in enumerate(os.listdir(src+'/'+folder)):
    			img = cv2.imread(src+'/'+folder+'/'+filename)
    			#img = np.asarray(img)
    			folder_path = src+'/'+folder
    			for i in range(25):
    				augmented = aug(image = img)
    				file_name = f'{filename[:-4]}_{i}.jpg'
    				cv2.imwrite(f'{folder_path}/{file_name}',augmented['image'])


create_dataset()