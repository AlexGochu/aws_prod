

import streamlit as st
from PIL import Image 
from segment import process

st.title('AWS Cifar10')

image_file = st.file_uploader('Load an image', type=['png', 'jpg'])  # Добавление загрузчика файлов

if not image_file is None:                                           # Выполнение блока, если загружено изображение
    image = Image.open(image_file)                                   # Открытие изображения
    result = process(image_file)                                    # Обработка изображения с помощью функции, реализованной в другом файле
    st.text(result)

