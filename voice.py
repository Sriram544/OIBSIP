import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import smtplib
import requests
import json

# Text-to-Speech engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry, I didn't catch that. Can you please repeat?")
        return "None"
    return query.lower()


def open_website(url):
    webbrowser.open(url)


def play_song():
    # Add your music player or streaming service logic here
    pass


def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")


def send_email(to, subject, body):
    # Add your email sending logic here
    pass


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        main = weather_data['main']
        temperature = main['temp']
        description = weather_data['weather'][0]['description']
        speak(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")
    else:
        speak("Sorry, I couldn't retrieve the weather information for that city.")


if __name__ == "__main__":
    greet()
    speak("I am Tillu, your voice assistant. How can I assist you today?")

    while True:
        query = take_command().lower()

        if 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

        elif 'hello' in query:
            speak("Hello! How can I help you today?")

        elif 'open youtube' in query:
            open_website("https://www.youtube.com/")

        elif 'play a song' in query:
            play_song()

        elif 'get the time' in query:
            get_time()

        elif 'send an email' in query:
            # Provide email details here
            send_email("recipient@example.com", "Test Subject", "Test Body")

        elif 'check the weather' in query:
            # Provide your OpenWeatherMap API key here
            weather_api_key = 'your_openweathermap_api_key'
            speak("Sure, which city would you like to check the weather for?")
            city_query = take_command().lower()
            get_weather(city_query, weather_api_key)
