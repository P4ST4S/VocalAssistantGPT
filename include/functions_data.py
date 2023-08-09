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
                       "Don't tell abbreviation like 'hPa' or 'h'. but 'hectopascal' or 'kilometer per hour'."
                       "Answer with sentences like 'The weather is sunny.' or 'The temperature is 20 degrees celsius.'",
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
    },
    {
        "name": "get_forecast_weather",
        "description": "Get the five days forecast of the weather. Answer with sentences like 'The weather will be sunny.' or "
                       "'The temperature will be 20 degrees celsius.'. Transform '.' (point) into ',' (comma) in your "
                       "response. Don't tell abbreviation like 'hPa' or 'h'. but 'hectopascal' or 'kilometer per hour'.",
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
    },
    {
        "name": "get_news",
        "description": "Get the news. Answer with sentences like 'The news is about the coronavirus.' or "
                          "'The news is about the election in the United States.'",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": ["business", "entertainment", "general", "health", "science", "sports", "technology"],
                    "description": "The category of the news",
                },
                "country": {
                    "type": "string",
                    "description": "The country of the news with the ISO 3166-1 code, e.g. fr for France",
                },
            },
            "required": []
        },
    }
]