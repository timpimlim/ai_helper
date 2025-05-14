# Vi AI Helper

A voice-activated assistant powered by Python, SpeechRecognition, and Gemini AI.

## Features

- Voice recognition using the SpeechRecognition library
- Responds to English voice commands (see `commands/commands.json`)
- Executes actions: greeting, play music, open Telegram, open YouTube
- Uses Gemini AI for general queries
- Text-to-speech responses with pyttsx3
- Easily extendable with new commands

## Usage

1. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

2. **Set up your environment:**

- Create a `.env` file in the project root:
  ```
  GOOGLE_API_KEY=your_google_api_key_here
  ```

3. **Configure your microphone:**

- To list available microphones, run:
  ```python
  import speech_recognition as sr
  print(sr.Microphone.list_microphone_names())
  ```
- Update the `device_index` in `main.py` if needed.

4. **Run the assistant:**
   ```
   python main.py
   ```

## Command List

Commands are defined in `commands/commands.json`. Example:

```json
{
  "commands": {
    "greeting": ["hello", "hi", "good afternoon"],
    "play_music": ["play music", "start music"],
    "open_telegram": ["open telegram", "start telegram", "telegram"],
    "open_youtube": ["open youtube", "start youtube"]
  },
  "exit_commands": ["exit", "stop", "shutdown"]
}
```

**Vi: Your personal Jarvis-inspired voice assistant!**
