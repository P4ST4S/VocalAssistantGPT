FUNCTIONS = [
    {
        "name": "get_current_time",
        "description": "Get the current time",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_current_weather",
        "description": "Get the current weather. Transform '.' (point) into ',' (comma) in your response. "
                       "Don't tell abbreviation like 'hPa' or 'h'. but 'hectopascal' or 'kilometer per hour'.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and country, e.g. Paris, France",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"]
        },
    }
]