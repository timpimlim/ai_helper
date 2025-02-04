import os
import pyautogui
import time
import psutil
import speech_recognition
import json
import webbrowser

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

with open('commands/commands.json', 'r', encoding='utf-8') as file:
    commands_dict = json.load(file)

def listen_command():
    """Распознает команду из голосового ввода"""
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(mic, duration=0.5)
            audio = sr.listen(mic)
            query = sr.recognize_google(audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return None

def greeting():
    """Приветствие"""
    return 'Приветик!'

def play_music():
    print("Есть Босс!") 
    for proc in psutil.process_iter():
        if proc.name() == "Spotify.exe":
            pyautogui.press('playpause')
            time.sleep(1)
            return

    os.startfile("C:\\Users\\kapus\\AppData\\Roaming\\Spotify\\Spotify.exe")
    time.sleep(2)
    pyautogui.press('playpause')
    return

def open_telegram():
    """Открытие Telegram"""
    telegram_path = os.path.expanduser("C:\\Users\\kapus\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
    if os.path.exists(telegram_path):
        os.startfile(telegram_path)
        return "Открываю Telegram..."
    return "Telegram не найден. Проверьте путь к программе."

def open_youtube():
    """Открытие YouTube"""
    webbrowser.open("https://www.youtube.com")
    return "Открываю YouTube..."

def main():
    while True:
        query = listen_command()
        if not query:
            print("Не удалось распознать команду.")
            continue
        
        if query in commands_dict.get('exit_commands', []):
            print("Завершение работы...")
            break
        
        for command, phrases in commands_dict['commands'].items():
            if query in phrases:
                response = globals()[command]()
                print(response)
                break

if __name__ == '__main__':
    main()