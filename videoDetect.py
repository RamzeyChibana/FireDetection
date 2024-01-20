import cv2 as cv
import tensorflow as tf
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np

model=tf.keras.models.load_model("firemodel")


labels=['fire', 'No fire', 'smoke', 'No fire']

def predict(image):
    image = np.expand_dims(image, axis=0)
    image = (image/255)
    predection=model.predict(image,verbose=0)
    
    return f"{labels[np.argmax(predection)]} {np.max(predection):.2f}%"

def draw_prediction( frame, class_string ):
    x_start = frame.shape[1] -600
    cv.putText(frame, class_string, (x_start, 75), cv.FONT_HERSHEY_SIMPLEX, 2.5, (255, 0, 0), 2, cv.LINE_AA)
    return frame

def read_video(video_path):
    vs=capture=cv.VideoCapture(video_path)
    fps = np.floor(vs.get(cv.CAP_PROP_FPS))
    i=0
    while True:
        isTrue,frame=capture.read()
        i+=1
        
        image=cv.resize(frame, (256, 256))
        image=np.array(image,dtype=np.float16)

        pred=predict(image)
        frame=draw_prediction(frame,pred)
        cv.imshow("win",frame)
        if cv.waitKey(20) & 0xFF==ord("x"):
            print("exit")
            break

    capture.release()
    cv.destroyAllWindows()

read_video("D:\\chill\\memories\\ai\\firetest.mp4")










