import os
import time
import warnings
from typing import Any

import requests
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline, set_seed
import psutil  # Added to monitor system resources
from utils.custom import css_code

# Suppress deprecated TensorFlow warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Disable oneDNN optimizations if causing issues
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def progress_bar(amount_of_time: int) -> Any:
    progress_text = "Please wait, Generative models hard at work"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def generate_text_from_image(url: str) -> str:
    # Using the BLIP model for image captioning
    try:
        image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base", framework="pt")
        generated_text = image_to_text(url)[0]["generated_text"]
        
        # Ensure the generated text is a complete sentence.
        if not generated_text.endswith(('.', '!', '?')):
            generated_text += '.'  # Ensures ending as a complete thought.

        print(f"IMAGE INPUT: {url}")
        print(f"GENERATED TEXT OUTPUT: {generated_text}")
        return generated_text
    except Exception as e:
        print(f"Error in generating text from image: {e}")
        return "Failed to generate a complete description."

def generate_story_from_text(scenario: str) -> str:
    # Updated to a more directive prompt that emphasizes creating a story directly from the provided scenario.
    prompt_template = f"Create a point to point essay on this scenario under 50 words: '{scenario}'."

    try:
        model = pipeline("text-generation", model="gpt2", framework="pt")
        set_seed(42)  # Ensures reproducibility
        # Adjust max_new_tokens if needed to control the length and scope of the generation
        generated_story = model(prompt_template, max_new_tokens=100, return_full_text=False)[0]["generated_text"]

        print(f"TEXT INPUT: {scenario}")
        print(f"GENERATED STORY OUTPUT: {generated_story}")
        return generated_story
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error generating story."

def generate_speech_from_text(message: str) -> Any:
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payloads = {"inputs": message}

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open("generated_audio.flac", "wb") as file:
        file.write(response.content)

def main() -> None:
    st.set_page_config(page_title="IMAGE TO STORY CONVERTER", page_icon="🖼️")
    st.markdown(css_code, unsafe_allow_html=True)

    with st.sidebar:
        st.image("img/gkj.jpg")
        st.write("---")

    st.header("ImageVoice-AI - A IMAGE TO STORY CONVERTER GEN AI TOOL")
    uploaded_file = st.file_uploader("Please choose a file to upload", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        progress_bar(100)
        scenario = generate_text_from_image(uploaded_file.name)
        story = generate_story_from_text(scenario)
        generate_speech_from_text(story)  # Pass only the story to TTS

        with st.expander("Generated Image scenario"):
            st.write(scenario)
        with st.expander("Generated short story"):
            st.write(story)

        st.audio("generated_audio.flac")

if __name__ == "__main__":
    main()
