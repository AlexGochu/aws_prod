

import streamlit as st
from PIL import Image 
from segment import process

st.title('AWS Cifar10')

image_file = st.file_uploader('Load an image', type=['png', 'jpg'])  # Добавление загрузчика файлов

if not image_file is None:                                           # Выполнение блока, если загружено изображение
    col1, col2 = st.beta_columns(2)
    image = Image.open(image_file)                                   # Открытие изображения
    pred_result = process(image_file)                                    # Обработка изображения с помощью функции, реализованной в другом файле
    
    
    result = '<p style="color: blue; font-size: 42px;">'+pred_result+'</p>'
    st.markdown(result, unsafe_allow_html=True)
    st.image(image)

