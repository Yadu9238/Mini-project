import cv2
import numpy as np
import skimage
from skimage.transform import resize

def nothing(x):
    pass

image_x, image_y = 50,50

from keras.models import load_model
classifier = load_model('Final_model.h5')

def predictor():
       import numpy as np
       from keras.preprocessing import image
       img = cv2.imread('1.png')
       img = skimage.transform.resize(img,(50,50,3))
       img_arr = np.asarray(img)
       test_image = np.expand_dims(img_arr, axis = 0)
       result = np.argmax(classifier.predict(test_image))
       

       if result == 0:
              return 'A'
       elif result == 1:
              return 'B'
       elif result == 2:
              return 'C'
       elif result == 3:
              return 'D'
       elif result == 4:
              return 'E'
       elif result == 5:
              return 'F'
       elif result == 6:
              return 'G'
       elif result == 7:
              return 'H'
       elif result == 8:
              return 'I'
       elif result == 9:
              return 'J'
       elif result == 10:
              return 'K'
       elif result == 11:
              return 'L'
       elif result == 12:
              return 'M'
       elif result == 13:
              return 'N'
       elif result == 14:
              return 'O'
       elif result == 15:
              return 'P'
       elif result == 16:
              return 'Q'
       elif result == 17:
              return 'R'
       elif result == 18:
              return 'S'
       elif result == 19:
              return 'T'
       elif result == 20:
              return 'U'
       elif result == 21:
              return 'V'
       elif result == 22:
              return 'W'
       elif result == 23:
              return 'X'
       elif result == 24:
              return 'Y'
       elif result == 25:
              return 'Z'
       

       

cam = cv2.VideoCapture(0)



img_counter = 0

img_text = ''
sentence = []
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    


    img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)

    
    imcrop = img[102:298, 427:623]
    
    img_y = cv2.cvtColor(imcrop,cv2.COLOR_BGR2YCrCb)
    #cv2.imshow('img_y',img_y)
    y_mask = cv2.inRange(img_y,(0,135,85),(255,180,135))
    #cv2.imshow('img_y',y_mask)
    y_mask = cv2.morphologyEx(y_mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
   
    res = cv2.bitwise_and(imcrop,imcrop, mask= y_mask)
    cv2.imshow('y',res)
    
    cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 0, 0))
    cv2.imshow("test", frame)
    
        
    img_name = "1.png"
    save_img = cv2.resize(res, (image_x, image_y))
    cv2.imwrite(img_name, save_img)
    
    img_text = predictor()
    

    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()