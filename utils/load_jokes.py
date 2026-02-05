import json
import os
import random

import anyio


async def load_welcome_jokes(language):
    if os.path.exists('assets/welcome_jokes.json'):
        async with await anyio.open_file('assets/welcome_jokes.json', 'r', encoding='utf-8') as file:
            content = await file.read()
            data_welcome_jokes = json.loads(content)
        if language == "de":
            random_joke = random.choice(data_welcome_jokes['jokes']['welcome_DE'])
        else:
            random_joke = random.choice(data_welcome_jokes['jokes']['welcome_EN'])
    else:
        random_joke = None
        print("der pfad existiert nicht")
    return random_joke