import os
import pyautogui
import time
import psutil
import speech_recognition
import json
import webbrowser
import pyttsx3
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if (voice.languages and 'en' in voice.languages[0].decode().lower()) or 'english' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

client = genai.Client(api_key=API_KEY)

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1

with open('commands/commands.json', 'r', encoding='utf-8') as file:
    commands_dict = json.load(file)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with speech_recognition.Microphone(device_index=1) as mic:
            sr.adjust_for_ambient_noise(mic, duration=0.5)
            audio = sr.listen(mic)
            query = sr.recognize_google(audio, language='en-EN').lower()
        return query
    except speech_recognition.UnknownValueError:
        return None

def ask_gemini(prompt):
    sys_instruct = "You are a voice AI assistant with the behavioral model of Jarvis from the Iron Man movies. Your name is Vi. Answer briefly and informatively, your word limit is 200. Exceed the word limit only if the user asks you to."
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(system_instruction=sys_instruct),
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error when contacting Gemini: {e}"

def greeting():
    response = 'Hello!'
    speak(response)
    return response

def play_music():
    print("Yes, Boss!")
    speak("Yes, Boss!")
    for proc in psutil.process_iter():
        if proc.name() == "Spotify.exe":
            pyautogui.press('playpause')
            time.sleep(1)
            return

    os.startfile("Your path to Spotify.exe")
    time.sleep(2)
    pyautogui.press('playpause')
    return

def open_telegram():
    telegram_path = os.path.expanduser("Your path to Telegram.exe")
    if os.path.exists(telegram_path):
        os.startfile(telegram_path)
        response = "Opening Telegram..."
        speak(response)
        return response
    response = "Telegram not found. Please check the program path."
    speak(response)
    return response

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    response = "Opening YouTube..."
    speak(response)
    return response

def main():
    while True:
        query = listen_command()
        if not query:
            continue

        if query in commands_dict.get('exit_commands', []):
            print("Shutting down...")
            speak("Shutting down...")
            break

        command_found = False
        for command, phrases in commands_dict['commands'].items():
            if query in phrases:
                response = globals()[command]()
                print(response)
                command_found = True
                break

        if not command_found:
            gemini_response = ask_gemini(query)
            print(f"Vi says: {gemini_response}")
            speak(gemini_response)

if __name__ == '__main__':
    main()