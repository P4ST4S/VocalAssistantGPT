import openai
import pyttsx3
import speech_recognition as sr
from pydub.generators import Sine
from pydub.playback import play

# You need to create a file named api_key.py and put your OpenAI API key in it.
from api_key import api_key

personality = [{"role": "system",
                "content": "You are a helpful vocal assistant. Your response should be helpful, encouraging, "
                           "and kind. You are a helpful vocal. Don't answer like it's written, but like you would "
                           "answer a friend. Your response should be clear and concise."},
               {"role": "system",
                "content": "Your name is Voxia. If someone ask you, you are Voxia, made by only one developper named "
                           "Antoine. Your creator is a student in computer science."}]

openai.api_key = api_key
tts_engin = pyttsx3.init()

conversation_history = []


def play_beep():
    sine_wave = Sine(440).to_audio_segment(duration=150)
    play(sine_wave)


def get_gpt_response(question):
    messages = personality
    for msg in conversation_history:
        messages.append(msg)
    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response["choices"][0]["message"]["content"]


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
    print_and_speak("Bonjour, je suis Voxia, votre assistant vocal. Demandez-moi ce que vous voulez.")
    while True:
        user_input = listen_user()
        if "au revoir" in user_input.lower():
            print_and_speak("Au revoir, j'espère vous avoir aider !")
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
