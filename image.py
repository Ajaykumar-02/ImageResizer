import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io

st.set_page_config(
    page_title="Smart Image Optimizer",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Smart Image Optimizer by AJAY 😉 ")

st.write("""
Resize images and optimize quality with ease.
Upload an image, set custom dimensions and quality,
then download the optimized version.
""")

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    img_array = np.array(image)

    original_width = img_array.shape[1]
    original_height = img_array.shape[0]

    st.subheader("📸 Original Image")

    st.image(
        image,
        use_container_width=True
    )

    st.info(
        f"Original Dimensions: {original_width} × {original_height}"
    )

    st.markdown("---")

    st.subheader("⚙️ Resize Settings")

    col1, col2 = st.columns(2)

    with col1:
        new_width = st.number_input(
            "Width (px)",
            min_value=1,
            value=original_width
        )

    with col2:
        new_height = st.number_input(
            "Height (px)",
            min_value=1,
            value=original_height
        )

    quality = st.slider(
        "Image Quality (%)",
        min_value=10,
        max_value=100,
        value=80
    )

    if st.button("🚀 Optimize Image"):

        resized = cv2.resize(
            img_array,
            (int(new_width), int(new_height))
        )

        st.subheader("✅ Optimized Image")

        st.image(
            resized,
            use_container_width=True
        )

        st.success(
            f"New Dimensions: {new_width} × {new_height}"
        )

        optimized_image = Image.fromarray(resized)

        buffer = io.BytesIO()

        optimized_image.save(
            buffer,
            format="JPEG",
            quality=quality,
            optimize=True
        )

        image_size_kb = len(buffer.getvalue()) / 1024

        st.info(
            f"Optimized File Size: {image_size_kb:.2f} KB"
        )

        st.download_button(
            label="📥 Download Optimized Image",
            data=buffer.getvalue(),
            file_name="optimized_image.jpg",
            mime="image/jpeg"
        )