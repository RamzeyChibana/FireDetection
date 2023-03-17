import cv2 as cv
import tensorflow as tf
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np

model=tf.keras.models.load_model("firemodel")


def ai(image):
    image = np.expand_dims(image, axis=0)
    image = 2*(image/255)-1
    predection=model.predict(image,verbose=0)
    print(str(predection[0][0])+"%")
    if predection < 0.3:
        print("no fire")
    else:
        print("fire")



capture=cv.VideoCapture("D:\\chill\\gifs\\forest.mp4")

while True:
    isTrue,frame=capture.read()
    
    image=cv.resize(frame, (512, 512))
    image=np.array(image,dtype=np.float16)
    ai(image)

    
    if cv.waitKey(20) & 0xFF==ord("x"):
        print("exit")
        break

capture.release()
cv.destroyAllWindows()












