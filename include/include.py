import time
import threading
import openai
import pyttsx3
import json
import speech_recognition as sr
from pydub.generators import Sine
from pydub.playback import play
from include.current_time import get_current_time
from include.weather import get_current_weather
from include.functions_data import FUNCTIONS

from api_key import api_key_openai
