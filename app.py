from cv2 import imread
import streamlit as st
import os
from PIL import Image
import cv2
import numpy as np
import test
import requests 


def makeDir():
    path_saved_imgs = './saved_images'
    path_h = './data/train/horses'
    path_z = './data/train/zebras'

    if not os.path.isdir(path_h):
        os.makedirs(path_h)

    if not os.path.isdir(path_z):
        os.makedirs(path_z)
    
    if not os.path.isdir(path_saved_imgs):
        os.makedirs(path_saved_imgs)


def checkPoint():
    if not 'genh.pth.tar' in os.listdir('.'):
        txt = st.warning("genh.pth.tar is not in dir")
        url = "https://www.dropbox.com/s/6ufvrdirivkex0u/genh.pth.tar?dl=1"
        r = requests.get(url, allow_redirects=True)
        open("genh.pth.tar", 'wb').write(r.content)
        del r
        txt.success("genh.pth.tar upload")

    if not 'genz.pth.tar' in os.listdir('.'):
        txt = st.warning("genh.pth.tar is not in dir")
        url = "https://www.dropbox.com/s/otrzvhgwj3fi8mk/genz.pth.tar?dl=1"
        r = requests.get(url, allow_redirects=True)
        open("genz.pth.tar", 'wb').write(r.content)
        del r
        txt.success("genz.pth.tar upload")

    if not 'critich.pth.tar' in os.listdir('.'):
        txt = st.warning("genh.pth.tar is not in dir")
        url = "https://www.dropbox.com/s/88bsu5a7lhs23ry/critich.pth.tar?dl=1"
        r = requests.get(url, allow_redirects=True)
        open("critich.pth.tar", 'wb').write(r.content)
        del r
        txt.success("critich.pth.tar upload")

    if not 'criticz.pth.tar' in os.listdir('.'):
        txt = st.warning("genh.pth.tar is not in dir")
        url = "https://www.dropbox.com/s/0b3ytkd2ot09iux/criticz.pth.tar?dl=1"
        r = requests.get(url, allow_redirects=True)
        open("criticz.pth.tar", 'wb').write(r.content)
        del r
        txt.success("criticz.pth.tar upload")

    

def photo2draw():
    checkPoint()
    test.main()
    img = imread('./saved_images/zebra_0.png')
    st.image(img, caption='output', use_column_width=True)
    img_array = np.array(img)
    cv2.imwrite('./saved_images/0.png', cv2.cvtColor(img_array, cv2.IMREAD_COLOR))

def upload_img():
    makeDir()
    uploaded_file = st.file_uploader("* 이미지 업로드하기(Upload Image)")
    if uploaded_file == None:
        None
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption='Input', use_column_width=True)
        st.markdown('⏳ 조금만 기다려 주세요. 이미지를 처리 중 입니다 ⏳')
        img_array = np.array(image)
        cv2.imwrite('./data/train/horses/0.png', cv2.cvtColor(img_array, cv2.IMREAD_COLOR))
        cv2.imwrite('./data/train/zebras/0.png', cv2.cvtColor(img_array, cv2.IMREAD_COLOR))
        photo2draw()

def main():
    st.title('Altist')
    describe1 = '<p style="font-size: 18px;">이미지를 업로드 하시면 똑똑한 사람냄새의 AI 화가 Altist가 사람냄새의 스타일로 그림을 그려줄거에요 🎨 평소 사람냄새의 그림을 좋아해주신 분들이라면 이제 원하는 이미지를 마음껏 다운받아 보세요 😊💖</p>'
    st.markdown(describe1, unsafe_allow_html=True)
    upload_img()

main()


