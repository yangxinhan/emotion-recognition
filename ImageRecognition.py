import cv2
from deepface import DeepFace
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import os

img = cv2.imread('photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # 將圖片轉成灰階



# 定義該情緒的中文字
text_obj={
    'angry': '生氣',
    'disgust': '噁心',
    'fear': '害怕',
    'happy': '開心',
    'sad': '難過',
    'surprise': '驚訝',
    'neutral': '正常'
}

def putText(x,y,text,size=70,color=(255, 255, 255)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array


try:
    emotion = DeepFace.analyze(img, actions=['emotion'])  # 情緒
    putText(0, 40,text_obj[emotion[0]['dominant_emotion']])     # 放入文字

    # print(emotion[0]['dominant_emotion'])
    
except:
    pass

cv2.imshow('oxxostudio', img)
cv2.waitKey(0)
file_path = 'photo.jpg'
os.remove(file_path)
cv2.destroyAllWindows()
