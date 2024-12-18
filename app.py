import streamlit as st
import openai 
from PIL import Image
import requests

# For local Stable Diffusion model
from diffusers import StableDiffusionPipeline
import torch

# Streamlit Page Configuration
st.set_page_config(page_title="AI Text-to-Image Generator", page_icon="🎮", layout="wide")

st.title("AI Text-to-Image Generator ")
st.subheader("Turn your words into stunning AI-generated images")

# OpenAI API key 
openai.api_key = "your_openai_api_key"

# User Inputs
prompt = st.text_input("Enter your text prompt", placeholder="e.g., A city at sunset")
size = st.selectbox("Select Image Size", ["256x256", "512x512", "1024x1024"], index=2)
style = st.radio("Select Style", ["Realistic", "Anime", "Cartoon"], index=0)
generate_button = st.button("Generate Image")

# Function to generate image using OpenAI DALL-E API
def generate_image(prompt, size="1024x1024"):
    """Generates an image from a text prompt using OpenAI DALL-E API"""
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size
        )
        image_url = response['data'][0]['url']
        image = Image.open(requests.get(image_url, stream=True).raw)
        return image
    except Exception as e:
        st.error(f"Error generating image with OpenAI DALL-E: {e}")
        return None

# Function to generate image using local Stable Diffusion model
def generate_image_stable_diffusion(prompt):
    """Generates an image from a text prompt using a local Stable Diffusion model"""
    try:
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")
        with torch.no_grad():
            image = pipe(prompt).images[0]
        return image
    except Exception as e:
        st.error(f"Error generating image with Stable Diffusion: {e}")
        return None

# Image Generation Logic
image = None
if generate_button and prompt:
    with st.spinner('Generating... Please wait'):
        if style == "Realistic":
            image = generate_image(prompt, size)
        elif style == "Anime" or style == "Cartoon":
            image = generate_image_stable_diffusion(prompt)
        if image:
            st.image(image, caption="Generated Image", use_column_width=True)

# Download Button for Generated Image
if image:
    image_bytes = image.tobytes()
    st.download_button(
        label="Download Image",
        data=image_bytes,
        file_name='generated_image.png',
        mime='image/png'
    )