import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# โหลดโมเดล
model = tf.keras.models.load_model("KoratCattle.h5")

st.title("ทำนายน้ำหนักวัวจากภาพ")
st.write("อัปโหลดภาพวัวของคุณ แล้วระบบจะคาดการณ์น้ำหนักให้ทันที")

uploaded_file = st.file_uploader("เลือกรูปภาพวัว (jpg, png)", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((224, 224)).convert("L")
    st.image(image, caption="ภาพที่อัปโหลด", use_column_width=True)

    img = np.array(image) / 255.0
    img = img.reshape(1, 224, 224, 1)

    prediction = model.predict(img)
    predicted_weight = prediction[0][0]

    st.success(f"น้ำหนักที่คาดการณ์: {predicted_weight:.2f} กิโลกรัม")
