import streamlit as st
import cv2 as cv
import numpy as np
import tensorflow as tf
import keras


label_name = ['Apple Apple scab', 'Apple Black rot', 'Apple Cedar apple rust', 'Apple healthy', 'Cherry (including sour) Powdery mildew', 'Cherry (including sour) healthy', 'Corn (maize) Cercospora leaf spot Gray leaf spot', 'Corn (maize) Common rust ', 'Corn (maize) Northern Leaf Blight', 'Corn (maize) healthy', 'Grape Black rot', 'Grape Esca (Black Measles)', 'Grape Leaf blight (Isariopsis Leaf Spot)', 'Grape healthy', 'Peach Bacterial spot', 'Peach healthy', 'Pepper, bell Bacterial spot', 'Pepper, bell healthy', 'Potato Early blight', 'Potato Late blight', 'Potato healthy', 'Strawberry Leaf scorch', 'Strawberry healthy', 'Tomato Bacterial spot', 'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold', 'Tomato Septoria leaf spot', 'Tomato Spider mites Two-spotted spider mite', 'Tomato Target Spot', 'Tomato Tomato Yellow Leaf Curl Virus', 'Tomato Tomato mosaic virus', 'Tomato healthy']


st.write("""The leaf disease detection model is built using deep learning techniques, and it uses transfer learning to leverage the pre-trained knowledge of a base model. The model is trained on a dataset containing images of 33 different types of leaf diseases. For more information about the architecture, dataset, and training process, please refer to the code and documentation provided.""")              

st.write("Please input only leaf Images of Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, and Tomato. Otherwise, the model will not work perfectly.")

model = tf.keras.models.load_model("Training/model/tl_model.h5")


uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    img = cv.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv.IMREAD_COLOR)
    normalized_image = np.expand_dims(cv.resize(cv.cvtColor(img, cv.COLOR_BGR2RGB), (150, 150)), axis=0)
    predictions = model.predict(normalized_image)
    st.image(image_bytes)
    if predictions[0][np.argmax(predictions)]*100 >= 80:
        st.write(f"Result is : {label_name[np.argmax(predictions)]}")
    else:st.write(f"Try Another Image")