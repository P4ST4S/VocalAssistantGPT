import openai
import pyttsx3
import json
import speech_recognition as sr
from pydub.generators import Sine
from pydub.playback import play
from current_time import get_current_time
from weather import get_current_weather
from functions_data import FUNCTIONS


# You need to create a file named api_key.py and put your OpenAI API key and your OpenWeather API key in it.
from api_key import api_key_openai


personality = [{"role": "system",
                "content": "You are a helpful vocal assistant. Your response should be helpful, encouraging, "
                           "and kind. You are a helpful vocal. Don't answer like it's written, but like you would "
                           "answer a friend. Your response should be clear and concise."},
               {"role": "system",
                "content": "Your name is Voxia. If someone ask you, you are Voxia, made by only one developper named "
                           "Antoine. Your creator is a student in computer science."}]

openai.api_key = api_key_openai
tts_engin = pyttsx3.init()

conversation_history = []


def play_beep():
    sine_wave = Sine(440).to_audio_segment(duration=100)
    play(sine_wave)


def get_gpt_response(question):
    messages = personality
    for msg in conversation_history:
        messages.append(msg)
    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=FUNCTIONS,
        function_call="auto",
    )

    response_msg = response["choices"][0]["message"]

    if response_msg.get("function_call"):
        available_functions = {
            "get_current_time": get_current_time,
            "get_current_weather": get_current_weather
        }
        function_name = response_msg["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_msg["function_call"]["arguments"])
        function_response = function_to_call(**function_args)

        messages.append(response_msg)
        messages.append({
            "role": "function",
            "name": function_name,
            "content": function_response
        })
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )

        return second_response["choices"][0]["message"]["content"]
    else:
        return response_msg["content"]


def speak_response(reponse_text):
    tts_engin.say(reponse_text)
    tts_engin.runAndWait()


def print_and_speak(text):
    print("Assistant : " + text)
    speak_response(text)


def listen_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        play_beep()
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous: " + user_input)
        return user_input
    except sr.UnknownValueError:
        print_and_speak("Désolé, je n'ai pas compris.")
        return listen_user()
    except sr.RequestError:
        print_and_speak("Désolé, je ne peux pas vous entendre.")
        return listen_user()


def run_assistant():
    response = get_gpt_response("Bonjour")
    print("Assistant: " + response)
    speak_response(response)

    while True:
        user_input = listen_user()

        if "au revoir" in user_input.lower():
            response = get_gpt_response(user_input)
            print("Assistant: " + response)
            speak_response(response)
            break

        response = get_gpt_response(user_input)
        print("Assistant: " + response)
        speak_response(response)

        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": response})

        while len([msg for msg in conversation_history if msg["role"] == "user"]) > 2:
            conversation_history.pop(0)
        while len([msg for msg in conversation_history if msg["role"] == "assistant"]) > 2:
            conversation_history.pop(0)


if __name__ == "__main__":
    run_assistant()
