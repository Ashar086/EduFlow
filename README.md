# EduTonic

## Setup  

### Prerequisites  

- Python 3.6 or higher  

### Create a Virtual Environment  

First, create and activate a virtual environment:  

For Unix or MacOS:

```sh  
python3 -m venv chatbot_env  
source chatbot_env/bin/activate  
```  

For Windows:  
```sh
python -m venv chatbot_env  
chatbot_env\Scripts\activate  
```  

### Install Dependencies  

Install the required dependencies using the `requirements.txt` file:  

```sh  
pip install -r requirements.txt  
```  

### Run the Application  

To run the Streamlit app, use the following command:  

```sh  
streamlit run chatbot_app.py  
```  

### Contributing

This is a Streamlit application that includes a microphone/audio input, camera/image input, text input, two text outputs, and one audio output in a chatbot interface.  

#### Tasks  

- The `text_to_speech` function in the app uses a placeholder API. Replace the URL with an actual Text-to-Speech (TTS) API endpoint.  
- Ensure your webcam and microphone are properly configured and accessible by the application.  

#### Application Features  

- **Text Input:** Enter your message in the text input field.  
- **Camera Input:** Capture an image from your webcam using the camera input widget.  
- **Microphone Input:** Record audio using the "Record Audio" button.  
- **Text Outputs:** Two text outputs display the echoed and reversed user input.  
- **Audio Output:** The echoed text is converted to speech and played back.  

#### Step 1: Create a Virtual Environment  

First, create a virtual environment to isolate the dependencies for your project.  

For Unix or MacOS:  

```sh  
python3 -m venv chatbot_env  
```  

For Windows:

```sh
python -m venv chatbot_env  
```  

Activate the virtual environment:  

For Unix or MacOS:  

```sh  
source chatbot_env/bin/activate  
```  

For Windows:

```sh
chatbot_env\Scripts\activate  
```  

#### Step 2: Install Dependencies  

With the virtual environment activated, install the dependencies using `pip`:  

```sh  
pip install -r requirements.txt  
```  

#### Step 5: Directory Structure  

Your project directory structure should look like this:  

```md
chatbot_project/  
│  
├── .streamlit/secrets.toml  
│  
├── chatbot_app.py  
├── requirements.txt  
└── README.md  
```
