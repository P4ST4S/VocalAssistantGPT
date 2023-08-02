import datetime
import json


def get_current_time():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    json_time = {"date":date, "hours": hours, "minutes": minutes, "seconds": seconds}
    return json.dumps(json_time)
