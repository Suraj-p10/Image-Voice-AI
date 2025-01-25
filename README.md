# ImageVoice AI

## Overview
The **ImageVoice AI** is a Streamlit-based web application that leverages advanced AI models to:

1. Extract text from uploaded images using an **OCR pipeline**.
2. Optionally refine the extracted text using **OpenAI's GPT model**.
3. Convert the refined text into natural-sounding speech using a **text-to-speech pipeline**.
4. Display an intuitive interface styled with custom CSS.

This project combines computer vision, natural language processing, and text-to-speech technology into one cohesive tool.

---

## Features
- **Image Upload**: Users can upload PNG, JPG, or JPEG images.
- **OCR (Image-to-Text)**: Extracts text using Hugging Face's `microsoft/vision-tress-base` pipeline.
- **Text Refinement**: Refines extracted text into a natural speech description using OpenAI's GPT model.
- **Text-to-Speech Conversion**: Converts text to speech using Hugging Face's `facebook/fastspeech2-en-ljspeech` model.
- **Streamlit UI**: Clean and interactive user interface.

---

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key (for text refinement functionality)

### Clone the Repository
```bash
git clone https://github.com/your-username/ImageVoice-AI.git
cd ImageVoice-AI
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

---

## Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

1. Upload an image file (PNG, JPG, or JPEG).
2. View the extracted text from the image.
3. (Optional) Refine the text using OpenAI's GPT model.
4. Listen to the generated speech output.

---

## Project Structure
```
ImageVoice-AI/
│
├── app.py               # Main Streamlit app
├── custom.py            # Contains CSS for styling
├── requirements.txt     # Lists project dependencies
├── .env.example         # Example for setting up API keys
└── README.md            # Project documentation
```

---

## Dependencies
- `transformers`: Hugging Face's Transformers library.
- `torch`: PyTorch framework for machine learning.
- `langchain`: Optional, if needed for LLM-related tasks.
- `openai`: For OpenAI API calls.
- `python-dotenv`: For managing environment variables.
- `requests`: For HTTP requests to APIs.
- `streamlit`: For building the web app.

---

## Future Enhancements
- Add support for additional languages in OCR and text-to-speech.
- Enhance error handling and user feedback.
- Deploy the application on a cloud platform like AWS, Azure, or Streamlit Sharing.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

---


