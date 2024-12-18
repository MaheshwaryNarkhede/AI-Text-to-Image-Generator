# AI Text-to-Image Generator

This project is a Streamlit-based web application that generates images from text prompts using AI models. Users can customize the image size, style, and download the generated image.

## 🛠️ **Features**
- **AI-Powered Image Generation**: Convert text prompts into stunning AI-generated images.
- **Image Customization**: Users can select image size (256x256, 512x512, 1024x1024) and image style (Realistic, Anime, Cartoon).
- **Download Option**: Download the generated image as a PNG file.

## ⚙️ **Requirements**

1. **Python 3.8+**
2. **Dependencies** (Install using `pip install -r requirements.txt`):
   - `streamlit`
   - `openai`
   - `Pillow`
   - `requests`
   - `diffusers`
   - `torch`

3. **Run the Streamlit App**:
   ```bash
   streamlit run ai_image_generator.py
   ```

## 🚀 **Usage**
1. **Enter Text Prompt**: Describe the image you want to generate (e.g., "A  city at sunset").
2. **Select Image Size**: Choose from 256x256, 512x512, or 1024x1024 resolutions.
3. **Select Style**: Choose from Realistic, Anime, or Cartoon styles.
4. **Click Generate Image**: The AI will create the image based on your prompt.
5. **Download Image**: Click the download button to save the image as a PNG file.
