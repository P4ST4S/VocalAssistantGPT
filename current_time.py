import datetime
import json


def get_current_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    json_time = {"hours": hours, "minutes": minutes, "seconds": seconds}
    return json.dumps(json_time)