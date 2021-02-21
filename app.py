
import streamlit as st
import numpy as np
from PIL import Image
import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)

def cartoon(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 5) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  
                                            cv2.THRESH_BINARY, 9, 9) 
    
    # Cartoonization 
    color = cv2.bilateralFilter(img, 9, 200, 200) 
    
    cartoon_img = cv2.bitwise_and(color, color, mask=edges) 
    return (cartoon_img)

def painting(img):
     painting_img = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
     return(painting_img) 


st.title("Image Effect App")
st.write("This Web App is to help convert your photos to Pencil sketch, Painting and Cartoon")

file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])

if file_image is None:
    st.write("You haven't uploaded any image file")

else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    cartoon_sketch = cartoon(np.array(input_img))
    painting_sketch = painting(np.array(input_img))
    st.write("**Input Photo**")
    st.image(input_img, use_column_width=True)
    st.write("**Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)
    st.write("**Cartoon Sketch**")
    st.image(cartoon_sketch, use_column_width=True)
    st.write("**Water Painting**")
    st.image(painting_sketch, use_column_width=True)

