A Python-based voice assistant that listens to user commands and performs everyday tasks such as telling the time and date, opening applications, and searching the web.

This project is built as a learning-focused assistant to strengthen Python fundamentals through a real-world use case.


🧠 Overview

The Python Voice Assistant uses speech recognition for taking voice input and text-to-speech for responding back to the user.
It runs in a continuous loop, listens for commands, processes them using conditional logic, and executes appropriate actions.

✨ Features

Voice-based command input

Text-to-speech output

Get current time

Get today’s date

Open Notepad (Windows)

Perform Google searches

Graceful handling of unknown commands

Exit assistant using voice command

🛠️ Tech Stack

Language: Python

Libraries:

speech_recognition

pyttsx3

webbrowser

os

datetime

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/python-voice-assistant.git
2️⃣ Navigate to the project folder
cd python-voice-assistant
3️⃣ Install required dependencies
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio

⚠️ Note:
pyaudio may require platform-specific installation.
On Windows, install using a precompiled wheel if needed.

▶️ Usage

Run the assistant using:

python assistant.py
Example Commands

"hello"

"time"

"date"

"open notepad"

"search python tutorial"

"stop"

📂 Project Structure
python-voice-assistant/
│
├── assistant.py
└── README.md
